import os 

def convert_temperatures(input_file, output_file):
    try:
        if not os.path.exists(input_file):
            with open(input_file, 'w', encoding='utf-8') as f:
                f.write("0\n")
                f.write("100\n")
                f.write("25.5\n")
                f.write("-10\n")
                f.write("abc\n")
                f.write("37.7")
            print(f"Created a dummy input file for Temperature Converter: {input_file}")

        results = []
        with open(input_file, 'r', encoding='utf-8') as infile:
            for line in infile:
                celsius_str = line.strip()
                if not celsius_str:
                    continue
                try:
                    celsius = float(celsius_str)
                    fahrenheit = (celsius * 9/5) + 32
                    results.append(f"{celsius:.1f}C = {fahrenheit:.1f}F")
                except ValueError:
                    print(f"Warning (Temperature Converter): Skipping invalid temperature '{celsius_str}' in '{input_file}'.")

        with open(output_file, 'w', encoding='utf-8') as outfile:
            for res in results:
                outfile.write(res + '\n')
        print(f"Temperature conversions successfully written to '{output_file}'.")

    except FileNotFoundError:
        print(f"Error (Temperature Converter): The file '{input_file}' was not found.")
    except IOError as e:
        print(f"Error (Temperature Converter) reading or writing file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred (Temperature Converter): {e}")