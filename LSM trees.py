LSM trees: https://www.youtube.com/watch?v=I6jB0nM9SKU

1. it is the secret sauce behind many NoSQL databases. 
2. LSM - Log structure merge tree, it is a datastructure
3. It is optimised for fast writes
4. Writes are bashed in a memory in a structure called a "memtable" 
5. a memtable is ordered by "object key"
6. memtable is usually implemented as a balaned binary tree
7. when a memtable reaches a certain size, it is flushed into the disk as an immutable sorted string table
8. an "sstable" stores a key-value pair in a sorted sequence
9. these rights are all "sequential I/O". they are fast on any storage media
10. the new sstable becomes the most recent segment of the LSM tree
11. deleting an object requires special effort too, as we cannot mark somthing as deleted 
12. to register deletes sstables have a marker called "tombstone marker" to the most recent object of the sstable. 
13. when we see a tombstone marker, it means the most recent object was deleted
14. to serve a read request, we first do a find in the memtable and then in the most recent sstable and then the next larger sstable and so on
15. (p.s. all this is set as a pyramid, 
     memtables
     sstable 
     larger sstable 
     very large sstables
16. The sstables are later on merged and hence forming lower levels
17. this merging is similar to the merge sort as the objects and hence smaller sstables are already in a sorted order
18. this merging is also called as "compaction:
19. there are 2 types of compaction strategies: 
     - size tier compaction ( done is cassandra, optimised for writes)
     - leveling (done in RocksDB, optmised for reads)
20. compaction keeps the number of sstables managable
21. compaction consumes a lot a I/O

FOR KEY LOOKUP:
1. we perform a search at each level of the tree, starting from memtables
2. since the data is already sorted, it is fast, but since the data is huge it can take a lot of resources, to prevent this many systems use as "bloom filter"
    this gives us a probabilty if data is present of not, hence increasing ths efficiency of the system
3. 

     
     
     
     
How data is typically stored in a RDBMS: MySQL and PostgreSQL?
- They are commonly backed by a DS called B-tree
- B-trees are optimised for reads 
- updating a B-tree is relatively expensive, as it requires random I/O and might require updating multiple pages on a disk


