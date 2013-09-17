import sys
import hashlib
from MerkleTree import merkle

# Class to find difference between 2 input files
class Diff(object):
    # Constructor for the class Diff
    def __init__(self,fpath1,fpath2):
        self.fpath1 = fpath1
	self.fpath2 = fpath2
	self.src = []
	self.dest = []

    # Make the merkel tree out of the given input files
    # and call "find_diff" method to find the difference 
    # between the two given files
    def make_trees(self):
	ob1 = merkle(self.fpath1)
	ob2 = merkle(self.fpath2)
	self.src = ob1.execute()
	self.dest = ob2.execute()
	self.find_diff(ob1,ob2)

    # Function to check every file block of target file and see 
    # if the block is similar to the source file or not
    def find_diff(self,ob1,ob2):
	start = len(ob2.tree)/2
	end = ob2.num_piece
	
	for i in xrange(start, start + end):
	    self.check_leaf(ob2,i,ob1)    
	
    # Function implementing the algo to build the root hash from a given leaf node
    # The file block under inspection is first hashed. The hash of sibling block is
    # requested from the original file. The two hashes are concatenated and hashed again (1)
    # The block also ask for hash of its uncle node(parent's sibling) (2). (1) & (2) are hashed 
    # and this process is repeated until the root is reached. Then we compare the root hash of the 
    # target block with the root hash of the source file. If they are the same it means the target
    # file block is same as that of the original file block, else they are different. 
    def check_leaf(self,ob2, index, ob1):
	tmpindex = index
	c1 = ob2.tree[index]
	c2 = ob1.tree[ob1.find_sibling(index)]

	while int(tmpindex) != 0:
	    if tmpindex % 2 == 0:
	        new_str = c2 + c1
	    else:
		new_str = c1 + c2
	    h = hashlib.sha1(new_str).hexdigest()
	    c1 = h
	    c2 = ob1.tree[ob1.find_uncle(tmpindex)]
	    tmpindex = ob1.find_parent(tmpindex) 
	
	if c1 == ob1.tree[0]:
	    print "No Difference at block " + str(index -len(ob2.tree)/2) + "\n" 
	else:
	    print "Difference at block " + str(index -len(ob2.tree)/2) + "\n" 
