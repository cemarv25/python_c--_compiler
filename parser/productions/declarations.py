import parser.main as parser
import parser.productions.statements as statements
import parser.productions.expressions as expressions

def declaration_prime():
    if parser.current_token == 12: # ;
        parser.match(12)
    elif parser.current_token == 19: # [
        parser.match(19)
        parser.match(11)
        parser.match(20)
        parser.match(12)
    elif parser.current_token == 17: # (
        parser.match(17)
        params()
        parser.match(18)
        statements.compound_stmt()
    else:
        raise Exception('Error')

def var_declaration_prime():
    if parser.current_token == 12: # ;
        parser.match(12)
    elif parser.current_token == 19: # [
        parser.match(19)
        parser.match(11)
        parser.match(20)
        parser.match(12)
    else:
        raise Exception('Error')

def params():
    if parser.current_token == 33: # int
        parser.match(33)
        parser.match(10)
        param_prime()
        param_list_prime()
    elif parser.current_token == 35: # void
        parser.match(35)
    else:
        raise Exception('Error')

def param_list_prime():
    if parser.current_token == 13: # ,
        parser.match(13)
        parser.match(33)
        parser.match(10)
        param_prime()
        param_list_prime()
    elif parser.current_token == 18: # )
        return
    else:
        raise Exception('Error')

def param_prime():
    if parser.current_token == 19: # [
        parser.match(19)
        parser.match(20)
    elif parser.current_token == 13 or parser.current_token == 18:
        return
    else:
        raise Exception('Error')

def local_declarations():
    if parser.current_token == 33: # int
        parser.match(33)
        parser.match(10) 
        var_declaration_prime()
        local_declarations()
    elif parser.current_token == 10 or parser.current_token == 21 or parser.current_token == 32 or parser.current_token == 36 or parser.current_token == 34 or parser.current_token == 37 or parser.current_token == 38 or parser.current_token == 22:
        return
    else:
        raise Exception('Error')

def args_list_prime():
    if parser.current_token == 13: # ,
        parser.match(13)
        expressions.arithmetic_expression()
        args_list_prime()
    elif parser.current_token == 18: # )
        return
    else:
        raise Exception('Error')
