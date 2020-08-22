"""
pygameFront.py
# This goes over how to make the pygame window appear in a certain location.
# This only works on windows!

# """


def pygame_windowing():
    #  Default Imports
    import os
    import time
    #  Other Imports
    import pygame
    #  My imports
    DEBUG = False

    if os.name == "nt":     # Windows
        from win32api import GetSystemMetrics   # pip install pypiwin32 OR pip install pywin32
    if os.name == "posix":  # Linux
        print("This does not currently work on linux.")
    if os.name == "mac?":   # Mac?
        print("This does not currently work on mac.")
    my_prof = ""
    if DEBUG:
        my_prof = profile_start()


    screen_width = 640
    screen_height = 480

    if os.name == "nt":
        screen_width = GetSystemMetrics(0)
        screen_height = GetSystemMetrics(1)

    width = 320
    height = 240
    x, y = screen_width-width-2, 2

    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)
    pygame.init()
    screen = pygame.display.set_mode((width, height))

    # wait for a while to show the window.
    time.sleep(1)

    if DEBUG:
        profile_end(my_prof)


def profile_start():
    import cProfile
    my_profile = cProfile.Profile()
    my_profile.enable()

    print(my_profile)
    return my_profile


def profile_end(my_profile):
    import pstats, io
    my_profile.disable()
    s = io.StringIO()
    sortby = 'cumulative'
    ps = pstats.Stats(my_profile, stream=s).sort_stats(sortby)
    ps.print_stats()
    print(s.getvalue())
    my_profile.dump_stats('mypygame.txt')


def until_paren(words, paren):
    current = ""
    for char in words:
        if char == "(":
            if paren:
                return current
            else:
                pass
        if char == ")":
            current += char
            return current
        current += char
    return current


def create_doc(stop_at_paren=True):
    import os
    os.environ["PATH"] += os.pathsep + "C:/Users/admin9/Downloads/Graphviz/bin"
    from graphviz import Digraph

    save_folder = "basic-docs/"
    file_folder = "Networking/"
    file_name = "LoveLetterServer"
    open_ext = ".py"
    save_ext = ".gv"

    s = Digraph('structs', filename=save_folder + file_name + open_ext + save_ext,
                node_attr={'shape': 'record'})

    with open(file_folder + file_name + open_ext, 'r') as r:
        my_file = r.read().split("\n")
    # print(my_file)
    current_class = {"name": "", "methods": []}
    global_class = {"name": "Global", "methods": []}
    all_classes = []
    in_class = False
    blank_lines = 0
    for line in my_file:
        if line == "":
            blank_lines += 1
            if blank_lines > 1:
                in_class = False
                if current_class != {"name": "", "methods": []}:
                    all_classes.append(current_class)
                    current_class = {"name": "", "methods": []}

        else:
            blank_lines = 0

        if in_class:
            if line.startswith("    def"):
                current_class["methods"].append(until_paren(line[8:-1], stop_at_paren))
        if line.startswith("def"):
            global_class["methods"].append(until_paren(line[4:-1], stop_at_paren))

        if line.startswith("class"):
            current_class["name"] = until_paren(line[6:-1], stop_at_paren)
            in_class = True
    all_classes.append(global_class)

    print("ALL CLASSES: ", all_classes)
    struct_name = "struct"
    current_struct = ""
    s.node(struct_name + "_origin", file_name)
    with s.subgraph(name="sub1") as sub:
        for number, cur_class in enumerate(all_classes):
            current_struct += "{" + cur_class["name"] + "|"
            for meth in cur_class["methods"]:
                current_struct += meth + "|"
            current_struct = current_struct[:-1] + "}"  # removes the last | and adds the close
            sub.node(struct_name + str(number), current_struct)
            current_struct = ""

    s.view()


def traffic():
    # traffic_lights.py - http://www.graphviz.org/content/traffic_lights

    import os
    os.environ["PATH"] += os.pathsep + "C:/Users/admin9/Downloads/Graphviz/bin"
    from graphviz import Digraph

    t = Digraph('TrafficLights', filename='traffic_lights.gv', engine='neato')

    t.attr('node', shape='box')
    for i in (2, 1):
        t.node('gy%d' % i)
        t.node('yr%d' % i)
        t.node('rg%d' % i)

    t.attr('node', shape='circle', fixedsize='true', width='0.9')
    for i in (2, 1):
        t.node('green%d' % i)
        t.node('yellow%d' % i)
        t.node('red%d' % i)
        t.node('safe%d' % i)

    for i, j in [(2, 1), (1, 2)]:
        t.edge('gy%d' % i, 'yellow%d' % i)
        t.edge('rg%d' % i, 'green%d' % i)
        t.edge('yr%d' % i, 'safe%d' % j)
        t.edge('yr%d' % i, 'red%d' % i)
        t.edge('safe%d' % i, 'rg%d' % i)
        t.edge('green%d' % i, 'gy%d' % i)
        t.edge('yellow%d' % i, 'yr%d' % i)
        t.edge('red%d' % i, 'rg%d' % i)

    t.attr(overlap='false')
    t.attr(label=r'PetriNet Model TrafficLights\n'
                 r'Extracted from ConceptBase and layed out by Graphviz')
    t.attr(fontsize='12')

    t.view()


def struct1():
    # structs.py - http://www.graphviz.org/doc/info/shapes.html#html

    import os
    os.environ["PATH"] += os.pathsep + "C:/Users/admin9/Downloads/Graphviz/bin"
    from graphviz import Digraph

    s = Digraph('structs', node_attr={'shape': 'plaintext'})

    s.node('struct1', '''<
    <TABLE BORDER="0" CELLSPACING="0">
      <TR>
        <TD BORDER="1">left</TD>
        <TD PORT="f1" BORDER="1">middle</TD>
        <TD PORT="f2" BORDER="1">right</TD>
      </TR>
    </TABLE>>''')
    s.node('struct2', '''<
    <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">
      <TR>
        <TD PORT="f0" >one</TD>
        <TD>two</TD>
      </TR>
    </TABLE>>''')
    s.node('struct3', '''<
    <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4">
      <TR>
        <TD ROWSPAN="4">hello<BR/>world</TD>
        <TD COLSPAN="3">b</TD>
        <TD ROWSPAN="3">g</TD>
        <TD ROWSPAN="3">h</TD>
      </TR>
      <TR>
        <TD>c</TD>
        <TD PORT="here">d</TD>
        <TD>e</TD>
      </TR>
      <TR>
        <TD COLSPAN="3">f</TD>
      </TR>
    </TABLE>>''')

    s.edges([('struct1:f1', 'struct2:f0'), ('struct1:f2', 'struct3:here')])

    s.view()


def zombie():
    import os
    os.environ["PATH"] += os.pathsep + "C:/Users/admin9/Downloads/Graphviz/bin"
    from graphviz import Graph

    g = Graph('G', filename='process.gv', engine='sfdp')
    g.edge('run', 'intr')
    g.edge('intr', 'runbl')
    g.edge('runbl', 'run')
    g.edge('run', 'kernel')
    g.edge('kernel', 'zombie')
    g.edge('kernel', 'sleep')
    g.edge('kernel', 'runmem')
    g.edge('sleep', 'swap')
    g.edge('swap', 'runswap')
    g.edge('runswap', 'new')
    g.edge('runswap', 'runmem')
    g.edge('new', 'runmem')
    g.edge('sleep', 'runmem')

    g.view()


def cluster():
    import os
    os.environ["PATH"] += os.pathsep + "C:/Users/admin9/Downloads/Graphviz/bin"
    from graphviz import Digraph

    g = Digraph('G', filename='cluster.gv')

    # NOTE: the subgraph name needs to begin with 'cluster' (all lowercase)
    #       so that Graphviz recognizes it as a special cluster subgraph

    with g.subgraph(name='cluster_0') as c:
        c.attr(style='filled', color='lightgrey')
        c.node_attr.update(style='filled', color='white')
        c.edges([('a0', 'a1'), ('a1', 'a2'), ('a2', 'a3')])
        c.attr(label='process #1')

    with g.subgraph(name='cluster_1') as c:
        c.attr(color='blue')
        c.node_attr['style'] = 'filled'
        c.edges([('b0', 'b1'), ('b1', 'b2'), ('b2', 'b3')])
        c.attr(label='process #2')

    g.edge('start', 'a0')
    g.edge('start', 'b0')
    g.edge('a1', 'b3')
    g.edge('b2', 'a3')
    g.edge('a3', 'a0')
    g.edge('a3', 'end')
    g.edge('b3', 'end')

    g.node('start', shape='Mdiamond')
    g.node('end', shape='Msquare')

    g.view()


def struct2():
    # structs_revisited.py - http://www.graphviz.org/pdf/dotguide.pdf Figure 12

    import os
    os.environ["PATH"] += os.pathsep + "C:/Users/admin9/Downloads/Graphviz/bin"
    from graphviz import Graph  # Graph - no arrows
    from graphviz import Digraph  # Digraph - arrows

    #s = Digraph('structs', filename='basic-docs/structs_revisited.gv',
    #            node_attr={'shape': 'record'})
    s = Digraph('structs', filename='basic-docs/structs_revisited.gv')

    s.attr(rankdir='LR', size='8,5')

    s.attr('node', shape='record')
    s.node('struct2', '<f0> one|<f1> two', _attributes={"style": "rounded", "border": "0"})
    s.node('struct4', r'<top>top|{a| {t1|{t2|{t3|<f1>bot\ntom}}}}')
    s.node('struct3', r'hello\nworld |{ b |{c|<here> d|e}| f}| g | h')
    s.node('struct1', '{<f0> left|<f1> middle|<f2> right}', _attributes={"color": "Blue"})

    # REMOVE THE ARROWS!
    s.edge('struct1:f1', 'struct2:f0', label="abc", _attributes={"dir": "none", "color": "Red"})
    # DOUBLE ENDED ARROWS!
    s.edge('struct1:f2', 'struct3:here', _attributes={"concentrate": "true", "dir": "both", "color": "Purple"})
    # DIAMOND ARROW HEAD!
    s.edge('struct1:f2', 'struct4:f1', _attributes={"arrowhead": "diamond"})
    s.edge('struct2', 'struct4', _attributes={'taillabel': 'tail', 'headlabel': 'head', 'fontcolor': 'Gold'})


    s.attr('node', shape='doublecircle')
    s.node('LR_0')
    s.node('LR_3')

    s.attr('node', shape='circle')
    s.edge('struct1:f0', 'LR_2', _attributes={"color": "Orange"})
    s.edge('struct1:f0', 'LR_3')
    s.edge('LR_2', 'LR_0')
    s.edge('LR_0', 'struct4:top', _attributes={"color": "Green"})

    s.attr('node', shape='record')
    s.node('struct5', '<f0> ABC|<f1> 123')

    s.attr('node', shape='plaintext')
    s.node('struct6', '''<
    <TABLE BORDER="0" CELLSPACING="0">
      <TR>
        <TD BORDER="1">left</TD>
        <TD PORT="f1" BORDER="1">middle</TD>
        <TD PORT="f2" BORDER="1">right</TD>
      </TR>
    </TABLE>>''')
    s.view()


def fdp():
    # fdpclust.py - http://www.graphviz.org/content/fdpclust
    import os
    # os.environ["PATH"] += os.pathsep + "C:/Program Files/Graphviz 2.44.1/bin"
    os.environ["PATH"] += os.pathsep + "C:/Users/admin9/Downloads/Graphviz/bin"
    from graphviz import Graph

    g = Graph('G', filename='basic-docs/examples/fdpclust.gv')  # , engine='fdp')

    g.node('e')

    with g.subgraph(name='clusterA') as a:
        a.edge('a', 'b')
        with a.subgraph(name='clusterC') as c:
            c.edge('C', 'D')

    with g.subgraph(name='clusterB') as b:
        b.edge('d', 'f')

    g.edge('d', 'D')
    g.edge('e', 'clusterB')
    g.edge('clusterC', 'clusterB')

    g.view()


def basic_graphviz():
    import os
    os.environ["PATH"] += os.pathsep + "C:/Users/admin9/Downloads/Graphviz/bin"
    from graphviz import Digraph
    s = Digraph('structs', filename="basic-docs/examples/basic.gv",
                node_attr={'shape': 'record'})
    s.node('struct1', '{ Main |{a|__init__}| f}')
    s.node('struct2', '<f0> one|<f1> two')
    s.node('struct3', r'hello\nworld |{ b |{c|<here> d|e}| f}| g | h')

    s.edges([('struct1:f1', 'struct2:f0'), ('struct1:f2', 'struct3:here')])
    s.view()
    # s.render('basic-docs/round-table.gv', view=True)


def unix():
    # unix.py - http://www.graphviz.org/content/unix
    import os
    os.environ["PATH"] += os.pathsep + "C:/Users/admin9/Downloads/Graphviz/bin"

    from graphviz import Digraph

    u = Digraph('unix', filename='unix.gv',
                node_attr={'color': 'lightblue2', 'style': 'filled'})
    u.attr(size='6,6')

    u.edge('5th Edition', '6th Edition')
    u.edge('5th Edition', 'PWB 1.0')
    u.edge('6th Edition', 'LSX')
    u.edge('6th Edition', '1 BSD')
    u.edge('6th Edition', 'Mini Unix')
    u.edge('6th Edition', 'Wollongong')
    u.edge('6th Edition', 'Interdata')
    u.edge('Interdata', 'Unix/TS 3.0')
    u.edge('Interdata', 'PWB 2.0')
    u.edge('Interdata', '7th Edition')
    u.edge('7th Edition', '8th Edition')
    u.edge('7th Edition', '32V')
    u.edge('7th Edition', 'V7M')
    u.edge('7th Edition', 'Ultrix-11')
    u.edge('7th Edition', 'Xenix')
    u.edge('7th Edition', 'UniPlus+')
    u.edge('V7M', 'Ultrix-11')
    u.edge('8th Edition', '9th Edition')
    u.edge('1 BSD', '2 BSD')
    u.edge('2 BSD', '2.8 BSD')
    u.edge('2.8 BSD', 'Ultrix-11')
    u.edge('2.8 BSD', '2.9 BSD')
    u.edge('32V', '3 BSD')
    u.edge('3 BSD', '4 BSD')
    u.edge('4 BSD', '4.1 BSD')
    u.edge('4.1 BSD', '4.2 BSD')
    u.edge('4.1 BSD', '2.8 BSD')
    u.edge('4.1 BSD', '8th Edition')
    u.edge('4.2 BSD', '4.3 BSD')
    u.edge('4.2 BSD', 'Ultrix-32')
    u.edge('PWB 1.0', 'PWB 1.2')
    u.edge('PWB 1.0', 'USG 1.0')
    u.edge('PWB 1.2', 'PWB 2.0')
    u.edge('USG 1.0', 'CB Unix 1')
    u.edge('USG 1.0', 'USG 2.0')
    u.edge('CB Unix 1', 'CB Unix 2')
    u.edge('CB Unix 2', 'CB Unix 3')
    u.edge('CB Unix 3', 'Unix/TS++')
    u.edge('CB Unix 3', 'PDP-11 Sys V')
    u.edge('USG 2.0', 'USG 3.0')
    u.edge('USG 3.0', 'Unix/TS 3.0')
    u.edge('PWB 2.0', 'Unix/TS 3.0')
    u.edge('Unix/TS 1.0', 'Unix/TS 3.0')
    u.edge('Unix/TS 3.0', 'TS 4.0')
    u.edge('Unix/TS++', 'TS 4.0')
    u.edge('CB Unix 3', 'TS 4.0')
    u.edge('TS 4.0', 'System V.0')
    u.edge('System V.0', 'System V.2')
    u.edge('System V.2', 'System V.3')

    u.view()


def neato():
    # er.py - http://www.graphviz.org/content/ER

    import os
    os.environ["PATH"] += os.pathsep + "C:/Users/admin9/Downloads/Graphviz/bin"
    from graphviz import Graph

    e = Graph('ER', filename='er.gv') # engine='neato')

    e.attr('node', shape='box')
    e.node('course')
    e.node('institute')
    e.node('student')

    e.attr('node', shape='ellipse')
    e.node('name0', label='name')
    e.node('name1', label='name')
    e.node('name2', label='name')
    e.node('code')
    e.node('grade')
    e.node('number')

    e.attr('node', shape='diamond', style='filled', color='lightgrey')
    e.node('C-I')
    e.node('S-C')
    e.node('S-I')

    e.edge('name0', 'course')
    e.edge('code', 'course')
    e.edge('course', 'C-I', label='n', len='1.00')
    e.edge('C-I', 'institute', label='1', len='1.00')
    e.edge('institute', 'name1')
    e.edge('institute', 'S-I', label='1', len='1.00')
    e.edge('S-I', 'student', label='n', len='1.00')
    e.edge('student', 'grade')
    e.edge('student', 'name2')
    e.edge('student', 'number')
    e.edge('student', 'S-C', label='m', len='1.00')
    e.edge('S-C', 'course', label='n', len='1.00')

    e.attr(label=r'\n\nEntity Relation Diagram\ndrawn by NEATO')
    e.attr(fontsize='20')

    e.view()


def more_graphs():
    # fsm.py - http://www.graphviz.org/content/fsm
    import os
    os.environ["PATH"] += os.pathsep + "C:/Users/admin9/Downloads/Graphviz/bin"
    from graphviz import Digraph

    f = Digraph('finite_state_machine', filename='fsm.gv')
    f.attr(rankdir='LR', size='8,5')

    f.attr('node', shape='doublecircle')
    f.node('LR_0')
    f.node('LR_3')
    f.node('LR_4')
    f.node('LR_8')

    f.attr('node', shape='circle')
    f.edge('LR_0', 'LR_2')
    f.edge('LR_2', 'LR_0')
    f.edge('LR_0', 'LR_1', label='SS(S)')
    f.edge('LR_1', 'LR_3', label='S($end)')
    f.edge('LR_2', 'LR_6', label='SS(b)')
    f.edge('LR_2', 'LR_5', label='SS(a)')
    f.edge('LR_2', 'LR_4', label='S(A)')
    f.edge('LR_5', 'LR_7', label='S(b)')
    f.edge('LR_5', 'LR_5', label='S(a)')
    f.edge('LR_6', 'LR_6', label='S(b)')
    f.edge('LR_6', 'LR_5', label='S(a)')
    f.edge('LR_7', 'LR_8', label='S(b)')
    f.edge('LR_7', 'LR_5', label='S(a)')
    f.edge('LR_8', 'LR_6', label='S(b)')
    f.edge('LR_8', 'LR_5', label='S(a)')

    f.view()

def example_graphviz1():
    # hello.py - http://www.graphviz.org/content/hello
    import os
    os.environ["PATH"] += os.pathsep + "C:/Users/admin9/Downloads/Graphviz/bin"
    from graphviz import Digraph

    g = Digraph('G', filename='hello.gv')
    g.edge('Hello', 'World')
    g.view()


def gcn():
    # http://www.graphviz.org/Gallery/gradient/g_c_n.html
    import os
    os.environ["PATH"] += os.pathsep + "C:/Users/admin9/Downloads/Graphviz/bin"

    from graphviz import Graph

    g = Graph('G', filename='g_c_n.gv')
    g.attr(bgcolor='purple:pink', label='agraph', fontcolor='white')

    with g.subgraph(name='cluster1') as c:
        c.attr(fillcolor='blue:cyan', label='acluster', fontcolor='white',
               style='filled', gradientangle='270')
        c.attr('node', shape='box', fillcolor='red:yellow',
               style='filled', gradientangle='90')
        c.node('anode')

    g.view()

if __name__ == "__main__":
    # cluster()
    # neato()
    # gcn()
    # struct1()
    struct2()
    # create_doc(stop_at_paren=False)

