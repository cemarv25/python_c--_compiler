transition_table = [
    [ 1,  2, 14, 15, 16,  7,  6,  4,  5,  3, 12, 13, 17, 18, 19, 20, 21, 22,  0, 37],
    [ 1, 32, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 32],
    [33,  2, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 33],
    [34, 34, 34, 34, 34, 34, 23, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34],
    [24, 24, 24, 24, 24, 24, 25, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 35],
    [26, 26, 26, 26, 26, 26, 27, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 35],
    [28, 28, 28, 28, 28, 28, 29, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 35],
    [30, 30, 30, 30,  8, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 37],
    [ 8,  8,  8,  8,  9,  8,  8,  8,  8,  8,  8,  8,  8,  8,  8,  8,  8,  8,  8,  8],
    [ 8,  8,  8,  8,  8, 31,  8,  8,  8,  8,  8,  8,  8,  8,  8,  8,  8,  8,  8,  8]
]

advance = [
    [ True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True ],
    [ True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True ],
    [ True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True ],
    [ True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True ],
    [ True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True ],
    [ True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True ],
    [ True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True ],
    [ True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True ],
    [ True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True ],
    [ True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True ]
]

acceptor = [
    # From state 0 - 9: not acceptor
    False, False, False, False, False, False, False, False, False, False,

    # From state 10 - 31: correct acceptor
    True, True, True, True, True, True, True, True, True, True,
    True, True, True, True, True, True, True, True, True, True,
    True, True,
    
    # From state 32 - 37: error acceptor
    True, True, True, True, True, True
]

error = [
    # From state 0 - 9: not acceptor
    False, False, False, False, False, False, False, False, False, False,

    # From state 10 - 31: correct acceptor
    False, False, False, False, False, False, False, False, False, False,
    False, False, False, False, False, False, False, False, False, False,
    False, False,

    # From state 32 - 37: error
    True, True, True, True, True, True
]

def gen_char_dict():
    """Create a dictionary with all the input characters.
    
    This works with dictionary comprehension, which is a short way of 
    creating a dictionary using a loop.
    """
    
    # Letter dictionaries
    lowercase_dict = {chr(ord('a') + i) : 0 for i in range(26)}
    uppercase_dict = {chr(ord('A') + i) : 0 for i in range(26)}

    # Digit dictiionary
    digit_dict = {str(i) : 1 for i in range(10)}

    # Special symbols dictionary
    special_symbols = {
        '+': 2,
        '-': 3,
        '*': 4,
        '/': 5,
        '=': 6,
        '<': 7,
        '>': 8,
        '!': 9,
        ';': 10,
        ',': 11,
        '(': 12,
        ')': 13,
        '[': 14,
        ']': 15,
        '{': 16,
        '}': 17,
    }

    # White space dictionary
    white_space = {
        ' ': 18,
        '\n': 18,
    }

    # Join both dictionaries with the union operator (|)
    return lowercase_dict | uppercase_dict | digit_dict | special_symbols | white_space