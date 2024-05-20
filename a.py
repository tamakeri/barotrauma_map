import re

# Example text
text = "Email us at contact@example.com or support@example.com"

# Example regex pattern to match email addresses
pattern = re.compile(r'(\w+@\w+\.\w+)')

# Using findall to get a list of all matches
matches = pattern.findall(text)

print("Using findall:")
for match in matches:
    print(match)

# Using finditer to get an iterator of match objects
matches_iter = pattern.finditer(text)

print("\nUsing finditer:")
for match in matches_iter:
    print(match.group(1))
