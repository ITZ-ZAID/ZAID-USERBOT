import datetime
import math
import random
import time
import uuid
from random import randint

def get_arg(message):
    msg = message.text
    msg = msg.replace(" ", "", 1) if msg[1] == " " else msg
    split = msg[1:].replace("\n", " \n").split(" ")
    if " ".join(split[1:]).strip() == "":
        return ""
    return " ".join(split[1:])

def split_list(input_list, n):
    n = max(1, n)
    return [input_list[i: i + n] for i in range(0, len(input_list), n)]


def human_time(*args, **kwargs):
    secs = float(datetime.timedelta(*args, **kwargs).total_seconds())
    units = [("day", 86400), ("hour", 3600), ("minute", 60), ("second", 1)]
    parts = []
    for unit, mul in units:
        if secs / mul >= 1 or mul == 1:
            if mul > 1:
                n = int(math.floor(secs / mul))
                secs -= n * mul
            else:
                n = secs if secs != int(secs) else int(secs)
            parts.append("%s %s%s" % (n, unit, "" if n == 1 else "s"))
    return ", ".join(parts)


def random_interval():
    rand_value = randint(14400, 43200)
    delta = (time.time() + rand_value) - time.time()
    return int(delta)


def get_random_hex(chars=4):
    my_hex = uuid.uuid4().hex[:chars]
    return my_hex


def get_mock_text(sentence):
    new_sentence = ""
    number = 0

    for letter in sentence.lower():
        if len(new_sentence) < 2:
            random_number = random.randint(
                0, 1
            )
            if random_number == 0:
                new_sentence += letter.upper()
            else:
                new_sentence += letter
        else:
            if (
                    new_sentence[number - 2].isupper()
                    and new_sentence[number - 1].isupper()
                    or new_sentence[number - 2].islower()
                    and new_sentence[number - 1].islower()
            ):
                if new_sentence[
                    number - 1
                ].isupper():
                    new_sentence += letter.lower()
                else:
                    new_sentence += letter.upper()
            else:
                random_number = random.randint(0, 1)
                if random_number == 0:
                    new_sentence += letter.upper()
                else:
                    new_sentence += letter

        number += 1
    return new_sentence
