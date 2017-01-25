.. add info about Voldemort

According to :cite:`www-voldemort`, project Voldemort, developed
by LinkedIN, is a non-relational database of key-value type that
supports eventual consistency. The distributed nature of the
system allows pluggable data placement and provides horizontal
scalability and high consistency. Replication and partitioning of
data is automatic and performed on multiple servers. Independent
nodes that comprise the server support transparent handling of
server failure and ensure absence of a central point of
failure. Essentially, Voldemort is a hashtable. It uses APIs for
data replication. In memory caching allows for faster
operations. It allows cluster expansion with no data
rebalancing. When Voldemort performance was benchmarked with the
other key-value databases such as Cassandra, Redis and HBase as
well as MySQL relational database
(:cite:`rabl_sadoghi_jacobsen_2012`), the Voldemart's throughput
was twice lower than MySQL and Cassandra and six times higher
than HBase. Voldemort was slightly underperforming in comparison
with Redis.  At the same time, it demonstrated consistent linear
performance in maximum throughput that supports high scalability.
The read latency for Voldemort was fairly consistent and only
slightly underperformed Redis. Similar tendency was observed with
the read latency that puts Voldermort in the cluster of databases
that require good read-write speed for workload
operations. However, the same authors noted that Voldemort
required creation of the node specific configuration and
optimization in order to successfully run a high throughput
tests. The default options were not sufficient and were quickly
saturated that stall the database.

