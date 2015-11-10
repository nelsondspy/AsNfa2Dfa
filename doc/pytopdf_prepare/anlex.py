#lista de caracteteres a ignorar

#simbolos_reservados = frozenset([".", "+", "="])
#alfabetos = {'LETRAS': [chr(l) for l in range(97, 122)],
#    'DIGITOS': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']}

"""Clase que administra los alfabetos y simbolos reservados"""
class SimbolosAdmin:
    def __init__(self):
        self.simbolos_reservados = frozenset([".", "+", "="])
        self.alfabetos = {'LETRAS': [chr(l) for l in range(97, 122)],
    'DIGITOS': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']}
    
    def agregar_alfabeto(self, nombre, listasimbolos):
        if nombre in self.alfabetos:
            return False
        self.alfabetos[nombre]= listasimbolos
        return True
    
    

"""clase estatica que encapsula las constantes"""
class Lexconst:
    EOF=-1
    SIMB_DEF = 1
    PARENT_DER = 2
    PARENT_IZQ = 3
    KLEENE = 4
    KLEENE_PLUS = 5
    UNION = 6
    UNOCERO = 7
    CONCAT = 8
    comp_lex = {"(": PARENT_IZQ, ")": PARENT_DER, "*": KLEENE, "+": KLEENE_PLUS,
"|": UNION, "?": UNOCERO, ".": CONCAT}
    ignore_list = frozenset([' '])


"""Tipos de componentes lexicos:
    tokens reservados son aquellos que no pueden formar parte de los alfabetos
    definidos.
    Luego estan los simbolos de los alfabetos definidos por el usuario
    """
class Token_attr:
    AT_LEXEMA = "lexema"
    AT_TIPO = "tipo"

class AnLex:
    """Analizador Lexico"""
    pos = -1
    num_linea = 0
    alfabetos = {}
    simbolos_reservados=[]
    def __init__(self, obSimbolAdmin):
        self.alfabetos = obSimbolAdmin.alfabetos
        self.simbolos_reservados = obSimbolAdmin.simbolos_reservados 
    
    def set_flujo(self, flujo):
        self.fuente = flujo
        #analogo al eof
        self.maxpos = len(flujo)-1
        AnLex.pos = -1
    """Retorna el siguiente caracter no vacio o bien None cuando ya no
    quedancaracteres a consumir"""
    def get_char(self):
        if AnLex.pos < self.maxpos:
            AnLex.pos += 1
            while self.fuente[AnLex.pos] in Lexconst.ignore_list:
                AnLex.pos += 1
            if AnLex.pos <= self.maxpos:
                return self.fuente[AnLex.pos]
        else:
            return None

    #Devuelve el caracter
    def unget_char(self):
        AnLex.pos -= 1
        return self.fuente[self.pos]

    def es_simbolo(self, s):
        for alfabeto in self.alfabetos:
            for simbolos in self.alfabetos[alfabeto]:
                if s in simbolos:
                    return True
        return False

    def next_token(self):
        while True:
            ch = self.get_char()
            if ch is None:
                return self.set_tokeninf('', Lexconst.EOF)
            if ch in Lexconst.ignore_list:
                True
            elif ch == "\n":
                AnLex.num_linea += 1
            elif ch in Lexconst.comp_lex:
                #coincide con algun caracter reservado
                return self.set_tokeninf(ch, Lexconst.comp_lex[ch])
            elif self.es_simbolo(ch):
                #debe ser el componente lexico definido por los alfabetos
                return self.set_tokeninf(ch, Lexconst.SIMB_DEF)

    def set_tokeninf(self, lexema, componente):
        return {"lexema": lexema, "tipo": componente}
