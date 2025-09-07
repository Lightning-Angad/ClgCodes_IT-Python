#word_frequency-dictionaries
x = input("Enter a sentence: ")
words = x.split()
new = {}
for i in words:
    if i in new:
        new[i] += 1
    else:
        new[i] = 1
print("\nWord Frequencies:")
for i, freq in new.items():
    print(f"{i}: {freq}")
