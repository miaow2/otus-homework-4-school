from time import sleep

from redis import Redis
from rq import Queue


queue = Queue(connection=Redis())


def send_email(to_email, from_email, theme, message):
    print(f"Sending email to {to_email!r} with theme {theme!r} and message {message!r}")
    sleep(5)