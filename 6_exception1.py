"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def hello_user():
    
    try:
      while input('How are you?    ') != 'Fine':
        continue

    except KeyboardInterrupt:
      print ('', 'Enough!', sep='\n')


if __name__ == "__main__":
    hello_user()
