def parse_input():
    input_file = "input.txt"
    workflows = {}
    parts = []
    is_workflow = True
    with open(input_file) as f:
        for line in f:
            line = line.strip()
            if line == "":
                is_workflow = False
                continue

            if is_workflow:
                split_parts = line[:-1].split("{")
                name = split_parts[0]
                rules = split_parts[1].split(",")
                parsed_rules = []
                for rule in rules:
                    parsed_rule = dict()
                    rule_parts = rule.split(":")
                    if len(rule_parts) == 2:
                        target = rule_parts[1]
                        parsed_rule["target"] = target
                        rule = rule_parts[0]
                        parameter = None
                        if rule.startswith("x"):
                            parameter = 0
                        elif rule.startswith("m"):
                            parameter = 1
                        elif rule.startswith("a"):
                            parameter = 2
                        elif rule.startswith("s"):
                            parameter = 3
                        parsed_rule["parameter"] = parameter
                        parsed_rule["operator"] = rule[1]
                        parsed_rule["value"] = int(rule[2:])
                    else:
                        parsed_rule["target"] = rule
                    parsed_rules.append(parsed_rule)
                workflows[name] = parsed_rules
            else:
                parameters = line[1:-1].split(",")
                part = [int(p.split("=")[1]) for p in parameters]
                parts.append(part)

    return workflows, parts


def evaluate_workflows(start_workflow, part, workflows_map):
    rules = workflows_map[start_workflow]
    while True:
        for i in range(len(rules) - 1):
            rule = rules[i]
            parameter = rule["parameter"]
            operator = rule["operator"]
            value = rule["value"]
            target = rule["target"]
            if operator == ">" and part[parameter] > value:
                if target == "A":
                    return True
                if target == "R":
                    return False
                rules = workflows_map[target]
                break

            if operator == "<" and part[parameter] < value:
                if target == "A":
                    return True
                if target == "R":
                    return False
                rules = workflows_map[target]
                break
        else:
            target = rules[-1]["target"]
            if target == "A":
                return True
            if target == "R":
                return False
            rules = workflows_map[target]


def part_one(input):
    workflows, parts = input
    total = 0
    for part in parts:
        is_accepted = evaluate_workflows("in", part, workflows)
        if is_accepted:
            total += sum(part)
    print(total)


def part_two(input):
    workflows, _ = input
    start_range = [(1, 4000), (1, 4000), (1, 4000), (1, 4000)]
    workflow = workflows["in"]
    accepted = []
    process_ruleset(start_range, workflow, workflows, accepted)
    total = sum(calculate_combinations(parameters) for parameters in accepted)
    print(total)


def calculate_combinations(parameters):
    total = 1
    for parameter in parameters:
        start, end = parameter
        total *= (end - start + 1)
    return total


def process_ruleset(parameters, ruleset, workflows_map, accepted):
    parameters = parameters.copy()
    for i in range(len(ruleset) - 1):
        rule = ruleset[i]
        parameter = rule["parameter"]
        operator = rule["operator"]
        value = rule["value"]
        target = rule["target"]
        start, end = parameters[parameter]
        if operator == ">":
            new_start = max(value + 1, start)
            if new_start > end:
                continue

            parameters[parameter] = (new_start, end)
            if target == "A":
                accepted.append(parameters.copy())
                parameters[parameter] = (start, new_start - 1)
                continue
            if target == "R":
                parameters[parameter] = (start, new_start - 1)
                continue

            process_ruleset(parameters, workflows_map[target], workflows_map, accepted)
            parameters[parameter] = (start, new_start - 1)

        if operator == "<":
            new_end = min(value - 1, end)
            if new_end < start:
                continue

            parameters[parameter] = (start, new_end)
            if target == "A":
                accepted.append(parameters.copy())
                parameters[parameter] = (new_end + 1, end)
                continue
            if target == "R":
                parameters[parameter] = (new_end + 1, end)
                continue

            process_ruleset(parameters, workflows_map[target], workflows_map, accepted)
            parameters[parameter] = (new_end + 1, end)

    target = ruleset[-1]["target"]
    if target == "A":
        accepted.append(parameters.copy())
        return
    if target == "R":
        return
    process_ruleset(parameters, workflows_map[target], workflows_map, accepted)


if __name__ == "__main__":
    input = parse_input()
    part_one(input)
    part_two(input)
