"""
Wrapper for communication with other nodes in the table
"""
import keys
import router

###############################################################################
## Helper functions/utilities #################################################
###############################################################################

def _unimplemented(name):
    raise Exception("%s has yet to be implemented." % name)

###############################################################################
## Remote element-set manipulation #############################################
###############################################################################

def retrieve(key):
    """
    Retrieve element value from remote node
    """
    _unimplemented(__name__)

def store(key, value, tag):
    """
    Store element in remote node
    """
    _unimplemented(__name__)

def delete(key):
    """
    Delete element from remote node
    """
    _unimplemented(__name__)

def retag(key, tag):
    """
    Retag element remote node
    """
    _unimplemented(__name__)
