import os


def read_lines(path):
    with open(path, 'r') as opened_file:
        return opened_file.read()

def parse_desired_state(raw_desired_state: str):
    _, *state_chars, __ = raw_desired_state

    desired_state = ''
    for char_index in range(len(state_chars)):
        is_on = state_chars[char_index] == '#'
        desired_state += str(int(is_on))

    return int(desired_state[::-1], 2)

def parse_buttons(raw_button_list: str):
    _, *raw_button, __ = raw_button_list

    button = []
    for button_value in ''.join(raw_button).split(','):
        button.append(2 ** int(button_value))

    return button

def parse_voltage(raw_voltage: str):
    raise NotImplementedError('parse_voltage')


def parse_lines(lines):
    machine_list = []

    for line in lines.splitlines():
        raw_desired_state, *raw_buttons, raw_voltage = line.split(" ")
        machine = {
            'desired_state': parse_desired_state(raw_desired_state),
            'buttons': list(map(parse_buttons, raw_buttons)),
            'voltage_buttons': []
        }

        machine_list.append(machine)

    return machine_list


def main():
    file_path = os.path.join(
        os.path.dirname(__file__),
        'input.txt',
        # 'input_real.txt',
    )

    lines = read_lines(file_path)

    machine_list = parse_lines(lines)
    # TODO: utilize xor for desired state
    # desired state: 6,
    # buttons: [[8], [2, 8], [4], [4, 8], [1, 4], [1, 2]]
    # buttons_sum = [8, 10, 4, 12, 5, 3]
    # current_state, desired_state, buttons_sum
    # 0            | 6            | 5
    # 5            | 6            | 3
    # 6            | 6            | 0

    print(machine_list)


if __name__ == '__main__':
    main()
    exit(0)