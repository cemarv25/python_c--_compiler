class IdGenerator:
    """A class that generates incremental ids."""

    def __init__(self, starting_id = 0) -> None:
        """
        :param starting_id: The first number that will be returned as an id (default is 0)
        """
        self.id = starting_id - 1
        self.starting_id = starting_id

    def next(self) -> int:
        """Returns the next id
        
        :rtype: int
        """

        self.id += 1
        return self.id

    def count(self) -> int:
        """Returns the amount of id's generated
        
        :rtype: int
        """
        return self.id - self.starting_id