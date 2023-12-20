from abc import ABC, abstractmethod
from collections import deque


def parse_input():
    input_file = "input.txt"
    modules = []
    inputs = {}
    with open(input_file) as f:
        for line in f:
            line = line.strip()
            parts = line.split(" -> ")
            module = parts[0]
            if module == "broadcaster":
                name = "broadcaster"
                module = "broadcaster"
            elif module.startswith("%"):
                name = module[1:]
                module = "flipflop"
            elif module.startswith("&"):
                name = module[1:]
                module = "conjunction"
            destinations = parts[1].split(", ")
            modules.append((module, name, destinations))
            for destination in destinations:
                if destination not in inputs:
                    inputs[destination] = []
                inputs[destination].append(name)

        modules.append(("disjunction", "rx", []))
        modules.append(("disjunction", "output", []))

    module_objects = {}
    for module in modules:
        module_type, name, destinations = module
        if module_type == "flipflop":
            module_objects[name] = FlipFlop(name, destinations)
        elif module_type == "conjunction":
            module_objects[name] = Conjunction(name, inputs[name], destinations)
        elif module_type == "disjunction":
            module_objects[name] = Disjunction(name, inputs.get(name, []))
        elif module_type == "broadcaster":
            module_objects[name] = Broadcaster(destinations)

    return module_objects


class Module(ABC):
    def __init__(self, name, destinations):
        self.name = name
        self.destinations = destinations

    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def process_signal(self, source, signal):
        pass

    def produce_signals(self, signal):
        return [(destination, self.name, signal) for destination in self.destinations]


class FlipFlop(Module):
    def __init__(self, name, destinations):
        super().__init__(name, destinations)
        self.enabled = False

    def reset(self):
        self.enabled = False

    def process_signal(self, source, signal):
        if signal:
            return []

        self.enabled = not self.enabled
        new_signal = self.enabled
        return self.produce_signals(new_signal)


class Conjunction(Module):
    def __init__(self, name, inputs, destinations):
        super().__init__(name,destinations)
        self.inputs = {i: False for i in inputs}
        self.low = len(inputs)
        self.high = 0

    def reset(self):
        self.inputs = {i: False for i in self.inputs}
        self.low = len(self.inputs)
        self.high = 0

    def process_signal(self, source, signal):
        if signal != self.inputs[source]:
            self.inputs[source] = signal
            if signal:
                self.low -= 1
                self.high += 1
            else:
                self.low += 1
                self.high -= 1

        new_signal = self.low != 0
        return self.produce_signals(new_signal)


class Disjunction(Module):
    def __init__(self, name, inputs):
        super().__init__(name, [])
        self.inputs = inputs

    def reset(self):
        pass

    def process_signal(self, source, signal):
        return []


class Broadcaster(Module):
    def __init__(self, destinations):
        super().__init__("broadcaster", destinations)

    def reset(self):
        pass

    def process_signal(self, source, signal):
        return self.produce_signals(signal)


def part_one(input):
    iterations = 1000
    high_signals, low_signals = press_button(input, iterations)
    print(low_signals * high_signals)


def press_button(modules_map, iterations):
    broadcaster = input["broadcaster"]
    low_signals = 0
    high_signals = 0
    for i in range(iterations):
        low_signals += 1
        queue = deque([(broadcaster, "button", False)])
        while queue:
            module, source, signal = queue.popleft()
            new_signals = module.process_signal(source, signal)
            if not new_signals:
                continue

            for name, source, signal in new_signals:
                if signal:
                    high_signals += 1
                else:
                    low_signals += 1
                queue.append((modules_map[name], source, signal))
    return high_signals, low_signals


def part_two(input):
    for m in input.values():
        m.reset()
    broadcaster = input["broadcaster"]
    rx_inputs = input[input["rx"].inputs[0]].inputs
    rx_inputs_copy = rx_inputs.copy()
    cycles = dict()
    iterations = 0
    while True:
        iterations += 1
        queue = deque([(broadcaster, "button", False)])
        while queue:
            module, source, signal = queue.popleft()
            new_signals = module.process_signal(source, signal)
            has_diff = False
            for k, v in rx_inputs.items():
                if v != rx_inputs_copy[k]:
                    cycles[k] = iterations
                    if len(cycles) == len(rx_inputs):
                        print(find_least_common_multiple(list(cycles.values())))
                        return
                    has_diff = True
            if has_diff:
                rx_inputs_copy = rx_inputs.copy()

            if not new_signals:
                continue

            for name, source, signal in new_signals:
                if name == "rx" and signal is False:
                    print(iterations)
                    return
                queue.append((input[name], source, signal))


def find_least_common_multiple(numbers):
    lcm = numbers[0]
    for i in numbers[1:]:
        lcm = lcm * i // find_greatest_common_divisor(lcm, i)
    return lcm


def find_greatest_common_divisor(a, b):
    while b:
        a, b = b, a % b
    return a


if __name__ == "__main__":
    input = parse_input()
    part_one(input)
    part_two(input)
