def avanzar_entrada():
    lmax = len(cadena)
    cont = -1
    while cont <= lmax:
        cont = cont + 1
        if cont == lmax:
            yield None
        yield cadena[cont]
global cadena
global aceptado
global pertenece 
cadena = raw_input('evaluar>')
lector = avanzar_entrada()
c_entrada = lector.next()
estado='st1'
ent = False
error = False
while not estado in ['st2', 'st1', 'st3'] or c_entrada != None:
    if estado == 'st1':
        if c_entrada=='0':
            estado = 'st2'
            c_entrada = lector.next()
            ent = True
            continue
    if estado == 'st2':
        if c_entrada=='0':
            estado = 'st2'
            c_entrada = lector.next()
            ent = True
            continue
    if estado == 'st1':
        if c_entrada=='1':
            estado = 'st3'
            c_entrada = lector.next()
            ent = True
            continue
    if not ent:
        error = True
        break
    ent = False
if estado in ['st2', 'st1', 'st3'] and not error :
    print 'correcto!'
else:
    print 'Error!'
raw_input('')