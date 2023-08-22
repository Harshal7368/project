# Write Python code to create a function called most_frequent that takes a string and prints the letters in decreasing order of frequency. Use dictionaries.
def most_frequent(string):
    # Create an empty dictionary
    frequencies = {}

    # Count the frequency of each letter in the string
    for letter in string:
        if letter in frequencies:
            frequencies[letter] += 1
        else:
            frequencies[letter] = 1

    # Sort the letters in decreasing order of frequency
    sorted_letters = sorted(frequencies, key=frequencies.get, reverse=True)

    # Print the letters in decreasing order of frequency
    for letter in sorted_letters:
        print(letter, ":", frequencies[letter])

# Example usage
most_frequent("Mississippi")

# output : 
# i : 4
# s : 4
# p : 2
# M : 1