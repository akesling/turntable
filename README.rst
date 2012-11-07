(Julython test)
segmented node-network with n partitions.

- All nodes retain a routing table which is updated in a gossip-style fashion.
- All data is replicated 3 times:
    Nodes:   _Y_   _Z_   _A_   _B_   _C_
    Data: ...|Y|Z|Y|Z|A|Z|A|B|A|B|C|B|C|...

    "Left" and "Right" neighbors replicate a node's data (element-set).

- Thus:
    - All STORES/DELETES to A are repeated by A to Z and B.
    - May retrieve from any/all (of the) three "replicants".

- Creation/insertion of a node creates a new partition once node is initialized.
    - An insertion of a node Q between A and B would result in A and B splitting their respective element-sets and "migrating" those portions to Q which it has now been allotted by the new partitioning scheme.  At the same time as this migration is occurring, A and B are sharing their core element-set with Q for replication.  NOTE that these are not mutually exclusive.  Q will end up storing _all_ data from the element sets of A and B, but some will be marked as Q's data and some marked as A's or B's. Thus, upon inserting a node, the entirety of A's and B's element sets may be transmitted to Q with "migration marking" occurring either before or after transmission (it should also be noted that all three nodes must be aware of who "owns" a given element after insertion is complete).

- Upon node deletion/failure, its element-set is divvied up and merged into its neighbors' core element-sets.  When deletion/failure occurs, the neighbors must also share their element sets as is done upon insertion.
    - This "divvying" is done by splitting the set along the new hash-table bounds. Note that each node already retains the full element set... it must now mark those elements within its partition block as part of its element-set and move those which are not into the appropriate neighbors replicant-set.

- Thus the only times when an element is deleted are upon node insertion or an explicit delete call.

- Because of the partitioning scheme, insertion/deletion must be distributed around the ring in an even fashion to provide maximal dispersion (try to have the greatest homogeneity for total quantity of elements per node).

- To prevent multi-insertion issues, require node to update "inserter" upon completing each initialization phase.

- Considering the inherently single-core design of TurnTable, allow multiple nodes to run from the same host.
    - This implies that a node should be able to "insert" a node on the same host by effectively forking
    - Allow node to run in non-storage mode.  Then each server can run a non-storage node independently of the ring which has a potentially current routing table. Allowing "passive" nodes to be "insertion-brokers".

- At some point "effective replicants" should be a TurnTable param. E.G. one should be able to choose the number of copies a given element-set should have.

- Potentially have replicants be an element level parameter?  This would allow for prioritizing some data as more durable/important (increasing fault tolerance for those subsets without decreasing general replicant performance)

- To further decrease issues with the "multi-insertion" problem, only allow neighbor nodes to process insertion requests.  Thus all insertions are forwarded to the neighbors of the desired insertion location.  Original requester should be informed of node creation stages as they occur to put a set of checks on insertion.  This would allow for a failed insertion on the neighbor level to be caught by the original inserter.

- Neighbors should also negotiate who will insert so that double insertion can't occur and an extra set of checks is built in for catching insertion failure.

- Nodes could potentially have a facility to do an insertion locally if they are under high load.  There needs to be some way to restrict this such that the ring can't grow beyond certain configured restrictions.
    - Maybe have an "open pool" count that decrements on insertion and is propagated like the routing table?

- Insertion of a node must wait for prior insertions in that location to complete (both neighbors must be "current").

- At some point, a pluggable backend store would be preferable.  Then one could swap in, say, PostgreSQL and link multiple local nodes to the same store (would likely increase local node performance) or link each node to a redis instance... there are a decent number of interesting things TurnTable could do with a pluggable backend.

- Populating a newly inserted node should only require that node to pull data from replicants (instead of replicants pushing).  This requires some bulk GET facility w/ a robust mechanism of acquiring incremental partial results (pages).

- Should a new node inform an "old" replicant upon successful insertion of a given element?  Maybe... though it would definitely increase traffic.

- Upon receipt of GET for non-local data, node may ask any known replicants for that data (they don't have to GET from the core node for that element).
    - Random selection from known pool of replicants could evenly distribute the load on those nodes... note that without further constraints that the left/right neighbor share, there are only three locations for a given element.