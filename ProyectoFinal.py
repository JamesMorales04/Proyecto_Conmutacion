import serial
import serial.tools.list_ports
import csv
import time
import os
import threading
import tkinter as tk
from tkinter import *
from tkinter import font
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox


class Proyecto():

    Base=Tk()
    Ruta=[StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar()]
    Generado=False
    Tabla={}
    Filas_totales=0
    Pestañas=ttk.Notebook()
    Pestaña1=Frame(Pestañas,bg="#C0DFFE")
    Puertos=["Cosa","Cosa1","Cosa2","Cosa3"]
    Estado=[StringVar(),StringVar(),StringVar(),StringVar()]
    Pedido=[StringVar(),StringVar(),StringVar(),StringVar()]
    ModificacionOld=[[0,0],[0,0],[0,0],[0,0]]
    Ventana = Frame(Pestaña1)  
    Ventana2 = Frame(Pestaña1)  
    Canvas=tk.Canvas(Ventana)
    Ventana3 = Frame(Canvas)  

    def Panel_Principal(self):
        self.Base.title("Almacenamiento")
        self.Base.minsize(1366,768)
        Proyecto.Crear_Pestañas()
        self.Base.protocol("WM_DELETE_WINDOW", self.Guardar)
        self.Base.mainloop()

    @classmethod
    def Crear_Pestañas(self):
       
        Pestaña2=Frame(self.Pestañas,bg="#C0DFFE")
        Proyecto.Rutas(Pestaña2)
        self.Pestañas.add(self.Pestaña1, text='Principal')
        self.Pestañas.add(Pestaña2, text='Rutas')
        self.Pestañas.pack(expan=1,fill='both')

    @classmethod
    def Rutas(self,Frame):
    
        Separadores=Label(Frame,width=60, height=2,bg="#C0DFFE").grid(row=0,column=0,sticky="wsn")
        Separadores2=Label(Frame,width=60, height=2,bg="#C0DFFE").grid(row=1,column=0,sticky="wsn")
        foto=PhotoImage(file="580b57fcd9996e24bc43c4c5.png")
        foto = foto.subsample(15)
        Boton1 = Button(Frame, text ="",command=lambda:Proyecto.Abrir_Tablas(0),bg="#C0DFFE")
        Boton1.image = foto   
        Boton1.config(image=foto)
        Boton1.grid(row=2,column=2,sticky="nsew")
        Boton2 = Button(Frame, text ="",command=lambda:Proyecto.Abrir_Tablas(1),bg="#C0DFFE")
        Boton2.image = foto   
        Boton2.config(image=foto)
        Boton2.grid(row=5,column=2,sticky="nsew")
        Boton3 = Button(Frame, text ="",command=lambda:Proyecto.Abrir_Tablas(2),bg="#C0DFFE")
        Boton3.image = foto   
        Boton3.config(image=foto)
        Boton3.grid(row=8,column=2,sticky="nsew")
        Boton4 = Button(Frame, text ="",command=lambda:Proyecto.Abrir_Tablas(3),bg="#C0DFFE")
        Boton4.image = foto   
        Boton4.config(image=foto)
        Boton4.grid(row=11,column=2,sticky="nsew")
        Boton5 = Button(Frame, text ="",command=lambda:Proyecto.Abrir_Tablas(4),bg="#C0DFFE")
        Boton5.image = foto   
        Boton5.config(image=foto)
        Boton5.grid(row=14,column=2,sticky="nsew")
        Boton6 = Button(Frame, text ="",command=lambda:Proyecto.Abrir_Tablas(5),bg="#C0DFFE")
        Boton6.image = foto   
        Boton6.config(image=foto)
        Boton6.grid(row=17,column=2,sticky="nsew")
        Boton7=(Button(Frame, text="Generar",command=lambda:Proyecto.Ruta_especifica(),width=4, height=1,bg="snow4",borderwidth=5)).grid(row=19,column=1,sticky="nsew")

        Label_1=Label(Frame, text="Seleccione el Archivo de Pedidos",width=30, height=2,bg="#C0DFFE",font='Helvetica 10 bold').grid(row=1,column=1,sticky="wsn")
        Label_2=Label(Frame, text="Seleccione la Tabla de Equivalencias",width=30, height=2,bg="#C0DFFE",font='Helvetica 10 bold').grid(row=4,column=1,sticky="wsn")
        Label_3=Label(Frame, text="Seleccione la Ruta del Modulo A",width=30, height=2,bg="#C0DFFE",font='Helvetica 10 bold').grid(row=7,column=1,sticky="wsn")
        Label_4=Label(Frame, text="Seleccione la Ruta del Modulo B",width=30, height=2,bg="#C0DFFE",font='Helvetica 10 bold').grid(row=10,column=1,sticky="wsn")
        Label_5=Label(Frame, text="Seleccione la Ruta del Modulo C",width=30, height=2,bg="#C0DFFE",font='Helvetica 10 bold').grid(row=13,column=1,sticky="wsn")
        Label_6=Label(Frame, text="Seleccione la Ruta del Modulo D",width=30, height=2,bg="#C0DFFE",font='Helvetica 10 bold').grid(row=16,column=1,sticky="wsn")

        entry_1=Label(Frame,textvariable=self.Ruta[0],bg="#FFFFFF",borderwidth=2,relief="sunken",width=90, height=1,).grid(row=2,column=1,sticky="nsew")
        entry_2=Label(Frame,textvariable=self.Ruta[1],bg="#FFFFFF",borderwidth=2,relief="sunken",width=90, height=1).grid(row=5,column=1,sticky="nsew")
        entry_3=Label(Frame,textvariable=self.Ruta[2],bg="#FFFFFF",borderwidth=2,relief="sunken",width=90, height=1,).grid(row=8,column=1,sticky="nsew")
        entry_4=Label(Frame,textvariable=self.Ruta[3],bg="#FFFFFF",borderwidth=2,relief="sunken",width=90, height=1).grid(row=11,column=1,sticky="nsew")
        entry_5=Label(Frame,textvariable=self.Ruta[4],bg="#FFFFFF",borderwidth=2,relief="sunken",width=90, height=1,).grid(row=14,column=1,sticky="nsew")
        entry_6=Label(Frame,textvariable=self.Ruta[5],bg="#FFFFFF",borderwidth=2,relief="sunken",width=90, height=1,).grid(row=17,column=1,sticky="nsew")
        
        Separadores3=Label(Frame,width=60, height=2,bg="#C0DFFE").grid(row=3,column=1,sticky="wsn")
        Separadores4=Label(Frame,width=60, height=2,bg="#C0DFFE").grid(row=6,column=1,sticky="wsn")
        Separadores5=Label(Frame,width=60, height=2,bg="#C0DFFE").grid(row=9,column=1,sticky="wsn")
        Separadores6=Label(Frame,width=60, height=2,bg="#C0DFFE").grid(row=12,column=1,sticky="wsn")
        Separadores6=Label(Frame,width=60, height=2,bg="#C0DFFE").grid(row=15,column=1,sticky="wsn")
        Separadores6=Label(Frame,width=60, height=2,bg="#C0DFFE").grid(row=18,column=1,sticky="wsn")



    @classmethod
    def Ruta_especifica(self):
        if self.Generado==False:
            if((self.Ruta[0].get()=="" or self.Ruta[1].get()=="" )):
                messagebox.showinfo("Informe error","Falta de datos o datos repetidos")
            else:
                Proyecto.Leer_Tablas(self)
    
    def Leer_Tablas(self):
        Lista_AUX=[]
        with open(self.Ruta[1].get()) as csv_File:
            csv_reader = csv.reader(csv_File)
            next(csv_reader,None)
            for row in csv_reader:
                row=row[0].split(';')
                Lista_AUX.append([row[0],row[1]])

        with open(self.Ruta[0].get()) as csv_File:
            csv_reader = csv.reader(csv_File)
            next(csv_reader,None)
            for row in csv_reader:
                row=row[0].split(';')
                self.Filas_totales+=1
                for Union in Lista_AUX:
                    if Union[0]==row[2]:
                        if self.Filas_totales not in self.Tabla:
                            self.Tabla[self.Filas_totales]=[row[0]]+[row[1]]+[row[2]]+[row[3]]+[row[4]]+[Union[1]]+[StringVar()]+[StringVar()]+[0]
                    
        if(self.Generado==False):
            self.Generado=True
            Proyecto.Tabla_Grafico()

    @classmethod
    def Tabla_Grafico(self):

        if(self.Filas_totales>0):
            self.Ventana2.config(width=600,height=600,relief="sunken",bd=25,bg="#808080") 
            self.Ventana2.grid(row=0,column=1,sticky="s")
            self.Ventana.config(width=1000,height=1000,relief="sunken",bd=25,bg="#808080") 
            self.Ventana.grid(row=2,column=1,sticky="s")

            scroll=tk.Scrollbar(self.Ventana)
            self.Canvas.configure(yscrollcommand=scroll.set,width=650,height=400)
            scroll.config(command=self.Canvas.yview)
            scroll.pack(side="right",fill=Y)
            self.Ventana3=Frame(self.Canvas,width=1000,height=1000)
            ports=[StringVar(),StringVar(),StringVar(),StringVar()]
            ports[0].set("Elige")
            ports[1].set("Elige")
            ports[2].set("Elige")
            ports[3].set("Elige")
            puertos1=serial.tools.list_ports.comports()
            aux=0
            for puerto in puertos1:
                self.Puertos.append(str(puerto))
                aux+=1
            Menu1=OptionMenu(self.Ventana2,ports[0],*self.Puertos)
            Menu1.config(width=10, height=2)
            Menu1.grid(row=5,column=0,sticky="ewsn")
            Menu2=OptionMenu(self.Ventana2,ports[1],*self.Puertos)
            Menu2.config(width=10, height=2)
            Menu2.grid(row=5,column=1,sticky="wsne")
            Menu3=OptionMenu(self.Ventana2,ports[2],*self.Puertos)
            Menu3.config(width=10, height=2)
            Menu3.grid(row=5,column=2,sticky="esnw")
            Menu4=OptionMenu(self.Ventana2,ports[3],*self.Puertos)
            Menu4.config(width=10, height=2)
            Menu4.grid(row=5,column=3,sticky="senw")

            Label_2=Label(self.Ventana2, text="Enviado_A",width=20, height=2,fg="white",bg="black",relief="solid",borderwidth=1).grid(row=0,column=0,sticky="ns")
            Label_2=Label(self.Ventana2, text="Enviado_B",width=20, height=2,fg="white",bg="black",relief="solid",borderwidth=1).grid(row=0,column=1,sticky="ens")
            Label_2=Label(self.Ventana2, text="Enviado_C",width=20, height=2,fg="white",bg="black",relief="solid",borderwidth=1).grid(row=0,column=2,sticky="ns")
            Label_2=Label(self.Ventana2, text="Enviado_D",width=20, height=2,fg="white",bg="black",relief="solid",borderwidth=1).grid(row=0,column=3,sticky="wns")

            Label_2=Label(self.Ventana2,textvariable=self.Estado[0],width=20, height=2,fg="black",bg="white",relief="solid",borderwidth=1).grid(row=1,column=0,sticky="ns")
            Label_2=Label(self.Ventana2, textvariable=self.Estado[1],width=20, height=2,fg="black",bg="white",relief="solid",borderwidth=1).grid(row=1,column=1,sticky="ens")
            Label_2=Label(self.Ventana2, textvariable=self.Estado[2],width=20, height=2,fg="black",bg="white",relief="solid",borderwidth=1).grid(row=1,column=2,sticky="ns")
            Label_2=Label(self.Ventana2, textvariable=self.Estado[3],width=20, height=2,fg="black",bg="white",relief="solid",borderwidth=1).grid(row=1,column=3,sticky="wns")

            Label_2=Label(self.Ventana2, text="Pedido A",width=20, height=2,fg="white",bg="black",relief="solid",borderwidth=1).grid(row=2,column=0,sticky="ns")
            Label_2=Label(self.Ventana2, text="Pedido B",width=20, height=2,fg="white",bg="black",relief="solid",borderwidth=1).grid(row=2,column=1,sticky="ens")
            Label_2=Label(self.Ventana2, text="Pedido C",width=20, height=2,fg="white",bg="black",relief="solid",borderwidth=1).grid(row=2,column=2,sticky="ns")
            Label_2=Label(self.Ventana2, text="Pedido D",width=20, height=2,fg="white",bg="black",relief="solid",borderwidth=1).grid(row=2,column=3,sticky="wns")

            
            Label_2=Label(self.Ventana2, textvariable=self.Pedido[0],width=20, height=2,fg="black",bg="white",relief="solid",borderwidth=1).grid(row=3,column=0,sticky="ns")
            Label_2=Label(self.Ventana2, textvariable=self.Pedido[1],width=20, height=2,fg="black",bg="white",relief="solid",borderwidth=1).grid(row=3,column=1,sticky="ens")
            Label_2=Label(self.Ventana2, textvariable=self.Pedido[2],width=20, height=2,fg="black",bg="white",relief="solid",borderwidth=1).grid(row=3,column=2,sticky="ns")
            Label_2=Label(self.Ventana2, textvariable=self.Pedido[3],width=20, height=2,fg="black",bg="white",relief="solid",borderwidth=1).grid(row=3,column=3,sticky="wns")

            Label_2=Label(self.Ventana2, text="VISA Modulo A",width=20, height=2,fg="white",bg="black",relief="solid",borderwidth=1).grid(row=4,column=0,sticky="ns")
            Label_2=Label(self.Ventana2, text="VISA Modulo B",width=20, height=2,fg="white",bg="black",relief="solid",borderwidth=1).grid(row=4,column=1,sticky="ens")
            Label_2=Label(self.Ventana2, text="VISA Modulo C",width=20, height=2,fg="white",bg="black",relief="solid",borderwidth=1).grid(row=4,column=2,sticky="ns")
            Label_2=Label(self.Ventana2, text="VISA Modulo D",width=20, height=2,fg="white",bg="black",relief="solid",borderwidth=1).grid(row=4,column=3,sticky="wns")

            Label_2=Label(self.Ventana3, text="Total",width=10, height=2,fg="white",bg="black",relief="solid",borderwidth=1).grid(row=3,column=9,sticky="nsew")
            Label_3=Label(self.Ventana3, text="Pedido",width=10, height=2,fg="white",bg="black",relief="solid",borderwidth=1).grid(row=3,column=1,sticky="nsew")
            Label_4=Label(self.Ventana3, text="Modulo",width=10, height=2,fg="white",bg="black",relief="solid",borderwidth=1).grid(row=3,column=2,sticky="nsew")
            Label_5=Label(self.Ventana3, text="Posicion",width=10, height=2,fg="white",bg="black",relief="solid",borderwidth=1).grid(row=3,column=3,sticky="nsew")
            Label_6=Label(self.Ventana3, text="Referencia",width=10, height=2,fg="white",bg="black",relief="solid",borderwidth=1).grid(row=3,column=4,sticky="nsew")
            Label_7=Label(self.Ventana3, text="Cantidad",width=10, height=2,fg="white",bg="black",relief="solid",borderwidth=1).grid(row=3,column=5,sticky="nsew")
            Label_8=Label(self.Ventana3, text="Numero",width=10, height=2,fg="white",bg="black",relief="solid",borderwidth=1).grid(row=3,column=6,sticky="nsew")
            Label_9=Label(self.Ventana3, text="Fecha",width=10, height=2,fg="white",bg="black",relief="solid",borderwidth=1).grid(row=3,column=7,sticky="nsew")
            Label_11=Label(self.Ventana3, text="Hora",width=10, height=2,fg="white",bg="black",relief="solid",borderwidth=1).grid(row=3,column=8,sticky="nsew")

            Separadores=Label(self.Pestaña1,width=55, height=2,bg="#C0DFFE").grid(row=0,column=0,sticky="wsn")
            Separadores=Label(self.Pestaña1,width=40, height=2,bg="#C0DFFE").grid(row=1,column=1,sticky="wsn")

            Auxiliar=8
            for Indices in self.Tabla:
                Auxiliar2=1
                for Valores in self.Tabla[Indices]:
                    if Auxiliar2==7 or Auxiliar2==8:
                        cell=Label(self.Ventana3,width=10,textvariable=Valores,relief="solid",borderwidth=1)
                        cell.grid(row=Auxiliar,column=Auxiliar2)
                        Auxiliar2+=1
                    else:
                        cell=Label(self.Ventana3,width=10,text=Valores,relief="solid",borderwidth=1)
                        cell.grid(row=Auxiliar,column=Auxiliar2)
                        Auxiliar2+=1
                Auxiliar+=1
            self.Canvas.create_window(0,0,window=self.Ventana3,anchor="nw")
            self.Canvas.pack(side="left",fill="both",expand=True)
            self.Ventana.update()
            self.Canvas.config(scrollregion=self.Canvas.bbox("all"))
            Proyecto.prueba()

    @classmethod
    def Verificar(self):
        Aux=0
        
        Posicion=0
        Estados=[False,False,False,False]
        for Modulos in range(2,6):
            if(self.ModificacionOld[Aux][0]==0):
                self.ModificacionOld[Aux][0]=os.path.getmtime(self.Ruta[Modulos].get())
                Estados[Aux]=False
            else:
                self.ModificacionOld[Aux][1]=(os.path.getmtime(self.Ruta[Modulos].get()))
                if(self.ModificacionOld[Aux][0]!=self.ModificacionOld[Aux][1]):
                    self.ModificacionOld[Aux][0]=self.ModificacionOld[Aux][1]
                    Posicion=Modulos
                else:
                    Estados[Aux]=False
            Aux+=1
        return Posicion
    @classmethod
    def Actualizar(self,Modulo):
        Proyecto.Tiempo(Modulo)
    @classmethod
    def prueba(self):
        hilo2 = threading.Thread(target=Proyecto.prueba2)
        hilo2.start()
    @classmethod
    def Tiempo(self,Modu):       
        Archivo=open(self.Ruta[Modu].get())
        Temporal=Archivo.read()
        Temporal=Temporal.splitlines()
        Temporal=Temporal[1].split('\t')
        Modulo=Temporal[0].strip()
        Valor=Temporal[1].strip()

        
        if Modulo=='A':
            self.Estado[0].set("Enviado")
            self.Pedido[0].set(Valor)
        elif Modulo=='B':
            self.Estado[1].set("Enviado")
            self.Pedido[1].set(Valor)
        elif Modulo=='C':
            self.Estado[2].set("Enviado")
            self.Pedido[2].set(Valor)
        else:
            self.Estado[3].set("Enviado")
            self.Pedido[3].set(Valor)


        for Modulos in self.Tabla:
            if Modulo==self.Tabla[Modulos][1] and self.Tabla[Modulos][0]==Valor:
                print(Valor)
                print(self.Tabla[Modulos][0])
                self.Tabla[Modulos][7].set(time.strftime("%X"))
                self.Tabla[Modulos][6].set(time.strftime("%d/%m/%y"))
    @classmethod
    def prueba2(self):
        while True:
            Valor=Proyecto.Verificar()
            if Valor != 0:
                Proyecto.Actualizar(Valor)
                
    @classmethod
    def Abrir_Tablas(self,a):  
        Archivo= filedialog.askopenfilename(title="Abrir",initialdir="C:\\Users\Desktop")
        self.Ruta[a].set(Archivo) 
    @classmethod
    def Guardar(self):  
        csv=open("BackUp.csv","w")
        for key in self.Tabla:
            fila=0
            contador=1
            for Valores_Tabla in self.Tabla[key]:
                if contador==7 or contador==8:
                    fila=str(fila)+str(Valores_Tabla.get())+";"
                else:
                    fila=str(fila)+str(Valores_Tabla)+";"
                contador+=1
            csv.write(fila+";"+"\n")
        self.Base.destroy()
        
    @classmethod
    def Arduino(self):
        cosa=b"Holi"
        ###establece Conexion con arduino
        for Coms in self.Puertos:
            PuertoSerie = serial.Serial(Coms, 9600, timeout=1.0)
            time.sleep(1.8)
        ####Envia y recibe String a/de arduino
        cadena = cosa
        print("Python " ,cadena.decode('ASCII'))
        PuertoSerie.write(cadena)
        if(PuertoSerie.readline().decode('ASCII')==cadena):
            return True
        else:
            return False

        #####Cierra conexion
        PuertoSerie.close()



Cosa=Proyecto()
Cosa.Panel_Principal()