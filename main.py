from scanner.main import recognize_tokens
from parser.main import parse

if __name__ == '__main__':
    f = open('scanner/test1.txt', 'r')
    output = recognize_tokens(f)

    if type(output) == tuple:
        token_sequence, ids_table, nums_table = output
        print(token_sequence)
        
        for entry in ids_table.entries:
            print(entry[0], entry[1].content)

        for entry in nums_table.entries:
            print(entry[0], entry[1].content)

        parse(token_sequence, ids_table, nums_table)
    else:
        error_msg = output
        print(error_msg)
    f.close()
    del f