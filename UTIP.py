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
# I tried a number of approaches here to avoid nested loops
# but I was unable to find one that works for all inputs and takes less time
# I reversed the string because a palindrome will appear the same in both priginal and reversed string
# this makes it easier to identify palindromes in given string

# efficiency will be O(n*n*n)

def question2(a):
	# reverse string a
	reversed_a = a[::-1]
	longest_palindrome = ''

	# iterate through string a
	for i in range(0, len(a)):
		for j in range(0, len(a)):
			temp = 0 
			palindrome = ''
			# as long as such of loop index and temp are less than string length
			# and characters at indexes are same
			# concatenate character at index to palindrome
			# and increment temp
			while(i+temp < len(a) and j+temp < len(reversed_a) and a[i+temp] == reversed_a[j+temp]):
				palindrome += a[i+temp]
				temp += 1
			# compare length of longest_palindrome and palindrome
			# replace longest_palindrome with palindrome if palindrome's length is greater
			# this helps find longest palindrome from all palindromes in string
			if(len(longest_palindrome) < len(palindrome)):
				longest_palindrome = palindrome
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
