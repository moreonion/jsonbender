import unittest

from jsonbender import K, S
from jsonbender.string_ops import Format
from jsonbender.test import BenderTestMixin


class TestFormat(unittest.TestCase, BenderTestMixin):
    def test_format(self):
        bender = Format('{} {} {} {noun}.',
                        K('This'), K('is'), K('a'),
                        noun=K('test'))
        self.assert_bender(bender, None, 'This is a test.')


if __name__ == '__main__':
    unittest.main()

