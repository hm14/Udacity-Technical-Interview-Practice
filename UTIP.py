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