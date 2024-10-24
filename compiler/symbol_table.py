# symbol_table.py

class SymbolTable:
    def __init__(self):
        self.symbols = {}

    def add_symbol(self, name: str, type_: str, value=None) -> None:
        """Add a symbol to the table. If it exists, update the value."""
        if name not in self.symbols:
            self.symbols[name] = {'type': type_, 'value': value}
            print(f"Added symbol '{name}' of type '{type_}' with initial value '{value}'.")
        else:
            print(f"Symbol '{name}' already exists. Updating its value.")
            self.symbols[name]['value'] = value

    def update_symbol(self, name: str, value) -> None:
        """Update the value of a symbol if it exists."""
        if name in self.symbols:
            self.symbols[name]['value'] = value
            print(f"Updated symbol '{name}' with new value '{value}'.")
        else:
            print(f"Symbol '{name}' not found.")

    def get_symbol(self, name: str):
        """Retrieve a symbol's details."""
        return self.symbols.get(name, None)

    def display(self) -> None:
        """Display the symbol table for presentation purposes."""
        print("\n----Symbol Table----")
        if not self.symbols:
            print("The symbol table is empty.")
        else:
            for name, details in self.symbols.items():
                print(f"{name}: Type = {details['type']}, Value = {details['value']}")

    def clear(self) -> None:
        """Clear the symbol table for testing purposes."""
        self.symbols.clear()
        print("Symbol table cleared.")
