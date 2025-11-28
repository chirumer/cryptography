# LaTeX to SVG Converter

A Python utility that converts LaTeX equations to SVG images with transparent backgrounds.

## Features

- Converts LaTeX equations to high-quality SVG images
- Transparent background for easy integration
- Batch processing of multiple equation files
- Support for common LaTeX math environments (equation, align, etc.)
- Configurable output directories

## Installation

1. Create a virtual environment (recommended):
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## System Requirements

This script requires LaTeX to be installed on your system for rendering equations:

- **macOS**: `brew install --cask mactex` or `brew install basictex`
- **Ubuntu/Debian**: `sudo apt-get install texlive-latex-base texlive-latex-extra`
- **Windows**: Install [MiKTeX](https://miktex.org/) or [TeX Live](https://www.tug.org/texlive/)

## Usage

### Basic Usage

Convert all `.tex` files in the `equations` folder:

```bash
python3 latex_to_svg.py
```

### Convert a Specific File

```bash
python3 latex_to_svg.py -f equations/differential_privacy.tex
```

### Custom Output Name

```bash
python3 latex_to_svg.py -f equations/my_equation.tex -o custom_name
```

### Custom Directories

```bash
python3 latex_to_svg.py -e path/to/equations -i path/to/images
```

## Command-Line Options

- `-f, --file`: Specific .tex file to convert
- `-o, --output`: Output filename (without extension)
- `-e, --equations-dir`: Directory containing equation files (default: equations)
- `-i, --images-dir`: Directory for output images (default: images)
- `-h, --help`: Show help message

## Input Format

Create `.tex` files in the `equations` folder with your LaTeX equations. The script supports various LaTeX math environments:

### Example 1: Differential Privacy
```latex
\begin{equation*}
    Pr[\mathcal{M}(x) \in \mathcal{S}] \leq e^\epsilon Pr[\mathcal{M}(y) \in \mathcal{S}] + \delta
\end{equation*}
```

### Example 2: Simple Equation
```latex
E = mc^2
```

### Example 3: Aligned Equations
```latex
\begin{align*}
    f(x) &= x^2 + 2x + 1 \\
    &= (x + 1)^2
\end{align*}
```

## Project Structure

```
latex_to_img/
├── equations/          # Place your .tex files here
│   └── differential_privacy.tex
├── images/            # SVG output files appear here
│   └── differential_privacy.svg
├── latex_to_svg.py    # Main converter script
├── requirements.txt   # Python dependencies
└── README.md         # This file
```

## Output

The script generates SVG files with:
- Transparent backgrounds
- High resolution (300 DPI)
- Tight bounding boxes
- Professional math typesetting using LaTeX

## Troubleshooting

### LaTeX Not Found Error

If you get an error about LaTeX not being found, ensure that:
1. LaTeX is installed on your system
2. The LaTeX binaries are in your PATH

### Font Issues

If equations don't render properly, try installing additional LaTeX packages:
```bash
# macOS
sudo tlmgr install amsmath amssymb

# Ubuntu/Debian
sudo apt-get install texlive-fonts-recommended texlive-fonts-extra
```

### Permission Errors

Make sure the script has execute permissions:
```bash
chmod +x latex_to_svg.py
```

## Examples

See the `equations/differential_privacy.tex` file for a working example of the differential privacy equation.

## License

Free to use for any purpose.
