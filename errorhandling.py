def ask_and_read_file():
    filename = input("Enter the filename to read: ")
    
    try:
        # Try to open and read the file
        with open(filename, 'r') as file:
            content = file.read()
            print(f"Content of the file '{filename}':\n{content}")
    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except IOError:
        print(f"Error: Could not read the file '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function to ask for the filename and attempt to read it
ask_and_read_file()
