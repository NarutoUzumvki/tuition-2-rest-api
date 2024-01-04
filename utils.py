import random
import string

characters = string.ascii_letters + string.digits

def create_random(length=4):
    random_str = ''.join(random.choice(characters) for _ in range(length))
    return random_str

# hell = create_random()
# print(hell)