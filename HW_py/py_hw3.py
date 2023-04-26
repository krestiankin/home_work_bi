students = [] #пустий список для студентів

# вводимо дані про студентів: ім'я, оцінка, здавчи не здав екзамен
n = int(input('Введіть кількість(числом) студентів які здавали екамен: '))
for i in range(n):
    name = input(f'Введіть им\'я студента {i+1}: ')  # тут ще збільшуємо на 1 і
    grade = int(input(f'Введіть оцінку студента {name}: '))
    result = input(f'Чи здав студент {name} экзамен? (Passed/Failed): ')
    students.append((name, grade, result.lower()))
    
#print(students) #прінт для візуального тесту першого списку

#створюємо пусти списки з оцінками в залежності чи здав студент чи ні.
passed_grades = []    
failed_grades = []

for i in students:
    match i[2]:                         #спробував метч, якось раніше не стикався з ціює конструкцією.
        case 'passed':
            passed_grades.append(i[1])
        case 'failed':
            failed_grades.append(i[1])

# print(passed_grades)    #прінт для візуального тесту
# print(failed_grades)    #прінт для візуального тесту

if len(failed_grades) == 0:
        print(f'Екзамен здали усі, сьогодні професор Грубл добряк') # прінт на випадок коли на вході всі здали )       
elif min(passed_grades) > max(failed_grades):
    print(f'Професор Грубл послідовний, а поріг для здачі в діапазоні {max(failed_grades)+1} - {min(passed_grades)}')
else:
    print(f'Професор Грубл не послідовний')
    
'''все це можна огорнути у функцію та клас і записати як модуль, не розумію чи варто,
   але якщо треба щоб підняти оцінку може перезалити'''
