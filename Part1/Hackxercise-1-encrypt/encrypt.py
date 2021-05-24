alphabet = 'abcdefghijklmnopqrstuvwxyz'


def encrypt(plaintext, k):
    cipher = ""
    for letter in plaintext:
        cipher = cipher + alphabet[(alphabet.index(letter) - k) % len(alphabet)]
    return cipher


def main():
    print(encrypt("hello", 5))


if __name__ == '__main__':
    main()
