import numpy as np
import matplotlib.pyplot as plt

# App Names
app1 = "Telegram"
app2 = "WhatsApp"

# Ratings
app1_ratings = [5, 4, 5, 3, 4, 3, 4, 5]
app2_ratings = [4, 5, 3, 5, 5, 5, 4, 3]

# Weights
weights = [15, 12, 10, 15, 15, 15, 8, 10]

# Characteristics
labels = [
    "Functional",
    "Performance",
    "Compatibility",
    "Usability",
    "Reliability",
    "Security",
    "Maintainability",
    "Portability"
]

# Weighted Scores
app1_score = sum(r * w for r, w in zip(app1_ratings, weights))
app2_score = sum(r * w for r, w in zip(app2_ratings, weights))

print(f"{app1} Total Score: {app1_score}")
print(f"{app2} Total Score: {app2_score}")

# Radar Chart Setup
angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()

# Close loop for radar chart
app1_plot = app1_ratings + [app1_ratings[0]]
app2_plot = app2_ratings + [app2_ratings[0]]
angles = angles + [angles[0]]

# Create plot
plt.figure(figsize=(8, 8))
ax = plt.subplot(111, polar=True)

# Plot app 1
ax.plot(angles, app1_plot, label=f"{app1} ({app1_score})")
ax.fill(angles, app1_plot, alpha=0.1)

# Plot app 2
ax.plot(angles, app2_plot, label=f"{app2} ({app2_score})")
ax.fill(angles, app2_plot, alpha=0.1)

# Labels
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels)

plt.title("ISO 25010 Quality Comparison")
plt.legend(loc='upper right')

plt.tight_layout()

# Save output image
filename = "quality_radar.png"
plt.savefig(filename, dpi=300)

print("Graph saved as:", filename)

# Show plot (IMPORTANT: no blocking issues)
plt.show()