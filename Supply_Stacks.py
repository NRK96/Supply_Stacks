import os.path
import sys

# Setting up the stack for the sample input.
def sample_setup():
    stack_one = []
    stack_two = []
    stack_three = []
    stacks = []

    stack_one.append('Z')
    stack_one.append('N')

    stack_two.append('M')
    stack_two.append('C')
    stack_two.append('D')

    stack_three.append('P')

    stacks.append(stack_one)
    stacks.append(stack_two)
    stacks.append(stack_three)

    return stacks

# Setting up the stack for the input file.
def supply_stack_setup():
    stack_one = []
    stack_two = []
    stack_three = []
    stack_four = []
    stack_five = []
    stack_six = []
    stack_seven = []
    stack_eight = []
    stack_nine = []
    stacks = []

    stack_one.append('R')
    stack_one.append('N')
    stack_one.append('F')
    stack_one.append('V')
    stack_one.append('L')
    stack_one.append('J')
    stack_one.append('S')
    stack_one.append('M')

    stack_two.append('P')
    stack_two.append('N')
    stack_two.append('D')
    stack_two.append('Z')
    stack_two.append('F')
    stack_two.append('J')
    stack_two.append('W')
    stack_two.append('H')

    stack_three.append('W')
    stack_three.append('R')
    stack_three.append('C')
    stack_three.append('D')
    stack_three.append('G')

    stack_four.append('N')
    stack_four.append('B')
    stack_four.append('S')

    stack_five.append('M')
    stack_five.append('Z')
    stack_five.append('W')
    stack_five.append('P')
    stack_five.append('C')
    stack_five.append('B')
    stack_five.append('F')
    stack_five.append('N')

    stack_six.append('P')
    stack_six.append('R')
    stack_six.append('M')
    stack_six.append('W')

    stack_seven.append('R')
    stack_seven.append('T')
    stack_seven.append('N')
    stack_seven.append('G')
    stack_seven.append('L')
    stack_seven.append('S')
    stack_seven.append('W')

    stack_eight.append('Q')
    stack_eight.append('T')
    stack_eight.append('H')
    stack_eight.append('F')
    stack_eight.append('N')
    stack_eight.append('B')
    stack_eight.append('V')

    stack_nine.append('L')
    stack_nine.append('M')
    stack_nine.append('H')
    stack_nine.append('Z')
    stack_nine.append('N')
    stack_nine.append('F')

    stacks.append(stack_one)
    stacks.append(stack_two)
    stacks.append(stack_three)
    stacks.append(stack_four)
    stacks.append(stack_five)
    stacks.append(stack_six)
    stacks.append(stack_seven)
    stacks.append(stack_eight)
    stacks.append(stack_nine)

    return stacks


current_directory = os.path.dirname(os.path.realpath(__file__))

# Setup variables for future computation.
filepath = current_directory + '\\Resources\\Supply_Stacks_Input.txt'
result = ''

# Check that file exists, if not exit with error message.
if not os.path.isfile(filepath):
    sys.exit("Error - File not found.")

# Open file and read it in line by line.
file = open(filepath, "r")
lines = file.readlines()

stack_list = supply_stack_setup()

for line in lines:
    # This line contains initial stack info, not instructions: skip.
    if line[0] != 'm':
        continue
    # Break instruction into it's components and execute it.
    instructions = line.strip().split(' ')
    for i in range(0, int(instructions[1])):
        stack_list[int(instructions[5])-1].append(stack_list[int(instructions[3])-1].pop())

# Grab the top crate from each stack and output the results.
for stack in stack_list:
    result += stack.pop()

print(f'The top crate for each stack is as follows: {result}')

file.close()
