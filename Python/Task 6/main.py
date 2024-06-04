import csv
import random
import os


def Show(filename, position="top", separator=','):
    with open(filename) as f:
        reader = list(csv.DictReader(f))
    headers = reader[0]
    reader.pop(0)
    print(separator.join(list(headers.keys())))
    if(len(reader) < 5): print("Not enough rows in file")
    count = 0
    if position == 'bottom':
        while count < min(5, len(reader)):
            print(separator.join(list(reader[len(reader)-count-1].values())))
            count += 1
    elif position == 'random':
        while count < min(5, len(reader)):
            print(separator.join(list(reader[random.randrange(0, len(reader))].values())))
            count += 1
    else:
        while count < min(5, len(reader)):
            print(separator.join(list(reader[count].values())))
            count += 1


def Info(filename):
    with open(filename) as f:
        reader = list(csv.DictReader(f))
    print(str(len(reader)) + 'x' + str(len(reader[0].values())))
    headers = reader[0]
    reader.pop(0)
    for column in list(reader[0].keys()):
        count = 0
        for i in range(len(reader)):
            if reader[i][column] != '': count += 1
        print(column + ': ' + str(count))


def DelNaN(file_in, file_out='processed.csv', separator=','):
    with open(file_in) as f_in:
        reader = list(csv.DictReader(f_in))
    with open(file_out, 'w') as f_out:
        for row in reader:
            has_empty_cell = False
            for i in list(row.keys()):
                if row[i] == '': has_empty_cell = True
            if not(has_empty_cell):
                f_out.write(separator.join(list(row.values()))+'\n')


def MakeDS(filename, separator=','):
    os.makedirs('workdata/learning', exist_ok=True)
    os.makedirs('workdata/testing', exist_ok=True)
    with open(filename) as f:
        reader = list(csv.DictReader(f))
        headers = reader[0]
        reader.pop(0)
    with open(f'workdata/learning/train.csv', 'w') as f_out:
        rows = int(len(reader)*0.7)
        f_out.write(separator.join(list(headers.keys()))+'\n')
        for i in range(rows):
            index = random.randrange(0, len(reader))
            f_out.write(separator.join(list(reader[index].values()))+'\n')
            reader.pop(index)
    with open(f'workdata/testing/test.csv', 'w') as f_out:
        f_out.write(separator.join(list(headers.keys()))+'\n')
        for row in reader:
            f_out.write(separator.join(list(row.values()))+'\n')


Show("Titanic.csv", position='random')
Info("Titanic.csv")
DelNaN("Titanic.csv")
MakeDS("Titanic.csv")