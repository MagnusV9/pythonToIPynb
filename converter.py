import sys
import re
import nbformat
from nbformat.v4 import new_code_cell, new_markdown_cell, new_notebook

def convert_to_ipynb(py_file, ipynb_file):
    with open(py_file, 'r') as f:
        content = f.read()

    # Split the content using triple quotes
    blocks = re.split("'''", content)

    # Create a new Jupyter Notebook
    nb = new_notebook()

    # Iterate through the blocks, adding either Markdown or code cells
    for i, block in enumerate(blocks):
        if i % 2 == 0:  # Code block
            if block.strip():
                nb.cells.append(new_code_cell(block.strip()))
        else:  # Markdown block
            if block.strip():
                nb.cells.append(new_markdown_cell(block.strip()))

    # Save the Jupyter Notebook
    with open(ipynb_file, 'w') as f:
        nbformat.write(nb, f)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: python convert_to_ipynb.py input.py output.ipynb')
        sys.exit(1)

    py_file = sys.argv[1]
    ipynb_file = sys.argv[2]

    convert_to_ipynb(py_file, ipynb_file)


