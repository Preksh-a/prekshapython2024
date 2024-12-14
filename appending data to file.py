with open("/content/Roll_43.txt","a")as file:
  file.write("Let's learn file handling.\n")

with open("/content/Roll_43.txt","r")as file:
  print(file.read())
