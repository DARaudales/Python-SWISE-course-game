import pandas as pd
import numpy as np
import pickle


#Funciones utilizadas de manera global

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


#Variables Globales

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


nombre_skill=["Factorización", "Cambio de Variable", "Límites", "Integral Indefinida", "Factorización Salvaje",
              "Cambio de Variale Turbio","Integral Definida", "Límites Multivariable", "Integración por Partes",
              "Fracciones Parciales", "Sustitución Trigonométrica", "Potencias Trigonométricas", "Método de Discos",
              "Tangente de Ángulos Medios", "Arandelas", "Cascarones Cilíndricos" ]
daño=[1,1,4,4,5,5,5,20,25,30,25,20,20,30,30,30]
cm_drain=[0,0,2,2,3,3,3,5,6,7,6,5,5,5,7,7]
cm_give=[0,0,1,1,1,1,1,1,2,2,2,2,2,3,3,3]
lvl=[1,1,2,2,2,2,2,2,3,3,3,3,3,4,4,4]

key_skills_act = ["Habilidad", "Daño", "CM Héroe", "CM Villano", "Nivel Requerido"]
value_skills_act = [nombre_skill, daño, cm_drain, cm_give, lvl]
dic_skills_act = {key:value for key, value in zip(key_skills_act,value_skills_act)}

df_skills_act=pd.DataFrame(dic_skills_act)


nombre_skill_pas=["'Mire su cuaderno'", "Guía Metodológica Calc II", "Fórmula del Haragán", "Pautas viejas",
                  "Tutorías", "Hacer curva", "Pagar para pasar"]
hp_give=[0,0,0,0,15,25,36]
cm_reduce=[10,20,20,30,25,0,100]
precio_base=[10,25,25,50,75,100,500]
precio_real=[10,25,25,50,75,100,500]

key_skills_pas=["Ítem", "Puntos", "Cansancio Aliviado","Precio_Base","Precio_Real"]
value_skills_pas=[nombre_skill_pas, hp_give, cm_reduce, precio_base, precio_real]
dic_skills_pas= {key:value for key, value in zip(key_skills_pas,value_skills_pas)}

df_skills_pas=pd.DataFrame(dic_skills_pas)
df_skills_pas.Precio_Base=df_skills_pas.Precio_Base.astype(float)
df_skills_pas.Precio_Real=df_skills_pas.Precio_Real.astype(float)

'''
print (df_héroes)
print (df_skills_act)
print(df_skills_pas)'''


#Clases

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
                "Nivel": df_héroes.Nivel[n],
                } if stats is None else stats
    
    self.skills = []

    keys=["Habilidad", "Daño", "CM Héroe", "CM Villano"]
    values=[]
    dic_act={key:value for key, value in zip(keys,values)}
    self.act_skills=pd.DataFrame(dic_act)

    keys_p = ["Ítem", "Puntos", "Cansancio Aliviado"]
    dic_pas = {key: value for key, value in zip(keys_p, values)}
    self.pas_skills = pd.DataFrame(dic_pas)

    dic_acte={key:value for key, value in zip(keys,values)}
    self.equipped_actskills=pd.DataFrame(dic_acte)

    dic_pase={key: value for key, value in zip(keys_p, values)}
    self.equipped_passkills=pd.DataFrame(dic_pase)

  def get_actskill(self, num_lista):
    print(f"Has obtenido la habilidad {df_skills_act.loc[num_lista,'Habilidad']}.")
    self.skills.append(df_skills_act.loc[num_lista,'Habilidad'])
    self.act_skills=self.act_skills.append(df_skills_act.loc[num_lista],ignore_index=True, sort=False)

  def get_passkill(self, num_lista):
    print(f"Has obtenido la habilidad {df_skills_pas.loc[num_lista,'Ítem']}.")
    self.skills.append(df_skills_pas.loc[num_lista,'Ítem'])
    self.pas_skills = self.pas_skills.append(df_skills_pas.loc[num_lista], ignore_index=True)

  def equip_skill(self):
    print("Selecciona las habilidades que deseas equipar.\nPara eso, ingresa el número de lista de la habilidad.")

  def cansancio(self,fatigue):
    self.cm+=fatigue
    
  def compras(self,dinero):
    self.stats["Dinero"]+=-dinero


  def lvl_up(self):
    self.stats["Carisma"]+=0.5
    self.stats["Inteligencia"] += 0.5
    self.stats["Dinero"] += 50
    self.stats["Nivel"] += 1
    self.replenish()


  def replenish(self):
    self.stats["Energía"]=10
    self.hp=36
    self.cm=0

n=1
player=Héroe()
player.get_actskill(0)
print(player.skills)
print(player.act_skills)


print("                      LUCHANDO POR EL TÍTULO                         ")
print(" --------------------------------------------------------------------")
print("   Ayuda                      Jugar                         Creditos")

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

    if player.stats["Nivel"]==1:
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
                    player.get_actskill(0)
                    player.get_actskill(1)
                    player.lvl_up()

                else:
                    if repitencias == 1:
                        print("Bueno, la siguiente vez que lleve la clase nos vemos.")
                    elif repitencias == 2:
                        print("Póngase las pilas, sólo una vez más puede llevar la clase.")
                    else:
                        print("Pues, siempre puede irse a estudiar Admin.")
                        play = game_over(completado)

#Parte 2: Donaire, Cálculo I
    repitencias=0

    if player.stats["Nivel"]==2:

        print("Donaire:Buen día señor, bienvenido a la asignatura de calculo I, que bueno que la metió con el ingeniero. \n Vaya a darle like a Team Donaire en facebook.\n")
        print("Donaire:Espero que haya aprendido mucho en 110, lo necesitará\n")
        print("Donaire:Lo primero es que vaya a comprar la guía metodológica,solo vale L.25 no debería ser problema para usted\n")
        print("Donaire:Con esta aprenderá a a calcular limites e integrales indefinidas\n")
        print("Luego de caminar hasta la fotocopiadora del F1.... \n")
        print("Vendedor:Por supuesto que tenemos la guía metódológica de Calculo I, pero no recuerdo cuanto costaba...¿Le dijo su profesor de casualidad? ")
        precio=float(input("Sí, me dijo que costaban:"))
        while(precio != 25):
            if precio>25:
                print("Vendedor: Mmmmm, no lo sé no creo que sean tan caras\n")
                precio=int(input("Cierto, a lo mejor es:"))
            elif precio<25:
                print("Vendedor: Nambe, no son tan baratos, no se quiera pasar de listo\n")
                precio=int(input("Disculpe, de verdad pensé que era ese. Ya recordé, era:"))
            else:
                print("Vendedor: Exacto, ese era el precio\n")

        player.get_actskill(2)
        player.get_actskill(3)
        player.compras(-25)
        print("Al siguiente día en clase...\n")
        print("Donaire: ¡Que bien!, se nota que adquirió la guía metodológica")
        print("Donaire: Lo siguiente que deberá hacer es revisar mi canal de Youtube 'Team Donaire' \n")
        print("Luego de pasar un tiempo viendo videos el cansancio mental subió...\n")
        player.cansancio(20)
        player.get_actskill(4)
        player.get_actskill(5)
        print("Al siguiente día en clase...\n")
        print("Donaire:Veo que aprendió mucho viendo los videos de Team Donaire, es tiempo de descansar un poco.\n")
        print("Donaire:Hoy juega en la champions el barca, vea el partido y luego estará listo para aprender el segundo teorema fundamental del calculo\n")
        print("Al llegar a casa...")
        print("¿Desea ver el partido?")
        vio_partido=input("Ingrese 'si' o 'no':")
        
        if vio_partido=="si":
            print("Que buen partido, el barca metió 2 goles")
        
        print("Al siguiente día....")
        print("Donaire:¿Cómo está Señor? A ver si vió el partido ayer...")
        goles=int(input("¿Cuántos goles metió el barca?:"))
        if goles==2:
            print("Donaire:Sí vió el partido, está listo para aprender el segundo teorema fundamental del calculo")
            player.get_actskill(6)
            print("Donaire:Está listo para calculo II señor, me temo que los maestros no serán tan amigables como yo")
        else:
            print("Donaire:Nambe señor, no vió el partido, le dije que necesitaba relajarse, vaya a comprar unos chicken fingers al CC")
            print("Luego de caminar hasta el CC...")
            print("Cubano: Hola chico, claro que tenemos los mejores chicken fingers, de L.70,L.100 y L.120")
            print("Cubano: ¿Solo le quedan L.25? Bueno, supongo que le puedo vender un ala y 7 papas por eso")
            comprar_fingers=input("¿Desea Aceptar? Ingrese 'si' o 'no':")
            if comprar_fingers=="si":
                player.compras(-25)
                print(player.stats["Dinero"])
            print("De vuelta en el aula de Donaire...")
            print("Donaire:¿Comió señor? es necesario para aprender,muestreme su billetera a ver si uso su dinero en comida...")
            if player.stats["Dinero"]==0:
                print("Donaire:Muy bien señor, está listo para aprender el segundo teorema fundamental del calculo")
                player.get_actskill("Integral Definida")
                print("Donaire:Está listo para calculo II señor, me temo que los maestros no serán tan amigables como yo")
            else:
                print("Donaire: Le dije que comiera señor, así no podrá comprender el segundo teorema fundamental del calculo, me temo que eso es todo")
                play=game_over(completado)
                
'''
#Parte 3: Urrutia, Cálculo II
    urrutia=Villano("Carlos Urrutia")
#Parte 4: Mark, Batalla Final (Repo Cálculo II)
    mark=Villano("Androide Mark III")


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
    return tienda(4) #devuelve una lista con habilidades pasivas

#Parte 2: Donaire, Cálculo I
#Parte 3: Urrutia, Cálculo II
    urrutia=Villano("Carlos Urrutia")
#Parte 4: Mark, Batalla Final (Repo Cálculo II)
    mark=Villano("Androide Mark")
'''

