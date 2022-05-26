from data_structures.symbol_table import SymbolTable
from parser import arithmetic_exp

current_token = None
token_sequence = None

def main(token_seq: list, ids_table: SymbolTable, nums_table: SymbolTable):
    global current_token, token_sequence
    token_seq.append('$')
    token_seq.reverse()
    token_sequence = token_seq
    temp_token = token_sequence.pop()
    if type(temp_token) == tuple:
        current_token = temp_token[0]
    else:
        current_token = temp_token

    current_token = arithmetic_exp.start(current_token, token_seq, ids_table, nums_table)
    if current_token == '$':
        print('syntax analysis ok')
    else:
        print('syntax analysis error')