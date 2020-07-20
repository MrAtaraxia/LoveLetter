import inspect
import os
import sys

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

"""
This SHOULD ALWAYS add the upper one. no matter what folder it is in.
Yep!
It works in ALL folders now I think.
"""

"""
This ONLY works from inside the upper directory.
#import sys
#import os
#sys.path.append(os.getcwd())


"""