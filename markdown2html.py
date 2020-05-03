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
          "code": "__.+__",
          "type": "in_content",
          "code_subelement": ""
        },
        "html": {
          "name": "em",
          "tags": {
            "init": "<em>",
            "end": "</em>"
          },
          "type": "mark_text"
        }
      },
      {
        "markdown": {
          "code": "\*\*.+\*\*",
          "type": "in_content",
          "code_subelement": ""
        },
        "html": {
          "name": "b",
          "tags": {
            "init": "<b>",
            "end": "</b>"
          },
          "type": "mark_text"
        }
      },
      {
        "markdown": {
          "code": "#",
          "type": "at_beginning",
          "code_subelement": ""
        },
        "html": {
          "name": "h1",
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
          "type": "at_beginning",
          "code_subelement": ""
        },
        "html": {
          "name": "h2",
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
          "type": "at_beginning",
          "code_subelement": ""
        },
        "html": {
          "name": "h3",
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
          "type": "at_beginning",
          "code_subelement": ""
        },
        "html": {
          "name": "h4",
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
          "type": "at_beginning",
          "code_subelement": ""
        },
        "html": {
          "name": "h5",
          "tags": {
            "init": "<h5>",
            "end": "</h5>"
          },
          "type": "headings"
        }
      },
      {
        "markdown": {
          "code": "######",
          "type": "at_beginning",
          "code_subelement": ""
        },
        "html": {
          "name": "h6",
          "tags": {
            "init": "<h6>",
            "end": "</h6>"
          },
          "type": "headings"
        }
      },
      {
        "markdown": {
          "code": "-",
          "type": "at_beginning",
          "code_subelement": ""
        },
        "html": {
          "name": "li",
          "tags": {
            "init": "<li>",
            "end": "</li>"
          },
          "type": "element_list"
        }
      },
      {
        "markdown": {
          "code": "*",
          "type": "at_beginning",
          "code_subelement": ""
        },
        "html": {
          "name": "li",
          "tags": {
            "init": "<li>",
            "end": "</li>"
          },
          "type": "element_list"
        }
      },
      {
        "markdown": {
          "code": "",
          "type": "",
          "code_subelement": "-"
        },
        "html": {
          "name": "ul",
          "tags": {
            "init": "<ul>",
            "end": "</ul>"
          },
          "type": "list"
        }
      },
      {
        "markdown": {
          "code": "",
          "type": "",
          "code_subelement": "*"
        },
        "html": {
          "name": "ol",
          "tags": {
            "init": "<ol>",
            "end": "</ol>"
          },
          "type": "list"
        }
      },
      {
        "markdown": {
          "code": "",
          "type": "",
          "code_subelement": "text"
        },
        "html": {
          "name": "p",
          "tags": {
            "init": "<p>",
            "end": "</p>"
          },
          "type": "paragraph"
        }
      },
      {
        "markdown": {
          "code": "text",
          "type": "",
          "code_subelement": ""
        },
        "html": {
          "name": "text",
          "tags": {
            "init": "",
            "end": ""
          },
          "type": "text"
        }
      },
      {
        "markdown": {
          "code": "breakline",
          "type": "",
          "code_subelement": ""
        },
        "html": {
          "name": "br",
          "tags": {
            "init": "<br/>",
            "end": ""
          },
          "type": "breakline"
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
    special_elements = ["-", "*", "text"]
    macro_element = None
    # import pdb; pdb.set_trace()
    string_converted = content
    for convertion in convertions_queue:
        if convertion["match"]:
            pass
        else:
            code = convertion["element"]["markdown"]["code"]
            if code in special_elements:
                macro_element = list(filter(
                    lambda element:
                        element["markdown"]["code_subelement"] == code,
                        database()["elements"]
                ))[0]

            string_converted = "{}{}{}\n".format(
              convertion["element"]["html"]["tags"]["init"],
              string_converted,
              convertion["element"]["html"]["tags"]["end"])

    return macro_element, string_converted


def converter_markdown_at_beginning(init_string):
    convertion = None
    at_beginning_elements = filter(
        lambda element: element['markdown']["type"] == "at_beginning",
        database()["elements"]
      )

    for element in at_beginning_elements:
        # import pdb; pdb.set_trace()
        # import pdb; pdb.set_trace()
        if init_string == element["markdown"]["code"]:
            convertion = {
              "element": element,
              "match": None
            }

    if not convertion:
        convertion = {
                "element": list(
                  filter(
                    lambda element: element["html"]["name"] == "text",
                    database()["elements"]
                  )
                )[0],
                "match": None
              }

    return convertion


def parser_to_html_multiples_lines(lines, convertions_multiple_lines):
    convertion_started = False
    running_lines = 0
    # import pdb; pdb.set_trace()
    for index, convertion in enumerate(convertions_multiple_lines):
        if not convertion_started:
            lines.insert(
              convertion["number_line"] + running_lines,
              convertion["macro_element"]["html"]["tags"]["init"] +
              '\n'
            )
            convertion_started = True
            running_lines += 1

        next_convertion = dict(
          enumerate(convertions_multiple_lines)
          ).get(index + 1)
        # import pdb; pdb.set_trace()
        if convertion["macro_element"]["html"]["name"] == "p" and \
            next_convertion and \
                next_convertion["macro_element"]["html"]["name"] == "p":
            lines.insert(
              convertion["number_line"] + running_lines + 1,
              list(
                filter(
                  lambda element: element["html"]["name"] == "br",
                  database()["elements"]
                )
              )[0]["html"]["tags"]["init"] + '\n'
            )
            running_lines += 1

        if not next_convertion or \
            next_convertion["macro_element"]["html"]["name"] != \
            convertion["macro_element"]["html"]["name"] or \
            (
              next_convertion["macro_element"]["html"]["name"] ==
              convertion["macro_element"]["html"]["name"] and
              convertion["number_line"] + 1 != next_convertion["number_line"]):
            lines.insert(
              convertion["number_line"] + running_lines + 1,
              convertion["macro_element"]["html"]["tags"]["end"] +
              '\n'
            )
            convertion_started = False
            running_lines += 1

    return lines


def converter_markdown_in_content(content):
    import re

    string = content
    in_content_elements = filter(
            lambda element: element['markdown']["type"] == "in_content",
            database()["elements"]
          )

    for element in in_content_elements:
        match = re.search(element["markdown"]["code"], string)
        while match:
            string_init = string[:match.start()] if match.start() != 0 else ""
            string = string_init + \
                element["html"]["tags"]["init"] + \
                string[match.start() + 2: match.end() - 2] + \
                element["html"]["tags"]["end"] + \
                string[match.end():]

            match = re.search(element["markdown"]["code"], string)
    return string


def parser_to_html(string):

    types = database()["types"]
    string_parts = string.split(" ", 1)
    content = string
    convertions_queue = []

    for type in types:
        if type["name"] == "at_beginning":
            convertion = converter_markdown_at_beginning(string_parts[0])
            convertions_queue.append(convertion) if convertion else None
            # import pdb; pdb.set_trace()
            if len(convertions_queue) == 1 and \
                    convertions_queue[0]["element"]["html"]["name"] != "text":
                content = string_parts[1] if len(string_parts) > 1 else ""

        if content:
            if type["name"] == "in_content":
                content = converter_markdown_in_content(content)

    return converter_string_by_line(content, convertions_queue)


def markdown2html(markdown_file_path, html_file_path):

    converted_lines = []
    convertions_queue_multiples_lines = []
    number_line = 0

    file = open(markdown_file_path, "r")

    for line in file:
        if line != "\n":
            line_formattted = line.replace('\n', "")
            macro_element, html_parsed_line = parser_to_html(line_formattted)
            converted_lines.append(html_parsed_line)

            if macro_element:
                convertions_queue_multiples_lines.append(
                  {
                    "number_line": number_line,
                    "macro_element": macro_element
                  }
                )
            number_line += 1
    # import pdb; pdb.set_trace()
    if len(convertions_queue_multiples_lines) > 0:
        converted_lines = parser_to_html_multiples_lines(
          converted_lines,
          convertions_queue_multiples_lines
        )

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
