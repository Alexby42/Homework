file_name = 'text.txt'
with open(file_name, mode='r') as file:
    content = file.read()
print(content)