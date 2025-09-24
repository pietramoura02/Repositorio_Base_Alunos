# utilizamos o try/except para apresentar uma exceção 
# de uma maneira mais amigavel ao usuario 

try: # o codigo  
    resultado = 10/0 
except: 
    print('ocorreu um erro na operação. não é possivel a divisão com denomiador igual a zero.')