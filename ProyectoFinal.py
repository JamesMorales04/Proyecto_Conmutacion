from tkinter import ttk
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

class Proyecto():

    Base=Tk()
    Ruta=[StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar()]
    Generado=False

    def Panel_Principal(self):
        self.Base.title("Almacenamiento")
        self.Base.minsize(1366,1080)
        Proyecto.Crear_Pestañas()
        self.Base.mainloop()

    @classmethod
    def Crear_Pestañas(self):
        Pestañas=ttk.Notebook()
        Pestaña1=Frame(Pestañas)
        Pestaña2=Frame(Pestañas,bg="#C0DFFE")
        Proyecto.Rutas(Pestaña2)
        Pestañas.add(Pestaña1, text='Principal')
        Pestañas.add(Pestaña2, text='Rutas')
        Pestañas.pack(expan=1,fill='both')

    @classmethod
    def Rutas(self,Frame):
        Separadores=Label(Frame,width=60, height=2,bg="#C0DFFE").grid(row=0,column=0,sticky="wsn")
        Separadores2=Label(Frame,width=60, height=2,bg="#C0DFFE").grid(row=1,column=0,sticky="wsn")

        Boton1=(Button(Frame, text="Abrir",command=lambda:Proyecto.Abrir_Tablas(0),width=4, height=1,bg="snow4",borderwidth=5)).grid(row=2,column=2,sticky="nsew")
        Boton2=(Button(Frame, text="Abrir",command=lambda:Proyecto.Abrir_Tablas(1),width=4, height=1,bg="snow4",borderwidth=5)).grid(row=5,column=2,sticky="nsew")
        Boton3=(Button(Frame, text="Abrir",command=lambda:Proyecto.Abrir_Tablas(2),width=4, height=1,bg="snow4",borderwidth=5)).grid(row=8,column=2,sticky="nsew")
        Boton4=(Button(Frame, text="Abrir",command=lambda:Proyecto.Abrir_Tablas(3),width=4, height=1,bg="snow4",borderwidth=5)).grid(row=11,column=2,sticky="nsew")
        Boton5=(Button(Frame, text="Abrir",command=lambda:Proyecto.Abrir_Tablas(4),width=4, height=1,bg="snow4",borderwidth=5)).grid(row=14,column=2,sticky="nsew")
        Boton6=(Button(Frame, text="Abrir",command=lambda:Proyecto.Abrir_Tablas(5),width=4, height=1,bg="snow4",borderwidth=5)).grid(row=17,column=2,sticky="nsew")
        
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



    @classmethod
    def Ruta_especifica(self):
        if self.Generado==False:
            if((self.Ruta[0].get()=="" or self.Ruta[1].get()=="")or(self.Ruta[0].get()==self.Ruta[1].get())):
                messagebox.showinfo("Informe error","Ingresa ambas direcciones")
            else:
                Ruta1_especifica=self.Ruta[0].get().split("/")
                Ruta2_especifica=self.Ruta[1].get().split("/")
                Ruta1_especifica=Ruta1_especifica[len(Ruta1_especifica)-1]
                Ruta2_especifica=Ruta2_especifica[len(Ruta2_especifica)-1]                

    @classmethod
    def Abrir_Tablas(self,a):  
        Archivo= filedialog.askopenfilename(title="Abrir",initialdir="C:\\Users\james\Desktop\Programacion\Conmutacion\Parcial",filetypes=(("Ficheros de CSV","*.csv"),("Todos los archivos","*.*")))
        self.Ruta[a].set(Archivo) 

Cosa=Proyecto()
Cosa.Panel_Principal()