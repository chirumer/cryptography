#!/usr/bin/env python3
"""
Convert path-based text in SVG to actual text elements while preserving graphics.
Uses OCR results to identify text regions and keeps non-text paths.
"""

import csv
import re
import xml.etree.ElementTree as ET


def parse_ocr_data(tsv_file, confidence_threshold=20):
    """Parse OCR TSV output and extract text with positions."""
    words = []

    with open(tsv_file, 'r') as f:
        reader = csv.DictReader(f, delimiter='\t')
        for row in reader:
            # Only process word-level entries (level 5)
            if row['level'] == '5' and row['text'].strip():
                try:
                    conf = float(row['conf'])
                    if conf >= confidence_threshold:
                        word_data = {
                            'text': row['text'].strip(),
                            'x': int(row['left']),
                            'y': int(row['top']),
                            'width': int(row['width']),
                            'height': int(row['height']),
                            'conf': conf
                        }
                        words.append(word_data)
                except (ValueError, KeyError):
                    continue

    return words


def parse_path_bounds(path_d):
    """Extract rough bounding box from path data."""
    # Extract all numbers from the path
    numbers = re.findall(r'-?\d+\.?\d*', path_d)
    if not numbers:
        return None

    coords = [float(n) for n in numbers]
    if len(coords) < 2:
        return None

    # Get x and y coordinates (every pair)
    x_coords = coords[0::2]
    y_coords = coords[1::2]

    return {
        'min_x': min(x_coords),
        'max_x': max(x_coords),
        'min_y': min(y_coords),
        'max_y': max(y_coords)
    }


def boxes_overlap(box1, box2, tolerance=50):
    """Check if two bounding boxes overlap with some tolerance."""
    # Add tolerance to text boxes to account for OCR inaccuracies
    return not (box1['max_x'] + tolerance < box2['min_x'] or
                box2['max_x'] + tolerance < box1['min_x'] or
                box1['max_y'] + tolerance < box2['min_y'] or
                box2['max_y'] + tolerance < box1['min_y'])


def convert_word_to_bbox(word):
    """Convert OCR word data to bounding box format."""
    return {
        'min_x': word['x'],
        'max_x': word['x'] + word['width'],
        'min_y': word['y'],
        'max_y': word['y'] + word['height']
    }


def estimate_font_size(height):
    """Estimate font size from text height."""
    return int(height * 0.75)


def create_svg_with_text(words, output_file, original_svg_file='img.svg'):
    """Create SVG with text elements and preserved graphic paths."""

    # Read original SVG
    with open(original_svg_file, 'r') as f:
        content = f.read()

    # Parse the original SVG
    # Extract header
    header_match = re.search(r'<\?xml.*?\?>\s*<!DOCTYPE.*?>\s*<svg[^>]*>\s*<metadata>.*?</metadata>\s*<g[^>]*>',
                             content, re.DOTALL)
    header = header_match.group(0) if header_match else ''

    # Extract paths
    paths = re.findall(r'<path d="([^"]*)"[^/]*/>', content)

    # Convert OCR words to bounding boxes
    text_boxes = [convert_word_to_bbox(w) for w in words]

    # Identify which paths are text (overlap with OCR detections)
    graphic_paths = []
    text_paths = []

    print(f"Analyzing {len(paths)} paths...")
    for path_d in paths:
        path_box = parse_path_bounds(path_d)
        if not path_box:
            graphic_paths.append(path_d)
            continue

        # Check if this path overlaps with any text region
        is_text = False
        for text_box in text_boxes:
            if boxes_overlap(path_box, text_box):
                is_text = True
                break

        if is_text:
            text_paths.append(path_d)
        else:
            graphic_paths.append(path_d)

    print(f"  Identified {len(text_paths)} text paths")
    print(f"  Identified {len(graphic_paths)} graphic paths")

    # Create new SVG
    with open(output_file, 'w') as f:
        f.write('<?xml version="1.0" standalone="no"?>\n')
        f.write('<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 20010904//EN"\n')
        f.write(' "http://www.w3.org/TR/2001/REC-SVG-20010904/DTD/svg10.dtd">\n')

        # Extract SVG attributes
        svg_match = re.search(r'<svg([^>]*)>', content, re.DOTALL)
        svg_attrs = svg_match.group(1).strip() if svg_match else ''
        f.write(f'<svg {svg_attrs}>\n')

        f.write('<metadata>\n')
        f.write('Converted from path-based text to actual text elements\n')
        f.write('</metadata>\n')

        # Extract g attributes
        g_match = re.search(r'<g\s+([^>]*)>', content)
        g_attrs = g_match.group(1).strip() if g_match else ''
        f.write(f'<g {g_attrs}>\n')

        # Write graphic paths (non-text)
        for path_d in graphic_paths:
            f.write(f'<path d="{path_d}"/>\n')

        f.write('</g>\n')

        # Add text layer on top
        f.write('<g id="text-layer" transform="translate(-488.180402,4608.000019) scale(0.100000,-0.100000)">\n')

        for word in words:
            x = word['x']
            y = word['y'] + word['height']
            text = word['text']
            font_size = estimate_font_size(word['height'])

            # Escape XML
            text = text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

            f.write(f'  <text x="{x}" y="{y}" ')
            f.write(f'font-family="Arial, Helvetica, sans-serif" ')
            f.write(f'font-size="{font_size}" ')
            f.write(f'fill="black">')
            f.write(text)
            f.write('</text>\n')

        f.write('</g>\n')
        f.write('</svg>\n')


def main():
    """Main function."""
    print("Parsing OCR data...")
    words = parse_ocr_data('ocr_output.tsv', confidence_threshold=20)
    print(f"Found {len(words)} words with confidence >= 20\n")

    # Show detected text
    print("Detected text:")
    for word in sorted(words, key=lambda w: (w['y'], w['x'])):
        print(f"  '{word['text']}' at ({word['x']}, {word['y']}) "
              f"size: {word['width']}x{word['height']} "
              f"conf: {word['conf']:.1f}")

    print(f"\nCreating SVG with text elements...")
    create_svg_with_text(words, 'img_with_text.svg')

    print(f"\n✓ Successfully created img_with_text.svg")


if __name__ == '__main__':
    main()
