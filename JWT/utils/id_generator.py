from typing import Generator

user_id_counter = 1
post_id_counter = 1

def user_id_generator() -> Generator[int, None, None]:
    global user_id_counter
    while True:
        yield user_id_counter
        user_id_counter += 1

def post_id_generator() -> Generator[int, None, None]:
    global post_id_counter
    while True:
        yield post_id_counter
        post_id_counter += 1

user_id_gen = user_id_generator()
post_id_gen = post_id_generator()
