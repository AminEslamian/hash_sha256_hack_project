import string
import random
from hashlib import sha256
hashed_password = '7902699be42c8a8e46fbbb4501726517e86b22c56a189f7625a6da49081b2451' # hash of number 7

def generate_random_word(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    random_word = "".join(random.choice(characters) for _ in range(length))
    return random_word

pass_dict = {}
def hash_dict_creator(length, num):
    for i in range(num):
        random_word = generate_random_word(length)
        hashed = sha256(random_word.encode('utf-8')).hexdigest()
        pass_dict[hashed] = random_word

length = int(input('how many characters does the password has? '))
num = int(input('how many times do you want the process to be looped? '))
hash_dict_creator(length, num)

if hashed_password in pass_dict.keys():
    print(pass_dict[hashed_password])
else:
    print('Not Found!')
