

class Generador3D:

    def __init__(self):
        self.temporales = 0
        self.etiquetas = 0
        self.codigo = ""


    def obtenerTemporal(self):

        temp = "t"+self.temporales.__str__()
        self.temporales  += 1
        return temp

    def obtenerEtiqueta(self):

        et = "L"+self.etiquetas.__str__()
        self.etiquetas += 1
        return self.et

    def generarEncabezado(self):
        encabezado = ""
        encabezado += """ 

            #include <stdio.h>
            float Stack[10000];
            float Heap[10000];
            
            int SP = 0;
            int HP = 0;
 
        """

    def generarMain(self):
        pass

    def reiniciarGenerador(self):
        self.temporales = 0
        self.etiquetas = 0
        self.codigo = ""


