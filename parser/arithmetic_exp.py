
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

def factor():
    global current_token
    if current_token == 17: # (
        match(17)
        exp()
        match(18)
    elif current_token == 11: # number
        match(11)
    else:
        raise Exception('Error')

def termPrime():
    global current_token
    if current_token == 16: # *
        match(16)
        factor()
        termPrime()
    elif current_token == 30: # /
        match(30)
        factor()
        termPrime()

    # $, ), +, -
    elif current_token == '$' or current_token == 18 or current_token == 14 or current_token == 15:
        return
    else:
        raise Exception('Error')

def term():
    factor()
    termPrime()

def expPrime():
    global current_token
    if current_token == 14: # +
        match(14)
        term()
        expPrime()
    elif current_token == 15: # -
        match(15)
        term()
        expPrime()
    elif current_token == '$' or current_token == 18: # $, )
        return
    else:
        raise Exception('Error')

def exp():
    term()
    expPrime()

def start(curr_token, token_seq, ids_table, nums_table):
    global token_sequence, current_token
    token_sequence = token_seq
    current_token = curr_token
    exp()
    return current_token