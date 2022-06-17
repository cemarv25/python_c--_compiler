from data_structures.symbol_table import SymbolTable
from parser.productions.program import program

token = None
current_token_id = None
token_sequence = None
token_line = None
token_content = None
current_entry = None
ids_table = None
nums_table = None

id_to_token = {
    0: 'EOF',
    10: 'identifier', 11: 'number literal',
    12: ';', 13: ',', 14: '+', 15: '-', 16: '*', 17: '(', 18: ')', 19: '[', 20: ']', 21: '{',
    22: '}', 23: '!=', 24: '<', 25: '<=', 26: '>', 27: '>=', 28: '=', 29: '==', 30: '/',

    31: 'else', 32: 'if', 33: 'int', 34: 'return', 35: 'void', 36: 'while', 37: 'input', 38: 'output'
}

class SyntaxException(Exception):
    """The Exception that will be raised in this stage of the compiler.
    """

    def __init__(self, msg: str):
        """SyntaxException constructor.

        Args:
            msg (str): The error message.
        """

        self.message = msg

def update_current_entry(property: str, value: str | int) -> None:
    """Update the current entry's info.

    Args:
        property (str): The property to be updated.
        value (str | int): The value to be updated with.
    """

    global current_entry

    current_entry.info[property] = value

def verify_main_fun():
    """Function used to verify that the program being analized contains the main function declaration.

    Raises:
        SyntaxException in case that the program does not contain a main function declaration.
    """

    global ids_table

    # Get the last entry with a global scope from the ids table
    last_dec = None
    for entry_id, entry in ids_table.entries:
        # If the entry is not global, continue to the next one
        if entry.info['global'] == False:
            continue

        # If the last declaration is not defined, get the current one and continue
        if not last_dec:
            last_dec = entry
            continue

        # If the current entry's line is greater than the one in last_dec,
        # assign last_dec equal to the current entry
        if entry.info['global_line'] > last_dec.info['global_line']:
            last_dec = entry

    if not last_dec or last_dec.content.casefold() != 'main' or last_dec.info['return_type'] != 'void':
        raise SyntaxException('SyntaxException: NoMain. Expected the last declaration to be a function declaration with the form \'void main(void)\' but it was not.')
    
    # entry = ids_table.get_entry_with_token('main')

    # # Check if there is a upcase 'MAIN' function
    # if not entry:
    #     entry = ids_table.get_entry_with_token('MAIN')

    # if not entry or entry[1].info['global'] != True or entry[1].info['return_type'] != 'void':
    #     raise SyntaxException('SyntaxException: NoMain. Expected a function declaration with the form \'void main(void)\' but it was not found.')

def match(terminal: int, updates: dict = None) -> int:
    """Match function to compare current token to the expected terminal symbol.

    Args:
        terminal (int): The expected terminal symbol
        updates (dict, optional): The Entry's properties and values to update

    Raises:
        SyntaxException when the current token and the expected terminal are not the same.

    Returns:
        int: The resulting current token
    """

    global current_token_id, token, token_sequence, token_line, token_content, current_entry
    
    if current_token_id == terminal:
        if current_token_id != 0:
            token_line = token[-1]

        if updates:
            for key, value in updates.items():
                update_current_entry(key, value)

        token = token_sequence.pop()
        current_token_id = token[0]

        # if the token is an id or a num, get its line from the entry
        if current_token_id == 10:
            current_entry = ids_table.get_entry_with_id(token[1])
            token_content = current_entry.content
        elif current_token_id == 11:
            current_entry = nums_table.get_entry_with_id(token[1])
            token_content = current_entry.content
        else:
            token_content = id_to_token[token[0]]
            
            

        return current_token_id
    else:
        raise SyntaxException(f"SyntaxException: Expected {id_to_token[terminal]} but got '{token_content}'\n\tAt line {token_line}")

def parse(token_seq: list, ids_t: SymbolTable, nums_t: SymbolTable):
    """The starting point of the parser

    Args:
        token_seq (list): A list with the token sequence generated by the scanner
        ids_t (SymbolTable): The symbol table for the ids
        nums_t (SymbolTable): The symbol table for the numbers
    """

    global current_token_id, token, token_sequence, token_line, token_content, ids_table, nums_table

    ids_table = ids_t
    nums_table = nums_t

    token_seq.append((0, -1))
    token_seq.reverse()
    token_sequence = token_seq
    token = token_sequence.pop()
    current_token_id = token[0]

    # if the token is an id or a num, get its line from the entry
    if current_token_id == 10:
        entry = ids_table.get_entry_with_id(token[1])
        token_content = entry.content
    elif current_token_id == 11:
        entry = nums_table.get_entry_with_id(token[1])
        token_content = entry.content
    else:
        token_content = id_to_token[token[0]]

    try:
        program()
        verify_main_fun()

        if current_token_id == 0:
            print('Syntax analysis ok')
    except SyntaxException as err:
        print(err.message)
    except Exception as err:
        print('syntax analysis error')
        print(err)
