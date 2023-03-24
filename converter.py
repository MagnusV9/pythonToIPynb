import sys
import nbformat
from nbformat.v4 import new_code_cell, new_notebook

def convert_to_ipynb(py_file, ipynb_file):
    with open(py_file, 'r') as f:
        content = f.read()

    # Split the Python file into a list of code blocks
    code_blocks = content.split('\n\n')

    # Create a new Jupyter Notebook and add code cells
    nb = new_notebook()
    for block in code_blocks:
        nb.cells.append(new_code_cell(block))

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

