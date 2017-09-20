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
