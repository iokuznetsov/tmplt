import pytest
from tmplt import Fibonacci

def test_import():
    # This checks __init__ was set up correctly
    try:
        from tmplt import Fibonacci
    except ImportError:
        assert False

##### YOUR CODE HERE #####

##########################