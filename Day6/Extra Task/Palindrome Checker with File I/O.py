import os
import string
import collections
from collections import defaultdict

def check_and_write_palindromes(input_file, output_file):
    try:
        if not os.path.exists(input_file):
            with open(input_file, 'w', encoding='utf-8') as f:
                f.write("Radar\n")
                f.write("Level\n")
                f.write("Hello\n")
                f.write("madam\n")
                f.write("world\n")
                f.write("Aibohphobia\n")
            print(f"Created a dummy input file for Palindrome Checker: {input_file}")

        palindromes = []
        with open(input_file, 'r', encoding='utf-8') as infile:
            for line in infile:
                word = line.strip()
                if not word:
                    continue
                if word.lower() == word[::-1].lower():
                    palindromes.append(word.upper())

        with open(output_file, 'w', encoding='utf-8') as outfile:
            for p_word in palindromes:
                outfile.write(p_word + '\n')
        print(f"Palindromes successfully written to '{output_file}'.")

    except FileNotFoundError:
        print(f"Error (Palindrome Checker): The file '{input_file}' was not found.")
    except IOError as e:
        print(f"Error (Palindrome Checker) reading or writing file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred (Palindrome Checker): {e}")