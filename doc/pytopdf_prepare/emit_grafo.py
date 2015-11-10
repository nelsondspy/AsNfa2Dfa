import pygraphviz as pgv

def dibujar(lista_arcos,einicial,eaceptacion,archivo):
    A=pgv.AGraph(strict=False,directed=True)
    A.node_attr['shape']='circle'
    A.node_attr['fixedsize']='true'
    A.node_attr['height']=0.5
    A.node_attr['width']=0.5
    for arco in lista_arcos:
        A.add_edge(arco[0],arco[1])
        
        n = A.get_edge(arco[0],arco[1])
        n.attr['label']=arco[2]
        node = A.get_node(arco[1])
        
        if arco[0] == einicial:
            node.attr['color'] = "#565050"
            node.attr['style']='setlinewidth(2)'
            
        if arco[1] in  eaceptacion:
            node.attr['color'] = "#514e86"
            node.attr['style']='setlinewidth(3)'

    A.write(archivo + '.dot')
    B=pgv.AGraph(archivo + '.dot')
    B.layout()
    B.draw(archivo + ".png")