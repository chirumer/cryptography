# LDP Protocol Attack - SVG Diagram

This repository contains an SVG diagram illustrating an **LDP (Local Differential Privacy) Protocol Attack** that skews emoji leaderboard statistics.

## Diagram

<div style="background-color: white; padding: 20px; border-radius: 8px;">
  <img src="img.svg" alt="LDP Protocol Attack Diagram" width="100%">
</div>

## Overview

The diagram demonstrates how attackers can manipulate emoji frequency statistics by flooding the system with specific emojis (angry emojis in this case) while the privacy filter aggregates data from both honest users and attackers.

### Components

- **Regular Users**: Submit varied emojis as honest data
- **Attackers**: Flood the system with attack emojis (malicious data)
- **Apple Server**: Collects data and applies aggregation through a privacy filter
- **Emoji Frequency Statistic**: Shows the skewed results where the attack emoji appears with high count

## Generating the SVG

Run the Python script to regenerate the SVG:

```bash
python3 generate_svg.py
```

The script uses dynamic positioning with:
- **20px spacing** between bars and text labels
- **20px padding** around content boxes

## Features

- ✅ Transparent background
- ✅ Modular Python generator
- ✅ Dynamic text positioning
- ✅ Dynamic box padding calculations
- ✅ Clean, semantic SVG structure
