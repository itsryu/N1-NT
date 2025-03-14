my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
multiplied = []
even = []

for i in my_list:
    multiplied.append(i * 2)

    if(i % 2 == 0):
        even.append(i)

print(multiplied)
print(even)