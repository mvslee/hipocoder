



a = eval(input("Please input integer A, 0<=A<=100: "))
b = eval(input('Please input integer B, 0<=B<=100: '))
if type(a)!=int or type(b)!=int:
    raise TypeError("invalid input type!")
if a<0 or a>100 or b<0 or b>100:
    raise ValueError("invalid input value!")
else:
    print(a+b)


