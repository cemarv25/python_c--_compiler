class IdGenerator:
    """A class that generates incremental ids.
    """

    def __init__(self, starting_id = 0) -> None:
        """The IdGenerator's constructor.

        Args:
            starting_id (int, optional): The first number that will be returned as an id. Defaults to 0.
        """
        self.id = starting_id - 1
        self.count = 0

    def next(self) -> int:
        """Returns the next id.

        Returns:
            int: The id number
        """

        self.id += 1
        self.count += 1
        return self.id

    def count(self) -> int:
        """Returns the amount of ids generated.

        Returns:
            int: The amount of ids generated
        """
        return self.count