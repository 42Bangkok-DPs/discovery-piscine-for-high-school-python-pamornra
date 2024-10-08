number1=int(input("Enter the first number :"))
print(number1)
number2=int(input("Enter the second number :"))
print(number2)

n=(number1 * number2)

print(number1,"x",number2,"=",n)
if n < 0 :
 print("The result is negative.")
elif n > 0 :
  print("The result is positive.")
elif n==0 :
  print("The result is positive and negative.")
