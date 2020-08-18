from .base import *
import string
import random

chars = ''.join([string.ascii_letters, string.digits, string.punctuation]).replace('\'', '').replace('"', '')\
    .replace('\\', '')

SECRET_KEY = os.getenv('SECRET_KEY', ''.join([random.SystemRandom().choice(chars) for i in range(50)]))

ALLOWED_HOSTS = []
