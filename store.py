"""
DB Wrapper so the HT can be blissfully ignorant of the storage layer.
"""
import keys

###############################################################################
## Helper functions/utilities #################################################
###############################################################################

def _unimplemented(name):
    raise Exception("%s has yet to be implemented." % name)

###############################################################################
## Local element-set manipulation #############################################
###############################################################################

def retrieve(key, value, tag, hsh=False):
    _unimplemented(__name__)

def store(key, value, tag, hsh=False):
    _unimplemented(__name__)

def delete(key, hsh=False):
    _unimplemented(__name__)

def retag(key, tag, hsh=False):
    _unimplemented(__name__)

###############################################################################
## Routing table management ###################################################
###############################################################################

def find_route(key, hsh=False):
    if not hsh:
        hsh = keys.get_hash(key, store.total_nodes())

    _unimplemented(__name__)

def get_route(index):
    _unimplemented(__name__)

def update_route(index, address):
    _unimplemented(__name__)

def remove_route(index, address):
    _unimplemented(__name__)

def total_nodes():
    _unimplemented(__name__)
