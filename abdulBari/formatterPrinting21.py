# unicode characters
s = '\u03b1'
print(s)

t = '\u03b1\u03b2\u03b3'
print(t)

c = '\u0041'
print(c)

h = '\u0915\u0916\u0917'
print(h)

s = '\u0041'
print(s)

s = '\x41'
print(s)


# escape sequences

# \n brings cursor to beginning of next line
print('Hello\nWorld')
# print function of python after printing something will move cursor to next line

# \r brings the cursor to beginning of same/current line
print('Valid\rSo') #Solid

# \f line feed. cursor moves to next line but in same column
print('Hello\fWorld')

# \t tab. moves cursor by 4 spaces to the right
print('Hello\tWorld')

# \v vertical tab. Moves vertically to next line. Usually its 1 line. Similar to line feed
print('Hello\vWorld')

# \b backspace. moves cursor 1 position to the left
print('Hello\bWorld')

# \a alert. you hear a beap sound
print('Hello\aWorld')

# \ ignore new line
print('Line1\
      Line2')

# \\ backslash
print('C:\\')

# \' quotes
print('ajay\'s')

# \" double quotes
print('ajay\"s')
print("ajay\"s")

# octal

# hexadecimal
