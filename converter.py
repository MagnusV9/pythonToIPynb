import sys
import re
import nbformat
from nbformat.v4 import new_code_cell, new_markdown_cell, new_notebook

def convert_to_ipynb(py_file, ipynb_file):
    with open(py_file, 'r') as f:
        content = f.read()

    # Split the content using triple quotes also making sure that first line is a code block
    blocks = re.split("'''", content)
    
    nb = new_notebook()

    for i, block in enumerate(blocks):
        if i % 2 == 0:  # Code block
            if block.strip():
                nb.cells.append(new_code_cell(block.strip()))
        else:  # Markdown block
            if block.strip():
                nb.cells.append(new_markdown_cell(block.strip()))

    with open(ipynb_file, 'w') as f:
        nbformat.write(nb, f)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('you need to pass the correct amount of arguments\nexample: python3 path/to/python/file path/to/ipynb/file')
        sys.exit(1)

    py_file = sys.argv[1]
    ipynb_file = sys.argv[2]

    convert_to_ipynb(py_file, ipynb_file)


