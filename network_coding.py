import network_encoding
import viterbi_decoding


if __name__ == '__main__':
    string = '110111'
    print string
    encoded = network_encoding.encode(string)
    print encoded
    viterbi_decoding.decode(encoded)

