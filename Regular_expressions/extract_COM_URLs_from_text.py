import re

with open('urls.txt', 'r') as file:
    content = file.read()

pattern = re.compile("https?://(?:www.)?[^ \n]+\.com")
matches = pattern.findall(content)
print(matches)