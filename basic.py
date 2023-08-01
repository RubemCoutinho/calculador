def calculate():
  operation = input('''Operações:
+ soma
- subtração
/ divisão
* multiplicação
Digite a seguir a operação desejada: ''')

  number_1 = int(input('Digite o primeiro número: '))
  number_2 = int(input('Digite o segundo número: '))

  if operation == '+':
      print (number_1 + number_2)

  elif operation == '-':
      print (number_1 - number_2)

  elif operation == '/':
      print (number_1 / number_2)

  elif operation == '*':
      print (number_1 * number_2)

  else :
      print('Tipo incorreto')

def again():
  calc_again = input('Digite C para continuar na calculadora e E para sair da calculadora. ')

  if calc_again.upper() == 'C' :
    calculate()

  elif calc_again.upper() == 'E' :
    print("Te vejo depois!")

calculate()
again()
