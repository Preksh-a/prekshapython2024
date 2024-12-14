with open("/content/Roll_43.txt", "r") as file:
    line_count = len(file.readlines())

print(f"Number of lines in /content/Roll_43.txt: {line_count}")
