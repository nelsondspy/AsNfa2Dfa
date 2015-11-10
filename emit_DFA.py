"""Clase que contiene las estructuras de datos y metodos 
   necesarios para convertir un NFA a un DFA 

"""
class DFA_output:
    lista_nfa = []
    lista_DFA =[]
    lista_DFA_renam = []
    lista_DFA_min=[]
    #estado inicial del nfa  
    est_nfa_inicial= 0 
    #estado de aceptacion del nfa
    est_nfa_aceptacion =  0
    #conjunto de estados de aceptacion  
        #y estado inicial , posterior al renombramiento del DFA 
    ls_renam_aceptacion = []
    est_renam_inicial = 0
    #para guardar las equivalencias del renombramiento
    mp_erenombrados = {}
    #conjunto de estados de aceptacion y estado inicial pos minimizacion
    ls_min_aceptacion=[]
    est_min_inicial = 0 
    
    """El constructor recibe como parametro una lista de tuplas que representa al NFA"""
    def __init__(self,lista_arcos_nfa):
        self.lista_nfa = lista_arcos_nfa
        #obtenemos estado final 
        self.est_nfa_inicial = self.lista_nfa[0][0]
        #obtenemos  el estado de aceptacion 
        longitud = len(self.lista_nfa)
        if longitud > 0:
            self.est_nfa_aceptacion = self.lista_nfa[longitud - 1][1]
    
    """Metodo que retorna una lista los estados alcanzables
    desde un estado  y un caracter recibidos como parametros
    """
    def estados_alcanz(self, estado, tr ,ls_arcos = None):
        estados_alcanzables=[]
        if ls_arcos is None:
            ls_arcos = self.lista_nfa
        for arco in ls_arcos:
            if arco[0] == estado and arco[2] == tr:
                estados_alcanzables.append(arco[1])
        return estados_alcanzables
    
    """Metodo que retorna una lista los estados alcanzanbles directamente,
    por transiciones epsilon desde un un cojunto de estados 
    """
    def trans_directa_E(self,conjunto):
        ealcanzables = []
        for estado in conjunto:
            estados = self.estados_alcanz(estado, "Ep")
            ealcanzables = ealcanzables + estados 
            #ealcanzables = ealcanzables  +  estados + [estado]
        return ealcanzables
    
    """Metodo que retorna una lista de estados, que representa al conjunto cerraduraEpsilon
    de un un conjunto de estados recibido como parametro 
    """
    def cerradura_E(self,conjunto):
        cerradura = conjunto
        resultante = self.trans_directa_E(conjunto)
        while ( len(resultante) > 0  ):
            cerradura = cerradura + resultante
            resultante = self.trans_directa_E(resultante)
        return cerradura 
    
    """Metodo que retorna una lista de tuplas , donde cada tupla  representa a un arco,
    y cada arco representa a una transicion de una lista de estados a otra solo por medio
    de un terminal osea distinto a Epsilon.  
    """
    def mover_terminal_x(self, conjunto):
        pre_resul = []
        ls_movx = [] 
        for estado in conjunto:
            for arco in self.lista_nfa:
                if arco[2] != "Ep" and  arco[0] == estado:
                    caracter = arco[2]
                    edestino = arco[1]
                    pre_resul.append((caracter, edestino))
        if len(pre_resul) == 0:
            return []
        if len(pre_resul) == 1:
            return [([pre_resul[0][1]], pre_resul[0][0])]
        #ordena por la terminal
        pre_resul.sort()
        
        caracter_actual = pre_resul[0][0]
        ls_aux = []
        for par in pre_resul:
            caracter = par[0]
            edestino = par[1]
            if caracter_actual == caracter:
                ls_aux.append(edestino)
            else:
                ls_movx.append((ls_aux, caracter_actual))
                ls_aux = []
                caracter_actual = caracter
                ls_aux.append(edestino)
        ls_movx.append((ls_aux, caracter_actual))
        return ls_movx
    
    """Retorna una lista de tuplas que represeta a un DFA, 
    utiliza la lista de tuplas NFA , que es un atributo de la clase ;
    seteado en el momento de la construccion del objeto.
    Esto es a fines de evitar que los metodos requieran constantemente 
    recibirla como parametro
    """
    def afn_to_afd(self):
        grupo_e = []
        self.lista_DFA=[]
        einicial = self.lista_nfa[0][0]
        grupo_e.append( self.cerradura_E([einicial]))
        #retorna una lista de tuplas  [([1,2],a)([a,b], ) ]
        for estados_e in grupo_e:
            conj_a = self.mover_terminal_x(estados_e)
            for ele_term in conj_a:
                conj_e = self.cerradura_E(ele_term[0])
                self.lista_DFA.append((estados_e, conj_e, ele_term[1]))
                if estados_e != conj_e:
                    if  not conj_e in grupo_e: 
                        grupo_e.append(conj_e)
            
    """Metodo que renombra la lista de arcos, para facilitar su legibilidad
    el procedimiento setea el nuevo estado de inicio y los de aceptacion
    """
    def renombrar_nfa(self):
        mapa_cadenas = {}
        nn_ini = ''
        nn_fin = ''
        char_actual = 0
        prefijo = "st"
        for tupla in self.lista_DFA:
            
            repr_ini = ''.join(str(tupla[0]))
            repr_fin = ''.join(str(tupla[1]))
            if repr_ini in mapa_cadenas:
                nn_ini = mapa_cadenas[repr_ini]
            else:
                char_actual = char_actual + 1
                nn_ini = prefijo + str(char_actual)
                mapa_cadenas[repr_ini] = nn_ini
               
            if repr_fin in mapa_cadenas:
                nn_fin = mapa_cadenas[repr_fin]
            else:
                char_actual = char_actual + 1
                nn_fin = prefijo + str(char_actual)
                mapa_cadenas[repr_fin] = nn_fin
            
            #verificamos si el estado es un estado inicial
            if self.est_nfa_inicial in tupla[0]:
                self.est_renam_inicial = nn_ini
            #verificamos si el estado inicial es un estado de aceptacion y aun no esta en la lista
            if self.est_nfa_aceptacion in tupla[0] and \
                not nn_ini in self.ls_renam_aceptacion :
                    self.ls_renam_aceptacion.append(nn_ini) 
            #verificamos si el estado es un estado de aceptacion y aun no esta en la lista
            if self.est_nfa_aceptacion in tupla[1] and \
                not nn_fin in self.ls_renam_aceptacion :
                    self.ls_renam_aceptacion.append(nn_fin)
            
            self.lista_DFA_renam.append((nn_ini, nn_fin, tupla[2]))
        #carga apunta al atributo que guarda el resultado del renombramiento
        self.mp_erenombrados = mapa_cadenas
    
    """metodo que obtiene la solo lista de terminales presentes , en la lista de arcos"""
    def __solo_terminales(self,lista_arcos):
        lista_terminales = []
        for arco in lista_arcos:
            if not arco[2] in lista_terminales:
                lista_terminales.append(arco[2])
        return lista_terminales
    
    """metodo que retorna lista la lista estados de no aceptacion """
    def __conj_no_aceptacion(self,lista_arcos):
        lista_noacep = []
        for arco in lista_arcos:
            if not(arco[0] in self.ls_renam_aceptacion): 
                if not(arco[0] in lista_noacep) :
                    lista_noacep.append(arco[0])
        return lista_noacep
    
    """Metodo que implemente el algoritmo de minimizacion de estados 
    sobre la lista de arcos renombrada """
    def minimizar(self, ls_arcos):
        ls_terminales = self.__solo_terminales(ls_arcos)
        ls_ls_no_acep = self.__conj_no_aceptacion(ls_arcos)
        ls_ls_aceptacion = self.ls_renam_aceptacion[:]
        ls_ls_estados = [ls_ls_no_acep] + [ls_ls_aceptacion]
        for terminal in ls_terminales:
            for conj_estados in ls_ls_estados:
                #si tiene un solo elemento se ignora
                if len(conj_estados) <= 1:
                    continue
                for estado in conj_estados:
                    #verifica si el estado puede alcanzar algun estado con esa terminal
                    alcanzable = self.estados_alcanz(estado, terminal, self.lista_DFA_renam)
                    #detemina si el estado alcanzable no esta en el propio conjunto
                    #si NO esta en el conjunto, debemos separar el estado en un nuevo conjunto
                    if len(alcanzable) == 0:
                        ls_ls_estados.append([estado])
                        conj_estados.remove(estado)
                    #al ser dfa , por medio de una terminal ya solo puede ir a un estado
                    elif not alcanzable[0][0] in conj_estados:
                        ls_ls_estados.append([estado])
                        conj_estados.remove(estado)
                         
        #eliminar conjuntos repeticos
        #sustituye cada elemento por su representante correspondiente 
        self.lista_DFA_min = []
        for arco in self.lista_DFA_renam:
            ini = arco[0]
            fin = arco[1]
            for conj_estados in ls_ls_estados:
                if len(conj_estados)<=1:
                    continue
                representa = conj_estados[0]
                if arco[0] in conj_estados:
                    ini = representa 
                if arco[1] in conj_estados:
                    fin = representa
            if not (ini,fin,arco[2]) in self.lista_DFA_min: 
                self.lista_DFA_min.append((ini,fin,arco[2]))
        
        #encuentra los nuevos estados de aceptacion, e inicial
        for conj_estados in ls_ls_estados:
            if len(conj_estados) == 0 :
                continue 
            if self.est_renam_inicial in conj_estados and self.est_min_inicial == 0 :
                self.est_min_inicial =  conj_estados[0]
            for eaceptacion in self.ls_renam_aceptacion:
                if  eaceptacion in conj_estados and not conj_estados[0]  in self.ls_min_aceptacion:
                    self.ls_min_aceptacion.append(conj_estados[0])
    
    """Metodos que retornan  los resultados de las operaciones en una diccionario
    con claves uniforme, para ser usadas por otros programas como el de reporte
    """
    
    """Resumen posterior a minimizar"""
    def get_dfa_minimo(self):
        return {"estado_inicial":self.est_min_inicial,
                "estados_aceptacion":self.ls_min_aceptacion,
                "lista_arcos":self.lista_DFA_min}
    
    """Resumen posterior a renombrar """
    def get_dfa_renombrado(self):
        return {"estado_inicial":self.est_renam_inicial,
                "estados_aceptacion":self.ls_renam_aceptacion,
                "lista_arcos":self.lista_DFA_renam,
                "renombrados":self.mp_erenombrados
                }

    """Resumen de nfa recibido como parametro
    es cuestionable que este metodo deberia estar en la clase que convierte a NFA 
    como la existencia de esta clase solo tiene sentido con la salida de los metodos de NFA
    se considero aceptable implementarlo aqui
    """
    def get_nfa_inst(self):
        return {"estado_inicial":self.est_nfa_inicial,
                "estados_aceptacion":self.est_nfa_aceptacion,
                "lista_arcos":self.lista_nfa}
