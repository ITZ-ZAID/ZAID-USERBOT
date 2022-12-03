import re


class IntervalHelper:
    class IntervalError(Exception):
        pass

    interval_re = re.compile(r"^(\d+)(w|d|h|m)?$")

    def __init__(self, _interval):
        self._interval = _interval
        if not self.interval_ok():
            raise Exception("Invalid interval format.")

    def interval_ok(self):
        if IntervalHelper.interval_re.match(self._interval):
            return True
        return False

    def to_secs(self):
        m = IntervalHelper.interval_re.match(self._interval)
        num, unit = m.groups()
        num = int(num)

        if not unit:
            unit = "m"

        if unit == "m":
            return [num * 60, num, "minute" if num == 1 else "minutes"]
        elif unit == "h":
            return [num * 60 * 60, num, "hour" if num == 1 else "hours"]
        elif unit == "d":
            return [num * 60 * 60 * 24, num, "day" if num == 1 else "days"]
        elif unit == "w":
            return [num * 60 * 60 * 24 * 7, num, "week" if num == 1 else "weeks"]

    interval = property(lambda self: self._interval)
