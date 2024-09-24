sentence = input("Enter a sentence: ")
words = sentence.lower().split()
print(words)
palindrome_count = 0
for word in words:
    if word == word[::-1]:
        palindrome_count += 1
print(palindrome_count)