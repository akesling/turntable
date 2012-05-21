"""
DB Wrapper so the HT can be blissfully ignorant of the storage layer.
"""
import keys

def _unimplemented(name):
    raise Exception("%s has yet to be implemented." % name)

def store_local(key, value, tag, hsh=False):
    _unimplemented(__name__)

def delete_local(key, hsh=False):
    _unimplemented(__name__)

def retag_local(key, tag, hsh=False):
    _unimplemented(__name__)
