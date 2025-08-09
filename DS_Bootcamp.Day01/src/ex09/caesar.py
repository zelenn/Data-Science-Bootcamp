import sys

def caesar_cipher(mode, text, shift):
    shift = int(shift)
    result = ""
    for char in text:
        if 'a' <= char <= 'z':
            if mode == "encode":
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:  # decode
                result += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
        elif 'A' <= char <= 'Z':
            if mode == "encode":
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
        else:
            if char.isalpha():
                raise Exception("The script does not support your language yet.")
            result += char
    return result

def main():
    if len(sys.argv) != 4:
        raise Exception("Incorrect number of arguments")
    mode = sys.argv[1]
    if mode not in ("encode", "decode"):
        raise Exception("First argument must be 'encode' or 'decode'")
    text = sys.argv[2]
    shift = sys.argv[3]
    print(caesar_cipher(mode, text, shift))

if __name__ == '__main__':
    main()
