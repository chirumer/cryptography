#!/usr/bin/env python3
"""
Create an SVG with actual text elements overlaid on the original graphics.
This preserves all original paths and adds text on top.
"""

import csv
import re


def parse_ocr_data(tsv_file, confidence_threshold=40):
    """Parse OCR TSV and extract high-confidence text."""
    words = []

    with open(tsv_file, 'r') as f:
        reader = csv.DictReader(f, delimiter='\t')
        for row in reader:
            if row['level'] == '5' and row['text'].strip():
                try:
                    conf = float(row['conf'])
                    if conf >= confidence_threshold:
                        word_data = {
                            'text': row['text'].strip(),
                            'x': float(row['left']),
                            'y': float(row['top']),
                            'width': float(row['width']),
                            'height': float(row['height']),
                            'conf': conf
                        }
                        words.append(word_data)
                except (ValueError, KeyError):
                    continue

    return words


def create_svg_with_overlay(words, output_file, original_svg_file='img.svg'):
    """Create SVG with text overlaid on original."""

    # Read original SVG
    with open(original_svg_file, 'r') as f:
        original_content = f.read()

    # Get SVG dimensions from viewBox
    viewbox_match = re.search(r'viewBox="([^"]*)"', original_content)
    if viewbox_match:
        viewbox = viewbox_match.group(1).split()
        svg_width = float(viewbox[2])
        svg_height = float(viewbox[3])
    else:
        svg_width, svg_height = 7658.71, 4608.0

    # The PNG was rendered at 150 DPI, so we have a coordinate mapping
    # PNG coordinates to SVG coordinates (they should be roughly 1:1)

    # Create new SVG
    with open(output_file, 'w') as f:
        f.write('<?xml version="1.0" standalone="no"?>\n')
        f.write('<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 20010904//EN"\n')
        f.write(' "http://www.w3.org/TR/2001/REC-SVG-20010904/DTD/svg10.dtd">\n')
        f.write(f'<svg version="1.0" xmlns="http://www.w3.org/2000/svg"\n')
        f.write(f' width="{svg_width}pt" height="{svg_height}pt" ')
        f.write(f'viewBox="0 0 {svg_width} {svg_height}"\n')
        f.write(' preserveAspectRatio="xMidYMid meet">\n')

        f.write('<metadata>\n')
        f.write('Original traced paths with text overlay\n')
        f.write('</metadata>\n')

        # Include all original paths
        paths_match = re.search(r'(<g[^>]*>)(.*?)(</g>)', original_content, re.DOTALL)
        if paths_match:
            f.write(paths_match.group(1) + '\n')  # Opening <g> tag
            f.write(paths_match.group(2))  # All paths
            f.write(paths_match.group(3) + '\n')  # Closing </g> tag

        # Add text overlay with white background boxes
        f.write('\n<!-- Text Overlay -->\n')
        f.write('<g id="text-overlay">\n')

        for word in words:
            # Coordinates are already in SVG space (roughly 1:1 with PNG)
            x = word['x']
            y = word['y'] + word['height'] * 0.75  # Approximate baseline
            width = word['width']
            height = word['height']
            text = word['text']
            font_size = int(height * 0.7)

            # Escape XML
            text = text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')

            # Draw white background rectangle
            f.write(f'  <rect x="{x}" y="{word["y"]}" ')
            f.write(f'width="{width}" height="{height}" ')
            f.write(f'fill="white" fill-opacity="0.9"/>\n')

            # Draw text
            f.write(f'  <text x="{x}" y="{y}" ')
            f.write(f'font-family="Arial, Helvetica, sans-serif" ')
            f.write(f'font-size="{font_size}px" ')
            f.write(f'font-weight="normal" ')
            f.write(f'fill="black">')
            f.write(text)
            f.write('</text>\n')

        f.write('</g>\n')
        f.write('</svg>\n')


def main():
    """Main function."""
    print("Parsing OCR data (confidence >= 40)...")
    words = parse_ocr_data('ocr_output.tsv', confidence_threshold=40)
    print(f"Found {len(words)} high-confidence words\n")

    # Show detected text
    print("Detected text (sorted by position):")
    for word in sorted(words, key=lambda w: (w['y'], w['x'])):
        print(f"  '{word['text']:20s}' at ({word['x']:6.0f}, {word['y']:6.0f}) "
              f"size: {word['width']:4.0f}x{word['height']:3.0f} "
              f"conf: {word['conf']:.1f}%")

    print(f"\nCreating SVG with text overlay...")
    create_svg_with_overlay(words, 'img_with_text.svg')

    print(f"\n✓ Successfully created img_with_text.svg")
    print(f"  - Original paths preserved")
    print(f"  - {len(words)} text elements overlaid with white backgrounds")


if __name__ == '__main__':
    main()
