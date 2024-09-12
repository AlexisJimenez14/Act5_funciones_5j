print("Ejemplo funciones")

#declarando funciones
def hola():
    print("alguien uso la funcion hola")
def chat(mensa):
    print(f"chat {mensa}")
def ellacontesta(mensa):
    print(f"chat ella :{mensa}")
def escribenombre(ap,n):
    print(f"tu nombre completo es:{n} {ap}")
def suma(a,b):
    s=a+b
    return s


def resta(c,d):
    r=c-d
    return r


def multi(f,g):
    m=f*g
    return m

def division(h,i):
    di=h/i
    return di


#llamadas a funciones
hola()
chat("que bonita estas")
ellacontesta("gracias")
escribenombre("Jimenez","Alexis")
print("operacion suma")
c1=int(input("ingresa un numero "))
c2=int(input("ingresa un numero "))
#llegada resultados
damesuma=suma(c1,c2)
print(f"La suma es {c1} + {c2} = {damesuma}")

#resta
print("resta")
c3=int(input("ingresa un numero "))
c4=int(input("ingresa un numero "))
dameresta=resta(c3,c4)
print(f"La resta es {c3} - {c4} = {dameresta}")

#multiplicacion
print("multiplicacion")
c5=int(input("ingresa un numero "))
c6=int(input("ingresa un numero "))
damemulti=multi(c5,c6)
print(f"La multiplicacion es {c5} * {c6} = {damemulti}")


#division
print("division")
c7=int(input("ingresa un numero "))
c8=int(input("ingresa un numero "))
damedivi=division(c7,c8)
print(f"La division es {c7} / {c8} = {damedivi}")