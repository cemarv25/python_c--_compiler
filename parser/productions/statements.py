import parser.main as parser
import parser.productions.declarations as declarations
import parser.productions.expressions as expressions

def compound_stmt():
    if parser.current_token_id == 21: # {
        parser.match(21)
        declarations.local_declarations()
        statement_list()
        parser.match(22)
    else: raise parser.SyntaxException(f"SyntaxException: Invalid function body. Expected '{{', but got '{parser.token_content}'.\n\tAt line {parser.token_line}.")

def statement_list():
    if parser.current_token_id == 10: # ID
        parser.match(10)
        statement_prime()
        statement_list()
    elif parser.current_token_id == 21: # {
        parser.match(21)
        declarations.local_declarations()
        statement_list()
        parser.match(22)
        statement_list()
    elif parser.current_token_id == 32: # if
        parser.match(32)
        parser.match(17)
        expressions.expression()
        parser.match(18)
        statement()
        selection_stmt_prime()
        statement_list()
    elif parser.current_token_id == 36: # while
        parser.match(36)
        parser.match(17)
        expressions.expression()
        parser.match(18)
        statement()
        statement_list()
    elif parser.current_token_id ==  34: # return
        parser.match(34)
        return_stmt_prime()
        statement_list()
    elif parser.current_token_id == 37: # input
        parser.match(37)
        parser.match(10)
        var_prime()
        parser.match(12)
        statement_list()
    elif parser.current_token_id == 38: # output
        parser.match(38)
        expressions.expression()
        parser.match(12)
        statement_list()
    elif parser.current_token_id == 22: # }
        return
    
    else:
        raise parser.SyntaxException(f"SyntaxException: Invalid statement. Expected a statement but got '{parser.token_content}'.\n\tAt line {parser.token_line}.")

def statement():
    if parser.current_token_id == 10: # ID
        parser.match(10)
        statement_prime()
    elif parser.current_token_id == 21: # {
        parser.match(21)
        declarations.local_declarations()
        statement_list()
        parser.match(22)
    elif parser.current_token_id == 32: # if
        parser.match(32)
        parser.match(17)
        expressions.expression()
        parser.match(18)
        statement()
        selection_stmt_prime()
    elif parser.current_token_id == 36: # while
        parser.match(36)
        parser.match(17)
        expressions.expression()
        parser.match(18)
        statement()
    elif parser.current_token_id == 34: # return
        parser.match(34)
        return_stmt_prime()
    elif parser.current_token_id == 37: # input
        parser.match(37)
        parser.match(10)
        var_prime()
        parser.match(12)
    elif parser.current_token_id == 38: # output
        parser.match(38)
        expressions.expression()
        parser.match(12)
    else:
        raise parser.SyntaxException(f"SyntaxException: Invalid statement. Expected a statement but got '{parser.token_content}'.\n\tAt line {parser.token_line}.")

def statement_prime():
    if parser.current_token_id == 19: # [
        parser.match(19)
        expressions.arithmetic_expression()
        parser.match(20)
        parser.match(28)
        expressions.expression()
        parser.match(12)
    elif parser.current_token_id == 28: # =
        parser.match(28)
        expressions.expression()
        parser.match(12)
    elif parser.current_token_id == 17: # (
        parser.match(17)
        call_prime()
        parser.match(12)
    else:
        raise parser.SyntaxException(f"SyntaxException: Incomplete statement. Expected '[', '=' or '(' but got '{parser.token_content}'.\n\tAt line {parser.token_line}.")

def selection_stmt_prime():
    if parser.current_token_id == 31: # else
        parser.match(31)
        statement()

    # ID, {, if, while, return, input, output, else, }
    elif parser.current_token_id == 10 or parser.current_token_id == 21 or parser.current_token_id == 32 or parser.current_token_id == 36 or parser.current_token_id == 34 or parser.current_token_id == 37 or parser.current_token_id == 38 or parser.current_token_id == 31 or parser.current_token_id == 22:
        return
    else:
        raise parser.SyntaxException(f"SyntaxException: Invalid if statement. Expected 'else', an identifier, '}}', or a statement but got '{parser.token_content}'.\n\tAt line {parser.token_line}.")

def return_stmt_prime():
    if parser.current_token_id == 12: # ;
        parser.match(12)
    elif parser.current_token_id == 17: # (
        parser.match(17)
        expressions.arithmetic_expression()
        parser.match(18)
        expressions.term_prime()
        expressions.arithmetic_expression_prime()
        expressions.expression_prime()
        parser.match(12)
    elif parser.current_token_id == 10: # ID
        parser.match(10)
        expressions.factor_prime()
        expressions.term_prime()
        expressions.arithmetic_expression_prime()
        expressions.expression_prime()
        parser.match(12)
    elif parser.current_token_id == 11: # NUM
        parser.match(11)
        expressions.term_prime()
        expressions.arithmetic_expression_prime()
        expressions.expression_prime()
        parser.match(12)
    else:
        raise parser.SyntaxException(f"SyntaxException: Invalid return statement. Expected ';' or an expression but got '{parser.token_content}'.\n\tAt line {parser.token_line}.")

def var_prime():
    if parser.current_token_id == 19: # [
        parser.match(19)
        expressions.arithmetic_expression()
        parser.match(20)
    elif parser.current_token_id == 12: # ;
        return
    else:
        raise parser.SyntaxException(f"SyntaxException: Invalid input statement. Expected '[' or ';' but got '{parser.token_content}'.\n\tAt line {parser.token_line}.")

def call_prime():
    if parser.current_token_id == 18: # )
        parser.match(18)
    elif parser.current_token_id == 17: # (
        parser.match(17)
        expressions.arithmetic_expression()
        parser.match(18)
        expressions.term_prime()
        expressions.arithmetic_expression_prime()
        args_list_prime()
        parser.match(18)
    elif parser.current_token_id == 10: # ID
        parser.match(10)
        expressions.factor_prime()
        expressions.term_prime()
        expressions.arithmetic_expression_prime()
        args_list_prime()
        parser.match(18)
    elif parser.current_token_id == 11: # NUM
        parser.match(11)
        expressions.term_prime()
        expressions.arithmetic_expression_prime()
        args_list_prime()
        parser.match(18)
    else:
        raise parser.SyntaxException(f"SyntaxException: Invalid function call. Expected an expression or ')' but got '{parser.token_content}'.\n\tAt line {parser.token_line}.")

def args_list_prime():
    if parser.current_token_id == 13: # ,
        parser.match(13)
        expressions.arithmetic_expression()
        args_list_prime()
    elif parser.current_token_id == 18: # )
        return
    else:
        raise parser.SyntaxException(f"SyntaxException: Invalid function parameters. Expected ',' or ')' but got '{parser.token_content}'.\n\tAt line {parser.token_line}.")
