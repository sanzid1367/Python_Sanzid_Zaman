#Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up! 

words = {
    "madad": "help",
    "billi": "cat",
    "kutta": "dog",
    "pani": "water"
}

word = input("Enter the word you want to translate : ")

print(words[word])