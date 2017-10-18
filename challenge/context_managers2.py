from contextlib import contextmanager
from io import StringIO

@contextmanager
def redirected_std_streams(stdout=StringIO(), stderr=StringIO(), stdin=StringIO()):
    yield (stdout, stderr, stdin)
