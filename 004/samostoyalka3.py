import random
MOVES = {
    'w': -3,
    's': 3,
    'a': -1,
    'd': 1,
}

def shuffle_field():
    field = list(range(1, 17))
    field[-1] = EMPTY_MARK
    random.shuffle(field)
    return field

def print_field(field):
    for i in range(0, 9, 3):
        print(field[i:i + 3])
    print('\n')

def perform_move(field, key):
    current_position = field.index(EMPTY_MARK)

    if key == 's' and current_position >= 7:
        raise IndexError('Cant move down')

    if key == 'd' and current_position % 4 == 3:
        raise IndexError('Cant move right')

    if key == 'w' and current_position < 3:
        raise IndexError('Cant move up')

    if key == 'a' and current_position % 4 == 0:
        raise IndexError('Cant move left')

    delta = MOVES[key]
    field[current_position], field[current_position + delta] = field[current_position + delta], field[current_position]
    return field

def is_game_finished(field):

def handle_user_input():
    while True:
        user_move = input('Please, input your move: ')
        if user_move in MOVES.keys():
            return user_move