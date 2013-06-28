import hashlib
from errors import *

def hash_key(key, partitions=0, hasher=hashlib.sha512):
    """Take a string-valued key and return its hash.

    Args:
        key: value to be hashed
        partitions: (long) number of segments in hashtable
        hasher: (object) hash object fulfilling interface seen in hashlib

    Returns:
        2-Tuple of hash as hex-string and to which segment of the
            partition it belongs
    """
    if isinstance(key, basestring):
        hsh = hasher(key)
    else:
        raise TypeError("Key of type (%s) must be a string value" % type(key))

    val = hsh.hexdigest()

    part = long(partitions)
    if part > 0:
        part = long(val, 16) % part

    return (val, part)


def calc_index(partition, total_parts):
    """Calculate the generic index for a given partition.

    The index returned is not necessarily the index of any node in the ring.
    This means that further search will need to occur on a local basis to
    find which node actually contains the element (this is likely to occur in
    a large number of cases).

    Local search may proceed linearly as each node is a pivot between known
    partitions.  This means that a node should be able to know which direction
    along the ring to move in order to find the given element.

    Args:
        partition: the segment along the ring in clockwise order for
            which we are calculating the appropriate index
        total_parts: the total number of partitions (equivalently, total number
            of nodes minus one) on the ring

    Returns:
        (index) the 2-tuple index (first element numerator, second denomenator)
        representing the point along the unit circle which should be close
        to the actual index of the element.
    """
    _unimplemented(__name__)
