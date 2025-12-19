import os



def read_lines(path):
    with open(path, 'r') as opened_file:
        return opened_file.read()

def parse_desired_state(raw_desired_state: str):
    _, *state_chars, __ = raw_desired_state

    desired_state = 0
    for char_index, char in enumerate(state_chars):
        is_on = char == '#'
        desired_state += int(is_on) << char_index

    return desired_state

def parse_button_wires(raw_button_wire_list: str):
    striped_button_wires = raw_button_wire_list[1:-1]

    button_wires = []
    for button_value in striped_button_wires.split(','):
        button_wires.append(1 << int(button_value))

    return button_wires

def parse_voltage(raw_voltage):
    raise NotImplementedError('parse_voltage')


def parse_lines(lines):
    machine_list = []

    for line in lines.splitlines():
        raw_desired_state, *raw_button_wires, raw_voltage = line.split(" ")
        machine = {
            'desired_state': parse_desired_state(raw_desired_state),
            'button_wires': list(map(parse_button_wires, raw_button_wires)),
            'voltage_buttons': []
        }

        machine_list.append(machine)

    return machine_list

def process_machine(machine):
    minimal_button_pressed = 0

    current_state = {0}
    while True:
        minimal_button_pressed += 1

        current_state = {
            state ^ sum(button_wire)
            for state in current_state
            for button_wire in machine['button_wires']
        }

        if machine['desired_state'] in current_state:
            break

    return minimal_button_pressed


def main():
    file_path = os.path.join(
        os.path.dirname(__file__),
        # 'input.txt',
        'input_real.txt',
    )

    lines = read_lines(file_path)

    machine_list = parse_lines(lines)
    # desired state: 6,
    # buttons: [[8], [2, 8], [4], [4, 8], [1, 4], [1, 2]]
    # buttons_sum = [8, 10, 4, 12, 5, 3]
    # current_state, desired_state, buttons_sum
    # 0            | 6            | 5
    # 5            | 6            | 3
    # 6            | 6            | 0

    print(machine_list)
    print(sum(map(process_machine, machine_list)))


if __name__ == '__main__':
    main()
    exit(0)