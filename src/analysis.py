from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
DATA = ROOT / "data" / "category_performance.csv"
ASSETS.mkdir(exist_ok=True)

df = pd.read_csv(DATA)
df = df.sort_values("revenue_gbp", ascending=True)

plt.style.use("seaborn-v0_8-whitegrid")
fig, ax = plt.subplots(figsize=(10, 6))
ax.barh(df["category"], df["revenue_gbp"], color="#0f766e")
ax.set_title("Revenue by snack category", loc="left", fontsize=18, weight="bold")
ax.set_xlabel("Revenue (£)")
ax.xaxis.set_major_formatter(lambda x, pos: f"£{x/1000:.0f}k")
for i, value in enumerate(df["revenue_gbp"]):
    ax.text(value + 700, i, f"£{value:,.2f}", va="center", fontsize=9)
fig.tight_layout()
fig.savefig(ASSETS / "category_revenue.png", dpi=180, bbox_inches="tight")
plt.close(fig)

fig, ax = plt.subplots(figsize=(10, 6))
scatter = ax.scatter(df["units_sold"], df["revenue_gbp"], s=140, c=df["revenue_gbp"], cmap="viridis", edgecolor="white", linewidth=1.2)
for _, row in df.iterrows():
    ax.annotate(row["category"], (row["units_sold"], row["revenue_gbp"]), xytext=(6, 6), textcoords="offset points", fontsize=9)
ax.set_title("Revenue versus customer demand", loc="left", fontsize=18, weight="bold")
ax.set_xlabel("Units sold")
ax.set_ylabel("Revenue (£)")
ax.yaxis.set_major_formatter(lambda x, pos: f"£{x/1000:.0f}k")
fig.tight_layout()
fig.savefig(ASSETS / "revenue_vs_units.png", dpi=180, bbox_inches="tight")
plt.close(fig)

fig, axes = plt.subplots(1, 3, figsize=(13, 3.8))
kpis = [("Revenue", "£277,652.03"), ("Profit", "£111,065.62"), ("Profit margin", "40%")]
for ax, (label, value) in zip(axes, kpis):
    ax.set_facecolor("#f0fdfa")
    ax.text(0.08, 0.58, value, fontsize=20, weight="bold", color="#115e59")
    ax.text(0.08, 0.28, label, fontsize=11, color="#334155")
    ax.axis("off")
fig.suptitle("Snacks Sales Performance — published headline metrics", x=0.03, ha="left", fontsize=16, weight="bold")
fig.tight_layout()
fig.savefig(ASSETS / "kpi_snapshot.png", dpi=180, bbox_inches="tight")
plt.close(fig)
