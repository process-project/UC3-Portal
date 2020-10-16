import sys
import os

#Path to your virtual environment
activate_py='env/bin/activate_this.py'

__basedir__ = os.path.abspath(os.path.dirname(__file__))
activate_this=os.path.join(__basedir__, activate_py)
execfile(activate_this, dict(__file__=activate_this))

sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)),'.'))

sys.path.append(__basedir__)

#Configure Directory 
from browsepy import app as application
application.config['directory_start']='/tmp'
application.config['directory_base']='/tmp'
application.config['directory_ignore'] = ['IGNOREME', 'MeToo']
application.config["use_binary_multiples"] = False
application.config['title'] = 'TITLE'

