import random
import string

def get_random_password(n: int=8) -> str:
    chars = string.digits + string.ascii_uppercase + string.ascii_lowercase
    return "".join(random.sample(chars, n))


print(get_random_password())
