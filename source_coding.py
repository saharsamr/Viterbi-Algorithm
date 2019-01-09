import parse_mat
import encrypt


if __name__ == '__main__':
    probs = parse_mat.parse('data\\freq.mat').get('freq')
    print encrypt.encrypt(probs, 'khers')
