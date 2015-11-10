"""
Clase que reconoce algun lenguaje generado por la sigte gramatica
expr ::= concat '|' concat
         concat
concat ::= rep '.' rep
        | rep
rep ::= atom '*' | atom '+' | atom '?'
        | atom
atom ::= '(' expr ')'
       | char
char ::= a..z

"""

from anlex import AnLex, Lexconst
 
class AnSintactico:
    pre_analisis = (None, None)
    #Referencia a una instancia del analizador lexico 
    anlex = None
    #referencia a una instancia del traductor NFA
    emisor_nfa = None
    #lista de arcos obtenido al final del analisis
    lista_arcos_nfa = None
    
    """La intanciacion del analizador sintactico requiere la instancia de:
    un analizador lexico
    un emisorNFA
    """
    def __init__(self, anlex, nfa_instance):
        self.anlex = anlex
        self.emisor_nfa = nfa_instance
        
    """metodo que avanza un caracter si el lexema es el esperado"""
    def parea(self, lexema):
        if self.pre_analisis["lexema"] == lexema:
            self.pre_analisis = self.anlex.next_token()
            if self.pre_analisis["tipo"] != Lexconst.EOF:
                print (("token consumido: '" + self.pre_analisis["lexema"] + "'"))
        else:
            raise Exception("Error sintactico, se esperaba: '" + lexema)
    
    """metodo principal que inicia el analisis sintactico"""
    def analizar(self):
        self.pre_analisis = self.anlex.next_token()
        #while self.pre_analisis['tipo'] != Lexconst.EOF:
        lista_arcos = self.expr()

        self.lista_arcos_nfa = lista_arcos
        if self.pre_analisis['tipo'] != Lexconst.EOF:
            raise Exception("Hubo algun Error,no se ha consumido toda la cadena")
    
    """Valida la sintaxis de un no terminal atomico y construye
    su lista de arcos de arcos  
    """
    def atomico(self):
        print (("atomico(),preanalisis='" + self.pre_analisis["lexema"] + "'"))
        if self.pre_analisis["tipo"] == Lexconst.SIMB_DEF:
            lexemaant = self.pre_analisis["lexema"]
            self.parea(self.pre_analisis["lexema"])
            #retorna el par de estados (arco) que representa al lexema
            return self.emisor_nfa.gen_arco(lexemaant)
        
        if self.pre_analisis["lexema"] == '(':
            self.parea('(')
            #obtiene la lista de arcos construida por los metodos llamados en jerarquia
            lista_nodos = self.expr()
            self.parea(')')
            #retorna la lista de nodos que le toco construir
            return lista_nodos
        raise Exception("Error al formar atomico")
    
    """Valida la sintaxis de un no terminal repeticion y construye
    su lista de arcos de arcos  
    """
    def repeticion(self):
        print (("repeticion(),preanalisis='" + self.pre_analisis["lexema"] + "'"))
        nodo_hijo = self.atomico()
        if self.pre_analisis["lexema"] == '*':
            self.parea('*')
            #genera la lista de arcos para la cerradura 
            nodos_res = self.emisor_nfa.gen_kleene(nodo_hijo)
            return nodos_res
        
        elif self.pre_analisis["lexema"] == '+':
            self.parea('+')
            #genera la lista de arcos para la cerradura positiva 
            nodos_res = self.emisor_nfa.gen_kleene_positivo(nodo_hijo)
            return nodos_res 
        elif self.pre_analisis["lexema"] == '?':
            self.parea('?')
            #genera la lista de arcos para la regla uno o cero
            nodos_res = self.emisor_nfa.gen_cero_o_uno(nodo_hijo)
            return nodos_res
        return nodo_hijo 

    def concat(self):
        print (("concat(),preanalisis='" + self.pre_analisis["lexema"] + "'"))
        listanueva = self.repeticion()
        while True :
            if self.pre_analisis["lexema"] == '.':
                self.parea('.')
                nuevo_nodo = self.repeticion()
                #concatena sucesivamente los resultados de generar listas de arcos 
                    #por medio de llamadas a repeticion()  
                listanueva = self.emisor_nfa.gen_concat(listanueva, nuevo_nodo)
                continue
            else:
                return listanueva

    def expr(self):
        print (("expr(),preanalisis='" + self.pre_analisis["lexema"] + "'"))
        listanueva = self.concat()
        
        while True:
            if self.pre_analisis["lexema"] == '|':
                self.parea('|')
                lista_nodoshijos = self.concat()
                
                listanueva = self.emisor_nfa.gen_decision(listanueva, lista_nodoshijos)
                continue
            else:
                return listanueva
