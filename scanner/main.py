from io import TextIOWrapper
from data_structures.symbol_table import SymbolTable
from .utils import transition_table, advance, acceptor, error, error_messages, reserved_words, gen_char_dict

def recognize_tokens(ids_table: SymbolTable, nums_table: SymbolTable, file: TextIOWrapper) -> list | str:
    """Recognize the tokens for the input file.

    Args:
        ids_table (SymbolTable): Symbol table to store identifiers in.
        nums_table (SymbolTable): Symbol table to store numbers in.
        file (TextIOWrapper): The file to read from.

    Returns:
        list | str: The sequence of tokens in a list if no error found. An error message instead.
    """

    curr_state = 0
    curr_char = file.read(1)
    char_to_idx = gen_char_dict()
    token = ''
    char_line = 1
    comment_line = 0

    token_seq = []

    # when the current char == '', means we reached the EOF
    while curr_char != '':
        while not acceptor[curr_state] and not error[curr_state] and curr_char != '':
            char_idx = get_char_idx(curr_char, char_to_idx)

            comment_line = update_comment_line(comment_line, char_line, curr_char, curr_state)
            new_state = transition_table[curr_state][char_idx]
            
            if advance[curr_state][char_idx]:
                # append curr_char to the token if we're not in a comment
                if curr_state != 8 and not curr_char.isspace():
                    token += curr_char
                
                # add one to the line count if curr_char is a newline
                if curr_char == '\n':
                    char_line += 1

                curr_char = file.read(1)
            curr_state = new_state
        
        if acceptor[curr_state]:
            record_token(curr_state, token, token_seq, ids_table, nums_table)
            token = ''
            curr_state = 0
        elif error[curr_state]:
            # send error message
            return f"{error_messages[curr_state - 32]}\n\tAt {file.name}:{char_line}"

    # check if there is a non-closing comment
    if curr_state == 8 or curr_state == 9:
        return f"{error_messages[5]}\n\tAt {file.name}:{comment_line}"

    return token_seq

def get_char_idx(char: str, idx_dict: dict) -> int:
    # if curr_char is not in the array, means it is a rare symbol
    if char in idx_dict:
        return idx_dict[char]
    
    return 19

def update_comment_line(comment_line: int, char_line: int, char: str, state: int) -> int:
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
                token_seq.append((20, token_id))
            else:
                token_seq.append((20, entry[0]))
    
    # numbers
    elif state == 11:
        token_id = nums_table.insert_entry(token)
        token_seq.append((21, token_id))

    # special symbols
    elif state in range(12, 31):
        token_seq.append(state - 3)