import os
import datetime
import sys

def write_entry(entry, journal_name):
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(f"{journal_name}.txt", "a") as file:
        file.write(f"{date}\n{entry}\n{'='*30}\n")

def read_entries(journal_name):
    journal_file = f"{journal_name}.txt"
    if os.path.exists(journal_file):
        with open(journal_file, "r") as file:
            entries = file.read()
            return entries
    else:
        return "No entries yet."

def main():
    while True:
        print("1. Write a new diary entry")
        print("2. Read all diary entries")
        print("3. Exit")
        
        choice = input("Select an option: ")
        
        if choice == "1":
            journal_name = input("Enter the journal name: ")
            print("Write your diary entry. Press [Ctrl+D] (or [Ctrl+Z] on Windows) to finish and save your text.")
            
            entry = sys.stdin.read()  # Read input until EOF (Ctrl+D/Ctrl+Z)
            
            write_entry(entry, journal_name)
            print("\nEntry saved!\n")
        elif choice == "2":
            journal_name = input("Enter the journal name: ")
            entries = read_entries(journal_name)
            print("\n")
            print(entries)
        elif choice == "3":
            print("Exiting the diary app.")
            break
        else:
            print("Invalid choice. Please select again.\n")

if __name__ == "__main__":
    main()
