"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""

def main():
  answer = ''
  age = int(input("Input your age: "))
  if 0 <=age<3 :
    answer = "You shoul stay at home"
  elif 3<=age<7:
    answer = "You should go to kindergarden"
  elif 7<=age<18:
    answer = "You should go to school"
  else:
    answer = "You may go to university or find a job"
  print (answer)

if __name__ == "__main__":
    main()
