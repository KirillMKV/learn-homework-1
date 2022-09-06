"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def hello_user():
  answer = ''  
  while answer != 'Fine':
    try:   
        print ('How are you?')
        v = input()   

    except KeyboardInterrupt:
      print ('', 'Enough!', sep='\n')
      break
    
       

if __name__ == "__main__":
    hello_user()
