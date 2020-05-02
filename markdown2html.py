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
def database():

    types = [
      {
        "name": "at_beginning",
        "element": "markdown"
      },
      {
        "name": "only_content",
        "element": "markdown"
      },
      {
        "name": "in_content",
        "element": "markdown"
      },
    ]

    elements = [
      {
        "markdown": {
          "code": "#",
          "type": "at_beginning"
        } ,
        "html_generated": {
          "tags": {
            "init": "<h1>",
            "end": "</h1>"
          },
          "type": "headings"
        }
      },
      {
        "markdown": {
          "code": "##",
          "type": "at_beginning"
        } ,
        "html_generated": {
          "tags": {
            "init": "<h2>",
            "end": "</h2>"
          },
          "type": "headings"
        }
      },
      {
        "markdown": {
          "code": "###",
          "type": "at_beginning"
        } ,
        "html_generated": {
          "tags": {
            "init": "<h3>",
            "end": "</h3>"
          },
          "type": "headings"
        }
      },
      {
        "markdown": {
          "code": "####",
          "type": "at_beginning"
        } ,
        "html_generated": {
          "tags": {
            "init": "<h4>",
            "end": "</h4>"
          },
          "type": "headings"
        }
      },
      {
        "markdown": {
          "code": "#####",
          "type": "at_beginning"
        } ,
        "html_generated": {
          "tags": {
            "init": "<h5>",
            "end": "</h5>"
          },
          "type": "headings"
        }
      }
    ]

    return elements, types

def markdown2html(markdown_file, name_html_file):
  # Database
  db = database()

  # Open file
  file = open(markdown_file, "r")

  for line in file:
    if line != "\n":
      line_formattted = line.replace('\n', "")
      html_parsed_line = parser_to_html(line_formattted, db)
      print(html_parsed_line)

def parser_to_html(string, database):
  import re

  #unpack database
  elements, types = database

  string_parts = string.split(" ", 1)
  convertions_queue = []

  for type in types:
    elements_to_search = filter(lambda element: element['markdown']["type"] == type["name"], elements)
    
    for element in elements_to_search:
      #import pdb; pdb.set_trace()
      if type["name"] == "at_beginning":
        if string_parts[0] == element["markdown"]["code"]:
          convertions_queue.append({
            "element": element,
            "match": None
          })
  
  string_converted = string_parts[1]
  for convertion in convertions_queue:
    if convertion["match"]:
      pass
    else:
      string_converted = convertion["element"]["html_generated"]["tags"]["init"] + string_converted + convertion["element"]["html_generated"]["tags"]["end"]
    
  return string_converted

if __name__ == "__main__":
    import sys
    from os import path

    # Entry point
    if len(sys.argv) < 3:
        error_mssg = "Usage: ./markdown2html.py README.md README.html\n"
        sys.stderr.write(error_mssg)
        exit(1)
    else:
        if path.exists(sys.argv[1]) and path.isfile(sys.argv[1]):
            markdown2html(sys.argv[1], sys.argv[2])
            exit(0)
        else:
            sys.stderr.write("Missing {}\n".format(sys.argv[1]))
            exit(1)