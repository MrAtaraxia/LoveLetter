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
    for number, cur_class in enumerate(all_classes):
        current_struct += "{" + cur_class["name"] + "|"
        for meth in cur_class["methods"]:
            current_struct += meth + "|"
        current_struct = current_struct[:-1] + "}"  # removes the last | and adds the close
        s.node(struct_name + str(number), current_struct)
        current_struct = ""
    s.view()

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
    create_doc(stop_at_paren=False)

