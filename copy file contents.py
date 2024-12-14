with open("/content/Roll_43.txt", "r") as source_file:
     with open("/content/Roll_43.txt", "w") as destination_file:
        for line in source_file:
            destination_file.write(line)
