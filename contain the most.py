heights=input("input the heights seperated by a ,:")
numbers=[]


height_split=heights.split(",")
print(height_split)


for i in range(len(height_split)):
    for value in range(i + 1, len(height_split)):
        number = int(height_split[i]) * int(height_split[value])
        numbers.append(number)
        if number==0:
            numbers.pop(-1)





for n in numbers[:]:  
    if n > 49:
        numbers.remove(n)

numbers.sort()
print(numbers[-1])