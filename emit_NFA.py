"""
Clase que asiste la implementacion de las reglas semanticas 
en la traduccion dirigida por la sintaxis. Cuya finalidad es obtener un NFA 
"""
class NFA_output:
    #atributo de clase que mantiene el conteo de estados
    iestado = 0
    lista_arcos_NFA = []

    
    """metodo que retorna una tupla que representa un arco"""
    def gen_arco(self, terminal):
        inicio = self.inc_iestado()
        fin = self.inc_iestado()
        
        return  [(inicio, fin, terminal)]
    
    """metodo que retorna una nueva lista de arcos,segun la definicion 
          de la cerradura de klenee
    """
    def gen_kleene(self, lista_arcos): 
        inicio = self.inc_iestado()
        arcoinicial = (inicio , self.get_eini(lista_arcos), "Ep") 
        fin = self.inc_iestado()
        arcoalvacio = (inicio, fin, "Ep")
        
        arcociclo = (self.get_efin(lista_arcos), self.get_eini(lista_arcos), "Ep")
 
        arcofinal = (self.get_efin(lista_arcos), fin, "Ep")
        
        listanueva = [arcoinicial] + [arcoalvacio] + lista_arcos + [arcociclo] + [arcofinal]
        
        return listanueva
    
    """metodo que retorna una nueva lista de arcos,segun la definicion 
        de la cerradura positiva de klenee
    """
    def gen_kleene_positivo(self, lista_arcos):
        inicio = self.inc_iestado()
        arcoinicial = (inicio , self.get_eini(lista_arcos), "Ep")
        fin = self.inc_iestado()
        arcociclo = (self.get_efin(lista_arcos), self.get_eini(lista_arcos), "Ep")
        arcofinal = (self.get_efin(lista_arcos), fin, "Ep")
        listanueva = [arcoinicial] + lista_arcos + [arcociclo]  +  [arcofinal]
        return listanueva
    
    """metodo que retorna una nueva lista de arcos segun la definicion
       de la concatenacion 
    """
    def gen_concat(self,lista_arcos1, lista_arcos2):
        arconuevo = (self.get_efin(lista_arcos1),self.get_eini(lista_arcos2), "Ep")
        listanueva =lista_arcos1 + [arconuevo] + lista_arcos2
        return listanueva
    
    """metodo que retorna una nueva lista de arcos segun la definicion de la 
       decision
    """
    def gen_decision(self, lista_arcos1, lista_arcos2):
        inicio = self.inc_iestado()
        fin = self.inc_iestado()
        arco_inicio_sup = ( inicio , self.get_eini(lista_arcos1) , "Ep" )
        arco_inicio_inf = ( inicio , self.get_eini(lista_arcos2) , "Ep" )
        arco_fin_sup = (self.get_efin(lista_arcos1), fin , "Ep")
        arco_fin_inf = (self.get_efin(lista_arcos2), fin , "Ep")
        return [arco_inicio_sup] + [arco_inicio_inf] + lista_arcos1 + lista_arcos2 + [arco_fin_sup] + [arco_fin_inf]
    
    """metodo que retorna una nueva lista de arcos segun la definicion de 
        cero o una repeticion
    """
    def gen_cero_o_uno(self,lista_arcos):
        inicio = self.inc_iestado()
        fin = self.inc_iestado()
        arcoinicial = (inicio, self.get_eini(lista_arcos), "Ep")
        arcofinal = (fin, self.get_efin(lista_arcos), "Ep")
        arco_cero = (inicio, fin, "Ep")
        return [arcoinicial] + [arco_cero] + lista_arcos + [arcofinal]
    
    """retorna el estado inicial de una lista de arcos"""
    def get_eini(self, lista_arcos):
        if len(lista_arcos) > 0:
            return lista_arcos[0][0]
        
    """retorna el estado final de una lista de arcos"""
    def get_efin(self, lista_arcos):
        longitud = len(lista_arcos)
        if longitud > 0:
            return lista_arcos[longitud - 1][1]
        
    """retorna el nuevo numero de estado que debe crearse """
    def inc_iestado(self):
        self.iestado = self.iestado + 1
        return self.iestado
