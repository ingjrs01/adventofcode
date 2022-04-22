import unittest
from intcode import Intcode

class TestIntCode(unittest.TestCase):

    #def test_get_modes(self): 
    #    compiler = Intcode()
    #    self.assertEqual(compiler.get_mode_parameters(1),[0,0,0])

    def test_get_mode_parameters(self):
        machine = Intcode()
        machine.set_data([3])
        self.assertEqual(machine.get_mode_parameters(),[0,0,0])
        machine.set_data([99])
        self.assertEqual(machine.get_mode_parameters(),[0,0,0])
        machine.set_data([100])
        self.assertEqual(machine.get_mode_parameters(),[1,0,0])
        machine.set_data([201])
        self.assertEqual(machine.get_mode_parameters(),[2,0,0])
        machine.set_data([1201])
        self.assertEqual(machine.get_mode_parameters(),[2,1,0])
        machine.set_data([10201])
        self.assertEqual(machine.get_mode_parameters(),[2,0,1])

    def test_get_instruction(self):
        machine = Intcode()
        machine.set_data([3])
        self.assertEqual(machine.get_instruction(),3)
        machine.set_data([0])
        self.assertEqual(machine.get_instruction(),0)
        machine.set_data([99])
        self.assertEqual(machine.get_instruction(),99)
        machine.set_data([103])
        self.assertEqual(machine.get_instruction(),3)
        machine.set_data([21209])
        self.assertEqual(machine.get_instruction(),9)

    def test_get_parameters(self):
        machine = Intcode()
        machine.set_data([101,23,2,3])
        self.assertEqual(machine.get_parameters(1,[1,0,1]),[23,2,3])

        machine.set_data([1,5,1,3,4,2,1,0])
        self.assertEqual(machine.get_parameters(1,[0,0,0]),[2,5,3])

        machine.set_data([2201,3,4,9,3,4,2,6,5])
        self.assertEqual(machine.get_parameters(1,[2,2,0]),[9,3,9])

        machine.set_data([2201,3,4,9,3,4,2,6,5])
        machine.relative_point = 2
        self.assertEqual(machine.get_parameters(1,[2,2,0]),[4,2,9])


    # Probando las operaciones
    def test_sum(self):
        machine = Intcode()
        data = [1101,23,2,3]
        machine.set_data(data)
        instruction = machine.get_instruction() 
        modes = machine.get_mode_parameters()
        parameters = machine.get_parameters(instruction,modes)
        machine.sum(parameters)
        self.assertEqual(machine.data,[1101,23,2,25])
        # Probamos con otros datos
        data = [2201,1,3,3,4,2,8,10]
        machine.relative_point = 2
        machine.set_data(data)
        instruction = machine.get_instruction() 
        modes = machine.get_mode_parameters()
        parameters = machine.get_parameters(instruction,modes)
        machine.sum(parameters)
        self.assertEqual(machine.data,[2201,1,3,5,4,2,8,10])

    def test_product(self):
        machine = Intcode()
        data = [1102,23,2,3]
        machine.set_data(data)
        instruction = machine.get_instruction() 
        modes = machine.get_mode_parameters()
        parameters = machine.get_parameters(instruction,modes)
        machine.product(parameters)
        self.assertEqual(machine.data,[1102,23,2,46])

    def test_input(self):
        machine = Intcode()
        data = [1103,2,2,3]
        machine.set_data(data)
        instruction = machine.get_instruction() 
        modes = machine.get_mode_parameters()
        parameters = machine.get_parameters(instruction,modes)
        machine.buffer.append(77)
        machine.input(parameters)
        self.assertEqual(machine.data,[1103,2,77,3])

        data = [203,2,2,3]
        machine.set_data(data)
        machine.relative_point = 1
        instruction = machine.get_instruction() 
        modes = machine.get_mode_parameters()
        parameters = machine.get_parameters(instruction,modes)
        machine.buffer.append(77)
        machine.input(parameters)
        self.assertEqual(machine.data,[1103,2,2,77])
        
    # Meter otros test

    #def test_run(self):
    #    machine = Intcode()
    #    machine.set_data([1101,2,2,3])
    #    self.assertEqual(machine.run([]),[])




if __name__ == '__main__':
    unittest.main()