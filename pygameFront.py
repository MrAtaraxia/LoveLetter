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
        <TD ROWSPAN="3">hello<BR/>world</TD>
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


def struct2():
    # structs_revisited.py - http://www.graphviz.org/pdf/dotguide.pdf Figure 12

    import os
    os.environ["PATH"] += os.pathsep + "C:/Users/admin9/Downloads/Graphviz/bin"
    from graphviz import Digraph

    s = Digraph('structs', filename='structs_revisited.gv',
                node_attr={'shape': 'record'})

    s.node('struct1', '<f0> left|<f1> middle|<f2> right')
    s.node('struct2', '<f0> one|<f1> two')
    s.node('struct3', r'hello\nworld |{ b |{c|<here> {aa|{cc|dd}bb}d|e}| f}| g | h')

    s.edges([('struct1:f1', 'struct2:f0'), ('struct1:f2', 'struct3:here')])

    s.view()

def fdp():
    # fdpclust.py - http://www.graphviz.org/content/fdpclust
    import os
    # os.environ["PATH"] += os.pathsep + "C:/Program Files/Graphviz 2.44.1/bin"
    os.environ["PATH"] += os.pathsep + "C:/Users/admin9/Downloads/Graphviz/bin"
    from graphviz import Graph

    g = Graph('G', filename='basic-docs/examples/fdpclust.gv', engine='fdp')

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


def example_graphviz1():
    # hello.py - http://www.graphviz.org/content/hello
    import os
    os.environ["PATH"] += os.pathsep + "C:/Users/admin9/Downloads/Graphviz/bin"
    from graphviz import Digraph

    g = Digraph('G', filename='hello.gv')
    g.edge('Hello', 'World')
    g.view()


if __name__ == "__main__":
    struct2()
    # create_doc(stop_at_paren=False)

