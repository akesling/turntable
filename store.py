"""
DB Wrapper so the HT can be blissfully ignorant of the storage layer.
"""
import keys
from errors import *

###############################################################################
## Helper functions/utilities #################################################
###############################################################################


###############################################################################
## Local element-set manipulation #############################################
###############################################################################

def retrieve(key, hsh=False):
    """
    Retrieve element value from local store
    """
    _unimplemented(__name__)

def store(key, value, tag, hsh=False):
    """
    Store element locally
    """
    _unimplemented(__name__)

def delete(key, hsh=False):
    """
    Delete element from local store
    """
    _unimplemented(__name__)

def retag(key, tag, hsh=False):
    """
    Retag element in local store
    """
    _unimplemented(__name__)

###############################################################################
## Routing table management ###################################################
###############################################################################

## Self #######################################################################

def get_self():
    """
    Get the index and address of this node
    """
    _unimplemented(__name__)

def set_self(index, address):
    """
    Set index and address of this node in the routing table
    """
    _unimplemented(__name__)

def get_neighbors(index):
    """
    Get the index and address of current neighbors
    """
    _unimplemented(__name__)

## General Table ##############################################################

def find_route(key, partition=0, hsh=False):
    """
    Look up routing index by key/hash
    """
    if not hsh:
        hsh,part = keys.get_hash(key, total_nodes())
    else:
        hsh = key
        part = partition

    return get_route((1,part))

def get_route(index):
    """
    Get routing address given index

    This index is in the form of a 2-tuple representation of the point on
    the unit interval which this hash represents. The table being represented
    as a ring with (0,0)=(1,1) and any given point on the ring being
    represented by such a fraction.

    """
    _unimplemented(__name__)

def update_route(index, address):
    """
    Update local routing index with provided address
    """
    _unimplemented(__name__)

def remove_route(index, address):
    """
    Remove route from table
    """
    _unimplemented(__name__)

def total_nodes():
    """
    Return total nodes in table
    """
    _unimplemented(__name__)
