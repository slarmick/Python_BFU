input_numbers = [int(i) for i in open('input.txt').readline().split()]
multiplication = 1
for a in input_numbers:
    multiplication *= a
with open('output.txt', 'w') as file_out:
    file_out.write(str(multiplication))

