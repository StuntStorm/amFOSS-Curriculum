data = [['apples', 'oranges', 'cherries', 'banana'],['Alice', 'Bob', 'Carol', 'David'],['dogs', 'cats', 'moose', 'goose']]
RowLen_Max = []

for row in range(len(data)):
    RowLen_Max.append(max([len(col) for col in data[row]]))

for column in range(len(data[0])):
    for row in range(len(data)):
        print(data[row][column].rjust(RowLen_Max[row]), end=' ')
    print()
