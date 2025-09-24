num1= input("digite o primeiro número: ")
num2= input("digite o segundo número: ")

try: 
    num1 = int(num1)
    num2 = int(num2)
    
    print(f'soma dos números é {num1 + num2}.')
except: 
    print("digite um número correto.")