#!/usr/bin/env python3
"""
LaTeX to SVG Converter
Converts LaTeX equations from the equations folder to SVG images with transparent backgrounds.
"""

import os
import sys
import argparse
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend


class LatexToSVG:
    def __init__(self, equations_dir="equations", images_dir="images"):
        self.equations_dir = Path(equations_dir)
        self.images_dir = Path(images_dir)

        # Create directories if they don't exist
        self.equations_dir.mkdir(exist_ok=True)
        self.images_dir.mkdir(exist_ok=True)

        # Configure matplotlib for LaTeX rendering
        plt.rcParams.update({
            "text.usetex": True,
            "font.family": "serif",
            "font.size": 16,
            "text.latex.preamble": r"\usepackage{amsmath}\usepackage{amssymb}"
        })

    def read_latex_file(self, filepath):
        """Read LaTeX equation from file."""
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read().strip()
        return content

    def clean_latex_equation(self, latex_str):
        """
        Clean and prepare LaTeX equation for rendering.
        Removes or adjusts equation environments for matplotlib.
        """
        latex_str = latex_str.strip()

        # Remove equation environments but keep the content
        # matplotlib will handle the math mode
        replacements = [
            (r'\begin{equation*}', ''),
            (r'\end{equation*}', ''),
            (r'\begin{equation}', ''),
            (r'\end{equation}', ''),
            (r'\begin{align*}', ''),
            (r'\end{align*}', ''),
            (r'\begin{align}', ''),
            (r'\end{align}', ''),
            (r'\begin{aligned}', ''),
            (r'\end{aligned}', ''),
            (r'\begin{gathered}', ''),
            (r'\end{gathered}', ''),
            (r'\label{', r'%\label{'),  # Comment out labels
        ]

        for old, new in replacements:
            latex_str = latex_str.replace(old, new)

        return latex_str.strip()

    def latex_to_svg(self, latex_str, output_path, dpi=300):
        """
        Convert LaTeX equation to SVG with transparent background.

        Args:
            latex_str: LaTeX equation string
            output_path: Path where SVG will be saved
            dpi: Resolution for rendering (higher = better quality)
        """
        # Clean the LaTeX string
        latex_str = self.clean_latex_equation(latex_str)

        # Check if content has multiple lines (for term descriptions)
        lines = [l.strip() for l in latex_str.split('\\\\') if l.strip()]
        
        if len(lines) > 1:
            # Multi-line content: render each line separately
            fig_height = 0.5 + 0.4 * len(lines)
            fig = plt.figure(figsize=(12, fig_height))
            fig.patch.set_alpha(0.0)
            ax = fig.add_subplot(111)
            ax.axis('off')
            ax.set_alpha(0.0)
            
            # Position each line
            for i, line in enumerate(lines):
                line = line.strip().rstrip(',')
                if not line.startswith('$'):
                    line = f'${line}$'
                y_pos = 1 - (i + 0.5) / len(lines)
                ax.text(0.0, y_pos, line,
                        horizontalalignment='left',
                        verticalalignment='center',
                        fontsize=16,
                        transform=ax.transAxes)
        else:
            # Single line: original behavior
            if not latex_str.startswith('$'):
                latex_str = f'${latex_str}$'

            fig = plt.figure(figsize=(10, 2))
            fig.patch.set_alpha(0.0)
            ax = fig.add_subplot(111)
            ax.axis('off')
            ax.set_alpha(0.0)

            ax.text(0.5, 0.5, latex_str,
                    horizontalalignment='center',
                    verticalalignment='center',
                    fontsize=20,
                    transform=ax.transAxes)

        # Save as SVG with tight bounding box
        plt.savefig(output_path,
                   format='svg',
                   bbox_inches='tight',
                   pad_inches=0.1,
                   transparent=True,
                   dpi=dpi)
        plt.close(fig)

        print(f"✓ Created: {output_path}")

    def convert_file(self, input_file, output_name=None):
        """
        Convert a single LaTeX file to SVG.

        Args:
            input_file: Path to input .tex file
            output_name: Optional custom output name (without extension)
        """
        input_path = Path(input_file)

        if not input_path.exists():
            print(f"✗ Error: File not found: {input_path}")
            return False

        # Read LaTeX content
        try:
            latex_content = self.read_latex_file(input_path)
        except Exception as e:
            print(f"✗ Error reading {input_path}: {e}")
            return False

        # Determine output filename
        if output_name is None:
            output_name = input_path.stem

        output_path = self.images_dir / f"{output_name}.svg"

        # Convert to SVG
        try:
            self.latex_to_svg(latex_content, output_path)
            return True
        except Exception as e:
            print(f"✗ Error converting {input_path}: {e}")
            return False

    def convert_all(self):
        """Convert all .tex files in the equations directory."""
        tex_files = list(self.equations_dir.glob("*.tex"))

        if not tex_files:
            print(f"No .tex files found in {self.equations_dir}")
            return

        print(f"Found {len(tex_files)} LaTeX file(s)")
        print("-" * 50)

        success_count = 0
        for tex_file in tex_files:
            if self.convert_file(tex_file):
                success_count += 1

        print("-" * 50)
        print(f"Successfully converted {success_count}/{len(tex_files)} file(s)")


def main():
    parser = argparse.ArgumentParser(
        description="Convert LaTeX equations to SVG images with transparent backgrounds"
    )
    parser.add_argument(
        '-f', '--file',
        help='Specific .tex file to convert',
        type=str
    )
    parser.add_argument(
        '-o', '--output',
        help='Output filename (without extension)',
        type=str
    )
    parser.add_argument(
        '-e', '--equations-dir',
        help='Directory containing equation files (default: equations)',
        default='equations',
        type=str
    )
    parser.add_argument(
        '-i', '--images-dir',
        help='Directory for output images (default: images)',
        default='images',
        type=str
    )

    args = parser.parse_args()

    # Create converter instance
    converter = LatexToSVG(args.equations_dir, args.images_dir)

    # Convert specific file or all files
    if args.file:
        converter.convert_file(args.file, args.output)
    else:
        converter.convert_all()


if __name__ == "__main__":
    main()
