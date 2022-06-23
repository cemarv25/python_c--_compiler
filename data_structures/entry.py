class Entry:
    """Class used to represent the Entries of the Symbol Table.
    """

    def __init__(self, content: str) -> None:
        """The Entry's constructor.

        Args:
            content (str): The Entry's content
        """

        self.content = content

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