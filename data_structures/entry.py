class Entry:
    """Class used to represent the Entries of the Symbol Table"""

    def __init__(self, content: str) -> None:
        """
        :param content: The content of the Entry
        :type content: str
        """

        self.content = content