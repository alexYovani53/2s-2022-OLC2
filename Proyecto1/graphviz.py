import graphviz

conteo = 1
grafica = graphviz.Digraph(filename='salida.dot')
grafica.attr('node', shape='circle', style='radial', gradientangle='360',  fontcolor='black')
grafica.attr(overlap='true',)
grafica.attr(compouned='true')
grafica.attr(rankdir='LR')

#grafica.attr(layout="twopi")
grafica.node("RAIZ","AST",shape="box3d")

# circo dot fdp neato nop nop1 nop2 osage patchwork sfdp twopi


def agregarInicio(nombre):
    global conteo
    conteo += 1

    with grafica.subgraph(name=f"cluster_{conteo}") as otro:
        grafica.edge("RAIZ",f"a_{conteo}_task")
        otro.attr(shape='box', style='rounded,filled', color='yellow')

        otro.attr('node', shape='circle', style='radial', gradientangle='360', fontcolor='black')
        otro.node(f"a_{conteo}_task", f"{conteo}")

        otro.attr('node', shape='box', style='radial', gradientangle='360', fontcolor='black')
        otro.node(f"b_{conteo}", nombre, shape="box3d")


        otro.node_attr.update(shape = "box",style='filled', color='white')
        otro.node(f"c_task{conteo}",'''<
           <table border="1" cellborder="0" cellspacing="1">
             <tr><td align="left"><b>Task 1</b></td></tr>
             <tr><td align="left">Choose Menu</td></tr>
             <tr><td align="left"><font color="darkgreen">done</font></td></tr>
           </table>>''',constraint="true")
        otro.node(f"task{conteo}_1",'''<
           <table border="1" cellborder="0" cellspacing="1">
             <tr><td align="left"><b>Task 1</b></td></tr>
             <tr><td align="left">Choose Mssssssssssssenu</td></tr>
             <tr><td align="left"><font color="darkgreen">done</font></td></tr>
           </table>>''',constraint="true")

        otro.edge(f"c_task{conteo}",f"task{conteo}_1")






# names = ["A", "B", "C", "D", "E", "F", "G", "H"]
# positions = ["CEO", "Team A Lead", "Team B Lead", "Staff A", "Staff B", "Staff C", "Staff D", "Staff E"]
# colors = ["black", "skyblue", "mistyrose", "skyblue", "skyblue", "mistyrose", "mistyrose", "mistyrose"]
# for name, position, color in zip(names, positions, colors):
#     if name == "A":
#         grafica.node(name, position, color=color)
#     else:
#         grafica.node(name, position, style="filled", color=color)
#
# # Specify edges
# grafica.edge("A", "B");
# grafica.edge("A", "C")  # CEO to Team Leads
# grafica.edge("B", "D");
# grafica.edge("B", "E")  # Team A relationship
# grafica.edge("C", "F");
# grafica.edge("C", "G");
# grafica.edge("C", "H")  # Team B relationship

# with grafica.subgraph(name='clusterExpresion') as c:
#     c.node("hola mundo")
#     c.edges(['AB', 'Ac', 'bd', 'cd'])
#
#     with c.subgraph(name='cluster_otro') as cc:
#         cc.attr(style='filled', color='lightgrey')
#         cc.node_attr.update(style='filled', color='white')
#         cc.attr(label='process #1')
#         cc.node("juan")





#grafica.view()
#grafica.render(directory='doctest-output', format='jpeg', filename="hola").replace('\\', '/')