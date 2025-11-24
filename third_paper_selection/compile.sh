#!/bin/bash

# Script to compile LaTeX to PDF
# Usage: ./compile.sh

echo "Compiling paper_comparison.tex to PDF..."

# Run pdflatex twice to resolve references
pdflatex -interaction=nonstopmode paper_comparison.tex
pdflatex -interaction=nonstopmode paper_comparison.tex

# Clean up auxiliary files
echo "Cleaning up auxiliary files..."
rm -f *.aux *.log *.out *.toc

echo "Compilation complete! Output: paper_comparison.pdf"
