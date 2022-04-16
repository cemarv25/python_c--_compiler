from utils import transition_table, advance, acceptor, error, gen_char_dict

def recognize_tokens(file):
    """Recognize the tokens in the input file
    
    :param file: The file to read from
    """
    curr_state = 0
    curr_char = file.read(1)
    char_to_idx = gen_char_dict()
    while not acceptor[curr_state] and not error[curr_state]:
        char_idx = char_to_idx[curr_char]
        new_state = transition_table[curr_state][char_idx]
        
        if advance[curr_state][char_idx]:
            curr_char = file.read(1)

        curr_state = new_state


if __name__ == '__main__':
    f = open('scanner/test1.txt', 'r')
    recognize_tokens(f)
    f.close()