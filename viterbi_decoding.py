from State import State


INF = 1000000000


def update_pms(pre_pms, current_pms, bits):
    current_pms[0] = min(pre_pms[0]+find_hamming_dist(State.first, State.first, bits),
                         pre_pms[1]+find_hamming_dist(State.second, State.first, bits))
    current_pms[1] = min(pre_pms[2]+find_hamming_dist(State.third, State.second, bits),
                         pre_pms[3]+find_hamming_dist(State.forth, State.second, bits))
    current_pms[2] = min(pre_pms[0]+find_hamming_dist(State.first, State.third, bits),
                         pre_pms[1]+find_hamming_dist(State.second, State.third, bits))
    current_pms[3] = min(pre_pms[2]+find_hamming_dist(State.third, State.forth, bits),
                         pre_pms[3]+find_hamming_dist(State.forth, State.forth, bits))
    pre_pms = current_pms


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


def find_data_bit(pre_state, current_state):
    result = ''
    if pre_state == 0 and current_state == 2:
        result = '1'
    elif pre_state == 0 and current_state == 0:
        result = '0'
    elif pre_state == 1 and current_state == 0:
        result = '0'
    elif pre_state == 1 and current_state == 2:
        result = '1'
    elif pre_state == 2 and current_state == 1:
        result = '0'
    elif pre_state == 2 and current_state == 3:
        result = '1'
    elif pre_state == 3 and current_state == 1:
        result = '0'
    elif pre_state == 3 and current_state == 3:
        result = '1'
    return result


def decode(string):
    decoded = ''
    pre_pms = [0, INF, INF, INF]
    current_pms = pre_pms
    pre_state = pre_pms.index(min(pre_pms))
    current_state = pre_state
    while len(string) > 0:
        update_pms(pre_pms, current_pms, string[0:2])
        current_state = current_pms.index(min(current_pms))
        decoded += find_data_bit(pre_state, current_state)
        string = string[2:]
    print 'minimum error: ' + str(current_pms[current_state])
    print 'decoded string: ' + decoded
