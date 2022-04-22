import unittest
from intcode import Intcode
import main

class TestIntCode(unittest.TestCase):

    def test_get_modes(self): 
        compiler = Intcode()
        self.assertEqual(compiler.get_mode_parameters(1),[0,0,0])


if __name__ == '__main__':
    unittest.main()