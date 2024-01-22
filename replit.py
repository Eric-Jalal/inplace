#!/usr/bin/env python3

import os
import fnmatch
import argparse

def find_and_replace(file_formats, search_text, replace_text=None):
    matches = []
    total_files_checked = 0

    for file_format in file_formats:
        for root, dirnames, filenames in os.walk('.'):
            for filename in fnmatch.filter(filenames, f'*.{file_format}'):
                total_files_checked += 1
                filepath = os.path.join(root, filename)
                try:
                    with open(filepath, 'r', encoding='utf-8') as file:
                        file_content = file.read()
                        if search_text in file_content:
                            matches.append(filepath)
                except Exception as e:
                    print(f"Error reading file {filepath}: {str(e)}")

    if not matches:
        print("No occurrences found.")
        print(f"Total files checked: {total_files_checked}")
        return

    print(f"Found {search_text} in:")
    for match in matches:
        print(match)
    confirmation = input("Do you want to proceed with the replacement? (yes/no): ")
    if confirmation.lower() == 'yes':
        for match in matches:
            try:
                with open(match, 'r', encoding='utf-8') as file:
                    file_content = file.read()
                new_content = file_content.replace(search_text, replace_text if replace_text is not None else '')
                with open(match, 'w', encoding='utf-8') as file:
                    file.write(new_content)
            except Exception as e:
                print(f"Error modifying file {match}: {str(e)}")

        print("Replacement complete.")
        print(f"Total files affected: {len(matches)}")
        print(f"Total files checked: {total_files_checked}")
        print("Paths to affected files:")
        for match in matches:
            print(match)
    else:
        print("Operation cancelled.")

def interactive_mode():
    try:
        file_formats = input("Enter the file formats (e.g., txt yml csv): ").split()
        search_text = input("Enter the text to search for: ")
        replace_text = input("Enter the text to replace with (leave blank to remove): ")
        find_and_replace(file_formats, search_text, replace_text)
    except Exception as e:
        print(f"An unexepcted error ocurred during interactive mode: {str(e)}")

def main():
    try:
        parser = argparse.ArgumentParser(description='Find and replace text in files.')
        parser.add_argument('-i', '--interactive', action='store_true', help='Interactive mode')
        parser.add_argument('-f', '--file-formats', type=str, help='File formats to search')
        parser.add_argument('strings', metavar='STRING', type=str, nargs='*', help='Strings for search and replace')

        args = parser.parse_args()

        if args.interactive:
            interactive_mode()
        elif args.file_formats and len(args.strings) >= 2:
            file_formats = args.file_formats.split()
            find_and_replace(file_formats, args.strings[0], args.strings[1])
        else:
            print("Invalid arguments. Use -i for interactive mode or -f to specify file formats along with search and replace strings.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()



