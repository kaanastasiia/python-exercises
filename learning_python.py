with open("learning_python.txt") as text:
    output = text.read()
    print(output.replace('Python','C'))

with open("learning_python.txt") as text:
    for i in text:
        print(i.replace('Python','C'))

with open("learning_python.txt") as text:   
    output3 = text.readlines()
for line in output3:
    line = line.replace('Python','C')
    print(f"This is output3: {line}")