import re

print(bool(re.match(r"^\w+$", "Hello_123")))   # True
print(bool(re.match(r"^\w+$", "Hello-123")))   # False  (dash not allowed)


print(bool(re.match(r"^He", "Hello-123"))) 


# extract html tag information
html = "<html><body><h1>hello world</h1></body></html>"

# Regex with capture group
pattern = r"<h1>([^<]+)</h1>"

match = re.search(pattern, html)

if match:
    print("Full match:", match.group(0))   # <h1>hello world</h1>
    print("Captured text:", match.group(1)) # hello world
else:
    print("No match found")



# Example 1: Simple capture

text = "My name is Akashdeep Singh"
pattern = r"My name is (\w+) (\w+)"
m = re.search(pattern, text)

print(m.group(0))   # "My name is Akashdeep Singh" (whole match)
print(m.group(1))   # "Akashdeep"
print(m.group(2))   # "Singh"
print(m.groups())   # ('Akashdeep', 'Singh')


# Example 2: Named groups
# You can name groups with (?P<name>...):
pattern = r"My name is (?P<first>\w+) (?P<last>\w+)"
m = re.search(pattern, text)

print(m.group("first"))  # "Akashdeep"
print(m.group("last"))   # "Singh"


# Example 3: Non-capturing groups (?:...)
# Sometimes you want to group things for logic 
# (like repetition, alternation) but don’t care about extracting them.
# That’s where non-capturing groups (?:...) come in.

text = "cat bat rat"
pattern = r"(?:cat|bat) rat"   # non-capturing
m = re.search(pattern, text)

print(m.group(0))   # "bat rat" (whole match)
print(m.groups())   # () → empty, nothing captured

# If we used (cat|bat) instead:
pattern = r"(cat|bat) rat"
m = re.search(pattern, text)

print(m.group(0))   # "bat rat"
print(m.group(1))   # "bat"
print(m.groups())   # ('bat',)
