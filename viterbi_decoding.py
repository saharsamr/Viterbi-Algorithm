from State import State
from copy import deepcopy


INF = 10000000


def update_pms(pre_pms, current_pms, bits, pre_path, path):
    first = pre_pms[0]+find_hamming_dist(State.first, State.first, bits)
    second = pre_pms[1]+find_hamming_dist(State.second, State.first, bits)
    current_pms[0] = min(first, second)
    if first <= second:
        path[0] = deepcopy(pre_path[0])
    else:
        path[0] = deepcopy(pre_path[1])
    path[0].append(0)

    first = pre_pms[2]+find_hamming_dist(State.third, State.second, bits)
    second = pre_pms[3]+find_hamming_dist(State.forth, State.second, bits)
    current_pms[1] = min(first, second)
    if first <= second:
        path[1] = deepcopy(pre_path[2])
    else:
        path[1] = deepcopy(pre_path[3])
    path[1].append(0)

    first = pre_pms[0]+find_hamming_dist(State.first, State.third, bits)
    second = pre_pms[1]+find_hamming_dist(State.second, State.third, bits)
    current_pms[2] = min(first, second)
    if first <= second:
        path[2] = deepcopy(pre_path[0])
    else:
        path[2] = deepcopy(pre_path[1])
    path[2].append(1)

    first = pre_pms[2]+find_hamming_dist(State.third, State.forth, bits)
    second = pre_pms[3]+find_hamming_dist(State.forth, State.forth, bits)
    current_pms[3] = min(first, second)
    if first <= second:
        path[3] = deepcopy(pre_path[2])
    else:
        path[3] = deepcopy(pre_path[3])
    path[3].append(1)

    return deepcopy(current_pms), deepcopy(path)


def find_hamming_dist(first_state, goal_state, bits):
    expected_bits = ''
    if first_state == State.first and goal_state == State.third:
        expected_bits = '11'
    elif first_state == State.first and goal_state == State.first:
        expected_bits = '00'
    elif first_state == State.second and goal_state == State.first:
        expected_bits = '10'
    elif first_state == State.second and goal_state == State.third:
        expected_bits = '01'
    elif first_state == State.third and goal_state == State.second:
        expected_bits = '11'
    elif first_state == State.third and goal_state == State.forth:
        expected_bits = '00'
    elif first_state == State.forth and goal_state == State.second:
        expected_bits = '01'
    elif first_state == State.forth and goal_state == State.forth:
        expected_bits = '10'

    hamming_dist = 0
    if expected_bits[0] != bits[0]:
        hamming_dist += 1
    if expected_bits[1] != bits[1]:
        hamming_dist += 1

    return hamming_dist


def decode(string):
    pre_path = [[], [], [], []]
    path = deepcopy(pre_path)
    pre_pms = [0, INF, INF, INF]
    current_pms = deepcopy(pre_pms)
    current_state = 0
    while len(string) > 0:
        pre_pms, pre_path = update_pms(pre_pms, current_pms, string[0:2], pre_path, path)
        current_state = current_pms.index(min(current_pms))
        string = string[2:]
    return str(current_pms[current_state]), ''.join(map(lambda x: str(x), path[current_state]))
