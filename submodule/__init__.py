import sys
import os
import inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
sys.path.append(current_dir)
"""
This DOES make it 'work' but I don't know if this is a GOOD way to do it or not...
It seems like a dumb way to make it work and there should be a 'better' way to do it.
but I have not been able to think of the better one. I am just GLAD I thought of THIS one.
and don't have to have all of those annoying try's for my imports.

"""

# from submodule import *
# from submodule.parent import *
# from submodule.child import *
