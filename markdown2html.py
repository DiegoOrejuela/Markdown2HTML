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
        },
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
        },
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
        },
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
        },
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
        },
        "html_generated": {
          "tags": {
            "init": "<h5>",
            "end": "</h5>"
          },
          "type": "headings"
        }
      }
    ]

    return {"elements": elements, "types": types}


def generate_file_html(path_file, lines):

    html_file = open(path_file, "w")

    for line in lines:
        html_file.write(line)

    html_file.close()

    return


def converter_string_by_line(content, convertions_queue):
    string_converted = content
    for convertion in convertions_queue:
        if convertion["match"]:
            pass
        else:
            string_converted = "{}{}{}\n".format(
              convertion["element"]["html_generated"]["tags"]["init"],
              string_converted,
              convertion["element"]["html_generated"]["tags"]["end"])

    return string_converted


def converter_markdown_at_beginning(init_string):

    convertion = None
    at_beginning_elements = filter(
        lambda element: element['markdown']["type"] == "at_beginning",
        database()["elements"]
      )

    for element in at_beginning_elements:
        # import pdb; pdb.set_trace()
        if init_string == element["markdown"]["code"]:
            convertion = {
              "element": element,
              "match": None
            }
    return convertion


def parser_to_html(string):

    types = database()["types"]
    string_parts = string.split(" ", 1)
    content = string
    convertions_queue = []

    for type in types:
        if type["name"] == "at_beginning":
            convertion = converter_markdown_at_beginning(string_parts[0])
            convertions_queue.append(convertion) if convertion else None
            if len(convertions_queue) == 1:
                content = string_parts[1] if len(string_parts) > 1 else ""

        if content:
            if type["name"] == "only_content":
                pass
                # convertions_queue = converter_markdown_only_content(content)
            elif type["name"] == "in_content":
                pass
                # convertions_queue = converter_markdown_in_content(content)

    string_converted = converter_string_by_line(content, convertions_queue)

    return string_converted


def markdown2html(markdown_file_path, html_file_path):

    converted_lines = []

    file = open(markdown_file_path, "r")

    for line in file:
        if line != "\n":
            line_formattted = line.replace('\n', "")
            html_parsed_line = parser_to_html(line_formattted)
            converted_lines.append(html_parsed_line)

    file.close()

    generate_file_html(html_file_path, converted_lines)

    return


# Entry point
if __name__ == "__main__":
    import sys
    from os import path

    if len(sys.argv) < 3:
        error_mssg = "Usage: ./markdown2html.py README.md README.html\n"
        sys.stderr.write(error_mssg)
        exit(1)
    else:
        if path.exists(sys.argv[1]) and path.isfile(sys.argv[1]):
            markdown_file_path, html_file_path = sys.argv[1], sys.argv[2]
            markdown2html(markdown_file_path, html_file_path)
            exit(0)
        else:
            sys.stderr.write("Missing {}\n".format(sys.argv[1]))
            exit(1)
