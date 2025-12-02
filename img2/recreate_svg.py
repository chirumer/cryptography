#!/usr/bin/env python3
"""
Modular script to recreate img.svg.
Uses SVGGenerator class and separated data.
"""

from svg_data import PATH_DATA

class SVGGenerator:
    def __init__(self, width="7658.710196pt", height="4608.000019pt", viewBox="0 0 7658.710196 4608.000019"):
        self.width = width
        self.height = height
        self.viewBox = viewBox
        self.paths = []
        self.texts = []
        
    def add_path(self, d_data, fill=None, stroke=None):
        self.paths.append({
            'd': d_data,
            'fill': fill,
            'stroke': stroke
        })

    def add_text(self, text, x, y, font_size, font_family="Arial", fill="black", text_anchor="middle", font_weight="normal", dominant_baseline="auto"):
        self.texts.append({
            'text': text,
            'x': x,
            'y': y,
            'font_size': font_size,
            'font_family': font_family,
            'fill': fill,
            'text_anchor': text_anchor,
            'font_weight': font_weight,
            'dominant_baseline': dominant_baseline
        })
        
    def generate(self):
        header = f'''<?xml version="1.0" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 20010904//EN"
 "http://www.w3.org/TR/2001/REC-SVG-20010904/DTD/svg10.dtd">
<svg version="1.0" xmlns="http://www.w3.org/2000/svg"
 width="{self.width}" height="{self.height}" viewBox="{self.viewBox}"
 preserveAspectRatio="xMidYMid meet">
<metadata>
Created by potrace 1.16, written by Peter Selinger 2001-2019
</metadata>
<g transform="translate(-488.180402,4608.000019) scale(0.100000,-0.100000)"
fill="#000000" stroke="none">
'''
        
        body = ""
        for p in self.paths:
            # If we wanted to support custom fill/stroke per path, we could add attributes here.
            # For now, the group has the fill/stroke.
            body += f'<path d="{p["d"]}"/>\n'
            
        group_end = '''</g>
'''
        
        text_elements = ""
        for t in self.texts:
            text_elements += f'<text x="{t["x"]}" y="{t["y"]}" font-size="{t["font_size"]}" font-family="{t["font_family"]}" fill="{t["fill"]}" text-anchor="{t["text_anchor"]}" font-weight="{t["font_weight"]}" dominant-baseline="{t["dominant_baseline"]}">{t["text"]}</text>\n'

        footer = '''</svg>
'''
        return header + body + group_end + text_elements + footer
        
    def save(self, filename):
        content = self.generate()
        with open(filename, 'w') as f:
            f.write(content)
        print(f"Saved SVG to {filename}")

def main():
    # Initialize generator with dimensions from original file
    svg_gen = SVGGenerator()
    
    # Indices of paths that correspond to the text we want to replace
    # "Honest User" and "MGA Attacker"
    # Also removing the empty arrow at index 139
    # Also removing "Target A" box and text (indices 26, 29, 41-46)
    # Note: Index 30 was previously removed but it belongs to Target C, so we keep it.
    text_path_indices = set(range(2, 23)) # 2 to 22 inclusive
    text_path_indices.add(139)
    text_path_indices.update([26, 29, 41, 42, 43, 44, 45, 46])
    
    # Add all paths from the data module, skipping the text paths
    for i, d in enumerate(PATH_DATA):
        if i not in text_path_indices:
            svg_gen.add_path(d)
            
    # Add the text elements
    # Coordinates derived from OCR bounding boxes
    # "Honest User": x=1609.5, y=376
    # "MGA Attacker": x=5868.5, y=369.5
    # Font size estimated around 230 based on bbox height
    
    svg_gen.add_text("Honest User", 1609.5, 376, 230, font_family="Arial", fill="black", font_weight="bold", dominant_baseline="middle")
    svg_gen.add_text("MGA Attacker", 5868.5, 369.5, 230, font_family="Arial", fill="black", font_weight="bold", dominant_baseline="middle")
        
    # Generate the file
    svg_gen.save('img_recreated.svg')

if __name__ == '__main__':
    main()
