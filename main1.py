import unittest
from conver_askee import conversion

class Ascii(unittest.TestCase):

    def test_ascii_conv(self):
        convertChar = '*'
        self.assertEqual(conversion(convertChar),42,msg='conversion({})) expected 42, got {}'.format(convertChar,conversion(convertChar)))
    def test_type(self):
        with self.assertRaises(TypeError):
            conversion(5)


if __name__ == '__main__':
  unittest.main(verbosity=2)