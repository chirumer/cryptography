import os
import subprocess

class SVGBuilder:
    # Layout constants
    BAR_TEXT_SPACING = 20  # Y: Gap between bar end and text label
    BOX_PADDING = 20       # X: Padding around content boxes
    
    def __init__(self, width=800, height=600):
        self.width = width
        self.height = height
        self.elements = []
        self.defs = []
        self._add_default_defs()

    def _add_default_defs(self):
        style = """
      @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&amp;display=swap');
      text { font-family: 'Roboto', sans-serif; fill: #1E3A5F; }
      .title { font-size: 24px; font-weight: bold; text-anchor: middle; fill: #0D2847; }
      .subtitle { font-size: 14px; text-anchor: middle; fill: #546E7A; }
      .label { font-size: 14px; text-anchor: middle; }
      .label-left { font-size: 14px; text-anchor: start; }
      /* White background for boxes to pop against colored slide */
      .box { fill: #FFFFFF; stroke: #2C5F8D; stroke-width: 3; rx: 10; ry: 10; }
      .group-box { fill: #FFFFFF; stroke: #2C5F8D; stroke-width: 2; stroke-dasharray: 5,5; rx: 10; ry: 10; }
      .arrow { stroke: #2C5F8D; stroke-width: 2; fill: none; marker-end: url(#arrowhead); }
      .emoji { font-size: 30px; text-anchor: middle; }
      .bar-red { fill: #C07864; } /* Matches Attackers icon color */
      .bar-gray { fill: #B0BEC5; } /* Neutral Blue-Gray */
        """
        self.defs.append(f"<style>{style}</style>")
        
        marker = """
    <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#2C5F8D" />
    </marker>
        """
        self.defs.append(marker)

    def _get_icon_chart(self, x, y, width, height, fill):
        """Returns inline SVG for chart icon"""
        scale = width / 512
        return f'<g transform="translate({x},{y}) scale({scale})"><path fill="{fill}" d="M32 32c17.7 0 32 14.3 32 32V400c0 8.8 7.2 16 16 16H480c17.7 0 32 14.3 32 32s-14.3 32-32 32H80c-44.2 0-80-35.8-80-80V64C0 46.3 14.3 32 32 32zM160 224c17.7 0 32 14.3 32 32v64c0 17.7-14.3 32-32 32s-32-14.3-32-32V256c0-17.7 14.3-32 32-32zm128-64V320c0 17.7-14.3 32-32 32s-32-14.3-32-32V160c0-17.7 14.3-32 32-32s32 14.3 32 32zm64 32c17.7 0 32 14.3 32 32v96c0 17.7-14.3 32-32 32s-32-14.3-32-32V224c0-17.7 14.3-32 32-32zM480 96V320c0 17.7-14.3 32-32 32s-32-14.3-32-32V96c0-17.7 14.3-32 32-32s32 14.3 32 32z"/></g>'
    
    def _get_icon_warning(self, x, y, width, height, fill):
        """Returns inline SVG for warning icon"""
        scale = width / 512
        return f'<g transform="translate({x},{y}) scale({scale})"><path fill="{fill}" d="M256 32c14.2 0 27.3 7.5 34.5 19.8l216 368c7.3 12.4 7.3 27.7 .2 40.1S486.3 480 472 480H40c-14.3 0-27.6-7.7-34.7-20.1s-7-27.8 .2-40.1l216-368C228.7 39.5 241.8 32 256 32zm0 128c-13.3 0-24 10.7-24 24V296c0 13.3 10.7 24 24 24s24-10.7 24-24V184c0-13.3-10.7-24-24-24zm32 224a32 32 0 1 0 -64 0 32 32 0 1 0 64 0z"/></g>'
    
    def _get_icon_check(self, x, y, width, height, fill):
        """Returns inline SVG for check icon"""
        scale = width / 512
        return f'<g transform="translate({x},{y}) scale({scale})"><path fill="{fill}" d="M256 512A256 256 0 1 0 256 0a256 256 0 1 0 0 512zM369 209L241 337c-9.4 9.4-24.6 9.4-33.9 0l-64-64c-9.4-9.4-9.4-24.6 0-33.9s24.6-9.4 33.9 0l47 47L335 175c9.4-9.4 24.6-9.4 33.9 0s9.4 24.6 0 33.9z"/></g>'
    
    def _get_icon_document(self, x, y, width, height, fill):
        """Returns inline SVG for document icon"""
        scale = width / 512
        return f'<g transform="translate({x},{y}) scale({scale})"><path fill="{fill}" d="M64 0C28.7 0 0 28.7 0 64V448c0 35.3 28.7 64 64 64H320c35.3 0 64-28.7 64-64V160H256c-17.7 0-32-14.3-32-32V0H64zM256 0V128H384L256 0zM112 256H272c8.8 0 16 7.2 16 16s-7.2 16-16 16H112c-8.8 0-16-7.2-16-16s7.2-16 16-16zm0 64H272c8.8 0 16 7.2 16 16s-7.2 16-16 16H112c-8.8 0-16-7.2-16-16s7.2-16 16-16zm0 64H272c8.8 0 16 7.2 16 16s-7.2 16-16 16H112c-8.8 0-16-7.2-16-16s7.2-16 16-16z"/></g>'


    def add_background(self, color="none"):
        self.elements.append(f'<rect width="100%" height="100%" fill="{color}" />')

    def add_title(self, text, x=400, y=40):
        self.elements.append(f'<text x="{x}" y="{y}" class="title">{text}</text>')

    def add_regular_users(self, x=150, y=200):
        content = f"""
    <!-- Group Box -->
    <rect x="-100" y="-60" width="200" height="120" class="group-box" />
    
    <text x="0" y="-30" class="label" font-weight="bold">Regular Users</text>
    <text x="0" y="-10" class="subtitle">(Honest Data)</text>
    {self._get_icon_chart(-70, 10, 20, 20, "#2C5F8D")}
    {self._get_icon_check(-30, 10, 20, 20, "#2C5F8D")}
    {self._get_icon_document(10, 10, 20, 20, "#2C5F8D")}
    {self._get_icon_chart(50, 10, 20, 20, "#2C5F8D")}
    <text x="0" y="50" class="label">Varied Emojis</text>
        """
        self.elements.append(f'<g transform="translate({x}, {y})">{content}</g>')

    def add_attackers(self, x=650, y=200):
        content = f"""
    <!-- Group Box -->
    <rect x="-100" y="-60" width="200" height="120" class="group-box" />

    <text x="0" y="-30" class="label" font-weight="bold">Attackers</text>
    <text x="0" y="-10" class="subtitle">(Malicious Data)</text>
    {self._get_icon_warning(-70, 10, 20, 20, "#C07864")}
    {self._get_icon_warning(-30, 10, 20, 20, "#C07864")}
    {self._get_icon_warning(10, 10, 20, 20, "#C07864")}
    {self._get_icon_warning(50, 10, 20, 20, "#C07864")}
    <text x="0" y="50" class="label" fill="#C07864">Attack Emoji</text>
        """
        self.elements.append(f'<g transform="translate({x}, {y})">{content}</g>')

    def add_server(self, x=400, y=200):
        content = """
    <rect x="-100" y="-60" width="200" height="120" class="box" />
    <text x="0" y="-30" class="label" font-weight="bold">Apple Server</text>
    <text x="0" y="-10" class="subtitle">(Data Collection)</text>
    
    <!-- Privacy Filter Inner Box -->
    <rect x="-80" y="10" width="160" height="40" fill="#BEBCB8" opacity="0.3" rx="5" />
    <text x="0" y="35" class="label">Aggregation</text>
        """
        self.elements.append(f'<g transform="translate({x}, {y})">{content}</g>')

    def add_leaderboard(self, x=400, y=450):
        # Bar definitions: (emoji, bar_width, label, color_class)
        bars = [
            ("icon-warning", 250, "Manipulated", "bar-red", "#C07864"),
            ("icon-chart", 150, "Normal", "bar-gray", "#2C5F8D"),
            ("icon-check", 80, "Normal", "bar-gray", "#2C5F8D"),
        ]
        
        # Layout constants
        emoji_x = -120
        bar_start_x = -90
        bar_height = 30
        bar_vertical_spacing = 50
        
        # Calculate text positions dynamically
        # Text x = bar_start_x + bar_width + BAR_TEXT_SPACING
        bar_contents = []
        y_positions = [-15, 35, 85]  # Vertical centers for each bar
        
        for i, (icon_id, bar_width, label, color_class, icon_color) in enumerate(bars):
            y_pos = y_positions[i]
            bar_y = y_pos - bar_height // 2
            
            # Dynamic text position: bar end + spacing
            text_x = bar_start_x + bar_width + self.BAR_TEXT_SPACING
            
            icon_methods = {
                "icon-warning": self._get_icon_warning,
                "icon-chart": self._get_icon_chart,
                "icon-check": self._get_icon_check
            }
            icon_svg = icon_methods[icon_id](emoji_x - 15, y_pos - 15, 30, 30, icon_color)
            
            bar_contents.append(f"""
    <!-- Bar {i+1}: {label} -->
    {icon_svg}
    <rect x="{bar_start_x}" y="{bar_y}" width="{bar_width}" height="{bar_height}" class="{color_class}" />
    <text x="{text_x}" y="{y_pos}" class="label-left" dominant-baseline="middle">{label}</text>""")
        
        # Calculate bounding box dynamically
        title_y = -50
        title_font_size = 20
        
        # Content bounds (approximate)
        content_top = title_y - title_font_size
        content_bottom = y_positions[-1] + bar_height // 2
        content_left = emoji_x - 15  # emoji width estimate
        
        # Find rightmost bar edge
        max_bar_end = max(bar_start_x + bar_width for _, bar_width, _, _, _ in bars)
        # Estimate text width (rough approximation)
        max_text_width = 80  # Approximate width for "Manipulated"
        content_right = max_bar_end + self.BAR_TEXT_SPACING + max_text_width
        
        # Apply padding
        box_x = content_left - self.BOX_PADDING
        box_y = content_top - self.BOX_PADDING
        box_width = (content_right - content_left) + (2 * self.BOX_PADDING)
        box_height = (content_bottom - content_top) + (2 * self.BOX_PADDING)
        
        content = f"""
    <!-- Dynamically calculated box: padding={self.BOX_PADDING}px -->
    <rect x="{box_x}" y="{box_y}" width="{box_width}" height="{box_height}" class="group-box" />

    <text x="0" y="{title_y}" class="title" font-size="20px">Emoji Frequency Statistic</text>
    {''.join(bar_contents)}
        """
        self.elements.append(f'<g transform="translate({x}, {y})">{content}</g>')

    def add_arrow(self, start_x, start_y, end_x, end_y, label=None):
        path = f"M {start_x} {start_y} L {end_x} {end_y}"
        self.elements.append(f'<path d="{path}" class="arrow" />')
        
        if label:
            # Calculate midpoint for label
            mid_x = (start_x + end_x) / 2
            mid_y = (start_y + end_y) / 2
            
            # Offset label slightly above the line
            label_y = mid_y - 10
            
            self.elements.append(f'<text x="{mid_x}" y="{label_y}" class="label" font-size="12px" fill="#584B47">{label}</text>')

    def save(self, filename):
        svg_content = f"""<svg width="{self.width}" height="{self.height}" viewBox="0 0 {self.width} {self.height}" xmlns="http://www.w3.org/2000/svg">
  <defs>
    {''.join(self.defs)}
  </defs>
  {''.join(self.elements)}
</svg>"""
        
        with open(filename, "w") as f:
            f.write(svg_content)
        print(f"Successfully generated {filename}")
        print(f"  - Bar-to-text spacing: {self.BAR_TEXT_SPACING}px")
        print(f"  - Box padding: {self.BOX_PADDING}px")
        
        # Generate PNG with transparent background
        png_filename = filename.replace('.svg', '.png')
        try:
            # Use higher DPI for better rendering of SVG symbols
            subprocess.run(
                ['magick', '-density', '300', filename, '-background', 'none', '-quality', '100', png_filename],
                check=True,
                capture_output=True
            )
            print(f"Successfully generated {png_filename} (transparent background, 300 DPI)")
        except subprocess.CalledProcessError as e:
            print(f"Warning: Could not generate PNG. Error: {e.stderr.decode()}")
        except FileNotFoundError:
            print("Warning: ImageMagick not found. PNG generation skipped.")

def main():
    builder = SVGBuilder()
    
    # 1. Background
    builder.add_background()
    
    # 2. Components
    builder.add_regular_users(100, 200)  # Moved left for longer arrow
    builder.add_server()
    builder.add_attackers(700, 200)  # Moved right for longer arrow
    
    # 4. Arrows
    builder.add_arrow(200, 200, 300, 200)  # Left -> Center
    builder.add_arrow(600, 200, 500, 200)  # Right -> Center
    builder.add_arrow(400, 260, 400, 350)  # Center -> Bottom
    
    # 5. Leaderboard
    builder.add_leaderboard()
    
    builder.save("img.svg")

if __name__ == "__main__":
    main()
