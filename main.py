import encrypt
import parse_mat
import network_encoding
import noise
import viterbi_decoding
import decrypt

string = 'saharrajabi'
probs = parse_mat.parse('data\\freq.mat').get('freq')
codes = {}
print 'name: ' + string
source_encrypted = encrypt.encrypt(probs, string, codes)
print 'source encoder output: ' + source_encrypted
network_encrypted = network_encoding.encode(source_encrypted)
print 'network encoder output: ' + network_encrypted
network_encrypted = map(lambda x: int(x), list(network_encrypted))
noisy_data = noise.noise(network_encrypted)
noisy_data = ''.join(map(lambda x: str(x), noisy_data))
print 'noisy data: ' + noisy_data
err, network_decoded = viterbi_decoding.decode(noisy_data)
print 'network decoder output: ' + network_decoded
decoded = decrypt.decrypt(network_decoded, codes)
print 'source decoder output: ' + decoded
