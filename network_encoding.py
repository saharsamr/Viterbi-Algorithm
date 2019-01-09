from enum import Enum


class State(Enum):
    first = 1
    second = 2
    third = 3
    forth = 4


def encode(string):
    state = State.first
    result = ''
    for i in string:
        if state == State.first:
            if i == '0':
                result += '00'
            else:
                result += '11'
                state = State.third
        elif state == State.second:
            if i == '0':
                result += '10'
                state = State.first
            else:
                result += '01'
                state = State.third
        elif state == State.third:
            if i == '0':
                result += '11'
                state = State.second
            else:
                result += '00'
                state = State.forth
        else:
            if i == '0':
                result += '01'
                state = State.second
            else:
                result += '10'

    return result



