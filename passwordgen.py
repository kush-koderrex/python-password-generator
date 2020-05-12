import string
import random

if __name__ == "__main__":
    s1 = string.ascii_lowercase
    # print(s1)
    s2 = string.ascii_uppercase
    # print(s1)
    s3 = string.digits
    s4 = string.punctuation
    plen = int(input("enter the password length:-"))
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    print()
    random.shuffle(s)
    print("Your password is :-")
    print("".join(random.sample(s, plen)))
