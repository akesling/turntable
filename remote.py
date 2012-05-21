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

def retrieve(key, value, tag, hsh=False):
    _unimplemented(__name__)

def store(key, value, tag, hsh=False):
    _unimplemented(__name__)

def delete(key, hsh=False):
    _unimplemented(__name__)

def retag(key, tag, hsh=False):
    _unimplemented(__name__)
