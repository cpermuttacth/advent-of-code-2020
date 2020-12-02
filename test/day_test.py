import sys
import unittest


class DayTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        try:
            sys.argv.pop(sys.argv.index("discover"))
        except ValueError:
            pass
        day = cls.__module__.split("day")[1]
        sys.argv.append("--input")
        sys.argv.append("test/test_day" + day + ".txt")
        module = __import__("day" + str(day))
        class_ = getattr(module, "Day" + str(day))
        cls.day = class_()
