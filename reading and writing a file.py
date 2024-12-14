with open("data.txt","w")as file:
  file.write("Python is awwesome!\n")

with open("data.txt","r")as file:
  print(file.read())
