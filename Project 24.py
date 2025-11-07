import random, string

def password(n=8):
    s = string.ascii_letters + string.digits
    p = random.sample(s, n)
    random.shuffle(p)
    return ''.join(p)

print(password())