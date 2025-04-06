import sys

class CustomException(Exception):
    pass

def encode_caesar(phrase, shift):
    res = ""
    shift = shift % 26
    for i in phrase:
        asc_letter = ord(i)
        if asc_letter > 127:
            raise CustomException("The script does not support your language yet")
        elif (asc_letter >= 65 and asc_letter <= 90):
            if (asc_letter + shift > 90):
                res += chr(asc_letter + shift % 26 - 26)
            else:
                res += chr(asc_letter + shift % 26)
        elif (asc_letter >= 97 and asc_letter <= 122):
            if (asc_letter + shift > 122):
                res += chr(asc_letter + shift % 26 - 26)
            else:
                res += chr(asc_letter + shift % 26)
        else:
            res += chr(asc_letter)
    return res


def decode_caesar(phrase, shift):
    res = ""
    shift = 26 - shift % 26
    for i in phrase:
        asc_letter = ord(i)
        if asc_letter > 127:
            raise CustomException("The script does not support your language yet")
        elif (asc_letter >= 65 and asc_letter <= 90):
            if (asc_letter + shift > 90):
                res += chr(asc_letter + shift % 26 - 26)
            else:
                res += chr(asc_letter + shift % 26)
        elif (asc_letter >= 97 and asc_letter <= 122):
            if (asc_letter + shift > 122):
                res += chr(asc_letter + shift % 26 - 26)
            else:
                res += chr(asc_letter + shift % 26)
        else:
            res += chr(asc_letter)
    return res


if __name__ == '__main__':
    if len(sys.argv) == 4:
        mode = sys.argv[1]
        phrase = sys.argv[2]
        shift = int(sys.argv[3])
        if mode == "encode":
            print(encode_caesar(phrase, shift))
        elif mode == "decode":
            print(decode_caesar(phrase, shift))