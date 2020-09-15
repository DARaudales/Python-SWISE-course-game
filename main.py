import pandas as pd
import numpy as np
from pprint import pprint

nombres=["Ábner","Ángel","David","María"]
hps=[36,36,36,36]
cms=[0,0,0,0]
car=[5,7,6,4]
ints=[5,5,7,6]
ens=[10,10,10,10]
din=[50,50,50,50]
nivel=[1,1,1,1]

key_héroes = ["Nombre", "HP", "CM", "Carisma", "Inteligencia", "Energía", "Dinero", "Nivel"]
value_héroes=[nombres, hps, cms, car, ints, ens, din, nivel ]
dic_héroes= {key:value for key, value in zip(key_héroes,value_héroes)}


df_héroes=pd.DataFrame(dic_héroes)
print(df_héroes)

print("Te damos la bienvenida a esta aventura.")
print("En este juego, lucharás contra las fuerzas del mal para rescatar tu índice acaémico.")
print("Elige como quién quieres jugar:")
print("1.Ábner\n2.Ángel\n3.David\n4.María")
while True:
  try:
    n=int(input("Opción: "))
  except ValueError:
    pass
  else:
    if 1<=n<=4:
      n-=1
      break
    else:
      pass


class Personaje:

  def __init__(self, nombre, hp, cm=0):
    self.nombre=nombre
    self.hp=hp
    self.cm=cm


class Villano(Personaje):

  def __init__(self, nombre, denuncias=0,  hp=100):
    Personaje.__init__(self, nombre, hp)
    self.denuncias=denuncias


class Héroe(Personaje):

  def __init__(self, nombre=df_héroes.Nombre[n], hp=36, stats=None):
    Personaje.__init__(self, nombre, hp)
    self.stats={
                "Carisma": df_héroes.Carisma[n],
                "Inteligencia":df_héroes.Inteligencia[n],
                "Energía": df_héroes.Energía[n],
                "Dinero": df_héroes.Dinero[n],
                "Nivel": df_héroes.Nivel[n]
                } if stats is None else stats

  def lvlup(self):
    df_héroes.Carisma[n]+=0.5
    df_héroes.Inteligencia[n]+=0.5
    df_héroes.Energía[n]=10
    df_héroes.Dinero[n]+=50
    df_héroes.Nivel[n]+=1

player=Héroe()
Urrutia=Villano("Carlos Urrutia")
Mark=Villano("Androide Mark III")

player.lvlup()
print(df_héroes)

r1=np.random.randint(1,11)
r2=np.random.randint(1,11)
coeficientes = np.poly([r1,r2])
f=np.poly1d(coeficientes)



print(f"A ver si sabe factorizar, deme uno de los ceros de este polinomio:\n\n{f}")
if r1==r2:
    print("Uy, es una mujer desnuda.")
try:
    y=int(input("\nRespuesta: "))
except ValueError:
    print("Le dije que mirara su cuaderno, coño")
    pregunta1=False
else:
    if y in [r1,r2]:
        print("Muy bien, cuando se gradúe me da su autógrafo")
        pregunta1=True
    else:
      print("Le dije que mirara su cuaderno, coño")
      pregunta1=False

if pregunta1:
    x=np.random.randint(-6,6)
    print(f"\nBueno, a ver si sabe evaluar una función. Probemos con el mismo de la Pregunta 1:\n\nf(x)=\n{f}")
    print(f"\nEncuentre f({x})")
    try:
        y=int(input(f"f({x})= "))
    except ValueError:
        print("Beh, no sabe que tiene que meter números.")
        pregunta2=False
    else:
        if y==f(x):
            print("Pucha, sí lee su cuaderno.")
            pregunta2=True
        else:
            print(f"Mire, que la respuesta es {y} dice JAJA.")
            pregunta2=False

if pregunta2:
    print("Felicidades, siga estudiando, ahora se viene Cálculo I, métala con Donaire.")
