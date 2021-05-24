alphabet = "abcdefghijklmnopqrstuvwxyz"


def encrypt(plaintext, k):
    ciphertext = []
    for c in plaintext:
        i = alphabet.index(c)
        j = (i + k) % len(alphabet)
        ciphertext.append(alphabet[j])
    return ''.join(ciphertext)


def decrypt(ciphertext, k):
    return encrypt(ciphertext, -k)


def brute_force(ciphertext):
    plaintext = ""

    for k in range(26):
        for letter in ciphertext:
            plaintext = plaintext + alphabet[(alphabet.index(letter) - k) % len(alphabet)]
        print(plaintext, k)
        plaintext = ""


brute_force("kyvtrmrcipnzccrkkrtbwifdkyvefikynvjkrkeffe")
