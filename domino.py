
brick_conversion = {'\\': 0, '|': 1, '/': 2}


class Brick:

    def __init__(self, state, previous=1, next=1):
        self.state = state
        self.previous = previous
        self.next = next

    def next_state(self):
        if self.previous == 2 and self.next in (1, 2) and self.state != 0:
            self.state = 2

        elif self.previous in (0, 1) and self.next == 0 and self.state != 2:
            self.state = 0

    def previous_state(self):
        if (self.state == 0 and self.previous != 0 and self.next == 0) or \
                (self.state == 2 and self.previous == 2 and self.next != 2):
            self.state = 1

    def __repr__(self):
        return f"Brick ({self.previous}, {self.state}, {self.next})"


def encode(domino_string):
    return [Brick(brick_conversion[symbol]) for symbol in list(domino_string)]


def decode(brick_instances):
    inv_brick_conversion = {v: k for k, v in brick_conversion.items()}
    return ''.join([inv_brick_conversion[brick.state] for brick in brick_instances])


def update_positions_forward(encoded_domino):
    for brick in encoded_domino:
        brick.next_state()
    return encoded_domino


def update_positions_backward(encoded_domino):
    for brick in encoded_domino:
        brick.previous_state()
    return encoded_domino


def update_neighbouring_positions(encoded_domino):
    for index, brick in enumerate(encoded_domino):
        if index == 0:
            brick.next = encoded_domino[index+1].state
        elif index == len(encoded_domino)-1:
            brick.previous = encoded_domino[index-1].state
        else:
            brick.previous = encoded_domino[index-1].state
            brick.next = encoded_domino[index+1].state
    return encoded_domino


def forward_iteration(domino_string):
    encoded_domino = encode(domino_string)
    starting_state = update_neighbouring_positions(encoded_domino)
    updated_positions = update_positions_forward(starting_state)
    ending_state = update_neighbouring_positions(updated_positions)
    return decode(ending_state)


def backward_iteration(domino_string):
    encoded_domino = encode(domino_string)
    starting_state = update_neighbouring_positions(encoded_domino)
    updated_positions = update_positions_backward(starting_state)
    ending_state = update_neighbouring_positions(updated_positions)
    return decode(ending_state)


def looper(data, iterator, num_iter):
    for i in range(num_iter):
        data = iterator(data)
    return data


def domino_algorithm(data, mode, num_iter):
    iterators = {'forward': forward_iteration, 'backward': backward_iteration}
    result = looper(data, iterators[mode], num_iter)

    return result


if __name__ == "__main__":

    print(domino_algorithm(r"||//||\||/\|", "forward", 2))

