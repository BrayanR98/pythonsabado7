# Crea una función  que reciba una lista con valores numéricos y devuelva el valor máximo y el mínimo ingresados
listas=[70,2,10,4,5]
def hallarValores(lista):
     M=lista[0]
     m=lista[0]
     for i in lista:      
        if M<i:
            M=i
        if m>i :
            m=i
     print(f'{M} es el numero mayor y {m} es el numero menor')
hallarValores(listas)
        
        
