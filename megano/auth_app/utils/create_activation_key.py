import hashlib
import random


def get_activation_key(email):
    salt = hashlib.sha1(str(random.random()).encode('utf8')).hexdigest()[:6]
    result = hashlib.sha1((email + salt).encode('utf8')).hexdigest()
    return result
