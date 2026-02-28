#!/bin/bash

# Get the absolute path to the system python3 where markdown-pdf is installed
PYTHON_PATH="/Library/Frameworks/Python.framework/Versions/3.11/bin/python3"

# Check if the python executable exists
if [ ! -f "$PYTHON_PATH" ]; then
    echo "Error: Python 3.11 environment not found at $PYTHON_PATH"
    echo "Please ensure the dependencies are installed correctly."
    exit 1
fi

echo "Generating PDF..."
"$PYTHON_PATH" generate_pdf.py

if [ $? -eq 0 ]; then
    echo "Done! You can find the PDF at assets/resume_leanlinmy.pdf."
else
    echo "An error occurred during PDF generation."
    exit 1
fi
