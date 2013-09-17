import sys
import os
import math
import hashlib

#Class for Merkle Tree Implementation
class merkle(object):
    # constructor for the class merkle	
    def __init__(self,fpath):
	# List to store merkle tree 
        self.tree = []
	# Variable to store the filepath
	self.fpath = fpath
	# Variable to store the number of chunks the file is broken into 
	self.num_piece = 0
	# Variable to get n such that 2^n  > self.num_piece. The idea is to 
	# create a binary tree with leaf nodes linking to the chunks. Suppose
	# the chunk size is 12 so next number which is > 12 and also a power
	# of 2 is 16, giving us n = 4. So we create a biary tree with 16
	# leaves. So total number of nodes in the tree will be 2^(n+1) -1
	# for simplicity we will be storing "n+1" rather than "n"
	self.next_pow = 0
	# List to store chunks of the text file
	self.file_pieces = []
	# Dictionary to link file chunks to leaves
	self.link = {}

    # function to make chunks of the input file and store these chunks in 
    # "file_pieces" list
    def make_file_pieces(self):
	with open(self.fpath, 'rb') as fin:
	    # Make chunks of size 40 KB each
            chunks = list(iter(lambda: fin.read(40 * 1024), ''))
	
	self.num_piece = len(chunks)
	for item in chunks:
	    self.file_pieces.append(item)

    # function to initialize the merkle tree
    def make_tree(self):
	self.next_pow = math.ceil(math.log(self.num_piece,2)) + 1
	tree_range = int(math.pow(2,self.next_pow) -1)
        for i in xrange(0,tree_range):
	    self.tree.append(i)

    # Function to link the file pieces to leaf nodes of merkle tree
    def link_piece_to_leaves(self):
        leaves = self.tree[len(self.tree)/2 : ]
	
	len_diff = len(self.tree) - len(self.file_pieces)
	for item in xrange(0,len_diff):
	    self.file_pieces.append(str(0))

	for a,b in zip(leaves, self.file_pieces):	
	    self.link[a] = b

    # Function to create hashes and build the complete merkle tree
    def make_hash(self):
	for key, val in self.link.items():
	    h = hashlib.sha1(val).hexdigest()
	    self.tree[key] = h

	for i in xrange(len(self.tree)/2 -1, -1,-1):
	    l = self.left_child(i)
	    r = self.right_child(i)
	    new_str = self.tree[l] + self.tree[r]
	    h = hashlib.sha1(new_str).hexdigest()
	    self.tree[i] = h

	return self.tree
	    
    # Function to find sibling of a node
    def find_sibling(self,i):
	if i%2 == 0:
	    return i - 1
	else:
	    return i + 1

    # Function to find uncle(parent's sibling) of a node
    def find_uncle(self,i):
	parent = self.find_parent(i)
	uncle = self.find_sibling(parent)
	return uncle

    # Function to find parent of a node
    def find_parent(self,i):
	return int(math.floor((i-1)/2));

    # Function to find left child of a parent node (non-leaf node)
    def left_child(self,i):
	return 2*i + 1

    # Function to find right child of a parent node (non-leaf node)
    def right_child(self,i):
	return 2*i + 2

    # Function to print the merkle tree
    def print_tree(self):
	print self.tree

    # Wrapper function to do all processing required in order to make 
    # merkle hash tree
    def execute(self):
	self.make_file_pieces()
	self.make_tree()
	self.link_piece_to_leaves()
	return self.make_hash()
