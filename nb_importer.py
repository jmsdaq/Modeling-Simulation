# nb_importer.py

import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from nbconvert import PythonExporter

def load_notebook(notebook_path):
    with open(notebook_path, "r", encoding="utf-8") as notebook_file:
        notebook_content = notebook_file.read()

    notebook = nbformat.reads(notebook_content, as_version=4)

    execute_preprocessor = ExecutePreprocessor(timeout=-1, kernel_name='python3')
    execute_preprocessor.preprocess(notebook, {"metadata": {"path": "./"}})

    python_exporter = PythonExporter()
    (python_code, resources) = python_exporter.from_notebook_node(notebook)

    exec(python_code, globals())
    
    return globals()
