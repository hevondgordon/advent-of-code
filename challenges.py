def get_lines(filename):
    lines = []
    with open(filename, 'r') as challenge1Input:
        lines = challenge1Input.readlines()
    return lines


def count_increased():
    lines = get_lines('./challenge1-input.txt')
    last_value = None
    current_value = None
    increases = 0

    for index, line in enumerate(lines):
        if index == 0:
            current_value = int(line)
            last_value = int(line)
        else:
            current_value = int(line)
            last_value = int(lines[index - 1])
        if(current_value > last_value):
            increases += 1
    return increases


def sliding_window():
    lines = get_lines('./challenge1-input.txt')
    window_head_position = 0

    last_value = None
    current_value = None

    increases = 0

    while(window_head_position < len(lines) - 3):
        last_value = int(lines[window_head_position]) + \
            int(lines[window_head_position + 1]) + \
            int(lines[window_head_position + 2])
        current_value = int(lines[window_head_position + 1]) + \
            int(lines[window_head_position + 2]) + \
            int(lines[window_head_position + 3])

        if current_value > last_value:
            increases += 1

        window_head_position += 1
    return increases


def pilot():
    lines = get_lines('./challenge2-input.txt')
    forward = 0
    depth = 0
    aim = 0
    for line in lines:
        command, value = line.split()
        if(command == 'forward'):
            forward += int(value)
            depth += aim * int(value)
        elif(command == 'up'):
            aim -= int(value)
        elif(command == 'down'):
            aim += int(value)
    return forward * depth


print(f'the value after piloting is {pilot()}')
