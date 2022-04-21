from scanner.main import recognize_tokens

if __name__ == '__main__':
    f = open('scanner/test1.txt', 'r')
    output = recognize_tokens(f)

    if type(output) == tuple:
        token_sequence, ids_table, nums_table = output
        print(token_sequence)
    else:
        error_msg = output
        print(error_msg)
    f.close()
    del f