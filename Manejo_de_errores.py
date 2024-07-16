# def suma():
#     n1 = int(input("numero 1: "))
#     n2 = int(input("numero 2: "))
#     print(n1+n2)
#     print("Gracias por sumar" + n1)




try:
    suma()
except TypeError:
    print("Estas concatenando tipos distintos") 
except ValueError:
    print("Eso no es un numero")     
else:
    print("Todo salio bien")
finally:
    print("Eso fue todo")      





def pedir_numero():

    while True:
        try:
            numero = int(input("Dame un numero: "))
        except:
            print("Ese no es un numero")    
        else:
            print(f"Ingresaste el numero {numero}") 
            break

    print("Grscias") 

pedir_numero()