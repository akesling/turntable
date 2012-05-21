import hashlib

def hash_key(key, partitions=0, hasher=hashlib.sha512):
    """
    Take a string-valued key and return its hash.

    Args:
        key: value to be hashed
        partitions: long, number of segments in hashtable
        hasher: object, hash object fulfilling interface seen in hashlib

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
        return (val, int(val,16) % part)

    return (val, part)
