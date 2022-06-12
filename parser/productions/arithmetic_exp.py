from parser.main import match, call_prime

current_token = None
token_sequence = None

def factor_prime(current_token):
    if current_token == 19:
        match(19)
        arithmetic_expression(current_token)
        match(20)
    elif current_token == 17:
        match(17)
        call_prime()

    # *, /, +, -, <=, <, >, >=, ==, !=, ), ;, ], ,
    elif current_token == 16 or current_token == 30 or current_token == 14 or current_token == 15 or current_token == 25 or current_token == 24 or current_token == 26 or current_token == 27 or current_token == 29 or current_token == 23 or current_token == 18 or current_token == 12 or current_token == 20 or current_token == 13:
        return
    else:
        raise Exception('Error')

def factor(current_token):
    if current_token == 17: # (
        match(17)
        arithmetic_expression(current_token)
        match(18)
    elif current_token == 10: # ID
        match(10)
        factor_prime(current_token)
    elif current_token == 11: # NUM
        match(11)
    else:
        raise Exception('Error')

def term_prime(current_token):
    if current_token == 16: # *
        match(16)
        factor(current_token)
        term_prime(current_token)
    elif current_token == 30: # /
        match(30)
        factor(current_token)
        term_prime(current_token)

    # +, -, <=, <, >, >=, ==, !=, ), ;, ], ,
    elif current_token == 14 or current_token == 15 or current_token == 25 or current_token == 24 or current_token == 26 or current_token == 27 or current_token == 29 or current_token == 23 or current_token == 18 or current_token == 12 or current_token == 20 or current_token == 13:
        return
    else:
        raise Exception('Error')

def term(current_token):
    if current_token == 17: # (
        match(17)
        arithmetic_expression(current_token)
        match(18)
        term_prime(current_token)
    elif current_token == 10: # ID
        match(10)
        factor_prime(current_token)
        term_prime(current_token)
    elif current_token == 11: # NUM
        match(11)
        term_prime(current_token)
    else:
        raise Exception('Error')

def arithmetic_expression_prime(current_token):
    if current_token == 14: # +
        match(14)
        term(current_token)
        arithmetic_expression_prime(current_token)
    elif current_token == 15: # -
        match(15)
        term(current_token)
        arithmetic_expression_prime(current_token)

    # <=, <, >, >=, ==, !=, ), ;, ], ,
    elif current_token == 25 or current_token == 24 or current_token == 26 or current_token == 27 or current_token == 29 or current_token == 23 or current_token == 18 or current_token == 12 or current_token == 20 or current_token == 13:
        return
    else:
        raise Exception('Error')

def arithmetic_expression(current_token):
    if current_token == 17: # (
        match(17)
        arithmetic_expression(current_token)
        match(18)
        term_prime(current_token)
        arithmetic_expression_prime(current_token)
    elif current_token == 10: # ID
        match(10)
        factor_prime(current_token)
        term_prime(current_token)
        arithmetic_expression_prime(current_token)
    elif current_token == 11: # NUM
        match(11)
        term_prime(current_token)
        arithmetic_expression_prime(current_token)
    else:
        raise Exception('Error')
