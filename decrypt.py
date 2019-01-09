def decrypt(string, codes):
    result = ''
    while len(string) > 0:
        for alphabet in codes.keys():
            pair = codes[alphabet]
            if string[0:len(pair)] == pair:
                string = string[len(pair):]
                result += alphabet
                break
    return result
