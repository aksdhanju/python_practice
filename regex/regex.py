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
