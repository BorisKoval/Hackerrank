import sys

""" 
class TasksSolves():
    
    
    @staticmethod
    def dict_and_maps(path):

        with open(path) as inp:
            _input = inp.read()

        input_strings = _input.split('\n')
        
        
        
        return input_strings


path = 'Inputs/day8_input.txt'
print(TasksSolves.dict_and_maps(path))

 """

input_str = ''
lines = input()

for i in range(0, int(lines)):
     input_str+= input()

#input_strings = input_str.split('\n')

#some_dict = input_strings[1:int(input_strings[0])].split(' ')

print(input_str)
