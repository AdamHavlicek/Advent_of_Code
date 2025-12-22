import os

# INFO: z3-solver package from pypi
import z3

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
    striped_button_wires = raw_button_wire_list[1:-1].split(',')

    button_wires = []
    for button_value in striped_button_wires:
        button_wires.append(int(button_value))

    return button_wires

def parse_voltage(raw_voltage):
    striped_voltage_list = raw_voltage[1:-1].split(',')

    return list(map(int, striped_voltage_list))


def parse_lines(lines):
    machine_list = []

    for line in lines.splitlines():
        raw_desired_state, *raw_button_wires, raw_voltage = line.split(" ")
        machine = {
            'desired_state': parse_desired_state(raw_desired_state),
            'button_wires_list': list(map(parse_button_wires, raw_button_wires)),
            'voltage_buttons': parse_voltage(raw_voltage),
        }

        machine_list.append(machine)

    return machine_list

def process_machine(machine):
    button_indexes_list = machine['button_wires_list']
    required_voltage = machine['voltage_buttons']

    z3_solver = z3.Solver()

    z3_button_press_counters = [
        z3.Int(f"b{button_index}")
        for button_index in range(len(button_indexes_list))
    ]

    # INFO: result must be positive or zero
    for z3_value in z3_button_press_counters:
        z3_solver.add(z3_value >= 0)

    # INFO: buttons must satisfy the required voltage
    for voltage_counter_index, required_voltage_counter_value in enumerate(required_voltage):
        # we want all the buttons that increase the voltage for the counter
        involved_buttons_for_counter = [
            z3_button_press_counters[button_index]
            for button_index, button in enumerate(button_indexes_list)
            if voltage_counter_index in button
        ]

        z3_solver.add(z3.Sum(involved_buttons_for_counter) == required_voltage_counter_value)

    # iter through as long as it satisfies the specified constraints
    minimal_button_presses = 0
    while z3_solver.check() == z3.sat:
        # get result for the counters
        button_press_counter_result = z3_solver.model()

        minimal_button_presses = sum([
            button_press_counter_result[button_press].as_long()
            for button_press in button_press_counter_result
        ])

        # must be the lowest possible satisfiable result
        z3_solver.add(z3.Sum(z3_button_press_counters) < minimal_button_presses)

    return minimal_button_presses

def main():
    file_path = os.path.join(
        os.path.dirname(__file__),
        # 'input.txt',
        'input_part2_real.txt',
    )

    lines = read_lines(file_path)

    machine_list = parse_lines(lines)

    # print(machine_list)
    # process_machine(machine_list[0])
    print(sum(map(process_machine, machine_list)))

if __name__ == '__main__':
    main()
    exit(0)
