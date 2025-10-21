import re

text = "The quick brown fox"
pattern = r"brown"                     

search = re.search(pattern, text)
if search:
    print("Pattern found:", search.group())     //search.group() returns the exact substring of text that matched pattern.
else:
    print("Pattern not found")
---------------------------------------------------------------------
With a raw string (prefix r or R), the literal tells Python: “Don’t interpret backslashes as the start of escape sequences — treat them more literally.” 

# Example 1: newline escape
a = "A\nB"
b = r"A\nB"
print(a)   # A
           # B
print(b)   # A\nB
