import matplotlib.pyplot as plt
import numpy as np


class pipx:
    def __init__(self):
        
        self.Ndar = 1000
        self.dardos_en_circulo = 0
        self.xDen = []
        self.yDen = []
        self.xFu = []
        self.yFu = []

    def oper(self):
        for _ in range(self.Ndar):
            x, y = np.random.uniform(-1, 1), np.random.uniform(-1, 1)  
            distancia_al_centro = np.sqrt(x**2 + y**2) 
            if distancia_al_centro <= 1:  
                self.dardos_en_circulo += 1
                self.xDen.append(x)
                self.yDen.append(y)
            else:
                self.xFu.append(x)
                self.yFu.append(y)

      
        pi_aprox = 4 * self.dardos_en_circulo / self.Ndar

        print(f"Aproximación de Pi usando el método de Monte Carlo: {pi_aprox}")
        self.grafico()
    def grafico(self):
        
        fig,ax = plt.subplots()
        ax.set_aspect('equal')
        ax.scatter(self.xDen, self.yDen, color='y', label='Dardos adentro del círculo')
        ax.scatter(self.xFu, self.yFu, color='g', label='Dardos  fuera del círculo')
        plt.legend()
        plt.show()
objeto=pipx()
objeto.oper()







