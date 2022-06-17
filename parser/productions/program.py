import parser.main as parser
import parser.productions.statements as statements
import parser.productions.declarations as declarations

def program() -> None:
    """Function for the non-terminal symbol program"""

    if parser.current_token_id == 33: # int
        parser.match(33)
        parser.match(10, { 'global': True, 'global_line': parser.token_line })
        declarations.declaration_prime()
        program()
    elif parser.current_token_id == 35: # void
        parser.match(35)
        parser.match(10, { 'isFun': True, 'global': True, 'return_type': 'void', 'global_line': parser.token_line })
        parser.match(17)
        declarations.params()
        parser.match(18)
        statements.compound_stmt()
        program()
    elif parser.current_token_id == 0:
        return
    else:
        raise parser.SyntaxException(f"SyntaxException: Expected a declaration, but found '{parser.token_content}'.\n\tAt line {parser.token_line}")