# import_helper.py
import os, sys

def import_from_root():
    ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../"))
    if ROOT not in sys.path:
        sys.path.insert(0, ROOT)
