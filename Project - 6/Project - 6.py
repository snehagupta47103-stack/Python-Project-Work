import os
from datetime import datetime
class JournalManager:
    def __init__(self, filepath="journal.txt"):
        """
        Initialize the JournalManager with the default filename 'journal.txt'.
        """
        self.filepath = filepath

    def add_entry(self):
        """
        Requirement 1: Add a New Entry
        Appends a new journal entry with a timestamp. Creates the file if it doesn't exist ('a' mode).
        """
        entry_text = input("\nEnter your journal entry:\n")
        
        # Current timestamp format: [YYYY-MM-DD HH:MM:SS]
        timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
        
        try:
            # Using 'a' mode to append and handle automatic file creation
            with open(self.filepath, "a", encoding="utf-8") as file:
                file.write(f"{timestamp}\n{entry_text}\n\n")
            print("\nEntry added successfully!")
        except PermissionError:
            print("\nError: Permission denied. Cannot write to the file.")
        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}")

    def view_all_entries(self):
        """
        Requirement 2: View All Entries
        Displays all entries from the file. Handles FileNotFoundError gracefully.
        """
        if not os.path.exists(self.filepath):
            print("\nError: The journal file does not exist. Please add a new entry first.")
            return

        try:
            with open(self.filepath, "r", encoding="utf-8") as file:
                content = file.read().strip()
                
            if not content:
                print("\nNo journal entries found. Start by adding a new entry!")
            else:
                print("\nYour Journal Entries:")
                print("-" * 30)
                print(content)
        except FileNotFoundError:
            print("\nError: The journal file does not exist. Please add a new entry first.")
        except PermissionError:
            print("\nError: Permission denied. Cannot read the file.")

    def search_entry(self):
        """
        Requirement 3: Search for an Entry
        Searches the file for a specific keyword or date.
        """
        if not os.path.exists(self.filepath):
            print("\nNo journal entries found. Start by adding a new entry!")
            return

        keyword = input("\nEnter a keyword or date to search: ").strip()
        
        try:
            with open(self.filepath, "r", encoding="utf-8") as file:
                # Entries are separated by double newlines '\n\n'
                content = file.read()
                entries = content.strip().split("\n\n")
            
            matched_entries = []
            for entry in entries:
                if keyword.lower() in entry.lower():
                    matched_entries.append(entry)
            
            if matched_entries:
                print("\nMatching Entries:")
                print("-" * 30)
                for index, entry in enumerate(matched_entries):
                    print(entry)
                    if index < len(matched_entries) - 1:
                        print() # Space between matches
            else:
                print(f"\nNo entries were found for the keyword: {keyword}.")
                
        except Exception as e:
            print(f"\nAn error occurred while searching: {e}")

    def delete_all_entries(self):
        """
        Requirement 4: Delete All Entries
        Clears the journal by deleting the file after user confirmation.
        """
        if not os.path.exists(self.filepath):
            print("\nOutput (If the file does not exist):")
            print("No journal entries to delete.")
            return

        confirm = input("\Are you sure you want to delete all entries? (yes/no): ").strip().lower()
        
        if confirm == "yes":
            try:
                os.remove(self.filepath)
                print("\nOutput (If the file is deleted successfully):")
                print("All journal entries have been deleted.")
            except FileNotFoundError:
                print("\nNo journal entries to delete.")
            except PermissionError:
                print("\nError: Permission denied. Cannot delete the file.")
        else:
            print("\nDeletion cancelled.")


def main():
    # Creating object of JournalManager class (OOP Principle)
    manager = JournalManager()

    while True:
        # Exact Menu Interface as shown in the documentation
        print("\nWelcome to Personal Journal Manager!")
        print("Please select an option:\n")
        print("1. Add a New Entry")
        print("2. View All Entries")
        print("3. Search for an Entry")
        print("4. Delete All Entries")
        print("5. Exit")
        
        user_input = input("\nUser Input:\n").strip()

        if user_input == "1":
            manager.add_entry()
        elif user_input == "2":
            manager.view_all_entries()
        elif user_input == "3":
            manager.search_entry()
        elif user_input == "4":
            manager.delete_all_entries()
        elif user_input == "5":
            print("\nOutput:")
            print("Thank you for using Personal Journal Manager. Goodbye!")
            break
        else:
            print("\nOutput:")
            print("Invalid option. Please select a valid option from the menu.")


if __name__ == "__main__":
    main()