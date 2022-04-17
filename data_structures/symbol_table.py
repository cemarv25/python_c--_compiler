from entry import Entry
from id_generator import IdGenerator

class SymbolTable:
    """Class used to store token entries with the token's information.
    """

    def __init__(self, name: str) -> None:
        """SymbolTable constructor

        Args:
            name (str): The name for the table
        """

        self.name = name
        self.entries = []
        self.id_gen = self.initialize_id_gen()

    def insert_entry(self, entry: Entry):
        """Inserts an entry to the entry list of the table.

        Args:
            entry (Entry): The entry to be inserted
        """

        entry_id = self.id_gen.next()
        self.entries.append((entry_id, entry))

    def initialize_id_gen(self) -> IdGenerator:
        """Initializes the Symbol Table's id generator.

        Returns:
            IdGenerator: An instance of the class IdGenerator
        """

        return IdGenerator()