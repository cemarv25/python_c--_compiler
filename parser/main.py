from data_structures.symbol_table import SymbolTable
from parser.productions import arithmetic_exp

current_token = None
token_sequence = None

def match(terminal: int):
    global current_token, token_sequence
    if current_token == terminal:
        temp_token = token_sequence.pop()
        if type(temp_token) == tuple:
            current_token = temp_token[0]
        else:
            current_token = temp_token
    else:
        raise Exception('Error')

def parse(token_seq: list, ids_table: SymbolTable, nums_table: SymbolTable):
    global current_token, token_sequence
    token_seq.append('$')
    token_seq.reverse()
    token_sequence = token_seq
    temp_token = token_sequence.pop()
    if type(temp_token) == tuple:
        current_token = temp_token[0]
    else:
        current_token = temp_token

    current_token = program()
    if current_token == '$':
        print('syntax analysis ok')
    else:
        print('syntax analysis error')

def program():
    global current_token

    if current_token == 33: # int
        match(33)
        match(10)
        declaration_prime()
        program()
    elif current_token == 35: # void
        match(35)
        match(10)
        match(17)
        params()
        match(18)
        compound_stmt()
        program()
    elif current_token == '$':
        return
    else:
        raise Exception('Error')

def declaration_prime():
    global current_token

    if current_token == 12: # ;
        match(12)
    elif current_token == 19: # [
        match(19)
        match(11)
        match(20)
        match(12)
    elif current_token == 17: # (
        match(17)
        params()
        match(18)
        compound_stmt()
    else:
        raise Exception('Error')

def var_declaration_prime():
    global current_token

    if current_token == 12: # ;
        match(12)
    elif current_token == 19: # [
        match(19)
        match(11)
        match(20)
        match(12)
    else:
        raise Exception('Error')

def params():
    global current_token

    if current_token == 33: # int
        match(33)
        match(10)
        param_prime()
        param_list_prime()
    elif current_token == 35: # void
        match(35)
    else:
        raise Exception('Error')

def param_list_prime():
    global current_token

    if current_token == 13: # ,
        match(13)
        match(33)
        match(10)
        param_prime()
        param_list_prime()
    elif current_token == 18: # )
        return
    else:
        raise Exception('Error')

def param_prime():
    global current_token

    if current_token == 19: # [
        match(19)
        match(20)
    elif current_token == 13 or current_token == 18:
        return
    else:
        raise Exception('Error')

def compound_stmt():
    global current_token

    if current_token == 21: # {
        match(21)
        local_declarations()
        statement_list()
        match(22)
    else: raise Exception('Error')

def local_declarations():
    global current_token

    if current_token == 33: # int
        match(33)
        match(10) 
        var_declaration_prime()
        local_declarations()
    elif current_token == 10 or current_token == 21 or current_token == 32 or current_token == 36 or current_token == 34 or current_token == 37 or current_token == 38 or current_token == 22:
        return
    else:
        raise Exception('Error')

def statement_list():
    global current_token

    if current_token == 10: # ID
        match(10)
        statement_prime()
        statement_list()
    elif current_token == 21: # {
        match(21)
        local_declarations()
        statement_list()
        match(22)
        statement_list()
    elif current_token == 32: # if
        match(32)
        match(17)
        expression()
        match(18)
        statement()
        selection_stmt_prime()
        statement_list()
    elif current_token == 36: # while
        match(36)
        match(17)
        expression()
        match(18)
        statement()
        statement_list()
    elif current_token ==  34: # return
        match(34)
        return_stmt_prime()
        statement_list()
    elif current_token == 37: # input
        match(37)
        var()
        match(12)
        statement_list()
    elif current_token == 38: # output
        match(38)
        expression()
        match(12)
        statement_list()
    elif current_token == 22: # }
        return