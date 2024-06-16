# Python to IPython Notebook Converter

![Python to IPython Notebook](https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExZm5qdmljZXc0bG91YW00aTA1ZWsybjNwY3UzZW85c3QwZTFkdWE0ZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/QfHVl7Zd1ZgDosoIjc/giphy.webp)

This Python script converts a `.py` file into a Jupyter Notebook (`.ipynb`) file. It splits the Python script into code and markdown cells based on triple quotes (`'''`), where content inside triple quotes is treated as markdown and the rest as code.

## Features

- **Code Blocks**: Python code blocks are directly converted to code cells in the notebook.
- **Markdown Blocks**: Text inside triple quotes is converted to markdown cells.

## Prerequisites

- Python 3.x

You can install the necessary dependencies by using pip the following way:  

```sh
pip install -r requirements.txt
```
## Acknowledgments
The nbformat library for providing the tools necessary to create and manipulate Jupyter Notebooks.
