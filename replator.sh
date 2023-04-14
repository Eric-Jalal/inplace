#!/bin/bash

# The directory to search for text files
search_dir="."

# Prompt the user to input the search and replace text
read -p "Enter the text to search for: " search_text
read -p "Enter the text to replace it with: " replace_text
read -P "Enter the postfix of the files you wanna affect: " postfix_text

# Find all the text files in the directory and its subdirectories
text_files=$(find "$search_dir" -type f -name *."$postfix_text")

# Loop through each text file and perform the search and replace
for file in $text_files; do
    # Perform the search and replace
    sed -i "s/$search_text/$replace_text/g" "$file"
done

echo "Search and replace complete."

