import sys

# Define dictionaries to translate between Braille and English
# `braille_to_english` maps Braille to English, separated into alphabet and number sections
braille_to_english = {
    "Alphabet": {
        # Letters a-z in Braille (uppercase letters are handled separately by a Capital indicator)
        "O.....": "A", "O.O...": "B", "OO....": "C", "OO.O..": "D", "O..O..": "E",
        "OOO...": "F", "OOOO..": "G", "O.OO..": "H", ".OO...": "I", ".OOO..": "J",
        "O...O.": "K", "O.O.O.": "L", "OO..O.": "M", "OO.OO.": "N", "O..OO.": "O",
        "OOO.O.": "P", "OOOOO.": "Q", "O.OOO.": "R", ".OO.O.": "S", ".OOOO.": "T",
        "O...OO": "U", "O.O.OO": "V", ".OOO.O": "W", "OO..OO": "X", "OO.OOO": "Y",
        "O..OOO": "Z",
    },
    
    "Number": {
        # Numbers 0-9 in Braille (same Braille symbols as A-J, but after a number indicator)
        ".O.OOO": "0",  # 0
        "O.....": "1",  # A
        "O.O...": "2",  # B
        "OO....": "3",  # C
        "OO.O..": "4",  # D
        "O..O..": "5",  # E
        "OOO...": "6",  # F
        "OOOO..": "7",  # G
        "O.OO..": "8",  # H
        ".OO...": "9",  # I
    },

    # Special symbols like capital letters, number indicators, spaces, and punctuation
    ".....O": "Capital",  # Indicates the next letter is uppercase
    ".O....": "Number",   # Number indicator before digits
    "......": " ",        # Space
    ".O.OOO": ".",  # Period
    ".O....": ",",  # Comma
    ".OO.OO": "?",  # Question mark
    ".OOO.O": "!",  # Exclamation mark
    "OO.OO.": ":",  # Colon
    "OO.O..": ";",  # Semicolon
    "..OO..": "-",  # Dash
    "..O.OO": "/",  # Forward slash
    "O.OO.O": "(",  # Open parenthesis
    "O.OO.O": ")",  # Close parenthesis
    "O.OOO.": "<",  # Less than
    ".OOO..": ">",  # Greater than
}

# English to Braille mapping - converts each letter, number, or punctuation back into Braille
english_to_braille = {
    # English letters A-Z mapped to their corresponding Braille symbols
    "A": "O.....", "B": "O.O...", "C": "OO....", "D": "OO.O..", "E": "O..O..",
    "F": "OOO...", "G": "OOOO..", "H": "O.OO..", "I": ".OO...", "J": ".OOO..",
    "K": "O...O.", "L": "O.O.O.", "M": "OO..O.", "N": "OO.OO.", "O": "O..OO.",
    "P": "OOO.O.", "Q": "OOOOO.", "R": "O.OOO.", "S": ".OO.O.", "T": ".OOOO.",
    "U": "O...OO", "V": "O.O.OO", "W": ".OOO.O", "X": "OO..OO", "Y": "OO.OOO",
    "Z": "O..OOO",

    # Numbers 0-9 (numbers are treated the same as letters A-J after a number indicator)
    "0": ".O.OOO",  # Same as J for 0
    "1": "O.....",  # Same as A for 1
    "2": "O.O...",  # Same as B for 2
    "3": "OO....",  # Same as C for 3
    "4": "OO.O..",  # Same as D for 4
    "5": "O..O..",  # Same as E for 5
    "6": "OOO...",  # Same as F for 6
    "7": "OOOO..",  # Same as G for 7
    "8": "O.OO..",  # Same as H for 8
    "9": ".OO...",  # Same as I for 9

    # Special symbols like capitalization, number indicator, space, and punctuation
    "Capital": ".....O",  # Indicates next letter is capitalized
    "Number": ".O.OOO",   # Number indicator before digits
    " ": "......",        # Space
    ".": ".O.OOO",  # Period
    ",": ".O....",  # Comma
    "?": ".OO.OO",  # Question mark
    "!": ".OOO.O",  # Exclamation mark
    ":": "OO.OO.",  # Colon
    ";": "OO.O..",  # Semicolon
    "-": "..OO..",  # Dash
    "/": "..O.OO",  # Forward slash
    "(": "O.OO.O",  # Open parenthesis
    ")": "O.OO.O",  # Close parenthesis
    "<": "O.OOO.",  # Less than
    ">": ".OOO..",  # Greater than
}

# Function to translate English to Braille
def translate_to_braille(english_input):
    braille_output = ""
    is_number = False  # To keep track if we're translating a number sequence

    # Loop through each character in the input string
    for char in english_input:
        if char.isdigit():
            if not is_number:
                # If a number sequence starts, we add the number indicator
                braille_output += english_to_braille["Number"]
                is_number = True
            # Convert digits to Braille numbers (mapped same as A-J)
            braille_output += english_to_braille[char]
        elif char.isalpha():
            if is_number:
                # If switching back to letters, reset the number flag
                is_number = False
            if char.isupper():
                # Add the capital letter indicator if the character is uppercase
                braille_output += english_to_braille["Capital"]
                char = char.lower()  # Convert the character to lowercase for Braille mapping
            braille_output += english_to_braille[char.upper()]
        elif char in english_to_braille:  # Handle punctuation and spaces
            is_number = False  # Reset number flag when punctuation or space is encountered
            braille_output += english_to_braille[char]
        else:
            # Handle any unrecognized characters (optional)
            braille_output += "[?]"

    return braille_output

# Function to translate Braille to English
def translate_to_english(braille_input):
    english_output = ""
    i = 0
    is_number = False  # Track if we're in number mode
    is_capital = False  # Track if the next letter should be capitalized

    # Loop through the Braille input in chunks of 6 (since each Braille symbol is 6 characters long)
    for i in range(i, len(braille_input), i+6):
        braille_char = braille_input[i:i+6]
        
        # Check for number and capital indicators
        if braille_char == english_to_braille["Number"]:
            is_number = True
            continue
        elif braille_char == english_to_braille["Capital"]:
            is_capital = True  # The next letter should be capitalized
            continue
        elif braille_char == english_to_braille[" "]:
            english_output += " "
            is_number = False  # Reset number mode after encountering a space
            continue
        else:
            if is_number:
                # Translate Braille numbers (A-J) to digits
                english_output += braille_to_english["Number"][braille_char]
            else:
                # Translate Braille letters and handle capitalization if needed
                if is_capital:
                    english_output += braille_to_english["Alphabet"][braille_char].upper()
                    is_capital = False  # Reset capital flag after using it
                else:
                    english_output += braille_to_english["Alphabet"][braille_char].lower()

    return english_output

# Main logic to detect if the input is Braille or English and translate accordingly
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: No input string provided.")
        sys.exit(1)

    input_string = sys.argv[1]

    # Determine if the input is Braille (contains only 'O' and '.' characters) or English
    if set(input_string).issubset({"O", "."}):
        # Input is Braille, so translate it to English
        result = translate_to_english(input_string)
    else:
        # Input is English, so translate it to Braille
        result = translate_to_braille(input_string)

    # Output the result
    print(result)
