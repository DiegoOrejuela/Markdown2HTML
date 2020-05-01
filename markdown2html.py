#!/usr/bin/python3
"""
0. Start a script

Write a script markdown2html.py that takes an argument 2 strings:
- First argument is the name of the Markdown file
- Second argument is the output file name
Requirements:
- If the number of arguments is less than 2: print
  in STDERR Usage: ./markdown2html.py README.md README.html and exit 1
- If the Markdown file doesn’t exist: print in STDER Missing
  <filename> and exit 1
- Otherwise, print nothing and exit 0
"""

if __name__ == "__main__":
    import sys
    from os import path

    if len(sys.argv) < 3:
        error_mssg = "Usage: ./markdown2html.py README.md README.html\n"
        sys.stderr.write(error_mssg)
        exit(1)
    else:
        if path.exists(sys.argv[1]) and \
            path.isfile(sys.argv[1]) and sys.argv[1].endswith('.md'):
            exit(0)
        else:
            sys.stderr.write("Missing {}\n".format(sys.argv[1]))
            exit(1)
