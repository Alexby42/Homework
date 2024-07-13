info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]
strings_positions = {}
def custom_write(file_name):
    file = open(file_name, mode='w', encoding='utf-8')
    for line in info:
        pos = file.tell()
        file.write(line + '\n')
        strings_positions[(len(strings_positions)+1, pos)] = line
    file.close()
    return strings_positions
res = custom_write('test.txt')
for elem in res.items():
    print(elem)