import re
# import re as regex #used alias here
# from re import * #dont have to use re.search. directly use search

pattern = '[abc]+'
# compile(pattern, flag = 0)

# for validation
pattern = '[abcd]'
s = 'akashdeep'
match_res = re.match(pattern, s, flags = 0)
# re.match matches only at the beginning of the string.
# If the pattern isn’t found at the start, it returns None.

print(match_res)

pattern = 'akashdeep'
full_match_res = re.fullmatch(pattern, s, flags = 0)
print(full_match_res)
print(full_match_res.group())

# for search and extract
# Scans the entire string and returns the first match anywhere in the string.
# If the pattern occurs later, it still matches.
# Finds the first occurrence of a pattern
print(re.search('easy',  'python is very easy', flags = 0).group())
print(re.search('very',  'python is very very easy', flags = 0).span())

# Finds all occurrences of a pattern
print(re.findall('can', 'can you can a can as a canner', flags = 0))

print(re.split(pattern, s, maxsplit = 0, flags= 0))

# 
# (Lecture 2)->> How to define patterns
# Quantifiers -> Special symbol that are used for defining patterns
# 

