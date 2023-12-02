# Advent of Code 2023 
# Day 1 

import re

file = open ("input", "r");
input = file.readlines()
file.close

number_map = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'zero': '0'
}

answer_one = 0
answer_two = 0

def convert_number_string_to_digits(input_string):
    number_map.update({str(i): str(i) for i in range(10)})
    numbers = re.compile("|".join(number_map))
    return "".join(number_map[w] for w in numbers.findall(input_string))

def strip_non_numerical_characters(input_string):
    return re.sub(r'[^0-9]', '', input_string)

for i in input:
# Process Answer One    
    j = strip_non_numerical_characters(i)
    number_string = j[0] + j[-1]
    answer_one += int(number_string)
        
# Process Answer Two
    k = convert_number_string_to_digits(i)
    new_string = k[0] + k[-1]
    answer_two += int(new_string)  

print(answer_one)
print(answer_two)
