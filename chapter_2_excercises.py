# 2-3 Personal Message
name = "John Doe"
message = f"Hello {name}, would you like to learn some Python today?"
print(message)

# 2-4 Name Cases
name = "ada lovelace"
print(name.upper())
print(name.lower())
print(name.title())

# 2-5 Famous Quote:
quote = "The happiness of your life depends upon the quality of your thoughts"
author = "Marcus Aurelius"
famous_quote = f'{author} once said, "{quote}"'
print(famous_quote)

# 2-6 Famous Quote 2:
quote = "The happiness of your life depends upon the quality of your thoughts"
famous_person = "Marcus Aurelius"
message = f'{famous_person} once said, "{quote}"'
print(message)

# 2-7 Stripping Names
persons_name = " Julius Ceasar  "
print(persons_name)
print(persons_name.lstrip())
print(persons_name.rstrip())
print(persons_name.strip())

# 2-8 File Extensions
filename = 'python_notes.txt'
print(filename.removesuffix('.txt'))