"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""


journal = [{'school_class': '4a', 'scores': [3,4,4,5,2]},
		   {'school_class': '4b', 'scores': [5,4,2,5,2,1,1]},
		   {'school_class': '5g', 'scores': [3,4,3,5,4]},
		   {'school_class': '5a', 'scores': [5,5,4,5,3,4,1,2]}]


def main(grades):
    avrg_school = 0
    all_score_quantity = 0

    for each_class in journal:
        avrg_range_class = sum(each_class['scores'])/len(each_class['scores'])
        name_class = each_class['school_class']
        all_score_quantity += len(each_class['scores'])
        avrg_school += sum(each_class['scores'])
        print(f'Средний балл класса {name_class}: {avrg_range_class}')


    print(f'Средний балл по школе: {avrg_school/all_score_quantity}')
    	
    
if __name__ == "__main__":
    main(journal)