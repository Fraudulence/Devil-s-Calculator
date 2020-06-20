#Level 27 on The Devil's Calculator, checks for a and b values equal to 666

#Test cases a odd b odd: 5ψ3=13
#
#Test cases a odd b even: 5ψ2=14
#
#Test cases a even b even: 20ψ10=165
#20ψ12=144
#Test cases a even b odd: 20ψ11=155
#
import math
for a in range(1,101):
  #print("a value:",a)
  for b in range(1,101):
    #print("b value:",b)
    if a%2!=0 & b%2==0:
      x = a*math.ceil(a/2)-b*math.ceil(b/2)+math.ceil(b/2)
    elif a%2!=0 & b%2!=0:
      x = a*math.ceil(a/2)-b*math.ceil(b/2)+b
    elif a%2==0 & b%2!=0:
      x = int((a+1)*a/2-b*math.ceil(b/2)+b)
    else:
      x = int((a+1)*a/2-(b+1)*b/2+b)

    ###x = a*math.ceil(a/2)-b*math.ceil(b/2)+math.ceil(b/2)
    if x == 666: 
      print("a is:",a)
      print("b is:",b)
      break
#Case works with a odd b even (Functional)
a = 5
b = 2
x = a*math.ceil(a/2)-b*math.ceil(b/2)+math.ceil(b/2)
print(x)

#Case works with a odd b odd (Functional)
a = 5
b = 3
x = a*math.ceil(a/2)-b*math.ceil(b/2)+b
print(x)

#Case works with a even b even (Functional)
a = 20
b = 10
x = int((a+1)*a/2-(b+1)*b/2+b)
print(x)

#Case works with a even b odd (Functional)
a = 20
b = 11
x = int((a+1)*a/2-b*math.ceil(b/2)+b)
print(x)