import string
import random
def generate_id (size = 8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def random_degrees (from_ = 68.00, to_ = 74.50):
    return round(random.uniform(from_, to_), 2)
