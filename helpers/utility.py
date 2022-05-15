import datetime
import math
import random
import time
import uuid
from random import randint


def split_list(input_list, n):
    """
    Takes a list and splits it into smaller lists of n elements each.
    :param input_list:
    :param n:
    :return:
    """
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
    """
    Get me a time delta between 4 hours and 12 hours.
    :return: int
    """
    rand_value = randint(14400, 43200)
    delta = (time.time() + rand_value) - time.time()
    return int(delta)


def get_random_hex(chars=4):
    """Generate random hex. limited to chars provided.
    If chars not provided then limit to 4
    """
    my_hex = uuid.uuid4().hex[:chars]
    return my_hex


def get_mock_text(sentence):
    new_sentence = ""
    number = 0  # Dummy number for tracking

    for letter in sentence.lower():
        if len(new_sentence) < 2:  # Creates the first two letter
            random_number = random.randint(
                0, 1
            )  # This randomly decides if the letter should be upper or lowercase
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
                # Checks if the two letters before are both upper or lowercase
                if new_sentence[
                    number - 1
                ].isupper():  # Makes the next letter the opposite of the letter before
                    new_sentence += letter.lower()
                else:
                    new_sentence += letter.upper()
            else:
                random_number = random.randint(0, 1)
                if random_number == 0:
                    new_sentence += letter.upper()
                else:
                    new_sentence += letter

        number += 1  # Add one more to the tracking

    return new_sentence
