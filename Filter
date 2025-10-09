"""
evaluation_pipeline_diagram.py

Generates a conceptual workflow figure for evaluating filtered vs unfiltered generated frames.

Dependencies:
pip install matplotlib
"""

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrow

# Create figure
fig, ax = plt.subplots(figsize=(12,6))
ax.axis('off')

# Positions of boxes (x, y, width, height)
boxes = {
    "Unfiltered Frames": (0, 3, 2, 1),
    "Filtered Frames": (0, 1, 2, 1),
    "Perceptual Encoder": (3, 2, 2, 1),
    "Metrics": (6, 2, 3, 1),
    "Comparison / Plots": (10, 2, 3, 1)
}

# Colors for boxes
colors = {
    "Unfiltered Frames": "#cce5ff",
    "Filtered Frames": "#ffd9b3",
    "Perceptual Encoder": "#d4f4dd",
    "Metrics": "#f2d4d4",
    "Comparison / Plots": "#f2e6ff"
}

# Add boxes and text
for key, (x, y, w, h) in boxes.items():
    ax.add_patch(Rectangle((x, y), w, h, edgecolor='black', facecolor=colors[key], lw=2, zorder=2))
    ax.text(x + w/2, y + h/2, key, ha='center', va='center', fontsize=10, zorder=3)

# Add arrows
def add_arrow(start, end):
    ax.annotate('', xy=end, xytext=start,
                arrowprops=dict(arrowstyle='->', lw=2))

# Arrows from frames to encoder
add_arrow((2, 3.5), (3, 2.5))  # Unfiltered -> Encoder
add_arrow((2, 1.5), (3, 2.5))  # Filtered -> Encoder

# Encoder -> Metrics
add_arrow((5, 2.5), (6, 2.5))

# Metrics -> Comparison
add_arrow((9, 2.5), (10, 2.5))

# Add metric details as subtext
metric_text = (
    "Spatial Fidelity (SSIM, PSNR)\n"
    "Temporal Consistency (frame-to-frame SSIM)\n"
    "Temporal Gradient Energy"
)
ax.text(7.5, 3.2, metric_text, ha='center', va='center', fontsize=9)

# Display / save
plt.tight_layout()
plt.savefig("evaluation_pipeline.png", dpi=150)
plt.show()
