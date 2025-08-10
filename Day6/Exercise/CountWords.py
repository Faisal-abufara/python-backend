counter = 0
try:
    with open(r'Exercise/test.txt', 'r') as file:
        content = file.read()
        
        if not content.strip():
            print("File is empty!")
        else:
            words = content.split()
            counter = len(words)
            print(f"Words: {words}")
            print(f"Total word count: {counter}")

except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print(f"An error occurred: {e}")
