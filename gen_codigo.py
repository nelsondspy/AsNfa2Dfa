from config import DIR_SALIDA_CODIGO,PREFIJO_ARCHIVO_GEN
import os.path
class Codigo_output():
    def __init__(self,d_dfa):
        self.estado_inicial = d_dfa["estado_inicial"]
        self.conjunto_aceptacion = d_dfa["estados_aceptacion"]
        self.__lsarcos = d_dfa['lista_arcos']
        self.__identacion = 4 
        __nombre_archivo = ""
        
    def codigo_out(self,d_estados):
        return ""

    def gen_inicio(self):
        out = "global cadena" + "\n"
        out += "global aceptado" + "\n"
        out += "global pertenece " + "\n"
        out += "cadena = raw_input('evaluar>')" + "\n"
        out += "lector = avanzar_entrada()" + "\n"
        out += "c_entrada = lector.next()" + "\n"
        out += "estado=" + self.__encerrar(str(self.estado_inicial)) + "\n"
        out += "ent = False\n"
        out += "error = False\n"
        

        #if self.estado_inicial in self.conjunto_aceptacion:
        #    out = out + "aceptado = True" + "\n"
        #else:
        #    out = out + "aceptado = False " + "\n"
        
        out += "while not estado in " + str(self.conjunto_aceptacion) + " or c_entrada != None"  + ":\n"
        return out
    
    def gen_func_avanzar(self):
        out = "def avanzar_entrada():" + "\n" \
           "    lmax = len(cadena)" + "\n" \
           "    cont = -1" + "\n" \
           "    while cont <= lmax:" + "\n" \
           "        cont = cont + 1" + "\n"\
           "        if cont == lmax:" + "\n"\
           "            yield None" + "\n"\
           "        yield cadena[cont]" +  "\n"
        return out
    
    def gen_bloque(self,arco):
        nivel = self.__identacion * ' '
        out = nivel + "if estado == " + self.__encerrar(str(arco[0])) + ":\n"
        out += nivel + "    if c_entrada==" + self.__encerrar(str(arco[2])) + ":\n"
        out += nivel + "        estado = " + self.__encerrar(str(arco[1])) + "\n"
        out += nivel + "        c_entrada = lector.next()" + "\n"
        out += nivel + "        ent = True\n"
        out += nivel + "        continue\n"
        return out 
    
    def __gen_evaluacion_final(self):
        out = "if estado in " + str(self.conjunto_aceptacion) + " and not error :"
        out += "\n    print 'correcto!'"
        out += "\nelse:"
        out += "\n    print 'Error!'"
        out += "\nraw_input('')"
        return out
    
    def gen_main(self):
        self.__crear_archivo()
        self.__persistir(self.gen_func_avanzar())
        self.__persistir(self.gen_inicio())
        for arco in self.__lsarcos:
            self.__persistir(self.gen_bloque(arco))
        
        self.__persistir(self.__final_while()) 
        
        self.__persistir(self.__gen_evaluacion_final())
    
    def __persistir(self,cadena):
        archivo = open(self.__nombre_archivo,'a')
        archivo.write(cadena)
        archivo.close()
    
    """crea un archivo en un directorio especificado , pero sin sobre escribir los
    generados anteriormente 
    """
    def __crear_archivo(self):
        if not os.path.exists(DIR_SALIDA_CODIGO):
            os.mkdir(DIR_SALIDA_CODIGO)
        
        self.__nombre_archivo = DIR_SALIDA_CODIGO + os.sep + PREFIJO_ARCHIVO_GEN
        archivo = open(self.__nombre_archivo ,'w')
        archivo.close()
        
    def __encerrar(self,cadena):
        return "'" + cadena + "'"
    
    def __final_while(self):
        out = "    if not ent:\n        error = True\n        break\n"
        out += "    ent = False\n"
        return out  