from data_structures.symbol_table import SymbolTable
from scanner.main import recognize_tokens

if __name__ == '__main__':
    ids_table = SymbolTable('identifiers')
    nums_table = SymbolTable('numbers')

    f = open('scanner/test1.txt', 'r')
    token_sequence = recognize_tokens(ids_table, nums_table, f)
    f.close()
    del f