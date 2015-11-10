from anlex import AnLex
from emit_NFA import NFA_output 
from emit_DFA import DFA_output
from gen_codigo import Codigo_output
from reporte import ReporteHTML
from ansintactico import AnSintactico

class PuntoEntrada:
    
    def principal(self,adm_simbolos, def_regular):
        
        expresion_reg = def_regular
        # se instancia un administrador de simbolos 
        simbolos_admin = adm_simbolos
        
        analizador_lex = AnLex(simbolos_admin)
        # instancia el flujo a analizar 
        analizador_lex.set_flujo(expresion_reg)
    
        # instancia un traductor NFA requerido por el analizador sintactico
        traductor_nfa = NFA_output()
    
        analizador_sintac = AnSintactico(analizador_lex , traductor_nfa)
        analizador_sintac.analizar()
    
        # instancia un traductor DFA con la lista de arcos generado anteriormente
        traductor_DFA = DFA_output(analizador_sintac.lista_arcos_nfa)
        #
        traductor_DFA.afn_to_afd() 
        
        # renombra estados del conjuntoDFA
        traductor_DFA.renombrar_nfa()
    
        # minimiza estados del NFA
        traductor_DFA.minimizar(traductor_DFA.lista_DFA_renam)
    
        generadorCodigo = Codigo_output(traductor_DFA.get_dfa_minimo())
        generadorCodigo.gen_main()
        reporteHTML = ReporteHTML("Resultados", 
                                  def_regular, 
                                  traductor_DFA.get_nfa_inst(), 
                                  traductor_DFA.get_dfa_renombrado(), 
                                  traductor_DFA.get_dfa_minimo())
        reporteHTML.secc_documento()
        reporteHTML.abrir_reporte()
        
        del(analizador_lex)
        del(traductor_nfa)
        del(analizador_sintac)
        del(traductor_DFA)
        del(generadorCodigo)
        del(reporteHTML)
    
