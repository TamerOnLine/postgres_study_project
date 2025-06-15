# base_header_template.py
import os
import sys

# تحديد المسار الجذر للمشروع
ROOT = os.path.abspath(os.path.dirname(__file__))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)
