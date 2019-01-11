import network_encoding
import viterbi_decoding


if __name__ == '__main__':
    print 'ENCODING PHASE:'
    print '---'
    string = '100101'
    print 'input string: ' + string
    encoded = network_encoding.encode(string)
    print 'encoded: ' + encoded
    print '--------------------'
    print 'DECODING PHASE:'
    print '---'
    min_error, decoded = viterbi_decoding.decode(encoded)
    print 'minimum error: ' + min_error
    print 'decoded: ' + decoded

