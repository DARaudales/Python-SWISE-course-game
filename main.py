import pandas as pd
import numpy as np
import pickle

print("                      LUCHANDO POR EL TÍTULO                         ")
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


def new_or_load(op1):
    while op1!=1 and op1!=2:
        try:
            opcion1=int(input("Desea 1) comenzar una nueva partida o 2) cargar una partida existente? "))
        except ValueError:
            print("Elija 1 o 2")
            return(new_or_load(3))
        return(opcion1)


def game_over(estado_ganador):
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
                    return True
                else:
                    return False

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
                    return True
                else:
                    return False


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
df_héroes.Dinero=df_héroes.Dinero.astype(float)

nombre_skill=["Factorización", "Cambio de Variable", "Límites", "Integral Definida", "Factorización Salvaje",
              "Cambio de Variale Turbio","Integral Definida", "Límites Multivariable", "Integración por Partes",
              "Fracciones Parciales", "Sustitución Trigonométrica", "Potencias Trigonométricas", "Método de Discos",
              "Tangente de Ángulos Medios", "Arandelas", "Cascarones Cilíndricos" ]
daño=[1,1,4,4,5,5,5,20,25,30,25,20,20,30,30,30]
cm_drain=[0,0,2,2,3,3,3,5,6,7,6,5,5,5,7,7]
cm_give=[0,0,1,1,1,1,1,1,2,2,2,2,2,3,3,3]
lvl=[1,1,2,2,2,2,2,2,3,3,3,3,3,4,4,4]

key_skiils_act = ["Nombre", "Daño", "CM Héroe", "CM Villano", "Nivel Requerido"]
value_skills_act = [nombre_skill, daño, cm_drain, cm_give, lvl]
dic_skills_act = {key:value for key, value in zip(key_skiils_act,value_skills_act)}

df_skills_act=pd.DataFrame(dic_skills_act)

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
    
    self.skills = []
    self.equipped_skills = []

  def get_skill(self, skill):
      self.skills.append(skill)

  def equip_skill(self):
      print("Selecciona las habilidades que deseas equipar.\nPara eso, ingresa el número de lista de la habilidad.")



  def lvl_up(self):
    self.stats["Carisma"]+=0.5
    self.stats["Inteligencia"] += 0.5
    self.stats["Dinero"] += 50
    self.stats["Nivel"] += 1
    self.replenish()


  def replenish(self, elección=None):
      self.stats["Energía"]=10
      self.stats["HP"]=36
      self.stats["CM"]=0

menu_ini(False)
play=True
x=new_or_load(3)
if x==1:
    pass

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

    while repitencias < 3 and aprobado == False:

        if repitencias==0:
            print("Esta es la clase de 110, soy el guardián de esta asignatura, llámeme Lord Borjas.")
            print("Aquí vamos a ver si tiene material para avanzar en la carrera.")

        while True:
            print("¿Le gustaría tomar el examen para saber si tiene lo que se necesita para llevar Cálculo I?\n1.Sí\n2.No")
            try:
                res=int(input("Respuesta: "))
            except ValueError:
                pass
            else:
                if res in [1,2]:
                    if res==1:
                        break
                    else:
                        repitencias+=1
                        if repitencias == 1:
                            print("Bueno, la siguiente vez que lleve la clase nos vemos.")
                        elif repitencias == 2:
                            print("Póngase las pilas, sólo una vez más puede llevar la clase.")
                        else:
                            print("Pues, siempre puede irse a estudiar Admin.")
                            play = game_over(completado)
                            break

        if res==1:
            
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
                        repitencias+=1

            if aprobado:
                print("Felicidades, siga estudiando, ahora se viene Cálculo I, métala con Donaire.")
                player.get_skill("Factorización")
                player.get_skill("Cambio de Variable")
                player.lvl_up()

            else:
                if repitencias==1:
                    print("Bueno, la siguiente vez que lleve la clase nos vemos.")
                elif repitencias==2:
                    print("Póngase las pilas, sólo una vez más puede llevar la clase.")
                else:
                    print("Pues, siempre puede irse a estudiar Admin.")
                    play=game_over(completado)

habilidades_pasivas=[]

def verifica_dinero(n,compra):
    if df_héroes.dinero[n]> df_tienda.Precio[compra]:
        return True
    else:
        return False

items = ["Baleadas", "Mirar su cuaderno", "Dormir"]
precio_items = ["12", "25", "20"]
descripcion = ["+3 HP", "+10 HP", "-10 CM (cansancio mental)"]

dic_items = {"Items": items, "Precio": precio_items, "Descripcion": descripcion}
df_tienda = pd.DataFrame(dic_items)

def tienda(op2):
    print("             Bienvenido a la tienda!           ")
    print(df_tienda)
    while op2!= 0 and op2!= 1 and op2!=2 and op2!=3:
        try:
            compra=int(input("Elige el numero del item que quieres comprar, si no deseas comprar escribe 3\n"))
        except ValueError:
            print("Ingresa 0, 1 ,2 o 3")
            return tienda(4)
        if compra==3:
            pass
        else:
            ajusta_dinero=verifica_dinero(n,compra)
            def agrega_items(ajusta_dinero):
                if ajusta_dinero==False:
                    print("No tienes suficiente dinero.")
                    print(f"Tus items son {habilidades_pasivas}")
                    return tienda(4)
                else:
                    print(f"Haz comprado {compra}")
                    habilidades_pasivas.append(compra)
                    print(f"Tus items son {habilidades_pasivas}")
                    return habilidades_pasivas
            agrega_items(ajusta_dinero)
tienda(4) #devuelve una lista con habilidades pasivas

#Parte 2: Donaire, Cálculo I
#Parte 3: Urrutia, Cálculo II
    urrutia=Villano("Carlos Urrutia")
#Parte 4: Mark, Batalla Final (Repo Cálculo II)
    mark=Villano("Androide Mark III")



