import xml.etree.ElementTree as ET

def create_generator_script():
    input_svg = "img.svg"
    output_script = "generate_svg.py"
    
    tree = ET.parse(input_svg)
    root = tree.getroot()
    
    width = root.attrib.get('width')
    height = root.attrib.get('height')
    viewBox = root.attrib.get('viewBox')
    
    # Extract paths and transforms
    paths_data = []
    
    # Namespace handling
    ns = {'svg': 'http://www.w3.org/2000/svg'}
    
    for group in root.findall('.//{http://www.w3.org/2000/svg}g'):
        transform = group.attrib.get('transform', '')
        group_paths = []
        for path in group.findall('{http://www.w3.org/2000/svg}path'):
            d = path.attrib.get('d')
            group_paths.append(d)
        if group_paths:
            paths_data.append({'transform': transform, 'paths': group_paths})
            
    # Generate the script content
    script_content = f"""import os

def generate_svg():
    output_file = "recreated.svg"
    width = "{width}"
    height = "{height}"
    viewBox = "{viewBox}"
    
    # Embedded path data
    groups = {paths_data}
    
    svg_content = []
    svg_content.append('<?xml version="1.0" standalone="no"?>')
    svg_content.append('<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 20010904//EN"')
    svg_content.append(' "http://www.w3.org/TR/2001/REC-SVG-20010904/DTD/svg10.dtd">')
    svg_content.append(f'<svg version="1.0" xmlns="http://www.w3.org/2000/svg"')
    svg_content.append(f' width="{{width}}" height="{{height}}" viewBox="{{viewBox}}"')
    svg_content.append(' preserveAspectRatio="xMidYMid meet">')
    
    # Note: Background is transparent (no rect added)
    
    for group in groups:
        transform = group['transform']
        svg_content.append(f'<g transform="{{transform}}" fill="#000000" stroke="none">')
        for d in group['paths']:
            svg_content.append(f'<path d="{{d}}"/>')
        svg_content.append('</g>')
        
    svg_content.append('</svg>')
    
    with open(output_file, 'w') as f:
        f.write('\\n'.join(svg_content))
        
    print(f"Successfully created {{output_file}} from scratch.")

if __name__ == "__main__":
    generate_svg()
"""

    with open(output_script, 'w') as f:
        f.write(script_content)
    print(f"Generated {output_script}")

if __name__ == "__main__":
    create_generator_script()
