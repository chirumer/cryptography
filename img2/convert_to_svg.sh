#!/bin/bash
set -e

INPUT_FILE="img.png"
PNM_FILE="img.pnm"
PBM_FILE="img.pbm"
OUTPUT_FILE="img.svg"

echo "Step 1: Converting $INPUT_FILE to PNM..."
convert "$INPUT_FILE" "$PNM_FILE"

echo "Step 2: Preprocessing with mkbitmap..."
# -s 3: Scale up by 3 for better resolution
# -b 1: Blur radius 1 to smooth jagged edges
# -t 0.45: Threshold
# -f 4: High-pass filter
mkbitmap -s 3 -b 1 -t 0.45 -f 4 "$PNM_FILE" -o "$PBM_FILE"

echo "Step 3: Tracing with potrace..."
# -s: SVG output
# --tight: Remove whitespace
# -t 5: Suppress speckles (turdsize)
# --alphamax 1.2: Smoother corners
potrace -s --tight -t 5 --alphamax 1.2 "$PBM_FILE" -o "$OUTPUT_FILE"

echo "Conversion complete. Output saved to $OUTPUT_FILE"

# Cleanup intermediate files
rm "$PNM_FILE" "$PBM_FILE"
