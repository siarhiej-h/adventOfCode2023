def part_one(input):
    (
        seeds,
        seed_to_soil,
        soil_to_fertilizer,
        fertilizer_to_water,
        water_to_light,
        light_to_temperature,
        temperature_to_humidity,
        humidity_to_location,
    ) = input

    locatin_min = -1
    for seed in seeds:
        soil_data = next((values for values in seed_to_soil if values[1] <= seed < values[1] + values[2]), None)
        soil = seed - soil_data[1] + soil_data[0] if soil_data else seed
        fertilizer_data = next((values for values in soil_to_fertilizer if values[1] <= soil < values[1] + values[2]), None)
        fertilizer = soil - fertilizer_data[1] + fertilizer_data[0] if fertilizer_data else soil
        water_data = next((values for values in fertilizer_to_water if values[1] <= fertilizer < values[1] + values[2]), None)
        water = fertilizer - water_data[1] + water_data[0] if water_data else fertilizer
        light_data = next((values for values in water_to_light if values[1] <= water < values[1] + values[2]), None)
        light = water - light_data[1] + light_data[0] if light_data else water
        temperature_data = next((values for values in light_to_temperature if values[1] <= light < values[1] + values[2]), None)
        temperature = light - temperature_data[1] + temperature_data[0] if temperature_data else light
        humidity_data = next((values for values in temperature_to_humidity if values[1] <= temperature < values[1] + values[2]), None)
        humidity = temperature - humidity_data[1] + humidity_data[0] if humidity_data else temperature
        location_data = next((values for values in humidity_to_location if values[1] <= humidity < values[1] + values[2]), None)
        location = humidity - location_data[1] + location_data[0] if location_data else humidity

        if locatin_min == -1 or location < locatin_min:
            locatin_min = location

    print(locatin_min)


def part_two(input):
    (
        seeds,
        seed_to_soil,
        soil_to_fertilizer,
        fertilizer_to_water,
        water_to_light,
        light_to_temperature,
        temperature_to_humidity,
        humidity_to_location,
    ) = input
    seeds = [[t[0], t[0] + t[1] - 1] for t in zip(seeds[::2], seeds[1::2])]
    seeds.sort(key=lambda x: x[0])
    soils = apply_map(seeds, seed_to_soil)
    fertilizers = apply_map(soils, soil_to_fertilizer)
    waters = apply_map(fertilizers, fertilizer_to_water)
    lights = apply_map(waters, water_to_light)
    temperatures = apply_map(lights, light_to_temperature)
    humidities = apply_map(temperatures, temperature_to_humidity)
    locations = apply_map(humidities, humidity_to_location)
    print(locations)


def merge_ranges(ranges):
    new_ranges = []
    if not ranges:
        return new_ranges
    if len(ranges) == 1:
        return ranges

    ranges.sort(key=lambda r: r[0])
    start = None
    for i in range(0, len(ranges) - 1):
        current_range = ranges[i]
        next_range = ranges[i + 1]
        if start is None:
            start = current_range[0]
        if current_range[1] + 1 != next_range[0]:
            end = current_range[1]
            new_ranges.append([start, end])
            start = next_range[0]
    if not new_ranges or ranges[-1][1] != new_ranges[-1][1]:
        new_ranges.append([start, ranges[-1][1]])
    return new_ranges


def apply_map(ranges, data):
    ranges = sorted(ranges, key=lambda x: x[0])
    sorted_data = sorted(data, key=lambda x: x[1])
    source_ranges = []
    destination_ranges = []
    for parameter_range in ranges:
        parameter_range_start = parameter_range[0]
        parameter_range_end = parameter_range[1]

        for data_range in sorted_data:
            source_data_start = data_range[1]
            source_data_end = data_range[1] + data_range[2] - 1
            if parameter_range_end < source_data_start:
                continue
            if source_data_start <= parameter_range_start and parameter_range_end <= source_data_end:
                destination_start = parameter_range_start - source_data_start + data_range[0]
                destination_end = parameter_range_end - source_data_start + data_range[0]
                destination_ranges.append([destination_start, destination_end])
                source_ranges.append(parameter_range)
                break
            if parameter_range_start < source_data_start and parameter_range_end <= source_data_end:
                destination_start = data_range[0]
                destination_end = parameter_range_end - source_data_start + data_range[0]
                destination_ranges.append([destination_start, destination_end])
                source_ranges.append([source_data_start, parameter_range_end])
                continue
            if source_data_start > parameter_range_start and source_data_end < parameter_range_end:
                destination_start = data_range[0]
                destination_end = data_range[0] + data_range[2] - 1
                destination_ranges.append([destination_start, destination_end])
                source_ranges.append([source_data_start, source_data_end])
                continue
            if parameter_range_start > source_data_end:
                continue
            if source_data_start <= parameter_range_start and parameter_range_end > source_data_end:
                destination_start = parameter_range_start - source_data_start + data_range[0]
                destination_end = data_range[0] + data_range[2] - 1
                destination_ranges.append([destination_start, destination_end])
                source_ranges.append([parameter_range_start, source_data_end])
                continue

    source_ranges = merge_ranges(source_ranges)
    for parameter_range in ranges:
        start = parameter_range[0]
        end = parameter_range[1]
        if parameter_range not in source_ranges:
            found = False
            for source_range in source_ranges:
                source_start = source_range[0]
                source_end = source_range[1]
                if start <= source_start and end >= source_end:
                    found = True
                    if start < source_start:
                        destination_ranges.append([start, source_start - 1])
                    if end > source_end:
                        destination_ranges.append([source_end + 1, end])
                    break
            if not found:
                destination_ranges.append(parameter_range)
    destination_ranges = merge_ranges(destination_ranges)
    return destination_ranges


def parse_input():
    input_file = "input.txt"
    with open(input_file) as f:
        sections = f.read().split("\n\n")
        for section in sections:
            if section.startswith("seeds:"):
                seed_numbers = section.split("seeds: ")[1].split(" ")
                seeds = [int(value) for value in seed_numbers]
            else:
                data = [
                    [int(value) for value in line.split(" ")]
                    for line in section.splitlines()[1:]
                ]
                if section.startswith("seed-to-soil map"):
                    seed_to_soil = data
                if section.startswith("soil-to-fertilizer map"):
                    soil_to_fertilizer = data
                if section.startswith("fertilizer-to-water map"):
                    fertilizer_to_water = data
                if section.startswith("water-to-light map"):
                    water_to_light = data
                if section.startswith("light-to-temperature map"):
                    light_to_temperature = data
                if section.startswith("temperature-to-humidity map"):
                    temperature_to_humidity = data
                if section.startswith("humidity-to-location map"):
                    humidity_to_location = data
        return (
            seeds,
            seed_to_soil,
            soil_to_fertilizer,
            fertilizer_to_water,
            water_to_light,
            light_to_temperature,
            temperature_to_humidity,
            humidity_to_location,
        )


if __name__ == "__main__":
    input = parse_input()
    part_one(input)
    part_two(input)
