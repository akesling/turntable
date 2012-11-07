"""
DB Wrapper so the HT can be blissfully ignorant of the storage layer.
"""
import keys
from threading import Lock
from errors import *

###############################################################################
## Helper functions/utilities #################################################
###############################################################################


###############################################################################
## Local element-set manipulation #############################################
###############################################################################

class AbstractStore(object):
    def retrieve(self, key, hsh=False):
        """Retrieve element value from local store

        Args:
            key: The key we would like to retrieve.
            hsh: Whether the key is already the desired hash

        Raises:
            KeyError: If key not present in table.

        Returns:
            (2-tuple) The information stored at this key. The first element is the
            value, the second is the tag.
        """
        _unimplemented(__name__)

    @dict_lock
    def store(self, key, value, tag, hsh=False):
        """ Store element locally

        Args:
            key: The key we would like to retrieve.
            value: Whatever value is being stored.
            hsh: Whether the key is already the desired hash
            tag: A tag storing some metadata about the value

        Returns:
            The key's hash
        """
        _unimplemented(__name__)

    def store(self, key, value, tag, hsh=False):
        """ Store element locally

        Args:
            key: The key we would like to retrieve.
            value: Whatever value is being stored.
            hsh: Whether the key is already the desired hash
            tag: A tag storing some metadata about the value

        Returns:
            The key's hash
        """
        _unimplemented(__name__)

    @dict_lock
    def delete(self, key, hsh=False):
        """Delete element from local store

        Args:
            key: The key we would like to delete.
            hsh: Whether the key is already the desired hash.

        Raises:
            KeyError: If key not present in table.

        Returns:
            (2-tuple) The information stored at this key. The first element is the
            value, the second is the tag.
        """
        _unimplemented(__name__)

    @dict_lock
    def retag(self, key, tag, hsh=False):
        """Retag element in local store

        Args:
            key: The key we would like to retag.
            hsh: Whether the key is already the desired hash
            tag: A tag storing some metadata about the value

        Returns:
            The key's hash

        Raises:
            KeyError: If key not present in table.
        """
         _unimplemented(__name__)


class DictionaryStore(AbstractStore):
    store = dict()
    store_lock = Lock()

    @staticmethod
    def dict_lock(function):
        def wrapper(args*, kwargs**):
            with self.store_lock:
                return function(args*, kwargs**)
        return wrapper

    @dict_lock
    def retrieve(self, key, hsh=False):
        if not hsh:
            key, part = keys.hash_key(key)
        return store[key]

    @dict_lock
    def store(self, key, value, tag, hsh=False):
        if not hsh:
            key, part = keys.hash_key(key)
        store[key] = [value, tag]
        return key

    @dict_lock
    def delete(self, key, hsh=False):
        if not hsh:
            key, part = keys.hash_key(key)
        result = store[key]
        del store[key]
        return result

    @dict_lock
    def retag(self, key, tag, hsh=False):
        if not hsh:
            key, part = keys.hash_key(key)
        store[key][1] = tag
        return key

###############################################################################
## Routing table management ###################################################
###############################################################################

class AbstractRoutingTable(object):

    ## Self ###################################################################

    def get_self(self):
        """
        Get the index and address of this node
        """
        _unimplemented(__name__)

    def set_self(self, index, address):
        """Set index and address of this node in the routing table.

        Args:
            index:
            address:

        Returns:
        """
        _unimplemented(__name__)

    def get_neighbors(self, index):
        """Get the index and address of this node's current neighbors.

        Args:
            index:

        Returns:
        """
        _unimplemented(__name__)

    ## General Table ##########################################################

    def find_route(self, key, partition=0, hsh=False):
        """Look up a routing index by key/hash.

        Args:
            key: The key we are looking up. 
            partition: 
            hsh:

        Returns:
        """
        if not hsh:
            hsh, part = keys.get_hash(key, total_nodes())
        else:
            hsh = key
            part = partition

        return self.get_route((1, part))

    def get_route(self, index):
        """Get the routing address for a given index.

        This index is in the form of a 2-tuple representation of the point on
        the unit interval which this hash represents. The table being
        represented as a ring with (0,0)=(1,1) and any given point on the ring
        being represented by such a fraction.

        Args:
            index:

        Returns:
        """
        _unimplemented(__name__)

    def set_route(self, index, address):
        """Set the given local routing index to the provided address.

        Args:
            index:
            address:

        Returns:
        """
        _unimplemented(__name__)

    def remove_route(self, index, address):
        """Remove a route from the routing table.

        Args:
            index:
            address:

        Returns:
        """
        _unimplemented(__name__)

    def total_nodes(self):
        """Return total number of nodes in the routing table.
        """
        _unimplemented(__name__)