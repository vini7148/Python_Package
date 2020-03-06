try:
    import datetime
except ImportError:
    raise ImportError("This package needs datetime to execute")
del datetime

from .file_1 import time, sum, avg
from .file_2 import hw