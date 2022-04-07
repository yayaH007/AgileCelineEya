import unittest
from cookie import Cookie


# @dataclass
class TestCookieMethods(unittest.TestCase):
    cookie = Cookie()

    def test_get_gout(self):
        self.assertEqual('choco', self.cookie.get_gout())

    def test_get_nb_pepites_choco(self):
        self.assertEqual(100, self.cookie.get_nb_pepites_choco())

    # def test_set_gout(self):

    # def test_set_nb_pepites_choco(self):


if __name__ == '__main__':
    unittest.main()




