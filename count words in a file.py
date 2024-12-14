with open("/content/Roll_43.txt", "r") as file:
    content = file.read()
    words = content.split()
    word_count = len(words)

print(f"Number of words in /content/Roll_43.txt: {word_count}")
