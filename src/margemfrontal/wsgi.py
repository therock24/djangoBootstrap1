import os 
import time 
import traceback 
import signal 
import sys 
 
from django.core.wsgi import get_wsgi_application 
 
sys.path.insert(0, '/home/ubuntu/djangoBootstrap1/src/margemfrontal')
sys.path.insert(1, '/home/ubuntu/djangoBootstrap1/src')
#sys.path.append('/home/ubuntu/djangoBootstrap1/src') 
# adjust the Python version in the line below as needed 
sys.path.append('/home/ubuntu/djangoBootstrap1/src/venv/lib/python3.6/site-packages') 
 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "margemfrontal.settings") 
 
try: 
    application = get_wsgi_application() 
except Exception: 
    # Error loading applications 
    if 'mod_wsgi' in sys.modules: 
        traceback.print_exc() 
        os.kill(os.getpid(), signal.SIGINT) 
        time.sleep(2.5) 
