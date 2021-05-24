def encrypt(plaintext, k):
    text_iter = enumerate(plaintext,0)
    for it in text_iter:
        plaintext[it] ^ k[it]


    return repr(enumerate(plaintext, 0) ^ enumerate(k, 0))
