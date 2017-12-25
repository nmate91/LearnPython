import sys
import math

def is_prime(number):
    if (number == 0) or (number == 1):
        return False
    for i in (2, math.sqrt(number)):
        if number % i == 0:
            return False
    return True

if __name__ == "__main__":
    print(is_prime(13))