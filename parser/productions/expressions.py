import parser.main as parser
import parser.productions.statements as statements

def expression():
    if parser.current_token == 17: # (
        parser.match(17)
        arithmetic_expression()
        term_prime()
        arithmetic_expression_prime()
        expression_prime()
    elif parser.current_token == 10: # ID
        parser.match(10)
        factor_prime()
        term_prime()
        arithmetic_expression_prime()
        expression_prime()
    elif parser.current_token == 11: # NUM
        parser.match(11)
        term_prime()
        arithmetic_expression_prime()
        expression_prime()
    else:
        raise parser.SyntaxException(f"SyntaxException: Invalid expression. Expected an identifier, number or '(' but got {parser.token_content}.\n\tAt line {parser.token_line}.")

def expression_prime():
    if parser.current_token == 25: # <=
        parser.match(25)
        arithmetic_expression()
    elif parser.current_token == 24: # <
        parser.match(24)
        arithmetic_expression()
    elif parser.current_token == 26: # >
        parser.match(26)
        arithmetic_expression()
    elif parser.current_token == 27: # >=
        parser.match(27)
        arithmetic_expression()
    elif parser.current_token == 29: # ==
        parser.match(29)
        arithmetic_expression()
    elif parser.current_token == 23: # !=
        parser.match(23)
        arithmetic_expression()

    # ) ; ]
    elif parser.current_token == 18 or parser.current_token == 12 or parser.current_token == 18:
        return
    else:
        raise parser.SyntaxException(f"SyntaxException: Invalid expression. Expected a comparison operator, ')', ']' or ';' but got '{parser.token_content}'.\n\tAt line {parser.token_line}.")

def arithmetic_expression():
    if parser.current_token == 17: # (
        parser.match(17)
        arithmetic_expression()
        parser.match(18)
        term_prime()
        arithmetic_expression_prime()
    elif parser.current_token == 10: # ID
        parser.match(10)
        factor_prime()
        term_prime()
        arithmetic_expression_prime()
    elif parser.current_token == 11: # NUM
        parser.match(11)
        term_prime()
        arithmetic_expression_prime()
    else:
        raise parser.SyntaxException(f"SyntaxException: Invalid arithmetic expression. Expected an identifier, number or '(' but got '{parser.token_content}'.\n\tAt line {parser.token_line}.")

def arithmetic_expression_prime():
    if parser.current_token == 14: # +
        parser.match(14)
        term()
        arithmetic_expression_prime()
    elif parser.current_token == 15: # -
        parser.match(15)
        term()
        arithmetic_expression_prime()

    # <=, <, >, >=, ==, !=, ), ;, ], ,
    elif parser.current_token == 25 or parser.current_token == 24 or parser.current_token == 26 or parser.current_token == 27 or parser.current_token == 29 or parser.current_token == 23 or parser.current_token == 18 or parser.current_token == 12 or parser.current_token == 20 or parser.current_token == 13:
        return
    else:
        raise parser.SyntaxException(f"SyntaxException: Invalid arithmetic expression. Expected '+', '-', ')', ']', ';', ',' or a comparison operator but got '{parser.token_content}'.\n\tAt line {parser.token_line}.")

def term():
    if parser.current_token == 17: # (
        parser.match(17)
        arithmetic_expression()
        parser.match(18)
        term_prime()
    elif parser.current_token == 10: # ID
        parser.match(10)
        factor_prime()
        term_prime()
    elif parser.current_token == 11: # NUM
        parser.match(11)
        term_prime()
    else:
        raise parser.SyntaxException(f"SyntaxException: Invalid expression term. Expected an identifier, number or '(' but got '{parser.token_content}'.\n\tAt line {parser.token_line}.")

def term_prime():
    if parser.current_token == 16: # *
        parser.match(16)
        factor()
        term_prime()
    elif parser.current_token == 30: # /
        parser.match(30)
        factor()
        term_prime()

    # +, -, <=, <, >, >=, ==, !=, ), ;, ], ,
    elif parser.current_token == 14 or parser.current_token == 15 or parser.current_token == 25 or parser.current_token == 24 or parser.current_token == 26 or parser.current_token == 27 or parser.current_token == 29 or parser.current_token == 23 or parser.current_token == 18 or parser.current_token == 12 or parser.current_token == 20 or parser.current_token == 13:
        return
    else:
        raise parser.SyntaxException(f"SyntaxException: Invalid expression. Expected an operator, ')', ']', ',' or ';' but got '{parser.token_content}'.\n\tAt line {parser.token_line}.")

def factor():
    if parser.current_token == 17: # (
        parser.match(17)
        arithmetic_expression()
        parser.match(18)
    elif parser.current_token == 10: # ID
        parser.match(10)
        factor_prime()
    elif parser.current_token == 11: # NUM
        parser.match(11)
    else:
        raise parser.SyntaxException(f"SyntaxException: Invalid expression. Expected an identifier, number or '(' but got '{parser.token_content}'.\n\tAt line {parser.token_line}.")

def factor_prime():
    if parser.current_token == 19: # [
        parser.match(19)
        arithmetic_expression()
        parser.match(20)
    elif parser.current_token == 17: # (
        parser.match(17)
        statements.call_prime()

    # *, /, +, -, <=, <, >, >=, ==, !=, ), ;, ], ,
    elif parser.current_token == 16 or parser.current_token == 30 or parser.current_token == 14 or parser.current_token == 15 or parser.current_token == 25 or parser.current_token == 24 or parser.current_token == 26 or parser.current_token == 27 or parser.current_token == 29 or parser.current_token == 23 or parser.current_token == 18 or parser.current_token == 12 or parser.current_token == 20 or parser.current_token == 13:
        return
    else:
        raise parser.SyntaxException(f"SyntaxException: Invalid expression. Expected an operator, '[', ']', '(', ')', ',' or ';' but got '{parser.token_content}'.\n\tAt line {parser.token_line}.")
