import pandas as pd
import numpy as np
import pickle

print("                            EL JUEGO                              ")
print(" --------------------------------------------------------------------")
print("   Ayuda                      Jugar                         Creditos")


def menu_ini(op):
    while op == False:
        opcion_menu_ini=str(input("Elige una opcion: "))
        opcion_menu_ini=opcion_menu_ini.lower()
        if opcion_menu_ini!="ayuda" and opcion_menu_ini!="jugar" and opcion_menu_ini!="creditos":
            print("Elige ayuda, jugar o creditos.")
            return menu_ini(False)
        elif opcion_menu_ini=="ayuda":
            print("Instrucciones: Elige la opcion Jugar.\n Deberas completar las asignaciones que se te otorguen en cada nivel.\n Para ello eliges primero un jugador; ademas tendras acceso a una tienda,\n despues de completar cada nivel, donde podras comprar habilidades que te \n ayuden a vencer a tus oponentes.\n Sigue las instrucciones detalladas en cada nivel. Suerte!")
            return menu_ini(False)
        elif opcion_menu_ini=="creditos":
            print("El menu principal y la tienda fueron hechos por Maria Renee Meza. \nLos personajes fueron creados por Angel Anariba.\nLas habilidades de los personajes y sus ataques por David Raudales y Abner Rivera.")
            return menu_ini(False)
        else:
            return menu_ini(True)


menu_ini(False)


def new_or_load(op1):
    while op1!=1 and op1!=2:
        try:
            opcion1=int(input("Desea 1) comenzar una nueva partida o 2) cargar una partida existente? "))
        except ValueError:
            print("Elija 1 o 2")
            return(new_or_load(3))
        return(opcion1)


x=new_or_load(3)
if x==1:
    pass

def game_over(estado_ganador,play):
    if estado_ganador:
        print("¿Te gustaría jugar de nuevo?\n1.Sí\n2.No")
        while True:
            try:
                opción=int(input("Opción: "))
            except ValueError:
                pass
            else:
                if opción not in [1,2]:
                    pass
                elif opción==1:
                    play=True
                    break
                else:
                    play=False
                    break

    else:
        print("FIN DEL JUEGO\n¿Qué te gustaría hacer?")
        while True:
            try:
                opción = int(input("Opción: "))
            except ValueError:
                pass
            else:
                if opción not in [1,2]:
                    pass
                elif opción == 1:
                    play = True
                    break
                else:
                    play = False
                    break
    return play


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
df_héroes.Carisma=df_héroes.Carisma.astype(float)
df_héroes.Inteligencia=df_héroes.Inteligencia.astype(float)
print(df_héroes)

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

  def __init__(self, nombre=None, hp=36, stats=None):
    Personaje.__init__(self, nombre, hp)
    self.nombre = df_héroes.Nombre[n] if nombre is None else nombre
    self.stats={
                "Carisma": df_héroes.Carisma[n],
                "Inteligencia":df_héroes.Inteligencia[n],
                "Energía": df_héroes.Energía[n],
                "Dinero": df_héroes.Dinero[n],
                "Nivel": df_héroes.Nivel[n]
                } if stats is None else stats
    self.skills=[]

  def get_skill(self, skill):
      self.skills.append(skill)

  def lvl_up(self):
    df_héroes.loc[n,"Carisma"]+=0.5
    df_héroes.loc[n,"Inteligencia"]+=0.5
    df_héroes.loc[n,"Dinero"]+=50
    df_héroes.loc[n,"Nivel"]+=1
    self.replenish()
    self.__init__()

  def replenish(self):
      df_héroes.loc[n,"Energía"]=10
      df_héroes.loc[n, "HP"]=36
      df_héroes.loc[n, "CM"]=0

play=True

while play:

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

    player=Héroe()
    completado=False

#Parte 1: Lord Borjas, 110

    repitencias=0
    aprobado=False

    while repitencias<3 and aprobado==False:

        pregunta1 = False
        pregunta2 = False
        r1 = np.random.randint(1, 11)
        r2 = np.random.randint(1, 11)
        coeficientes = np.poly([r1, r2])
        f = np.poly1d(coeficientes)

        print(f"A ver si sabe factorizar, deme uno de los ceros de este polinomio:\n\n{f}")
        if r1==r2:
            print("Uy, es una mujer desnuda.")
        try:
            y=int(input("\nRespuesta: "))
        except ValueError:
            print("Le dije que mirara su cuaderno, coño")
            repitencias+=1
        else:
            if y in [r1,r2]:
                print("Pucha, sí lee su cuaderno.")
                pregunta1=True
            else:
              print("Le dije que mirara su cuaderno, coño")
              repitencias+=1

        if pregunta1:
            x=np.random.randint(-6,6)
            print(f"\nBueno, a ver si sabe evaluar una función. Probemos con el mismo de la Pregunta 1:\n\nf(x)=\n{f}")
            print(f"\nEncuentre f({x})")
            try:
                y=int(input(f"f({x})= "))
            except ValueError:
                print("Beh, no sabe que tiene que meter números.")
                repitencias+=1
            else:
                if y==f(x):
                    print("Muy bien, cuando se gradúe me da su autógrafo.")
                    pregunta2=True
                    aprobado=True
                else:
                    print(f"Mire, que la respuesta es {y} dice JAJA.")

        if aprobado:
            print("Felicidades, siga estudiando, ahora se viene Cálculo I, métala con Donaire.")
            player.lvl_up()
        else:
            if repitencias==1:
                print("Bueno, la siguiente vez que lleve la clase nos vemos.")
            elif repitencias==2:
                print("Póngase las pilas, sólo una vez más puede llevar la clase.")
            else:
                print("Pues, siempre puede irse a estudiar Admin.")
                play=game_over(completado,play)

#Parte 2: Donaire, Cálculo I
#Parte 3: Urrutia, Cálculo II
    urrutia=Villano("Carlos Urrutia")
#Parte 4: Mark, Batalla Final (Repo Cálculo II)
    mark=Villano("Androide Mark III")