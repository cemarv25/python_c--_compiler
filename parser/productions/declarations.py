import parser.main as parser
import parser.productions.statements as statements

def declaration_prime():
    if parser.current_token == 12: # ;
        parser.match(12, { 'isVar': True })
    elif parser.current_token == 19: # [
        parser.match(19, { 'isVar': True })
        parser.match(11)
        parser.match(20)
        parser.match(12)
    elif parser.current_token == 17: # (
        parser.match(17, { 'isFun': True, 'return_type': 'int' })
        params()
        parser.match(18)
        statements.compound_stmt()
    else:
        raise parser.SyntaxException(f"SyntaxException: Unfinished declaration. Expected either ';', '[' or '(' but got '{parser.token_content}'.\n\tAt line {parser.token_line}")

def var_declaration_prime():
    if parser.current_token == 12: # ;
        parser.match(12)
    elif parser.current_token == 19: # [
        parser.match(19)
        parser.match(11)
        parser.match(20)
        parser.match(12)
    else:
        raise parser.SyntaxException(f"SyntaxException: Unfinished variable declaration. Expected either ';' or '[' but got '{parser.token_content}.\n\tAt line {parser.token_line}")

def params():
    if parser.current_token == 33: # int
        parser.match(33)
        parser.match(10, { 'isVar': True, 'local': True })
        param_prime()
        param_list_prime()
    elif parser.current_token == 35: # void
        parser.match(35)
    else:
        raise parser.SyntaxException(f"SyntaxException: Invalid function parameters. Expected either a variable declaration or 'void' but got '{parser.token_content}'.\n\tAt line {parser.token_line}")

def param_list_prime():
    if parser.current_token == 13: # ,
        parser.match(13)
        parser.match(33)
        parser.match(10, { 'isVar': True, 'local': True })
        param_prime()
        param_list_prime()
    elif parser.current_token == 18: # )
        return
    else:
        raise parser.SyntaxException(f"SyntaxException: Invalid function parameters. Expected either ',' or ')' but got {parser.token_content}.\n\tAt line {parser.token_line}")

def param_prime():
    if parser.current_token == 19: # [
        parser.match(19)
        parser.match(20)

    # ,, )
    elif parser.current_token == 13 or parser.current_token == 18:
        return
    else:
        raise parser.SyntaxException(f"SyntaxException: Invalid function parameters. Expected either '[', ',' or ')' but got {parser.token_content}.\n\tAt line {parser.token_line}")

def local_declarations():
    if parser.current_token == 33: # int
        parser.match(33)
        parser.match(10, { 'isVar': True, 'local': True }) 
        var_declaration_prime()
        local_declarations()

    # ID, {, if, while, return, input, output, }
    elif parser.current_token == 10 or parser.current_token == 21 or parser.current_token == 32 or parser.current_token == 36 or parser.current_token == 34 or parser.current_token == 37 or parser.current_token == 38 or parser.current_token == 22:
        return
    else:
        raise parser.SyntaxException(f"SyntaxException: Invalid function body, expected a variable declaration or a statement but got '{parser.token_content}'.\n\tAt line {parser.token_line}")
