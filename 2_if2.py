"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def main():
  str1, str2 = input(), input()
  if type(str1) != str or type(str2) != str:
    print(0)
  elif str1 == str2:
    print(1)
  elif len(str1)>len(str2):
    print(2)
  elif str2 =='learn':
    print(3)
  return
  

    
if __name__ == "__main__":
    main()
