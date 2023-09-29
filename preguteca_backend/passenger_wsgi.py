import os
import sys

from preguteca_backend.wsgi import application
print(application)
print("test marius")

sys.path.insert(0, os.path.dirname(__file__))

