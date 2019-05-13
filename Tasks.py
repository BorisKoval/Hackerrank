import sys

class TasksSolves():    
    
    @staticmethod
    def dict_and_maps(path):
        _input = ''
        input_dict = {}

        with open(path) as inp:
            _input = inp.read()

        n = int(_input.split('\n')[0])
        input_list = _input.split('\n')

        for i in range(1, n+1):
            key = input_list[i].split(' ')[0]
            value = input_list[i].split(' ')[1]
            input_dict[key] = value
            
        for i in range(n+1, len(input_list)):
            input_dict[key] = value
            line = input_list[i]
            if (line in input_dict.keys()):
                print("%s=%s" % (line, input_dict[line]))
            else:
                print("Not found")

    @staticmethod
    def divisor_sum(n):
        sum = 0
        for i in range(1, n+1):
            if n % i is 0:
                sum+=id
        return sum

path = 'Inputs/day8_input.txt'
print(TasksSolves.dict_and_maps(path))


""" 
lines = input()
input_str = ''

for i in range(0, int(lines)):
     input_str+= input()

input_strings = input_str.split('\n')

some_dict = input_strings[1:int(input_strings[0])].split(' ')

print(input_str)
 """