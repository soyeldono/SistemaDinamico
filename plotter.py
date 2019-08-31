#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from calculate import ReadEquation as RE
import matplotlib.pyplot as plt


def plotter(Yx, equation):
    fig, ax = plt.subplots()
    for i in list(Yx.keys()):
        #plt.plot(list(range(1,len(Yx[i])+1)), Yx[i])
        ax.plot(Yx[i],label=equation)
        plt.yscale('log')
        plt.grid(True)
        plt.xlabel('Y axis')
        plt.ylabel('Num of iterations')
        #plt.setp('linewidth', 2.0)
        #plt.title('Aqui va equation','equation')
   
        plt.show()


  
    
#observaciones o funciones analiticas