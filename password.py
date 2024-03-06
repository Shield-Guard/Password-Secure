from colorama import Fore, Style, init
import colorama
import random
from faker import Faker

def generate_random_id():
    return random.randint(1000000000, 9999999999)

num_ids = 10
fake = Faker()
pseudos = [fake.user_name() for _ in range(num_ids)]

for pseudo in pseudos:
    user_id = generate_random_id()
    print(f"{Fore.LIGHTWHITE_EX}[{Fore.GREEN}+{Fore.LIGHTWHITE_EX}] PASSWORD: {pseudo}{user_id}HF{pseudo}")
