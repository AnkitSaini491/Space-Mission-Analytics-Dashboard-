
import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# SPACE MISSION DATA
# ==========================================

space = {

    "Month":[
        "Jan","Feb","Mar","Apr","May","Jun",
        "Jul","Aug","Sep","Oct","Nov","Dec"
    ],

    "Missions":[
        5,6,7,8,9,10,
        11,12,13,14,15,16
    ],

    "Successful":[
        4,5,6,7,8,9,
        10,11,12,13,14,15
    ],

    "Failed":[
        1,1,1,1,1,1,
        1,1,1,1,1,1
    ],

    "Satellites":[
        8,10,12,15,18,20,
        22,25,28,30,32,35
    ],

    "Budget":[
        120,135,150,165,180,195,
        210,225,240,255,270,290
    ],

    "Astronauts":[
        6,7,8,9,10,11,
        12,13,14,15,16,18
    ],

    "Success_Rate":[
        80,83,86,88,89,90,
        91,92,93,94,95,96
    ]
}

df = pd.DataFrame(space)

# ==========================================
# KPI VALUES
# ==========================================

total_missions = df["Missions"].sum()

successful = df["Successful"].sum()

failed = df["Failed"].sum()

satellites = df["Satellites"].sum()

avg_budget = df["Budget"].mean()

avg_success = df["Success_Rate"].mean()

# ==========================================
# DASHBOARD STYLE
# ==========================================

plt.style.use("dark_background")

fig = plt.figure(figsize=(20,12))

fig.patch.set_facecolor("#0B1020")

fig.suptitle(
    "SPACE MISSION ANALYTICS DASHBOARD",
    fontsize=28,
    color="white",
    fontweight="bold"
)

# ==========================================
# KPI CARDS
# ==========================================

plt.figtext(
0.02,0.90,
f"Missions\n{total_missions}",
fontsize=14,
bbox=dict(facecolor="#2563EB",boxstyle="round,pad=0.8")
)

plt.figtext(
0.18,0.90,
f"Successful\n{successful}",
fontsize=14,
bbox=dict(facecolor="#16A34A",boxstyle="round,pad=0.8")
)

plt.figtext(
0.35,0.90,
f"Failed\n{failed}",
fontsize=14,
bbox=dict(facecolor="#DC2626",boxstyle="round,pad=0.8")
)

plt.figtext(
0.52,0.90,
f"Satellites\n{satellites}",
fontsize=14,
bbox=dict(facecolor="#F59E0B",boxstyle="round,pad=0.8")
)

plt.figtext(
0.69,0.90,
f"Avg Budget\n${avg_budget:.0f}M",
fontsize=14,
bbox=dict(facecolor="#9333EA",boxstyle="round,pad=0.8")
)

plt.figtext(
0.85,0.90,
f"Success\n{avg_success:.1f}%",
fontsize=14,
bbox=dict(facecolor="#06B6D4",boxstyle="round,pad=0.8")
)

# ==========================================
# CHART 1 - MONTHLY MISSIONS
# ==========================================

ax1 = plt.subplot(3,2,1)

ax1.plot(
    df["Month"],
    df["Missions"],
    marker="o",
    linewidth=3,
    color="cyan"
)

ax1.fill_between(
    df["Month"],
    df["Missions"],
    color="cyan",
    alpha=0.30
)

ax1.set_title("Monthly Space Missions")
ax1.set_ylabel("Missions")
ax1.grid(alpha=0.3)
ax1.tick_params(axis="x", rotation=45)
# ==========================================
# CHART 2 - SUCCESSFUL VS FAILED MISSIONS
# ==========================================

ax2 = plt.subplot(3,2,2)

ax2.plot(
    df["Month"],
    df["Successful"],
    marker="o",
    linewidth=3,
    color="lime"
)

ax2.plot(
    df["Month"],
    df["Failed"],
    marker="o",
    linewidth=3,
    color="red"
)

ax2.set_title("Mission Success vs Failure")
ax2.set_ylabel("Missions")
ax2.legend(["Successful","Failed"])
ax2.grid(alpha=0.3)
ax2.tick_params(axis="x", rotation=45)


# ==========================================
# CHART 3 - SATELLITE LAUNCH TREND
# ==========================================

ax3 = plt.subplot(3,2,3)

ax3.bar(
    df["Month"],
    df["Satellites"],
    color="deepskyblue"
)

ax3.set_title("Satellite Launch Trend")
ax3.set_ylabel("Satellites")
ax3.grid(alpha=0.3)
ax3.tick_params(axis="x", rotation=45)


# ==========================================
# CHART 4 - SPACE BUDGET
# ==========================================

ax4 = plt.subplot(3,2,4)

ax4.plot(
    df["Month"],
    df["Budget"],
    marker="o",
    linewidth=3,
    color="gold"
)

ax4.fill_between(
    df["Month"],
    df["Budget"],
    color="gold",
    alpha=0.30
)

ax4.set_title("Mission Budget Trend")
ax4.set_ylabel("Budget ($ Million)")
ax4.grid(alpha=0.3)
ax4.tick_params(axis="x", rotation=45)


# ==========================================
# CHART 5 - ASTRONAUT MISSIONS
# ==========================================

ax5 = plt.subplot(3,2,5)

ax5.bar(
    df["Month"],
    df["Astronauts"],
    color="orange"
)

ax5.set_title("Astronaut Missions")
ax5.set_ylabel("Astronauts")
ax5.grid(alpha=0.3)
ax5.tick_params(axis="x", rotation=45)


# ==========================================
# CHART 6 - SUCCESS RATE
# ==========================================

ax6 = plt.subplot(3,2,6)

ax6.plot(
    df["Month"],
    df["Success_Rate"],
    marker="o",
    linewidth=3,
    color="violet"
)

ax6.fill_between(
    df["Month"],
    df["Success_Rate"],
    color="violet",
    alpha=0.30
)

ax6.set_title("Mission Success Rate")
ax6.set_ylabel("Success (%)")
ax6.grid(alpha=0.3)
ax6.tick_params(axis="x", rotation=45)

plt.tight_layout(rect=[0,0,1,0.88])

# ==========================================
# CHART 7 - COUNTRY WISE MISSIONS
# ==========================================

country = pd.DataFrame({

    "Country":[
        "USA",
        "India",
        "China",
        "Russia",
        "Europe"
    ],

    "Missions":[
        42,
        24,
        30,
        18,
        20
    ]
})

plt.figure(figsize=(10,5))
plt.style.use("dark_background")

plt.bar(
    country["Country"],
    country["Missions"],
    color="dodgerblue"
)

plt.title("Country-wise Space Missions")
plt.ylabel("Number of Missions")
plt.grid(alpha=0.3)

plt.tight_layout()
plt.show()


# ==========================================
# CHART 8 - MISSION DESTINATIONS
# ==========================================

destination = pd.DataFrame({

    "Destination":[
        "Earth Orbit",
        "Moon",
        "Mars",
        "ISS",
        "Deep Space"
    ],

    "Count":[
        60,
        15,
        8,
        20,
        5
    ]
})

plt.figure(figsize=(8,6))
plt.style.use("dark_background")

plt.pie(
    destination["Count"],
    labels=destination["Destination"],
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Mission Destination Distribution")

plt.tight_layout()
plt.show()


# ==========================================
# CHART 9 - BUDGET VS MISSIONS
# ==========================================

plt.figure(figsize=(10,5))
plt.style.use("dark_background")

plt.plot(
    df["Month"],
    df["Budget"],
    marker="o",
    linewidth=3,
    label="Budget",
    color="gold"
)

plt.plot(
    df["Month"],
    df["Missions"],
    marker="o",
    linewidth=3,
    label="Missions",
    color="cyan"
)

plt.title("Budget vs Missions")
plt.xlabel("Month")
plt.legend()
plt.grid(alpha=0.3)

plt.tight_layout()
plt.show()


# ==========================================
# SUMMARY REPORT
# ==========================================

best_month = df.loc[df["Missions"].idxmax()]

print("="*65)
print("SPACE MISSION ANALYTICS SUMMARY")
print("="*65)

print(f"Total Missions        : {total_missions}")
print(f"Successful Missions   : {successful}")
print(f"Failed Missions       : {failed}")
print(f"Satellites Launched   : {satellites}")
print(f"Average Budget        : ${avg_budget:.2f} Million")
print(f"Mission Success Rate  : {avg_success:.2f}%")

print(f"\nBest Performance Month : {best_month['Month']}")
print(f"Total Missions         : {best_month['Missions']}")

print("="*65)


# ==========================================
# SAVE DASHBOARD
# ==========================================

fig.savefig(
    "space_mission_dashboard.png",
    dpi=300,
    bbox_inches="tight"
)

print("\nDashboard saved as space_mission_dashboard.png")


# ==========================================
# PROJECT DETAILS
# ==========================================

print("\nProject Name : Space Mission Analytics Dashboard")
print("Technology   : Python | Pandas | Matplotlib")
print("Domain       : Space & Aerospace Analytics")
print("Status       : Dashboard Generated Successfully")


# ==========================================
# FOOTER
# ==========================================

plt.figtext(
    0.28,
    0.02,
    "Developed using Python | Pandas | Matplotlib",
    fontsize=11,
    color="white"
)

plt.show()
