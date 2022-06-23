from scanner.main import recognize_tokens
from parser.main import SyntaxException, parse

if __name__ == '__main__':
    f = open('scanner/test1.txt', 'r')
    output = recognize_tokens(f)

    if type(output) == tuple:
        token_sequence, ids_table, nums_table = output
        # print(token_sequence)
        print('----- BEFORE PARSING -----\n')
        print('----- IDs -----\n')
        for entry in ids_table.entries:
            print(entry[0], entry[1].content)
        print('\n')

        print('----- NUMs -----\n')
        for entry in nums_table.entries:
            print(entry[0], entry[1].content)
        print('\n')

        try:
            parse(token_sequence, ids_table, nums_table)

            print('\n----- AFTER PARSING -----\n')
            print('----- IDs -----\n')
            for entry in ids_table.entries:
                print(f"{entry[0]}\t{entry[1].content}\t{entry[1].info}")
            print('\n')

            print('----- NUMs -----\n')
            for entry in nums_table.entries:
                print(entry[0], entry[1].content)
            print('\n')

        except SyntaxException as err:
            print(err.message)
            
        except Exception as err:
            print('syntax analysis error')
            print(err)

    else:
        error_msg = output
        print(error_msg)
    f.close()
    del f