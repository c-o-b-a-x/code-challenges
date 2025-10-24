length=0
try:
    check_str= input ("Input your numbers: ")
    for i in range (len(check_str)):
        if i == 0:
            value = -1
        else:
            value = 0
        if int(check_str[i]) == int(check_str[-i + value]):
            print (check_str[i])
            print(check_str[-i])
            length+=1

        if check_str[i] == check_str[-1]:
            print("palindrome")
            break

        elif int(check_str[i]) != int(check_str[i-1]):
           print("Not a Palindrome")
           break
except ValueError :
    print ("This Number isnt a palliondrome since there is non number symbols in it ")