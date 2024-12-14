#Try except block
try:
  num = int(input("Enter a number:"))
  print(10/num)
except ZeroDivisionError:
  print("You cannot divide by zero.")
except ValueError:
  print("Invalid input! Please enter a number.")

#Finally Block
try:
  file = open("/content/india map.jpg","r")
except FileNotFoundError:
  print("File not found.")
finally:
  print("Execution complete.")

#Raising Executions
def check_age(age):
  if age<18:
    raise ValueError("age must be 18 or older.")
    return True
try:
   check_age(16)
except ValueError as e:
   print(e)
