import csv
person_name = []
person_have_visited = set()
person_want_to_visit = set()
next_city_to_visit = person_want_to_visit
def write_holiday_cities(first_letter):
    with open(file='travel-notes.csv', mode='r', newline='', encoding='utf-8') as data_file:
        read_file = csv.reader(data_file, delimiter=',')
        for read_line in read_file:
            if first_letter.lower() in read_line[0][0].lower():
                for row in read_line[0].split(';'):
                    person_name.append(row)
                for row in read_line[1].split(';'):
                    person_have_visited.add(row)
                for row in read_line[2].split(';'):
                    person_want_to_visit.add(row)
    with open(file='holiday.csv', mode='w', newline='', encoding='utf-8') as data_file:
        writer = csv.writer(data_file)
        writer.writerow(('Студенты: ', sorted(person_name)))
        writer.writerow(('Уже были в городах: ', sorted(person_have_visited)))
        writer.writerow(('Хотят посетить города: ', sorted(person_want_to_visit)))
        writer.writerow(('Еще не были в городах: ', sorted(person_want_to_visit.difference(person_have_visited))))
        writer.writerow(('Cледующий город для посещения: ', sorted(person_want_to_visit.difference
                                                                   (person_have_visited))[0]))
write_holiday_cities('R')