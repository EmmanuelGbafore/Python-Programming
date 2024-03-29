import json
import difflib

# Load the json data into a python dictionary
def load_dictionary(fileName):
    with open(fileName, 'r') as file:
        data = json.load(file)
    return data
 
# Define functions to search for words definitions
def search_definition(dictionary, word):
    word = word.lower()  # Convert word to lowercase
    if word in dictionary:
        return dictionary[word]
    else:
        # Suggest similar word if the word is not found
        similar_words = difflib.get_close_matches(word, dictionary.keys(), n=3)
        if similar_words:
            suggestion = ", ".join(similar_words)
            return f"Word not found. Did you mean: {suggestion}?"
        else:
            return "Word not found."

# Main function
def main():
    # Load dictionary data
    dictionary = load_dictionary('Python Programming Projects/data.json')


    # User input
    word = input("Enter a word: ")

    # Search for definition
    definition = search_definition(dictionary, word)

    # Display definition
    print(definition)

if __name__ == "__main__":
    main()
