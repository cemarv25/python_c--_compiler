from io import TextIOWrapper
from typing import Tuple
from data_structures.symbol_table import SymbolTable
from .utils import transition_table, advance, acceptor, error, error_messages, reserved_words, gen_char_dict

def recognize_tokens(file: TextIOWrapper) -> Tuple[list, SymbolTable, SymbolTable] | str:
    """Recognize the tokens from the provided file.

    Args:
        file (TextIOWrapper): The file to read from

    Returns:
        Tuple[list, SymbolTable, SymbolTable] | str: A tuple containing the token sequence as a list, the identifiers SymbolTable and the numbers SymbolTable
    """

    ids_table = SymbolTable('identifiers')
    nums_table = SymbolTable('numbers')
    curr_state = 0
    curr_char = file.read(1)
    char_to_idx = gen_char_dict()
    token = ''
    curr_line = 1
    comment_line = 0

    token_seq = []

    # when the current char == '', means we reached the EOF
    while curr_char != '':
        while not acceptor[curr_state] and not error[curr_state]:
            if curr_char == '':
                # if token is empty, get out of loop
                if len(token) == 0:
                    break

                # if state is comment (8), return non-closing comment error
                if curr_state == 8:
                    return f"{error_messages[5]}\n\tAt {file.name}:{comment_line}"

                # if token is not empty, act as if there was a delimiter
                if len(token) > 0:
                    char_idx = get_char_idx(' ', char_to_idx)
            else:
                char_idx = get_char_idx(curr_char, char_to_idx)

            comment_line = update_comment_line(comment_line, curr_line, curr_char, curr_state)
            new_state = transition_table[curr_state][char_idx]
            
            if advance[curr_state][char_idx]:
                # append curr_char to the token if we're not in a comment
                if curr_state != 8 and not curr_char.isspace():
                    token += curr_char
                
                # add one to the line count if curr_char is a newline
                if curr_char == '\n':
                    curr_line += 1

                curr_char = file.read(1)
            curr_state = new_state
        
        if acceptor[curr_state]:
            record_token(curr_state, token, token_seq, ids_table, nums_table)
            token = ''
            curr_state = 0
        elif error[curr_state]:
            # send error message
            return f"{error_messages[curr_state - 32]}\n\tAt {file.name}:{curr_line}"

    return token_seq, ids_table, nums_table

def get_char_idx(char: str, idx_dict: dict) -> int:
    """Get the corresponding index for a specific character to access the transition table.

    Args:
        char (str): The char to get the index for
        idx_dict (dict): The dictionary where every index for every char is stored

    Returns:
        int: The index that corresponds to the character
    """

    # if curr_char is not in the array, means it is a rare symbol
    if char in idx_dict:
        return idx_dict[char]
    
    return 19

def update_comment_line(comment_line: int, char_line: int, char: str, state: int) -> int:
    """Updates the line where a comment started. If there isn't a comment, it is left unmodified.

    The logic is, if the current character is '*' and the current state is 7, means that a comment is starting.

    Args:
        comment_line (int): The variable where the comment line is stored
        char_line (int): The current line where the character is
        char (str): The current char
        state (int): The current state

    Returns:
        int: The current line
    """

    # if curr_char is '*' and curr_state is 7, means a comment is starting so save the line
    if char == '*' and state == 7:
        return char_line
    
    return comment_line


def record_token(state: int, token: str, token_seq: list, ids_table: SymbolTable, nums_table: SymbolTable) -> None:
    """Record a token into the sequence of tokens and its SymbolTable if needed.

    Args:
        state (int): The current state
        token (str): The token to record
        token_seq (list): The token sequence
        ids_table (SymbolTable): The identifiers SymbolTable
        nums_table (SymbolTable): The numbers SymbolTable
    """

    # pseudo-tokens
    # In this case, check if the token == a reserved word. If true, save as such, else save as identifier
    if state == 10:
        # reserved words
        if token.casefold() in reserved_words:
            token_seq.append(reserved_words.index(token.casefold()) + 1)

        # identifiers
        # In this case, check if the identifier is already in the symbol table
        else:
            entry = ids_table.get_entry_with_token(token)

            if not entry:
                token_id = ids_table.insert_entry(token)
                token_seq.append((30, token_id))
            else:
                token_seq.append((30, entry[0]))
    
    # numbers
    # Check if the number is already in the symbol table
    elif state == 11:
        entry = nums_table.get_entry_with_token(token)

        if not entry:
            token_id = nums_table.insert_entry(token)
            token_seq.append((31, token_id))
        else:
            token_seq.append((31, entry[0]))

    # special symbols
    elif state in range(12, 31):
        token_seq.append(state - 3)