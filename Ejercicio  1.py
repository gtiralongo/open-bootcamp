# ----------------------------------------------------------------
#                    Primera Parte                       
# ----------------------------------------------------------------
def sum(num1, num2, num3):
    return num1 + num2 +num3

sum(1,2,3)
# ----------------------------------------------------------------
#                    Ssegunda Parte                       
# ----------------------------------------------------------------

class Coche():
    puertas = 4
    def mas_puertas(self,puertas):
        return puertas +1

miCoche = Coche()
miCoche.puertas = miCoche.mas_puertas(miCoche.puertas)
print(miCoche.puertas)
