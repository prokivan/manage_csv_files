import csv
import sys


def read_csv(input_file):
    with open(input_file, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        data = [row for row in reader]
    return data


def write_csv(output_file, data):
    with open(output_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)


def apply_changes(data, changes):
    for change in changes:
        x, y, value = change.split(',')
        x = int(x)
        y = int(y)
        data[y][x] = value
    return data


def main():
    try:
        if len(sys.argv) < 3:
            print("Usage: python main.py <input_file> <output_file> <change_1> <change_2> ... <change_n>")
            sys.exit(1)

        input_file = sys.argv[1]
        output_file = sys.argv[2]
        changes = sys.argv[3:]

        # Reading CSV file
        data = read_csv(input_file)
        print(f"Original file content '{input_file}':")
        for row in data:
            print(row)

        # Changes
        data = apply_changes(data, changes)

        # Displaying the modified content
        print(f"\nModified file content '{output_file}':")
        for row in data:
            print(row)

        # Saving to new CSV
        write_csv(output_file, data)
        print("\nModified content saved!")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except IndexError:
        print("Error: Invalid coordinates provided for change.")
    except ValueError:
        print("Error: Invalid change format. Use the format 'x,y,value'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
