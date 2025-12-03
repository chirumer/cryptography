import re

svg_file = "img.svg"
color = "#BDDDFC"

with open(svg_file, "r") as f:
    content = f.read()

# Find the end of the opening <svg> tag
match = re.search(r'<svg[^>]*>', content)
if match:
    insert_pos = match.end()
    # Create the rect element. Using 100% width/height to cover the viewBox.
    rect = f'\n<rect width="100%" height="100%" fill="{color}"/>'
    
    new_content = content[:insert_pos] + rect + content[insert_pos:]
    
    with open(svg_file, "w") as f:
        f.write(new_content)
    print(f"Added background {color} to {svg_file}")
else:
    print("Could not find <svg> tag")
