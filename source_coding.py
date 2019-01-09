import parse_mat
import encrypt
import decrypt


if __name__ == '__main__':
    probs = parse_mat.parse('data\\freq.mat').get('freq')
    codes = {}
    encrypted = encrypt.encrypt(probs, 'khers', codes)
    print encrypted
    string = decrypt.decrypt(encrypted, codes)
    print string
