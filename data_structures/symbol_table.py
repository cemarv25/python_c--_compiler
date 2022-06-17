from .entry import Entry
from .id_generator import IdGenerator

class SymbolTable:
    """Class used to store token entries with the token's information.
    """

    def __init__(self, name: str) -> None:
        """SymbolTable constructor

        If the name is 'identifiers', each entry in the SymbolTable will have a dictionary'info' storing the following info:
        - isVar (bool): If the entry is a variable, this value will be true
        - isFun (bool): If the entry is a function, this value will be true
        - global (bool): If the entry appears in a global scope, this value will be true
        - local (bool): If the entry appears in a local scope, this value will be true (the entry can be both global and local)
        - args_num (int): If the entry is a function, it will have the number of arguments. None otherwise

        Args:
            name (str): The name for the table
        """

        self.name = name
        self.entries = []
        self.id_gen = self.initialize_id_gen()

    def insert_entry(self, entry_content: str) -> int:
        """Inserts an entry to the entry list of the table. If the SymbolTable's name is 'identifiers', it will create the entry's info dictionary.

        Args:
            entry_content (str): The entry's content.
        Returns:
            entry_id: The new entry's id.
        """
        entry = Entry(entry_content)
        if self.name == 'identifiers':
            entry.create_info_dict()

        entry_id = self.id_gen.next()
        self.entries.append((entry_id, entry))
        return entry_id

    def exists(self, token: str) -> bool:
        """Check if a token is already in the table.

        Args:
            token (str): The token to verify

        Returns:
            bool: True if the token is in the table, False otherwise
        """

        for entry_id, entry in self.entries:
            if token == entry.content:
                return True
        
        return False

    def get_entry_with_id(self, id: int) -> Entry | None:
        """Get an entry with its id if it exists. Otherwise return None.

        Args:
            id (int): The entry's id

        Returns:
            Entry | None: The entry if found, None if not found.
        """

        for entry_id, entry in self.entries:
            if entry_id == id:
                return entry

        return None

    def get_entry_with_token(self, token: str) -> tuple | None:
        """Gen an entry with the token if exists. Otherwise return None.

        Args:
            token (str): The token to search for

        Returns:
            tuple | None: The tuple (entry_id, entry) if found, None if not found.
        """

        for entry_id, entry in self.entries:
            if token == entry.content:
                return (entry_id, entry)
        
        return None

    def initialize_id_gen(self) -> IdGenerator:
        """Initializes the Symbol Table's id generator.

        Returns:
            IdGenerator: An instance of the class IdGenerator
        """

        return IdGenerator()