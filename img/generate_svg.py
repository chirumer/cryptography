import os

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
      text { font-family: 'Roboto', sans-serif; fill: #151313; }
      .title { font-size: 24px; font-weight: bold; text-anchor: middle; }
      .subtitle { font-size: 14px; text-anchor: middle; fill: #584B47; }
      .label { font-size: 14px; text-anchor: middle; }
      .label-left { font-size: 14px; text-anchor: start; }
      .box { fill: #F8FBFB; stroke: #584B47; stroke-width: 2; rx: 10; ry: 10; }
      .group-box { fill: none; stroke: #BEBCB8; stroke-width: 1; stroke-dasharray: 5,5; rx: 10; ry: 10; }
      .arrow { stroke: #584B47; stroke-width: 2; fill: none; marker-end: url(#arrowhead); }
      .emoji { font-size: 30px; text-anchor: middle; }
      .bar-red { fill: #C07864; }
      .bar-gray { fill: #BEBCB8; }
        """
        self.defs.append(f"<style>{style}</style>")
        
        marker = """
    <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#584B47" />
    </marker>
        """
        self.defs.append(marker)

    def add_background(self, color="none"):
        self.elements.append(f'<rect width="100%" height="100%" fill="{color}" />')

    def add_title(self, text, x=400, y=40):
        self.elements.append(f'<text x="{x}" y="{y}" class="title">{text}</text>')

    def add_regular_users(self, x=150, y=200):
        content = """
    <!-- Group Box -->
    <rect x="-100" y="-60" width="200" height="120" class="group-box" />
    
    <text x="0" y="-30" class="label" font-weight="bold">Regular Users</text>
    <text x="0" y="-10" class="subtitle">(Honest Data)</text>
    <text x="0" y="30" class="emoji">😀 😂 ❤️ 👍</text>
    <text x="0" y="50" class="label">Varied Emojis</text>
        """
        self.elements.append(f'<g transform="translate({x}, {y})">{content}</g>')

    def add_attackers(self, x=650, y=200):
        content = """
    <!-- Group Box -->
    <rect x="-100" y="-60" width="200" height="120" class="group-box" />

    <text x="0" y="-30" class="label" font-weight="bold">Attackers</text>
    <text x="0" y="-10" class="subtitle">(Malicious Data)</text>
    <text x="0" y="30" class="emoji">😠 😠 😠 😠</text>
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
    <text x="0" y="35" class="label">LDP Decoding</text>
        """
        self.elements.append(f'<g transform="translate({x}, {y})">{content}</g>')

    def add_leaderboard(self, x=400, y=450):
        # Bar definitions: (emoji, bar_width, label, color_class)
        bars = [
            ("😠", 250, "Manipulated", "bar-red"),
            ("😂", 150, "Normal", "bar-gray"),
            ("❤️", 80, "Normal", "bar-gray"),
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
        
        for i, (emoji, bar_width, label, color_class) in enumerate(bars):
            y_pos = y_positions[i]
            bar_y = y_pos - bar_height // 2
            
            # Dynamic text position: bar end + spacing
            text_x = bar_start_x + bar_width + self.BAR_TEXT_SPACING
            
            bar_contents.append(f"""
    <!-- Bar {i+1}: {label} -->
    <text x="{emoji_x}" y="{y_pos}" class="emoji" dominant-baseline="middle">{emoji}</text>
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
        max_bar_end = max(bar_start_x + bar_width for _, bar_width, _, _ in bars)
        # Estimate text width (rough approximation)
        max_text_width = 80  # Approximate width for "High Count"
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

def main():
    builder = SVGBuilder()
    
    # 1. Background
    builder.add_background()
    
    # 2. Title
    builder.add_title("LDP Protocol Attack Skewing the Frequently Used Emoji Statistic")
    
    # 3. Components
    builder.add_regular_users(100, 200)  # Moved left for longer arrow
    builder.add_server()
    builder.add_attackers(700, 200)  # Moved right for longer arrow
    
    # 4. Arrows (now 100px long to fit text)
    builder.add_arrow(200, 200, 300, 200, "+ ε-LDP noise")  # Left -> Center (100px)
    builder.add_arrow(600, 200, 500, 200, "+ ε-LDP noise")  # Right -> Center (100px)
    builder.add_arrow(400, 260, 400, 350)  # Center -> Bottom
    
    # 5. Leaderboard
    builder.add_leaderboard()
    
    builder.save("img.svg")

if __name__ == "__main__":
    main()
