from scanner.main import recognize_tokens

if __name__ == '__main__':
    f = open('scanner/tests/text_files/test_non_closing_comment.txt', 'r')
    output = recognize_tokens(f)

    if type(output) == tuple:
        token_sequence, ids_table, nums_table = output
    else:
        token_sequence = output
    print(token_sequence)
    f.close()
    del f