from pathlib import Path

from django.test import TestCase

# Create your tests here.
# file_dir=Path(__file__).resolve().parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)
