class Entry:
    """Class used to represent the Entries of the Symbol Table.
    """

    def __init__(self, content: str) -> None:
        """The Entry's constructor.

        Args:
            content (str): The Entry's content
        """

        self.content = content