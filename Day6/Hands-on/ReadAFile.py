def process_line(line):
    # Example: convert to uppercase
    return line.upper()

def process_file(input_file, output_file):
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            for line in infile:
                processed = process_line(line)
                outfile.write(processed)
        print(f"Processed content written to '{output_file}'.")
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except IOError as e:
        print(f"I/O error occurred: {e}")

# Example usage
if __name__ == "__main__":
    input_filename = "Hands-on/input.txt"
    output_filename = "Hands-on/output.txt"
    process_file(input_filename, output_filename)
