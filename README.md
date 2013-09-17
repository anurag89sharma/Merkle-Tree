Merkle-Tree
===========

** NOTE **
--- This program checks the difference in the 2 files by breaking them into chunks of size 40 KB each. So if to append some characters in the file(at the beginning or at the middle) then the characters going into the chunks (or file blocks) will change and all the chunks will differ from the original so the program will compute all the blocks as different. To get the correct implementation we should add and delete the same number of chracters in the file, so as to preserve the ordering of characters going into the chunks(file blocks).

-- This make sense because the main purose of merkle tree is to check the correctness of file transferred over the network and find which file block/s is/are corrupted 

-- Referred merkle from this link -- http://www.tribler.org/trac/wiki/MerkleHashes

About code.
This folder has 2 files .
	MerkleTree.py -- Contains basic implementation of Merkle Tree
	problem2.py -- Contain implementation of finding difference between
		       the file blocks of the given input files 


How to run(Tested on ubuntu 12.04, unsure about windows (should work though))
1. From the terminal go the the directory where code is present
2. Type "python" (without quotes)
3. Suppose the files to be tested are file1.txt(original/correct file) and file2.txt (file to be checked for corruption in file blocks)
4. Type the follwing lines to execute the program
	import problem2 as pr
	obj = pr.Diff('file1.txt', 'file2.txt')
	obj.make_trees()
	
Sample Run

anurag@Anurag:~/Desktop/Problem2$ python

>>> import problem2 as pr
>>> obj = pr.Diff('cguide1.txt', 'cguide2.txt')
>>> obj.make_trees()
Difference at block 0

No Difference at block1

No Difference at block2

No Difference at block3

No Difference at block4

No Difference at block5

No Difference at block6

No Difference at block7

No Difference at block8

No Difference at block9

No Difference at block10


