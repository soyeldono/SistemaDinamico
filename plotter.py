#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from calculate import ReadEquation as RE
import matplotlib.pyplot as plt


def plotter(Yx, equation): #Crea una funcion para el plotter donde llevara los parametros obligatorios Xy que es el diccionario de los valores del eje Y a graficar y equation que es la ecuacion ingresada y que sera agregada como titulo
    fig, ax = plt.subplots() #Asigna la variable fig y ax a los subplot para graficar los valores de la Y, aun no se usa fig
    for i in list(Yx.keys()): #ciclo que recorre todas las llaves de los diccionarios
        #plt.plot(list(range(1,len(Yx[i])+1)), Yx[i])
        ax.plot(Yx[i],label=equation) # hace las graficas para todos los valores que contienen las llaves, o sea los valores de Y
        plt.yscale('log') #Escala las graficas 
        plt.grid(True) #Hace una cuadricula en la figura
        plt.xlabel('Y axis') #Etiqueta del eje X, aun no esta definida
        plt.ylabel('Num of iterations') #Etiqueta del eje Y, aun no esta definida
        #plt.setp('linewidth', 2.0)
        #plt.title('Aqui va equation','equation')
   
        plt.show() #muestra la grafica


  
    
#observaciones o funciones analiticas: ignorar esto.