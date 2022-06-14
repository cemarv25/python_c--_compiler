class Entry:
    """Class used to represent the Entries of the Symbol Table.
    """

    def __init__(self, content: str, line: int) -> None:
        """The Entry's constructor.

        Args:
            content (str): The Entry's content
            line (int): The Entry's line
        """

        self.content = content
        self.line = line

    def create_info_dict(self) -> None:
        """Method to create the entry's info dictionary.
        """

        self.info = {
            'isVar': False,
            'isFun': False,
            'global': False,
            'local': False,
            'arg_num': None,
            'return_type': None
        }