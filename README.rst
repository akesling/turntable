segmented node-network with n partitions.

- All nodes retain a routing table which is updated in a gossip-style fashion.
- All data is replicated 3 times:
    Nodes:   _Y_   _Z_   _A_   _B_   _C_
    Data: ...|Y|Z|Y|Z|A|Z|A|B|A|B|C|B|C|...

    "Left" and "Right" neighbors replicate a node's data (element-set).

- Thus:
    - All STORES/DELETES to A are repeated by A to Z and B.
    - May retrieve from any/all (of the) three "replicants".

- Creation/insertion of a node creates a new partiiton once node is initialized.
    - An insertion of a node Q between A and B would result in A and B splitting their respective element-sets and "migrating" those portions to Q which it has now been allotted by the new partitioning scheme.  At the same time as this migration is occurring, A and B are sharing their core element-set with Q for replication.  NOTE that these are not mutually exclusive.  Q will end up storing _all_ data from the element sets of A and B, but some will be marked as Q's data and some marked as A's or B's. Thus, upon inserting a node, the entirety of A's and B's element sets may be transmitted to Q with "migration marking" occurring either before or after transmission (it should also be noted that all three nodes must be aware of who "owns" a given element after insertion is complete).

- Upon node deletion/failure, its element-set is divvied up and merged into its neighbors core element-sets.  When deletion/failure occurs, the neighbors must also share their element sets as is done upon insertion.
    - This "divvying" is done by splitting the set along the new hash-table bounds. Note that each node already retains the full element set... it must now mark those elements within its partition block as part of its element-set and move those which are not into the appropriate neighbors replicant-set.

- Thus the only times when an element is deleted are upon node insertion or an explicit delete call.

- Because of the partitioning scheme, insertion/deletion must be distributed around the ring in an even fashion to provide maximal dispersion (try to have the greatest homogeneity for total quantity of elements per node).
