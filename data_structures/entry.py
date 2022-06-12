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