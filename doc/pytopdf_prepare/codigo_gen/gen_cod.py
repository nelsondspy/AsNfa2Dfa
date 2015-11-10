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
while not estado in ['st4', 'st1', 'st3', 'st2'] or c_entrada != None:
    if estado == 'st1':
        if c_entrada=='a':
            estado = 'st2'
            c_entrada = lector.next()
            ent = True
            continue
    if estado == 'st1':
        if c_entrada=='c':
            estado = 'st3'
            c_entrada = lector.next()
            ent = True
            continue
    if estado == 'st1':
        if c_entrada=='d':
            estado = 'st4'
            c_entrada = lector.next()
            ent = True
            continue
    if estado == 'st2':
        if c_entrada=='a':
            estado = 'st2'
            c_entrada = lector.next()
            ent = True
            continue
    if estado == 'st3':
        if c_entrada=='c':
            estado = 'st3'
            c_entrada = lector.next()
            ent = True
            continue
    if estado == 'st4':
        if c_entrada=='d':
            estado = 'st4'
            c_entrada = lector.next()
            ent = True
            continue
    if not ent:
        error = True
        break
    ent = False
if estado in ['st4', 'st1', 'st3', 'st2'] and not error :
    print 'correcto!'
else:
    print 'Error!'
raw_input('evaluar>')