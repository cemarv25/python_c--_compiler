from data_structures.symbol_table import SymbolTable
from parser.productions.program import program

current_token = None
token_sequence = None
ids_table = None
nums_table = None

class SyntaxException(Exception):
    def __init__(self, msg: str):
        self.message = msg


def match(terminal: int):
    global current_token, token_sequence
    if current_token == terminal:
        temp_token = token_sequence.pop()
        if type(temp_token) == tuple:
            current_token = temp_token[0]
            return current_token
        else:
            current_token = temp_token
            return current_token
    else:
        raise SyntaxException('SyntaxException: Unexpected token.')

def parse(token_seq: list, ids_t: SymbolTable, nums_t: SymbolTable):
    global current_token, token_sequence, ids_table, nums_table

    ids_table = ids_t
    nums_table = nums_t

    token_seq.append('$')
    token_seq.reverse()
    token_sequence = token_seq
    temp_token = token_sequence.pop()
    if type(temp_token) == tuple:
        current_token = temp_token[0]
    else:
        current_token = temp_token

    try:
        program()
    except SyntaxException as err:
        print(err.message)
    except Exception:
        print('syntax analysis error')

    if current_token == '$':
        print('syntax analysis ok')