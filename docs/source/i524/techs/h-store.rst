.. add info about H-Store

H-Store is an in memory and parallel database management system
for on-line transaction processing (OLTP). Specifically ,
:cite:`www-Hstore` illustrates that H-Store is a highly
distributed, row-store-based relational database that runs on a
cluster on shared-nothing, main memory executor nodes.As Noted in
:cite:`kallman2008` "the architectural and application shifts
have resulted in modern OLTP databases increasingly falling short
of optimal performance.In particular, the availability of
multiple-cores, the abundance of main memory, the lack of user
stalls, and the dominant use of stored procedures are factors
that portend a clean-slate redesign of RDBMSs".The H-store which
is a complete redesign has the potential to outperform legacy
OLTP databases by a significant factor.  As detailed in
:cite:`www-Hstorewiki` H-Store is the first implementation of a
new class of parallel DBMS, called NewSQL, that provides the
high-throughput and high-availability of NoSQL systems, but
without giving up the transactional guarantees of a traditional
DBMS.  The H-Store system is able to scale out horizontally
across multiple machines to improve throughput, as opposed to
moving to a more powerful , more expensive machine for a
single-node system.

