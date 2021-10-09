import random
import string

from app.settings.settings import settings


def create_random_string(n: int) -> str:
    return ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(n))


def prepare_link(short_link) -> str:
    return f"{settings.APP_HOST}:{settings.APP_PORT}/short/redirect/{short_link}"
