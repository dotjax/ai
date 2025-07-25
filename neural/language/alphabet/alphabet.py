"""ASCII letter dictionary with uppercase and lowercase values, positions, and vowel/consonant classification."""

ascii_letters = {
    # Uppercase letters (A-Z: 65-90)
    'A': {
        'ascii_value': 65, 
        'position': 1, 
        'type': 'vowel', 
        'type_value': 1
    },
    'B': {
        'ascii_value': 66, 
        'position': 2, 
        'type': 'consonant', 
        'type_value': 0
    },
    'C': {
        'ascii_value': 67, 
        'position': 3, 
        'type': 'consonant', 
        'type_value': 0
    },
    'D': {
        'ascii_value': 68, 
        'position': 4, 
        'type': 'consonant', 
        'type_value': 0
    },
    'E': {
        'ascii_value': 69, 
        'position': 5, 
        'type': 'vowel', 
        'type_value': 1
    },
    'F': {
        'ascii_value': 70, 
        'position': 6, 
        'type': 'consonant', 
        'type_value': 0
    },
    'G': {
        'ascii_value': 71, 
        'position': 7, 
        'type': 'consonant', 
        'type_value': 0
    },
    'H': {
        'ascii_value': 72, 
        'position': 8, 
        'type': 'consonant', 
        'type_value': 0
    },
    'I': {
        'ascii_value': 73, 
        'position': 9, 
        'type': 'vowel', 
        'type_value': 1
    },
    'J': {
        'ascii_value': 74, 
        'position': 10, 
        'type': 'consonant', 
        'type_value': 0
    },
    'K': {
        'ascii_value': 75, 
        'position': 11, 
        'type': 'consonant', 
        'type_value': 0
    },
    'L': {
        'ascii_value': 76, 
        'position': 12, 
        'type': 'consonant', 
        'type_value': 0
    },
    'M': {
        'ascii_value': 77, 
        'position': 13, 
        'type': 'consonant', 
        'type_value': 0
    },
    'N': {
        'ascii_value': 78, 
        'position': 14, 
        'type': 'consonant', 
        'type_value': 0
    },
    'O': {
        'ascii_value': 79, 
        'position': 15, 
        'type': 'vowel', 
        'type_value': 1
    },
    'P': {
        'ascii_value': 80, 
        'position': 16, 
        'type': 'consonant', 
        'type_value': 0
    },
    'Q': {
        'ascii_value': 81, 
        'position': 17, 
        'type': 'consonant', 
        'type_value': 0
    },
    'R': {
        'ascii_value': 82, 
        'position': 18, 
        'type': 'consonant', 
        'type_value': 0
    },
    'S': {
        'ascii_value': 83, 
        'position': 19, 
        'type': 'consonant', 
        'type_value': 0
    },
    'T': {
        'ascii_value': 84, 
        'position': 20, 
        'type': 'consonant', 
        'type_value': 0
    },
    'U': {
        'ascii_value': 85, 
        'position': 21, 
        'type': 'vowel', 
        'type_value': 1
    },
    'V': {
        'ascii_value': 86, 
        'position': 22, 
        'type': 'consonant', 
        'type_value': 0
    },
    'W': {
        'ascii_value': 87, 
        'position': 23, 
        'type': 'consonant', 
        'type_value': 0
    },
    'X': {
        'ascii_value': 88, 
        'position': 24, 
        'type': 'consonant', 
        'type_value': 0
    },
    'Y': {
        'ascii_value': 89, 
        'position': 25, 
        'type': 'consonant', 
        'type_value': 0
    },
    'Z': {
        'ascii_value': 90, 
        'position': 26, 
        'type': 'consonant', 
        'type_value': 0
    },
    
    # Lowercase letters (a-z: 97-122)
    'a': {
        'ascii_value': 97, 
        'position': 1, 
        'type': 'vowel', 
        'type_value': 1
    },
    'b': {
        'ascii_value': 98, 
        'position': 2, 
        'type': 'consonant', 
        'type_value': 0
    },
    'c': {
        'ascii_value': 99, 
        'position': 3, 
        'type': 'consonant', 
        'type_value': 0
    },
    'd': {
        'ascii_value': 100, 
        'position': 4, 
        'type': 'consonant', 
        'type_value': 0
    },
    'e': {
        'ascii_value': 101, 
        'position': 5, 
        'type': 'vowel', 
        'type_value': 1
    },
    'f': {
        'ascii_value': 102, 
        'position': 6, 
        'type': 'consonant', 
        'type_value': 0
    },
    'g': {
        'ascii_value': 103, 
        'position': 7, 
        'type': 'consonant', 
        'type_value': 0
    },
    'h': {
        'ascii_value': 104, 
        'position': 8, 
        'type': 'consonant', 
        'type_value': 0
    },
    'i': {
        'ascii_value': 105, 
        'position': 9, 
        'type': 'vowel', 
        'type_value': 1
    },
    'j': {
        'ascii_value': 106, 
        'position': 10, 
        'type': 'consonant', 
        'type_value': 0
    },
    'k': {
        'ascii_value': 107, 
        'position': 11, 
        'type': 'consonant', 
        'type_value': 0
    },
    'l': {
        'ascii_value': 108, 
        'position': 12, 
        'type': 'consonant', 
        'type_value': 0
    },
    'm': {
        'ascii_value': 109, 
        'position': 13, 
        'type': 'consonant', 
        'type_value': 0
    },
    'n': {
        'ascii_value': 110, 
        'position': 14, 
        'type': 'consonant', 
        'type_value': 0
    },
    'o': {
        'ascii_value': 111, 
        'position': 15, 
        'type': 'vowel', 
        'type_value': 1
    },
    'p': {
        'ascii_value': 112, 
        'position': 16, 
        'type': 'consonant', 
        'type_value': 0
    },
    'q': {
        'ascii_value': 113, 
        'position': 17, 
        'type': 'consonant', 
        'type_value': 0
    },
    'r': {
        'ascii_value': 114, 
        'position': 18, 
        'type': 'consonant', 
        'type_value': 0
    },
    's': {
        'ascii_value': 115, 
        'position': 19, 
        'type': 'consonant', 
        'type_value': 0
    },
    't': {
        'ascii_value': 116, 
        'position': 20, 
        'type': 'consonant', 
        'type_value': 0
    },
    'u': {
        'ascii_value': 117, 
        'position': 21, 
        'type': 'vowel', 
        'type_value': 1
    },
    'v': {
        'ascii_value': 118, 
        'position': 22, 
        'type': 'consonant', 
        'type_value': 0
    },
    'w': {
        'ascii_value': 119, 
        'position': 23, 
        'type': 'consonant', 
        'type_value': 0
    },
    'x': {
        'ascii_value': 120, 
        'position': 24, 
        'type': 'consonant', 
        'type_value': 0
    },
    'y': {
        'ascii_value': 121, 
        'position': 25, 
        'type': 'consonant', 
        'type_value': 0
    },
    'z': {
        'ascii_value': 122, 
        'position': 26, 
        'type': 'consonant', 
        'type_value': 0
    }
}