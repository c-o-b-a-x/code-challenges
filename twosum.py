numbers=[]
num_of_num=input("how many numbers : ")
for i in range (int(num_of_num)):
    number=int(input("Number: "))

    numbers.append(number)
sum=int(input("what is the sum?: "))

print (len(numbers))
for i in range (len(numbers)):
    value1=0
    value2=1
    if numbers[value1]+numbers[value2]==sum:
        print("number 1 :" + str(numbers[value1]))
        print("number 2 :" + str(numbers[value2]))
        break
    else:
        value1+=1
        value2+=1

    