# Author: Maycon Meier 
# Source: https://en.wikipedia.org/wiki/Shear_modulus

# Description: Computes all property values for a given material

# Parameters: Provide at least 2 from K, G, E, lame, Poisson
# Attribuites: K, G, E, lame, Poisson, display, display_long
# Methods: UpdateAll, BulkModulus, YoungModulus, LameFirst, ShearModulus, vPoisson

# Usage: from material import material; variable_name = material(K = num1, G = num2); variable_name.display

import numpy as np

class material: 
    def __init__(self, K = -1, E = -1, lame = -1, G = -1, Poisson = -1):
        self.K = K
        self.E = E
        self.lame = lame 
        self.G = G
        self.Poisson = Poisson 

        count = 0
        for i in [self.K, self.E, self.lame, self.G, self.Poisson]:
            if i == -1:
                count += 1
        if count > 3:
            raise TypeError("Provide at least two property values from the list: (K, E, G, lame, Poisson)")

        self.var = ""
        if   (self.K >= 0):
            if   (self.E >= 0): self.var = "K,E"
            elif (self.lame >= 0): self.var = "K,lame"
            elif (self.G >= 0): self.var = "K,G"
            elif (self.Poisson >= 0): self.var = "K,Poisson"
        elif (self.E >= 0): 
            if   (self.lame >= 0): self.var = "E,lame"
            elif (self.G >= 0): self.var = "E,G"
            elif (self.Poisson >= 0): self.var = "E,Poisson"
        elif (self.lame >= 0):
            if   (self.G >= 0): self.var = "lame,G"
            elif (self.Poisson >= 0): self.var = "lame,Poisson"
        elif (self.G >= 0 and self.Poisson >= 0): self.var = "G,Poisson"
        else: raise TypeError("Wrong Input Parameters")

        self.UpdateAll()

        self.display = "Bulk Modulus = " + str(float("{:.2f}".format(self.K)))  + " | Young Modulus = " + str(float("{:.2f}".format(self.E))) + " | Shear Modulus = " + str(float("{:.2f}".format(self.G))) + " | Lame First Parameter = " + str(float("{:.2f}".format(self.lame))) + " | Poisson Coeficient = " + str(float("{:.2f}".format(self.Poisson)))
        self.display_long = "Bulk Modulus = " + str(self.K)  + " | Young Modulus = " + str(self.E) + " | Shear Modulus = " + str(self.G) + " | Lame First Parameter = " + str(self.lame) + " | Poisson Coeficient = " + str(self.Poisson)

    def UpdateAll(self):
        self.K = self.BulkModulus()
        self.E = self.YoungModulus()
        self.lame = self.LameFirst()
        self.G = self.ShearModulus()
        self.Poisson = self.vPoisson()
        return

    def BulkModulus(self):
        if (self.K != -1): return self.K

        if   (self.var == "E,lame"):
            R = np.sqrt(self.E ** 2 + 9.0 * self.lame ** 2 + 2.0 * self.E * self.lame)
            return (self.E + self.lame * 3.0 + R) / 6.0
        elif (self.var == "E,G"):
            return (self.E * self.G) / 3.0 / (3.0 * self.G - self.E)
        elif (self.var == "E,Poisson"):
            return self.E / 3.0 / (1.0 - 2.0 * self.Poisson)
        elif (self.var == "lame,G"): 
            return self.lame + ((2.0 * self.G) / 3.0) 
        elif (self.var == "lame,Poisson"): 
            return self.lame * (1.0 +self.Poisson) / (3.0 * self.Poisson)
        elif (self.var == "G,Poisson"):
            return 2.0 * self.G * (1.0 + self.Poisson) / 3.0 / (1.0 - 2.0 * self.Poisson)
        else: raise TypeError("Wrong Input Parameters")
    
    def YoungModulus(self):
        if (self.E != -1): return self.E 

        if   (self.var == "K,lame"):
            return 9.0 * self.K * (self.K - self.lame) / (3.0 * self.K - self.lame)
        elif (self.var == "K,G"):
            return 9.0 * self.K * self.G / (3.0 * self.K + self.G)
        elif (self.var == "K,Poisson"):
            return 3.0 * self.K * (1.0 - 2.0 * self.Poisson)
        elif (self.var == "lame,G"): 
            return self.G * (3.0 * self.lame + 2.0 * self.G) / (self.lame + self.G)
        elif (self.var == "lame,Poisson"): 
            return self.lame * (1.0 - self.Poisson) * (1.0 - 2.0 * self.Poisson) / self.Poisson
        elif (self.var == "G,Poisson"):
            return 2.0 * self.G * (1.0 + self.Poisson)
        else: raise TypeError("Wrong Input Parameters")
        
    def LameFirst(self):
        if (self.lame != -1): return self.lame

        if   (self.var == "K,E"):
            return 3.0 * self.K * (3.0 * self.K - self.E) / (9.0 * self.K - self.E)
        elif (self.var == "K,G"):
            return self.K - 2.0 * self.G / 3.0
        elif (self.var == "K,Poisson"):
            return 3.0 * self.K * self.Poisson / (1.0 + self.Poisson) 
        elif (self.var == "E,G"): 
            return self.G * (self.E - 2.0 * self.G) / (3.0 * self.G - self.E)
        elif (self.var == "E,Poisson"): 
            return self.E * self.Poisson / ((1.0 + self.Poisson) * (1.0 - 2.0 * self.Poisson))
        elif (self.var == "G,Poisson"):
            return 2.0 * self.G * self.Poisson / (1.0 - 2.0 * self.Poisson)
        else: raise TypeError("Wrong Input Parameters")
        
    def ShearModulus(self):
        if (self.G != -1): return self.G 

        if   (self.var == "K,E"):
            return 3.0 * self.K * self.E / (9.0 * self.K - self.E)
        elif (self.var == "K,lame"):
            return 3.0 * (self.K - self.lame) / 2.0
        elif (self.var == "K,Poisson"):
            return 3.0 * self.K * (1.0 - 2.0 * self.Poisson) / 2.0 / (1.0 + self.Poisson)
        elif (self.var == "E,lame"): 
            R = np.sqrt(self.E ** 2 + 9.0 * self.lame ** 2 + 2.0 * self.E * self.lame)
            return (self.E - 3.0 * self.lame + R) / 4.0 
        elif (self.var == "E,Poisson"): 
            return self.E / 2.0 / (1.0 + self.Poisson)
        elif (self.var == "lame,Poisson"):
            return self.lame * (1.0 - 2.0 * self.Poisson) / 2.0 / self.Poisson
        else: raise TypeError("Wrong Input Parameters")
        
    def vPoisson(self):
        if (self.Poisson != -1): return self.Poisson

        if   (self.var == "K,E"):
            return (3.0 * self.K - self.E) / 6.0 / self.K 
        elif (self.var == "K,lame"):
            return self.lame / (3.0 * self.K - self.lame)
        elif (self.var == "K,G"):
            return (3.0 * self.K - 2.0 * self.G) / 2.0 / (3.0 * self.K + self.G)
        elif (self.var == "E,lame"): 
            R = np.sqrt(self.E ** 2 + 9.0 * self.lame ** 2 + 2.0 * self.E * self.lame)
            return 2.0 * self.lame / (self.E + self.lame + R)
        elif (self.var == "E,G"): 
            return (self.E / 2.0 / self.G) - 1.0 
        elif (self.var == "lame,G"):
            return self.lame / 2.0 / (self.lame + self.G)
        else: raise TypeError("Wrong Input Parameters")
        
    