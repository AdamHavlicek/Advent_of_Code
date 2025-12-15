import os

class CircularBuffer:
    def __init__(self, size):
        self.size = size
        self.buffer = [None] * size
        self.head = 0
        self.tail = 0
        self.count = 0

    def write(self, value):
        self.buffer[self.tail] = value
        self.tail = (self.tail + 1) % self.size
        self.count = min(self.count + 1, self.size)

    def move_head_forward(self, steps=0):
        new_head = (self.head + steps) % self.size
        self.head = new_head
        
    def move_head_backward(self, steps=0):
        new_head = (self.head - steps) % self.size
        self.head = new_head

    def current(self):
        return self.buffer[self.head]


def get_circular_buffer(initial_position=0):
    buffer = CircularBuffer(100)
    buffer.head = initial_position

    for i in range(100):
        buffer.write(i)

    return buffer


def read_lines(path):
    with open(path, 'r') as opened_file:
        return opened_file.readlines()


def process_instructions(buffer, instruction_list):
    counter = 0
    for instruction in instruction_list:
        number = int(instruction[1:])

        move_fn = None
        if instruction.startswith('R'):
            move_fn = buffer.move_head_forward
        if instruction.startswith('L'):
            move_fn = buffer.move_head_backward

        # yeah me not likey either
        for _ in range(number):
            move_fn(1)
            if buffer.current() == 0:
                counter += 1
            
    return counter


if __name__ == '__main__':
    file_path = os.path.join(
        os.path.dirname(__file__),
        'input_part2_real.txt',
    )

    instructions = read_lines(file_path)

    circular_buffer = get_circular_buffer(50)

    print(process_instructions(circular_buffer, instructions))

    exit(0)
