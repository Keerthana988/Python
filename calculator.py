a  = input("enter the first number : ")
b = input("enter the second number : ")
opp = input("enter the operator(+,-,*,/,%) : ")

if opp == "+" :
          print("the sun is ", int(a) + int(b))
elif opp == "-" :
          print("the sun is ", int(a) - int(b))
elif opp == "*" :
          print("the sun is ", int(a) * int(b))
elif opp == "/" :
          print("the sun is ", int(a) / int(b))
elif opp == "%" :
          print("the sun is ", int(a) % int(b))
else:
          print("invalid operation")

