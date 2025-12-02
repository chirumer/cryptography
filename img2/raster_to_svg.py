import subprocess
import os
import re
import xml.etree.ElementTree as ET

def run_command(command):
    print(f"Running: {command}")
    subprocess.run(command, shell=True, check=True)

def main():
    input_file = "img.png"
    pnm_file = "temp.pnm"
    pbm_file = "temp.pbm"
    temp_svg = "temp.svg"
    final_output = "final_output.svg"
    bg_color = "#BDDDFC"

    # Step 1: Convert to PNM
    run_command(f"convert '{input_file}' '{pnm_file}'")

    # Step 2: Preprocess with mkbitmap
    # Using the smoothing parameters defined earlier
    run_command(f"mkbitmap -s 3 -b 1 -t 0.45 -f 4 '{pnm_file}' -o '{pbm_file}'")

    # Step 3: Trace with potrace
    run_command(f"potrace -s --tight -t 5 --alphamax 1.2 '{pbm_file}' -o '{temp_svg}'")

    # Step 4: Build the final SVG incrementally
    print("Building final SVG...")
    
    # Parse the temp SVG to get dimensions and paths
    tree = ET.parse(temp_svg)
    root = tree.getroot()
    
    # Namespace handling for SVG
    ns = {'svg': 'http://www.w3.org/2000/svg'}
    
    width = root.attrib.get('width')
    height = root.attrib.get('height')
    viewBox = root.attrib.get('viewBox')
    
    # Start building the new SVG content
    svg_lines = []
    svg_lines.append('<?xml version="1.0" standalone="no"?>')
    svg_lines.append('<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 20010904//EN"')
    svg_lines.append(' "http://www.w3.org/TR/2001/REC-SVG-20010904/DTD/svg10.dtd">')
    svg_lines.append(f'<svg version="1.0" xmlns="http://www.w3.org/2000/svg"')
    svg_lines.append(f' width="{width}" height="{height}" viewBox="{viewBox}"')
    svg_lines.append(' preserveAspectRatio="xMidYMid meet">')
    
    # Add background color
    svg_lines.append(f'<rect width="100%" height="100%" fill="{bg_color}"/>')
    
    # Extract and add paths
    # Potrace usually puts paths in a group with a transform
    # We will copy the group structure or just the paths if they are direct children
    # But usually potrace output structure is: <svg><g transform...> <path .../></g></svg>
    
    for group in root.findall('.//{http://www.w3.org/2000/svg}g'):
        transform = group.attrib.get('transform', '')
        svg_lines.append(f'<g transform="{transform}" fill="black" stroke="none">')
        
        for path in group.findall('{http://www.w3.org/2000/svg}path'):
            d = path.attrib.get('d')
            svg_lines.append(f'<path d="{d}"/>')
            
        svg_lines.append('</g>')

    svg_lines.append('</svg>')
    
    # Write final output
    with open(final_output, 'w') as f:
        f.write('\n'.join(svg_lines))
        
    print(f"Successfully created {final_output}")

    # Cleanup
    for f in [pnm_file, pbm_file, temp_svg]:
        if os.path.exists(f):
            os.remove(f)

if __name__ == "__main__":
    main()
