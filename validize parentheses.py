text=input()
textdict=[]
order=[]
for letter in text:
    textdict.append(letter)
for letter in text:
    if letter == "(" :
        order.append(")")
    if letter == "{" :
        order.append("}")
    if letter == "[" :
        order.append("]")

for item in reversed(order):
    textdict.append(item)

text_str=str(textdict)
print (text_str)