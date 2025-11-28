import re

text = "The quick brown fox"
pattern = r"brown"                     

search = re.search(pattern, text)
if search:
    print("Pattern found:", search.group())     //search.group() returns the exact substring of text that matched pattern.
else:                                      //If you call .group() with no arguments (or with argument 0), you get the entire substring of the target string that matched the pattern.
    print("Pattern not found")
---------------------------------------------------------------------
With a raw string (prefix r or R), the literal tells Python: “Don’t interpret backslashes as the start of escape sequences — treat them more literally.” 

# Example 1: newline escape
a = "A\nB"
b = r"A\nB"
print(a)   # A
           # B
print(b)   # A\nB


✅ What happens with the normal string (a)

In a normal string literal, \n is interpreted as an escape sequence for newline. 
FreeCodeCamp
+1

So "A\nB" means: character "A", then newline, then "B".

When you print(a), Python outputs:

A
B


Because the \n causes a line break. That’s why your comment shows:

# A
# B

✅ What happens with the raw string (b)

In a raw string literal (prefixed with r or R), backslashes are not treated specially: they don’t start escape sequences. Instead they are treated just like normal characters. 
Python documentation
+1

So r"A\nB" means the characters: "A", then a backslash \, then "n", then "B". There is no newline character — just a literal \ and n.

When you print(b), Python outputs exactly what’s in the string:
