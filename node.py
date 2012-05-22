"""
Manage node-level maintenance/repair
"""

###############################################################################
## Helper functions/utilities #################################################
###############################################################################

def _unimplemented(name):
    raise Exception("%s has yet to be implemented." % name)

###############################################################################
## Helper functions/utilities #################################################
###############################################################################

def insert_self(address):
    """
    Initialization upon first entering the table
    """
    _unimplemented(__name__)

def new_neighbor(index):
    """
    Handle the insertion of a new neighbor
    """
    _unimplemented(__name__)

def dead_neighbor(index):
    """
    Handle the deletion/failure of a neighbor
    """
    _unimplemented(__name__)

def delete_self(left, right):
    """
    Gracefully remove this node from the table
    """
    _unimplemented(__name__)
