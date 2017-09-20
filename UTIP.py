##############
# QUESTION 1 #
##############

# My understanding of the question: 
# 1) If t contains only the letters from s return True
# 2) Letters from s can appear in t only as many times as they do in s
# 3) Empty strings are no considered anagrams

# Why I approached the question this way:
# no nested for loops that take extra time
# if a character occurs more times in t then t cannot be a substring of s

# efficiency will be O(n)

def question1(s, t):
	# check if function input is valid
	if s and t:
		# iterate through all characters in s
		for i in range(0, len(t)):
			# compare count of a character in t with the count of same character in s
			# if count of a character in t exceeds s, return False 
			if t.count(t[i]) > s.count(t[i]):
				return False
		return True
	# return False if nothing is entered
	else:
		return False

# test cases
# empty strings
# repetition of letter in string i.e. 'a' in 'anagram'
# string without anagram
# string with anagram

##############
# QUESTION 2 #
##############

# My understanding of the question:
# 1) If a contains a palindrome then return longest such palindrome
# 2) A palindrome is a string that is the same backwards as forwards i.e. anna = anna
# 3) If string contains no palindrome then return first character in string

# Why I approached the question this way:
# This approach breaks down the longest palindrome problem into two sepaarte problems
# First find all possible substrings of a string
# Then check if a substring is a palindrome

# efficiency will be O(n*n)

# returns all possible substrings of a string
def getSubStrings(a):
    length = len(a)
    sub_strings = []
    # iterates through given string
    for i in range(length):
    	sub_string = ''
    	# iterates through given string from both sides
    	# to identify all possible substrings
    	# between first and last character
        for j in range(i + 1, length + 1):
            sub_string = a[i:j]
            # appends each substring to substrings array
            sub_strings.append(sub_string)
    # returns all substrings of a string
    return sub_strings

# checks if a string is a palindrome
def isPalindrome(a):
	# checks if a string is the same as teh reverse of that string
	if a == a[::-1]:
		# returns True if string equals reverse string
		return True
	# else returns False
	return False

# returns longest palindrome in a string
def getLongestPalindrome(a):
	longest_palindrome = ''
	# if given string is shorter than 2 characters, returns string
	if len(a) < 2:
		return a
	else:
		# iterates through all substrings of the given string
		for i in getSubStrings(a):
			# checks if a substring is a palindrome
			# checks for the longest palindrome by comparing len of palindrome substrings
			if isPalindrome(i) and len(i) > len(longest_palindrome):
				# saves a substring palindrome as longest palindrome based on length of substring
				longest_palindrome = i
	# returns longest palindrome
	return longest_palindrome

# test cases
# string without any palindromes i.e. 'abcde'
# entire string is palindrome i.e. 'alevela'
# string has only one palindrome i.e. 'banana'
# string has multipl palindromes i.e. 'annalevels'

##############
# QUESTION 4 #
##############

# My understanding of the question:
# Find Least Common Ancestor of two nodes in a BST
# BST is represented by a 2D matrix
# Each node is an integer
# Both of the given nodes are always in BST
# T = tree, r = int value of root, n1 and n2 are non-negative integers

# Why I approached the question this way:
# I wanted to avoid nested loops leading to greater time
# Simple solution run recursively
# Build upon the fact that BST is sorted

def question4(T, r, n1, n2):
    print ' '
    # check if n1 and n2 are on different sides of the root
    if (n1 > r and n2 < r) or (n1 < r and n2 > r):
        # return root if n1 and n2 are on different sides
        # because in this case the root is the only common ancestor
        return r
    # check if both n1 and n2 are smaller than root
    elif (n1 < r and n2 < r):
        left = T[r].index(1)
        # check if n1 or n2 equals left child of root
        if n1 == left or n2 == left:
            return r
        # change root to left child
        else:
            r = left
    # check if both n1 and n2 are greater than root
    elif (n1 > r and n2 > r):
        right = len(T[r]) - T[r][::-1].index(1) - 1
        # check if n1 or n2 equals right child of root
        if n1 == right or n2 == right:
            return r
        else:
            # change root to right child
            r = right
            
    # run recursively with updated root
    return question4(T, r, n1, n2)

# test cases
# Given nodes are children of same parent
# Given nodes are children of different parents
# Given nodes have a parent child relationship
# Given nodes are on same side of BST
# Given nodes are on different sides of BST

##############
# QUESTION 5 #
##############

# My understanding of the questions:
# Given first node of a linkedlist, return the element at a backwards index
# For instance: for 3 return the 3rd last element in list
# If linkedlist is empty then return None
# If given number is outside range return None

# efficiency O(n)

# Why I approached the question this way:
# counting the number of nodes in list will take O(n) which is decent time for lookup
# I was limited by the definition of nodes in the linkedlist
# if I could change the definition I will change it to allow for a doubly linkedlist
# That will allow for faster lookup

# class for elements of the linkedlist
class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None

# counts number of nodes in linked list
def get_count(node):
	if self.head:
		count = 1
		current = self.head
		# iterate through all nodes in list
		while current.next:
			current = current.next
			count += 1
		return count
	# return 0 if list is empty
	return 0

def question5(ll, m):
	# check if node exists
	if ll:
		# count will keep track of number of nodes in linkedlist
		count = 1
		current = ll
		# iterate through linkedlist as long as there is a next node
		while current.next:
			current = current.next
			# increment count for each node
			count += 1

		# use count and m to find index of mth node
		index = count - m

		if index < 0:
			# return None if given mth node does not exist
			return None

		else:
			current = ll
			# iterate through nodes till reaching mth node
			while index > 0:
				current = current.next
				# decrease index by 1 for each node
				index -= 1

			# return mth node
			return current
	# return None if given node does not exist
	return None

# test cases
# empty linkedlist
# linkedlist with elements an index out of range
# linkedlist with elements with an index within range
