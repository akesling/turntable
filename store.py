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

class AbstractLocalStore(object):
    def retrieve(self, key):
        """Retrieve element value from local store

        Args:
            key: The key we would like to retrieve.

        Raises:
            KeyError: If key not present in table.

        Returns:
            (2-tuple) The information stored at this key. The first element is
            the value, the second is the tag.
        """
        _unimplemented(__name__)

    def store(self, key, value, tag):
        """ Store element locally

        Args:
            key: The key we would like to retrieve.
            value: Whatever value is being stored.
            tag: A tag storing some metadata about the value.

        Returns:
            The key
        """
        _unimplemented(__name__)

    def delete(self, key):
        """Delete element from local store

        Args:
            key: The key we would like to delete.

        Raises:
            KeyError: If key not present in table.

        Returns:
            (2-tuple) The information stored at this key. The first element is
            the value, the second is the tag.
        """
        _unimplemented(__name__)

    def retag(self, key, tag):
        """Retag element in local store

        Args:
            key: The key we would like to retag.
            tag: A tag storing some metadata about the value

        Returns:
            The key

        Raises:
            KeyError: If key not present in table.
        """
         _unimplemented(__name__)


class DictionaryStore(AbstractLocalStore):
    store = dict()
    store_lock = Lock()

    @staticmethod
    def _dict_lock(function):
        def wrapper(args*, kwargs**):
            with store_lock:
                return function(args*, kwargs**)
        return wrapper

    @_dict_lock
    def retrieve(self, key):
        if key in store:
            return store[key]
        else:
            raise KeyError(key)

    @_dict_lock
    def store(self, key, value, tag):
        store[key] = [value, tag]
        return key

    @_dict_lock
    def delete(self, key):
        if key in store:
            result = store[key]
            del store[key]
            return result
        else:
            raise KeyError(key)

    @_dict_lock
    def retag(self, key, tag):
        if not hsh:
            key, part = keys.hash_key(key)
        if key in store:
            store[key][1] = tag
            return key
        else:
            raise KeyError(key)

###############################################################################
## Routing table management ###################################################
###############################################################################

class AbstractRoutingTable(object):

    ## Self ###################################################################

    def get_self(self):
        """
        Get the index and address of this node.
        """
        _unimplemented(__name__)

    def set_self(self, index, address):
        """Set index and address of this node in the routing table.

        Args:
            index: The index to set.
            address: The routing address to store.

        Returns:
            (bool) True if successful, False otherwise.
        """
        _unimplemented(__name__)

    def get_neighbors(self, index):
        """Get the index and address of this node's current neighbors.

        Args:
            index: The index to set to find the neighbors of.

        Returns:
            (2-tuple/bool) If the index exists in the table, return that
            index's neighbors as (left, right), otherwise return None.
        """
        _unimplemented(__name__)

    ## General Table ##########################################################

    def find_route(self, key):
        """Look up a routing index by key.

        Args:
            key: The key we are looking up.

        Returns:
            The routing address where this key is stored or None if this key
            isn't stored in the table.
        """
        hsh, part = keys.get_hash(key, total_nodes())

        return self.get_route((1, part))

    def get_route(self, index):
        """Get the routing address for a given index.

        This index is in the form of a 2-tuple representation of the point on
        the unit interval which this hash represents. The table being
        represented as a ring with (0,0)=(1,1) and any given point on the ring
        being represented by such a fraction.

        Args:
            index: The index for a desired node.

        Returns:
            The routing address for the given index or None if the node does
            not exist.
        """
        _unimplemented(__name__)

    def set_route(self, index, address):
        """Set the given local routing index to the provided address.

        Args:
            index: The index for the node to set.
            address: The address to set for this node.

        Returns:
            (bool) Whether the set operation succeeded.
        """
        _unimplemented(__name__)

    def remove_route(self, index):
        """Remove a route from the routing table.

        Args:
            index: The index for the node to remove.

        Returns:
            The address of the index removed if it existed, None if it didn't.
        """
        _unimplemented(__name__)

    def total_nodes(self):
        """Return total number of nodes in the routing table.
        """
        _unimplemented(__name__)
