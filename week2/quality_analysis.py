import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# DATA (YOUR ACTUAL RATINGS)
# -----------------------------
categories = [
    "Functional Suitability",
    "Performance Efficiency",
    "Compatibility",
    "Usability",
    "Reliability",
    "Security",
    "Maintainability",
    "Portability"
]

# Ratings
APP1_RATINGS = [5, 4, 5, 4, 4, 3, 4, 5]  # Telegram
APP2_RATINGS = [4, 5, 4, 5, 4, 5, 4, 4]  # WhatsApp

# Weighted Scores (for legend)
APP1_SCORE = 4.20
APP2_SCORE = 4.42

# -----------------------------
# RADAR CHART SETUP
# -----------------------------
N = len(categories)

angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()

# Close the loop
APP1_RATINGS += APP1_RATINGS[:1]
APP2_RATINGS += APP2_RATINGS[:1]
angles += angles[:1]

# -----------------------------
# PLOT
# -----------------------------
plt.figure(figsize=(8, 8))
ax = plt.subplot(111, polar=True)

# Plot App 1 (Telegram)
ax.plot(angles, APP1_RATINGS, linewidth=2, label=f"Telegram (Score: {APP1_SCORE})")
ax.fill(angles, APP1_RATINGS, alpha=0.1)

# Plot App 2 (WhatsApp)
ax.plot(angles, APP2_RATINGS, linewidth=2, linestyle='dashed',
        label=f"WhatsApp (Score: {APP2_SCORE})")
ax.fill(angles, APP2_RATINGS, alpha=0.1)

# Labels
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories)

# Scale (1–5)
ax.set_yticks([1, 2, 3, 4, 5])
ax.set_ylim(0, 5)

# Title
plt.title("Quality Comparison: Telegram vs WhatsApp", size=14)

# Legend
plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))

# Save chart
plt.savefig("week2/radar_chart.png", bbox_inches='tight')

# Show chart
plt.show()