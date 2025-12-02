#!/usr/bin/env python3
"""
Convert path-based text in SVG to actual text elements.
Uses OCR results to identify and replace text paths with <text> elements.
"""

import csv
import re


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
                    # Filter out low-confidence detections
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


def group_words_into_lines(words, line_height_tolerance=50):
    """Group words that are on the same line."""
    if not words:
        return []

    # Sort by y position
    words_sorted = sorted(words, key=lambda w: w['y'])

    lines = []
    current_line = [words_sorted[0]]

    for word in words_sorted[1:]:
        # Check if word is on the same line as current_line
        avg_y = sum(w['y'] for w in current_line) / len(current_line)
        if abs(word['y'] - avg_y) < line_height_tolerance:
            current_line.append(word)
        else:
            # Sort current line by x position
            current_line.sort(key=lambda w: w['x'])
            lines.append(current_line)
            current_line = [word]

    # Add the last line
    if current_line:
        current_line.sort(key=lambda w: w['x'])
        lines.append(current_line)

    return lines


def estimate_font_size(height):
    """Estimate font size from text height in pixels."""
    # Rough approximation: height in pixels ≈ font size in points
    # Adjust by a factor since OCR bounding boxes may be larger
    return int(height * 0.75)


def create_svg_with_text(words, output_file, original_svg_file='img.svg'):
    """Create a new SVG with text elements instead of path-based text."""

    # Read the original SVG header
    with open(original_svg_file, 'r') as f:
        content = f.read()

    # Extract SVG attributes
    svg_match = re.search(r'<svg([^>]*)>', content, re.DOTALL)
    svg_attrs = svg_match.group(1).strip() if svg_match else ''

    # Group words into lines for better spacing
    lines = group_words_into_lines(words)

    # Create new SVG
    with open(output_file, 'w') as f:
        f.write('<?xml version="1.0" standalone="no"?>\n')
        f.write('<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 20010904//EN"\n')
        f.write(' "http://www.w3.org/TR/2001/REC-SVG-20010904/DTD/svg10.dtd">\n')
        f.write(f'<svg {svg_attrs}>\n')
        f.write('<metadata>\n')
        f.write('Converted from path-based text to actual text elements\n')
        f.write('</metadata>\n')

        # Add a white background
        f.write('<rect width="100%" height="100%" fill="white"/>\n')

        # Add all the text elements
        f.write('<g id="text-layer">\n')

        for line in lines:
            for word in line:
                x = word['x']
                y = word['y'] + word['height']  # Baseline is at bottom of bounding box
                text = word['text']
                font_size = estimate_font_size(word['height'])

                # Escape special XML characters
                text = text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

                f.write(f'  <text x="{x}" y="{y}" ')
                f.write(f'font-family="Arial, sans-serif" ')
                f.write(f'font-size="{font_size}" ')
                f.write(f'fill="black">')
                f.write(text)
                f.write('</text>\n')

        f.write('</g>\n')

        # Add any non-text paths (graphic elements like arrows, boxes, etc.)
        # For now, we'll just close the SVG
        # In a more sophisticated version, we'd identify and keep graphic paths

        f.write('</svg>\n')


def main():
    """Main function."""
    print("Parsing OCR data...")
    words = parse_ocr_data('ocr_output.tsv', confidence_threshold=20)
    print(f"Found {len(words)} words with confidence >= 20")

    # Show some detected text
    print("\nDetected text (sample):")
    for word in words[:10]:
        print(f"  '{word['text']}' at ({word['x']}, {word['y']}) "
              f"size: {word['width']}x{word['height']} "
              f"conf: {word['conf']:.1f}")

    print(f"\nCreating SVG with text elements...")
    create_svg_with_text(words, 'img_with_text.svg')

    print(f"✓ Successfully created img_with_text.svg")
    print(f"  Total text elements: {len(words)}")


if __name__ == '__main__':
    main()
