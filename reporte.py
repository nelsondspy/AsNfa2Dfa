#la idea es obtener un solo html con todo el resultado de la salida
import os 
import webbrowser
from config import DIR_SALIDA_REPORTE , NAM_ARCHIVO_REPORTE
from emit_grafo import dibujar
#from emit_grafo import dibujar

class ReporteHTML: 
    titulo=""
    subtitulo=""
    file = None
    dicc_nfa = None
    dicc_dfa = None 
    dicc_nfamin = None
    dir_salida = DIR_SALIDA_REPORTE
    nombre_archivo= NAM_ARCHIVO_REPORTE

    
    def __init__(self, titulo, subtitulo, dicc_nfa, dicc_dfa, dicc_nfamin ):
        self.titulo = titulo
        self.subtitulo = subtitulo
        self.dicc_nfa = dicc_nfa 
        self.dicc_dfa = dicc_dfa
        self.dicc_nfamin = dicc_nfamin
         
    def abrir_archivo(self):
        if not os.path.exists(self.dir_salida):
            os.mkdir(self.dir_salida)
        self.file = open(self.dir_salida + os.path.sep + self.nombre_archivo, "w")
        
    def cerrar_archivo(self):
        self.file.close()
    
    def ht_html(self, cerrar=True):
        if cerrar:
            return "</html>"
        else:
            return "<html>"
    
    def ht_hn(self, valor,  texto):
        return "<h"+str(valor) + ">" + texto + "<h"+str(valor) + "/>"
    
        
    def secc_documento(self):
        self.abrir_archivo()
        #inicio
        self.file.write(self.ht_html())
        self.file.write("<head>")
        
        self.file.write(self.css_segmento())
        
        self.file.write("</head>")
        
        self.file.write("<body>")
        
        #titulos  
        self.file.write(self.ht_hn(1,self.titulo))
        self.file.write(self.ht_hn(1,self.subtitulo))
        
        #secciones 
        self.file.write(self.secc_paso("NFA",self.dicc_nfa ))
        self.file.write(self.secc_paso("DFA",self.dicc_dfa))
        self.file.write(self.secc_paso("DFA Min",self.dicc_nfamin))
        self.file.write(self.__img_dibujografo())
        #fin
        self.file.write("</body>")
        self.file.write(self.ht_html(True))
        
        
        self.cerrar_archivo()
        
    def ht_tabla(self, ls_arcos):
        lista_estados=[]
        tabla = {}
        for arco in ls_arcos:
            einicial = arco[0]
            efinal = arco[1]
            terminal = arco[2]
            #
            if not terminal in tabla :
                tabla[terminal]={}
            #
            if einicial not in tabla[terminal]:
                tabla[terminal][einicial]=[]
            #
            if efinal not in tabla[terminal]:
                tabla[terminal][efinal]=[]
            #
            tabla[terminal][einicial].append(efinal)
            
            if not einicial in lista_estados:
                lista_estados.append(einicial)
                
            if not efinal in lista_estados:
                lista_estados.append(efinal)
            
        terminal = ''
        fila_cab = '<th></th>'
        fila_est = ''
        #generalos la columnas  
        for terminal in tabla :
            fila_cab += '<th>'
            fila_cab += terminal
            fila_cab += '</th>'
            
        for iestado in lista_estados:
            fila_est += "<tr>\n"
            fila_est += "\t" + '<td>' + str(iestado) + '</td>' + "\n"
            for terminal in tabla :
                if iestado in tabla[terminal] and len(tabla[terminal][iestado]) > 0: 
                    fila_est += "\t" + '<td>' +  str(tabla[terminal][iestado]) + '</td>' + "\n"
                else:
                    fila_est += "\t" + '<td>' +  " - " + '</td>' + "\n"
            
            fila_est += "</tr>\n"
        salida = "<table>\n" + "<caption>Tabla de transiciones</caption>" + \
        "<tr>" + fila_cab + "</tr>"  + fila_est  + "</table>"
        return salida
        
    def secc_paso(self,tituloseccion, dicc_paso):
        
        salida = self.ht_hn(2, tituloseccion)
        salida += self.ht_hn(3, "Estado de inicial:" + str(dicc_paso['estado_inicial']))
        salida += self.ht_hn(3, "Estados de aceptacion:" + str(dicc_paso['estados_aceptacion']))
        if 'renombrados' in dicc_paso:
            for equiv in dicc_paso['renombrados']:
                salida += "<p>" + dicc_paso['renombrados'][equiv] + "=" + str(equiv) + "</p>"
        
        salida += self.ht_tabla(dicc_paso['lista_arcos'])
        salida += "\n<hr>\n" 
        return salida
    
    def css_segmento(self):
        return """
        <style>
        body {font-family:"Lucida Console";margin-left:5%; color : rgb(40,40,40); }
         table, th, td {border: 1px solid grey;  padding:3px;} 
         </style>
         """
    def abrir_reporte(self):
        webbrowser.open_new(self.dir_salida + os.path.sep + self.nombre_archivo)
        
    def __img_dibujografo(self):
        dibujar(self.dicc_nfamin['lista_arcos'],self.dicc_nfamin['estado_inicial'],
                self.dicc_nfamin['estados_aceptacion'],
                 self.dir_salida + os.path.sep + "grafo")
        return "\n" + '<p>'+ self.subtitulo +'<img src="grafo.png"/> </p>' +"\n" 