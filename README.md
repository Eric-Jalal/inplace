### Find & Replace CLI Tool v1.0.0

Introducing the Find & Replace CLI Tool which actually works easily. Working with `find` sometimes for easy tasks is overkill :). I made this tool to make my-life easier. Specially when I need to change some text in multiple files in a repo without opening extra editors and such. This utility allows users to search for a specific text string within files of specified formats in the current directory and its subdirectories. Upon finding occurrences, the tool provides an interactive prompt for the user to confirm if they wish to proceed to replace the found text with another string.

Key Features:

- Supports multiple file formats.
- Interactive mode for a guided text replacement process.
- Command-line flags for streamlined text replacement.
- Provides a summary report of files checked, files affected, and the paths to affected files.
- Enhanced error handling for a robust user experience.

Usage:

- Interactive Mode: find_replace -i
- Direct Mode: find_replace -f txt,yml search-for-me replace-it-with-me
- Installation:

Available for installation via Homebrew: 

    ```
brew tap Eric-Jalal/tap
brew install repelit

    ```
