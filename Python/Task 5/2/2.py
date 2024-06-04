with open('input.txt') as file_in:
    numbers = sorted(file_in.readlines())
with open('output.txt', 'w') as file_out:
    for i in range(len(numbers)):
        file_out.write(numbers[i])
