import time
import sys  # ignore

sys.path.insert(0, '.')  # ignore

real_password = "9370"


def check_password(password):  # Don't change it

    if len(password) != len(real_password):
        return False
    for x, y in zip(password, real_password):
        time.sleep(0.1)  # Simulates the wait time of the safe's mechanism
        if int(x) != int(y):
            return False
    return True


def crack_password():
    password = ""

    for i in range(3):
        for digit in range(10):
            start_time = time.time()
            check_password(password + (str(digit) * (4 - i)))
            difference = time.time() - start_time
            print(difference)
            if difference > (0.1 * (i+2)):
                password = password + str(digit)
                break
    for j in range(10):
        if check_password(password + str(j)):
            password = password + str(j)
            break
    return password


def main():
    print(crack_password())


if __name__ == '__main__':
    main()
