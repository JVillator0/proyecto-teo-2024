import sys
from lexer import lexer
from parse import parse, symbol_table_print

def main():
    # Available test files
    test_files = {
        1: "tests/test1.c",
        2: "tests/test2.c", 
        3: "tests/test3.c",
        4: "tests/test4.c", 
        5: "tests/test5.c"
    }

    # Prompt user for file selection
    try:
        print("Select a test file to compile:")
        for key, filename in test_files.items():
            print(f"{key}: {filename}")
        
        user_choice = int(input("Enter file number (1-5): "))
        
        # Validate user input
        if user_choice not in test_files:
            print("Invalid input")
            sys.exit(1)
        
        file_path = test_files[user_choice]
        
        try:
            with open(file_path, 'r') as f:
                code = f.read()
                parse(code)
                symbol_table_print()
        
        except FileNotFoundError:
            print(f"File not found: {file_path}")
            sys.exit(1)
    
    except ValueError:
        print("Invalid input")
        sys.exit(1)

if __name__ == "__main__":
    main()