# -Crear una subrutina llamada “Login”, que recibe un nombre de usuario y una contraseña y te devuelve Verdadero si el nombre de usuario es “admin” y la contraseña es “admin123*”. Además recibe el número de intentos que se ha intentado hacer login y si no se ha podido hacer login incremente este valor.

r=False
c=0
while r ==False:
    user=input('Digite el nombre de usuario: ')
    pas=input('Digite la contraseña: ')
    if user=='admin' and pas=='admin123':
        r=True
        print('Exito...')
    else:
       c+=1
print(f'Exito en login despues de {c} intentos') 