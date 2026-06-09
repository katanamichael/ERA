# PythonAnywhere WSGI configuration for Emergency Response App
# Place this content into the WSGI configuration file on PythonAnywhere
# (accessible from Web tab → WSGI configuration file)

import os
import sys

# Set the project path
project_home = '/home/michaelkatana/ERA/emergencyresponse_pr'

# Add the project directory to the Python path
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'emergencyresponse_pr.settings')

# Django application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
