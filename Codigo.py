"""
Importacion de las librerias necesarias
"""
import csv
import time
import os
import threading
from tkinter import font
from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import serial

"""
Creacion de variables globales para poder usarlas en cualquier metodo
Ruta1: String donde se almacena la ruta del archivo1 que queremos abrir
Ruta2: String donde se almacena la ruta del archivo2 que queremos abrir
Filas_totales: entero donde se almacena el tamaño total del archivo
Generado: es una variable tipo booleano que nos dice si la tabla fue creada por primera vez o no
Tabla: es un diccionario donde se almacena toda la informacion de los archivos
Base: creacion de la interfaz grafica
frame: creacion de un frame
frame2: creacion de un frame
Letra: para darle tipo de letra y el tamaño
ModificacionOld: creacion de un arreglo que almacena fechas de modificacion de los archivos
"""
Ruta1=""
Ruta2=""
Filas_totales=0
Generado=False
Tabla={}
Base=Tk()
frame = Frame(Base)  
frame2 = Frame(Base)  
Letra = font.Font(family="Times", size=10, weight='bold')
ModificacionOld=[0,0]

"""
Creacion del metodo principal, donde llamamos a el metodo Interface
"""
def main():
    Interface()
    
"""
Creacion del metodo Arduino que recibe dos parametros, el valor que se encuentra en el pedido y en modulo.
Me permite establecer la comunicacion con el arduino, el cual recibe el valor del swiche y eso se 
ve reflejado en la accion de actualizar o no la tabla
"""
def Arduino(Valor,Modulo):
    arduino = serial.Serial('COM15', 9600)
    time.sleep(2)
    rawString = arduino.readline().decode('ascii')
    rawString=(int)(rawString)
    if(rawString==1):
        return True
    elif rawString==0:
        return False
    arduino.close()

"""
Creacion del metodo Verificar que revisa si ha sido cambiada la fecha y la almacena en el arreglo ModificacioOld
para luego cambiar este valor en la actualizacion
"""
def Verificar():
    if(ModificacionOld[0]==0):
        ModificacionOld[0]=os.path.getmtime("moduloa.txt")
        return False
    else:
        ModificacionOld[1]=(os.path.getmtime("moduloa.txt"))
        if(ModificacionOld[0]!=ModificacionOld[1]):
            ModificacionOld[0]=ModificacionOld[1]
            return True
        else:
            return False

"""
Creacion de nuestra interfaz grafica, con frames, y botones.
"""
def Interface():
    global Ruta1,Ruta2,Filas_totales,Generado,frame,Letra
    Ruta1=StringVar()
    Ruta2=StringVar()
    Base.title("Menu")
    Base.resizable(False,False)
    frame.config(width=300,height=300,relief="sunken",bd=25) 
    frame2.config(width=300,height=300,relief="sunken",bd=25,bg="#808080") 
    frame2.pack(side=BOTTOM,anchor=SW)     
    frame.pack(side=RIGHT,anchor=NW)      
    Base.configure(width=800, height=800)
    Grid.rowconfigure(frame, 0, weight=0)
    Grid.columnconfigure(frame,0, weight=0)
    Boton1=(Button(frame, text="Abrir",command=lambda:Abrir_Tablas(2),width=9, height=2,bg="snow4",borderwidth=5)).grid(row=0,column=2,sticky="nsew")
    Boton2=(Button(frame, text="Abrir",command=lambda:Abrir_Tablas(1),width=9, height=2,bg="snow4",borderwidth=5)).grid(row=1,column=2,sticky="nsew")
    Boton3=(Button(frame, text="Generar",command=lambda:Ruta_especifica(),width=6, height=1,bg="snow4",borderwidth=5)).grid(row=2,column=1,sticky="nsew")
    Label_1=Label(frame, text="Pedidos",width=10, height=2,font=Letra).grid(row=0,column=0,sticky="nsew")
    Label_2=Label(frame, text="Equivalencia",width=10, height=2,font=Letra).grid(row=1,column=0,sticky="nsew")
    entry_1=Label(frame,textvariable=Ruta2).grid(row=0,column=1,sticky="nsew")
    entry_2=Label(frame,textvariable=Ruta1).grid(row=1,column=1,sticky="nsew")
    Base.mainloop()

"""
Creacion de la tabla con la informacion de las tablas que se muestra en el frame de la parte inferior 
"""
def Tabla_Grafico():
    global Filas_totales,Letra
    if(Filas_totales>0):
        Label_2=Label(frame2, text="Total",width=10, height=2,font=Letra,fg="white",bg="black",relief="solid",borderwidth=1).grid(row=5,column=8,sticky="nsew")
        Label_3=Label(frame2, text="Pedido",width=10, height=2,font=Letra,fg="white",bg="black",relief="solid",borderwidth=1).grid(row=5,column=0,sticky="nsew")
        Label_4=Label(frame2, text="Modulo",width=10, height=2,font=Letra,fg="white",bg="black",relief="solid",borderwidth=1).grid(row=5,column=1,sticky="nsew")
        Label_5=Label(frame2, text="Posicion",width=10, height=2,font=Letra,fg="white",bg="black",relief="solid",borderwidth=1).grid(row=5,column=2,sticky="nsew")
        Label_6=Label(frame2, text="Referencia",width=10, height=2,font=Letra,fg="white",bg="black",relief="solid",borderwidth=1).grid(row=5,column=3,sticky="nsew")
        Label_7=Label(frame2, text="Cantidad",width=10, height=2,font=Letra,fg="white",bg="black",relief="solid",borderwidth=1).grid(row=5,column=4,sticky="nsew")
        Label_8=Label(frame2, text="Numero",width=10, height=2,font=Letra,fg="white",bg="black",relief="solid",borderwidth=1).grid(row=5,column=5,sticky="nsew")
        Label_9=Label(frame2, text="Fecha",width=10, height=2,font=Letra,fg="white",bg="black",relief="solid",borderwidth=1).grid(row=5,column=6,sticky="nsew")
        Label_11=Label(frame2, text="Hora",width=10, height=2,font=Letra,fg="white",bg="black",relief="solid",borderwidth=1).grid(row=5,column=7,sticky="nsew")
        
        Auxiliar=7
        for Indices in Tabla:
            Auxiliar2=0
            for Valores in Tabla[Indices]:
                cell=Label(frame2,width=10,text=Valores,relief="solid",borderwidth=1)
                cell.grid(row=Auxiliar,column=Auxiliar2)
                Auxiliar2+=1
            Auxiliar+=1
    Boton3=(tk.Button(frame, text="Actualizar",command=lambda:prueba(),width=6, height=1,bg="snow4",borderwidth=5)).grid(row=2,column=1,sticky="nsew")

"""
Creacion de los hilos
"""
def prueba():
    hilo2 = threading.Thread(target=prueba2)
    hilo2.start()

"""
Creacion de los hilos
"""
def prueba2():
    while True:
        time.sleep(2)
        if Verificar():
            Actualizar()

"""
Metodo que actualiza la tabla
"""
def Actualizar():
    Tiempo()
    Auxiliar=7
    for Indices in Tabla:
        Auxiliar2=0
        for Valores in Tabla[Indices]:
            cell=Label(frame2,text=Valores,width=10,relief="solid",borderwidth=1)
            cell.grid(row=Auxiliar,column=Auxiliar2)
            Auxiliar2+=1
        Auxiliar+=1

"""
Metodo para poder abrir los archivos que se necesitan
"""
def Abrir_Tablas(a):
    global Ruta1, Ruta2
    if (a==1) :
        Archivo= filedialog.askopenfilename(title="Abrir",initialdir="C:\\Users\james\Desktop\Programacion\Conmutacion\Parcial",filetypes=(("Ficheros de CSV","*.csv"),("Todos los archivos","*.*")))
        Ruta1.set(Archivo) 
    else:
        Archivo= filedialog.askopenfilename(title="Abrir",initialdir="C:\\Users\james\Desktop\Programacion\Conmutacion\Parcial",filetypes=(("Ficheros de CSV","*.csv"),("Todos los archivos","*.*")))
        Ruta2.set(Archivo)

"""
Metodo que selecciona la ruta especifica en el arreglo ya seleccionado
"""
def Ruta_especifica():
    global Ruta1, Ruta2
    if Generado==False:
        if((Ruta1.get()=="" or Ruta2.get()=="")or(Ruta1.get()==Ruta2.get())):
            messagebox.showinfo("Informe error","Ingresa ambas direcciones")
        else:
            Ruta1_especifica=Ruta1.get().split("/")
            Ruta2_especifica=Ruta2.get().split("/")
            Ruta1_especifica=Ruta1_especifica[len(Ruta1_especifica)-1]
            Ruta2_especifica=Ruta2_especifica[len(Ruta2_especifica)-1]
            Leer_Tablas(Ruta2_especifica,Ruta1_especifica)

"""
Metodo que lee los archivos seleccionados
"""
def Leer_Tablas(Ruta_pedidos,Ruta_equivalencias):
    global Tabla,Filas_totales,Generado
    Lista_AUX=[]
    with open(Ruta_equivalencias) as csv_File:
        csv_reader = csv.reader(csv_File,delimiter=',')
        next(csv_reader,None)
        for row in csv_reader:
            Lista_AUX.append([row[0],row[1]])

    with open(Ruta_pedidos) as File:
        reader = csv.DictReader(File)
        for row in reader:
            Filas_totales+=1
            for Union in Lista_AUX:
                if Union[0]==row['Posicion']:
                    if Filas_totales not in Tabla:
                        Tabla[Filas_totales]=[row['Pedido']]+[row['Modulo']]+[row['Posicion']]+[row['Referencia']]+[row['Cantidad']]+[Union[1]]+[0]+[0]+[0]
                    
    if(Generado==False):
        Generado=True
        Tabla_Grafico()
        
"""
Metodo que obtiene la fecha y hora del sistema cuando se hace alguna actualizacion
"""      
def Tiempo():
    Archivo=open('moduloa.txt')
    Temporal=Archivo.read()
    Temporal=Temporal.splitlines()
    Temporal=Temporal[1].split('\t')
    Modulo=Temporal[0].strip()
    Valor=Temporal[1].strip()
    if Arduino(Valor,Modulo):
        for Modulos in Tabla:
            if Modulo==Tabla[Modulos][1] and Tabla[Modulos][0]==Valor:
                print(Valor)
                print(Tabla[Modulos][0])
                Tabla[Modulos][7]= time.strftime("%X")
                Tabla[Modulos][6]= time.strftime("%d/%m/%y")
                     

main()