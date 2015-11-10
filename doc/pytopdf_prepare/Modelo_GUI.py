class Modelogui:
    lista_temp_simbolos =[]
    lista_alfabetos_creados={}
    
    def nuevo_simbolo(self, simb):
        self.lista_temp_simbolos.append(str(simb))
        
    def nuevo_alfabeto(self, nombre):
        self.lista_alfabetos_creados[nombre] = self.lista_temp_simbolos
        self.lista_temp_simbolos=[]
    
    def get_ultimo_agregado(self):
        tam= len(self.lista_alfabetos_creados)
        return str  + str(self.lista_alfabetos_creados[tam-1])