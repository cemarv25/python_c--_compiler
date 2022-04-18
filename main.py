from scanner.main import recognize_tokens

if __name__ == '__main__':
    f = open('scanner/test1.txt', 'r')
    token_sequence, ids_table, nums_table = recognize_tokens(f)
    print(token_sequence)
    f.close()
    del f