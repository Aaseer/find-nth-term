print('This program finds the n term of an arithmetic sequence')
numbers = str(input('Give me the first 3 numbers of the sequence (split them with a ", "): '))
n_term = int(input('The term you wanna find: '))

pattern = numbers.split(', ')
pattern_list = list(map(int, pattern))


if pattern_list[0] - pattern_list[1] == pattern_list[1] - pattern_list[2]: # SUBTRACTION ARITHMATIC
    print(pattern_list[0] + (n_term - 1) * (pattern_list[1] - pattern_list[0]))

elif pattern_list[0] + pattern_list[1] == pattern_list[1] + pattern_list[2]: # ADDITION ARITHMATIC
    print(pattern_list[0] + (n_term - 1) * (pattern_list[1] + pattern_list[0]))
else:
    print('That is not an arithmetic sequence')
