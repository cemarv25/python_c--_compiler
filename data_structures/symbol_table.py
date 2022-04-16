from entry import Entry
from id_generator import IdGenerator

class SymbolTable:
    """Class used to store token entries with the token's information."""

    def __init__(self, name: str) -> None:
        """
        :param name: The name of the symbol table.
        :type name: str
        """

        self.name = name
        self.entries = []
        self.id_gen = self.initialize_id_gen()

    def insert_entry(self, entry: Entry):
        """Inserts an entry to the entry list of the table.
        
        :param entry: The entry to be inserted
        :type entry: Entry
        """

        entry_id = self.id_gen.next()
        self.entries.append((entry_id, entry))

    def initialize_id_gen(self) -> IdGenerator:
        """Initializes the Symbol Table's id generator.
        
        :returns: An id generator
        :rtype: IdGenerator
        """

        return IdGenerator()