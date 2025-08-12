import os
from collections import defaultdict
def analyze_log_file(input_file, output_file):
    status_counts = defaultdict(int)
    required_statuses = {200, 404, 500}

    try:
        if not os.path.exists(input_file):
            with open(input_file, 'w', encoding='utf-8') as f:
                f.write("192.168.1.1 200 /index.html\n")
                f.write("192.168.1.2 404 /missing.css\n")
                f.write("192.168.1.3 200 /images/logo.png\n")
                f.write("192.168.1.4 500 /api/data\n")
                f.write("192.168.1.5 200 /about.html\n")
                f.write("192.168.1.6 404 /favicon.ico\n")
                f.write("192.168.1.7 200 /contact.html\n")
                f.write("192.168.1.8 302 /redirect\n")
            print(f"Created a dummy log file for Log Analyzer: {input_file}")

        with open(input_file, 'r', encoding='utf-8') as infile:
            for line in infile:
                parts = line.strip().split()
                if len(parts) >= 2:
                    try:
                        status_code = int(parts[1])
                        if status_code in required_statuses:
                            status_counts[status_code] += 1
                    except ValueError:
                        print(f"Warning (Log Analyzer): Could not parse status code from line: '{line.strip()}'")
                else:
                    print(f"Warning (Log Analyzer): Malformed log line: '{line.strip()}'")

        with open(output_file, 'w', encoding='utf-8') as outfile:
            outfile.write("Server Log Analysis Report\n")
            outfile.write("--------------------------\n")
            outfile.write(f"Successful (200): {status_counts[200]}\n")
            outfile.write(f"Not Found (404): {status_counts[404]}\n")
            outfile.write(f"Server Error (500): {status_counts[500]}\n")
        print(f"Log analysis report successfully written to '{output_file}'.")

    except FileNotFoundError:
        print(f"Error (Log Analyzer): The log file '{input_file}' was not found.")
    except IOError as e:
        print(f"Error (Log Analyzer) reading or writing file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred (Log Analyzer): {e}")