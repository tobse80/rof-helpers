# Use *EXPLICIT* path modification to resolve local packages properly
# From: https://docs.python-guide.org/writing/structure/

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
