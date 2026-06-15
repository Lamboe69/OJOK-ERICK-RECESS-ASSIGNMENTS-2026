# Assignment 3: Real world application of loop control statements
# World Cup 2026 Simulation

import random

# Each team: Name, GOAT, LastWC, ContCups, FIFARank, Strength, Form,
# Injuries, CoachRank, Fans, EPL, LaLiga, SerieA, Bundes, Ligue1, Other,
# AvgAge, WCExp, Keeper, Defender, Midfielder, Forward
teams = [
    ["Mexico", 0, 22, 12, 14, 81.2, 10, 1, 18, 5, 2, 3, 1, 0, 1, 19, 27.3, 9, 79, 80, 82, 79],
    ["South Korea", 0, 16, 2, 25, 79.8, 13, 0, 21, 4, 3, 0, 0, 3, 1, 19, 26.9, 11, 76, 82, 84, 85],
    ["Czech Republic", 0, 0, 1, 40, 76.5, 10, 2, 29, 3, 3, 0, 2, 6, 0, 15, 26.4, 0, 81, 77, 79, 81],
    ["South Africa", 0, 0, 1, 60, 71, 8, 1, 38, 4, 0, 0, 0, 0, 1, 25, 27.8, 0, 80, 70, 72, 71],
    ["Switzerland", 0, 12, 0, 19, 85.5, 8, 1, 14, 3, 4, 1, 3, 8, 2, 8, 28.1, 15, 87, 84, 85, 79],
    ["Canada", 0, 31, 2, 38, 80.4, 8, 0, 22, 4, 1, 1, 1, 1, 1, 21, 26.5, 12, 77, 81, 78, 83],
    ["Qatar", 0, 32, 2, 34, 75.8, 10, 2, 31, 4, 0, 0, 0, 0, 0, 26, 27.9, 14, 74, 75, 76, 78],
    ["Bosnia & Herzegovina", 0, 0, 0, 72, 72.1, 5, 1, 42, 3, 0, 0, 2, 3, 0, 21, 26.8, 0, 75, 72, 74, 73],
    ["Scotland", 0, 0, 0, 39, 78.4, 10, 1, 25, 5, 6, 0, 3, 0, 0, 17, 27.2, 0, 77, 82, 83, 75],
    ["Morocco", 0, 4, 1, 13, 88.5, 11, 0, 11, 4, 3, 2, 2, 1, 3, 15, 25.8, 9, 85, 86, 84, 83],
    ["Brazil", 0, 7, 9, 5, 93.2, 11, 2, 5, 5, 9, 5, 2, 1, 2, 7, 26.4, 14, 89, 90, 89, 94],
    ["Haiti", 0, 0, 1, 86, 66.8, 5, 1, 45, 3, 0, 0, 0, 0, 2, 24, 26.1, 0, 68, 66, 69, 71],
    ["United States", 0, 14, 10, 17, 86.4, 10, 1, 16, 5, 5, 2, 3, 2, 1, 13, 25.4, 13, 80, 82, 84, 86],
    ["Australia", 0, 11, 1, 27, 80.1, 10, 0, 23, 4, 1, 0, 1, 2, 1, 21, 27.4, 10, 82, 79, 78, 77],
    ["Turkiye", 0, 0, 0, 22, 83.7, 10, 2, 15, 5, 2, 1, 3, 2, 0, 18, 26.1, 0, 81, 82, 86, 80],
    ["Paraguay", 0, 0, 2, 41, 75.2, 7, 1, 32, 3, 2, 1, 1, 0, 0, 22, 27.9, 0, 74, 77, 76, 78],
    ["Germany", 0, 17, 4, 11, 92.8, 13, 1, 6, 4, 3, 2, 1, 19, 0, 1, 26.8, 11, 88, 89, 93, 88],
    ["Ivory Coast", 0, 0, 3, 31, 82.4, 10, 0, 19, 5, 4, 1, 3, 2, 5, 11, 26.2, 0, 76, 83, 81, 82],
    ["Ecuador", 0, 18, 0, 29, 81.6, 10, 1, 20, 4, 3, 0, 0, 1, 1, 21, 25.1, 13, 78, 84, 82, 77],
    ["Curacao", 0, 0, 2, 84, 64.5, 7, 2, 46, 3, 0, 0, 0, 0, 0, 26, 28.3, 0, 72, 65, 66, 68],
    ["Sweden", 0, 0, 0, 28, 84.8, 10, 0, 17, 4, 4, 1, 2, 2, 1, 16, 26.3, 4, 79, 82, 83, 89],
    ["Japan", 0, 9, 4, 15, 87.2, 11, 1, 12, 5, 3, 1, 0, 5, 2, 15, 26.6, 15, 78, 85, 88, 83],
    ["Netherlands", 0, 5, 1, 7, 91.5, 8, 2, 9, 5, 7, 2, 4, 3, 1, 9, 27.1, 14, 82, 93, 88, 86],
    ["Tunisia", 0, 21, 1, 43, 73.4, 8, 1, 33, 4, 0, 0, 1, 1, 4, 20, 27.5, 8, 73, 74, 76, 72],
    ["Belgium", 0, 23, 0, 9, 89.9, 13, 1, 10, 4, 6, 1, 3, 4, 1, 11, 26.9, 10, 91, 82, 90, 87],
    ["Egypt", 0, 0, 7, 29, 81.4, 10, 0, 22, 5, 1, 0, 0, 1, 2, 22, 27.4, 4, 78, 77, 79, 86],
    ["Iran", 0, 26, 3, 20, 78.5, 13, 1, 26, 4, 1, 0, 1, 0, 0, 24, 28.5, 12, 76, 75, 78, 82],
    ["New Zealand", 0, 0, 5, 85, 67.2, 8, 0, 43, 3, 1, 0, 0, 0, 0, 25, 25.8, 1, 71, 70, 68, 74],
    ["Spain", 0, 13, 5, 3, 95.2, 13, 1, 3, 4, 4, 18, 1, 1, 1, 1, 25.7, 10, 86, 91, 96, 92],
    ["Cabo Verde", 0, 0, 0, 63, 72.8, 8, 0, 35, 3, 0, 1, 1, 0, 3, 21, 27.4, 0, 72, 73, 71, 74],
    ["Saudi Arabia", 0, 25, 3, 56, 76.2, 10, 2, 27, 5, 0, 0, 0, 0, 0, 26, 27.9, 14, 75, 76, 75, 74],
    ["Uruguay", 0, 20, 17, 12, 90.5, 10, 1, 4, 4, 2, 3, 2, 0, 1, 18, 26.1, 11, 81, 88, 91, 87],
    ["France", 0, 2, 4, 2, 95.8, 12, 1, 1, 4, 6, 5, 4, 3, 7, 1, 26.4, 15, 87, 94, 90, 96],
    ["Senegal", 0, 10, 1, 18, 84.2, 10, 0, 13, 5, 4, 1, 2, 1, 6, 12, 27.2, 13, 82, 83, 81, 84],
    ["Iraq", 0, 0, 1, 55, 74, 10, 1, 30, 4, 1, 0, 0, 0, 0, 25, 25.9, 0, 73, 72, 75, 76],
    ["Norway", 0, 0, 0, 24, 86.1, 10, 1, 21, 3, 3, 2, 1, 2, 0, 18, 25.6, 0, 75, 79, 89, 95],
    ["Argentina", 1, 1, 16, 1, 96.2, 13, 1, 2, 5, 6, 5, 4, 1, 1, 9, 28.2, 16, 89, 90, 92, 95],
    ["Algeria", 0, 0, 2, 44, 80.5, 10, 0, 24, 5, 1, 0, 3, 1, 5, 16, 27.1, 2, 76, 79, 82, 80],
    ["Austria", 0, 0, 0, 23, 85.4, 10, 2, 12, 4, 1, 1, 2, 16, 1, 5, 26.5, 0, 80, 84, 86, 79],
    ["Jordan", 0, 0, 0, 68, 70.8, 7, 1, 37, 4, 0, 1, 0, 0, 0, 25, 26.2, 0, 71, 69, 71, 76],
    ["Portugal", 1, 8, 2, 6, 94.6, 13, 1, 7, 4, 8, 2, 2, 1, 4, 9, 26.9, 13, 86, 91, 94, 92],
    ["DR Congo", 0, 0, 2, 61, 76.5, 8, 0, 28, 5, 2, 0, 0, 0, 6, 18, 26.4, 0, 75, 76, 77, 80],
    ["Uzbekistan", 0, 0, 0, 62, 74.2, 13, 1, 31, 4, 0, 0, 1, 0, 2, 23, 25.5, 0, 72, 75, 74, 77],
    ["Colombia", 0, 0, 1, 12, 89.8, 10, 1, 9, 5, 4, 2, 1, 0, 0, 19, 26.8, 8, 80, 85, 87, 90],
    ["England", 0, 6, 1, 4, 94.8, 13, 2, 5, 5, 23, 1, 0, 1, 1, 0, 26.1, 14, 83, 91, 95, 96],
    ["Croatia", 0, 3, 0, 10, 88.2, 10, 1, 8, 4, 2, 1, 3, 4, 0, 16, 28.4, 15, 84, 86, 89, 80],
    ["Ghana", 0, 24, 4, 58, 78.6, 10, 1, 25, 4, 4, 2, 0, 0, 3, 17, 24.9, 9, 74, 78, 82, 81],
    ["Panama", 0, 0, 0, 42, 74.5, 7, 0, 29, 3, 0, 0, 0, 0, 1, 25, 27.2, 2, 77, 73, 74, 72],
]


def get_team_index(name):
    for i in range(len(teams)):
        if teams[i][0] == name:
            return i
    return -1


def calc_goals(attack_power, defense_power):
    expected = attack_power / max(defense_power, 1) * 1.5
    if expected > 4:
        expected = 4
    goals = 0
    for _ in range(3):
        if random.random() < expected / 4:
            goals = goals + 1
    return goals


def auto_match(t1_name, t2_name):
    i1 = get_team_index(t1_name)
    i2 = get_team_index(t2_name)
    t1 = teams[i1]
    t2 = teams[i2]
    att1 = t1[5] * 0.4 + t1[21] * 0.4 + t1[6] * 0.2
    def1 = t1[5] * 0.3 + t1[19] * 0.35 + t1[18] * 0.35
    att2 = t2[5] * 0.4 + t2[21] * 0.4 + t2[6] * 0.2
    def2 = t2[5] * 0.3 + t2[19] * 0.35 + t2[18] * 0.35
    if t1[1] == 1:
        att1 = att1 + 5
    if t2[1] == 1:
        att2 = att2 + 5
    g1 = calc_goals(att1, def2)
    g2 = calc_goals(att2, def1)
    return g1, g2


def get_group_standings(group_teams, results):
    standings = []
    for name in group_teams:
        mp = 0
        w = 0
        d = 0
        l = 0
        gf = 0
        ga = 0
        pts = 0
        for r in results:
            if r[0] == name:
                mp = mp + 1
                gf = gf + r[1]
                ga = ga + r[3]
                if r[1] > r[3]:
                    w = w + 1
                    pts = pts + 3
                elif r[1] == r[3]:
                    d = d + 1
                    pts = pts + 1
                else:
                    l = l + 1
            elif r[2] == name:
                mp = mp + 1
                gf = gf + r[3]
                ga = ga + r[1]
                if r[3] > r[1]:
                    w = w + 1
                    pts = pts + 3
                elif r[3] == r[1]:
                    d = d + 1
                    pts = pts + 1
                else:
                    l = l + 1
        gd = gf - ga
        standings.append([name, mp, w, d, l, gf, ga, gd, pts])
    standings.sort(key=lambda x: (x[8], x[7], x[5]), reverse=True)
    return standings


def print_standings(standings, group_name):
    print()
    print(f"  {group_name} Final Standings:")
    print(f"  {'Team':20s} {'MP':3s} {'W':3s} {'D':3s} {'L':3s} {'GF':3s} {'GA':3s} {'GD':4s} {'Pts':3s}")
    print("  " + "-" * 46)
    for s in standings:
        print(f"  {s[0]:20s} {s[1]:3d} {s[2]:3d} {s[3]:3d} {s[4]:3d} {s[5]:3d} {s[6]:3d} {s[7]:+3d} {s[8]:3d}")


print()
print("=" * 60)
print("         2026 FIFA WORLD CUP SIMULATION")
print("=" * 60)

# Show available teams
print("\nAvailable Teams:")
print("-" * 60)
for i in range(len(teams)):
    name = teams[i][0]
    s = teams[i][5]
    fifa = teams[i][4]
    print(f"  {i+1:2d}. {name:22s}  Strength: {s:5}  FIFA Rank: {fifa}")
print("-" * 60)

# Let user pick a team
choice = input("\nSelect your team (enter number): ")
index = int(choice) - 1

country = teams[index][0]
strength = teams[index][5]
morale = teams[index][6]
injuries = teams[index][7]
goat = teams[index][1]
forward = teams[index][21]
defender = teams[index][19]
midfielder = teams[index][20]
keeper = teams[index][18]
fifa_rank = teams[index][4]
coach_rank = teams[index][8]
wc_exp = teams[index][17]

print()
print("-" * 60)
print(f"  You are the manager of {country}!")
print(f"  FIFA Rank: {fifa_rank}  |  Strength: {strength}  |  Form: {morale}/15")
print(f"  Injuries: {injuries}  |  Coach Rank: {coach_rank}  |  WC Exp: {wc_exp} players")
print(f"  Keeper: {keeper}  |  Defender: {defender}  |  Midfielder: {midfielder}  |  Forward: {forward}")
if goat == 1:
    print("  ★ GOAT Effect active! Legendary inspiration lifts the team.")
if injuries == 0:
    print(f"  ★ {country} has NO injuries — a big advantage!")
print("-" * 60)
print()

# Convert form (1-15) to morale (0-100)
morale = int(morale * 7.69)

# ==============================
# PHASE 1: PRE-TOURNAMENT PREPARATION
# ==============================
print("=" * 60)
print("   PHASE 1: PRE-TOURNAMENT PREPARATION")
print("=" * 60)

preparation_done = False

while not preparation_done:
    if strength > 100:
        strength = 100
    if morale > 100:
        morale = 100
    print()
    print(f"  Team Status | Strength: {strength} | Morale: {morale} | Injuries: {injuries}")
    print("  " + "-" * 40)
    print("  1. Training session")
    print("  2. Play friendly match")
    print("  3. Recovery day")
    print("  4. Start tournament")
    print("  " + "-" * 40)

    choice = input("  Enter your choice: ")

    if choice == "1":
        print()
        print(f"  {country} completes a training session.")
        strength = strength + 5
        morale = morale + 5
        print("  Effect: Strength +5 | Morale +5")

    elif choice == "2":
        print()
        print(f"  {country} plays a friendly match.")
        result = input("  Did you win? (y/n): ")
        if result == "y":
            morale = morale + 10
            strength = strength + 3
            print("  Effect: Great win! Morale +10 | Strength +3")
        else:
            morale = morale - 8
            injuries = injuries + 1
            print("  Effect: Tough loss. Morale -8 | Injuries +1")

    elif choice == "3":
        print()
        print(f"  {country} takes a recovery day.")
        morale = morale + 5
        if injuries > 0:
            injuries = injuries - 1
            print("  Effect: One player recovered! Injuries -1 | Morale +5")
        else:
            print("  Effect: No injuries to treat. Morale +5")

    elif choice == "4":
        if strength < 30 or morale < 20:
            print()
            print(f"  {country} is not ready yet! Train more.")
            continue
        print()
        print(f"  {country} is ready! Heading to the World Cup!")
        preparation_done = True
        break

    else:
        print()
        print("  Invalid choice. Try again.")
        continue

    pass

# ==============================
# PHASE 2: GROUP STAGE
# ==============================
print()
print("=" * 60)
print("   PHASE 2: GROUP STAGE")
print("=" * 60)

# All 48 teams participate in 12 groups of 4
all_team_names = []
for t in teams:
    all_team_names.append(t[0])

random.shuffle(all_team_names)

groups = []
user_group_index = -1
group_names = ["Group A", "Group B", "Group C", "Group D", "Group E", "Group F",
               "Group G", "Group H", "Group I", "Group J", "Group K", "Group L"]
all_tournament_teams = []
added_country = False

# Assign all 48 teams to 12 groups
for g in range(12):
    group = []
    for _ in range(4):
        if not added_country:
            group.append(country)
            added_country = True
        else:
            for t_name in all_team_names:
                if t_name not in all_tournament_teams and t_name != country:
                    group.append(t_name)
                    all_tournament_teams.append(t_name)
                    break
    groups.append(group)
    if country in group:
        user_group_index = g

# Store all results for group stage
all_group_results = []

# First, auto-simulate all non-user groups
for g in range(12):
    if g == user_group_index:
        continue
    group = groups[g]
    group_results = []
    # Each team plays each other
    for i in range(4):
        for j in range(i + 1, 4):
            t1 = group[i]
            t2 = group[j]
            g1, g2 = auto_match(t1, t2)
            group_results.append([t1, g1, t2, g2])
    all_group_results.append(group_results)

# Now simulate user's group
user_group = groups[user_group_index]
print()
print(f"  Your Group: {group_names[user_group_index]}")
print(f"  Teams: {user_group[0]}, {user_group[1]}, {user_group[2]}, {user_group[3]}")
print("  Top 2 + best 8 third-placed advance to Round of 32!")
print()

# Find user's opponents in the group
user_opponents = []
for t in user_group:
    if t != country:
        user_opponents.append(t)

user_group_results = []
match_number = 0
wins = 0
user_matches_played = 0

while user_matches_played < 3:
    opponent = user_opponents[user_matches_played]
    if strength > 100:
        strength = 100
    if morale > 100:
        morale = 100
    print("  " + "-" * 40)
    print(f"  Match {user_matches_played + 1}: {country} vs {opponent}")
    print("  " + "-" * 40)
    print(f"  Strength: {strength}  |  Morale: {morale}  |  Injuries: {injuries}")

    tactic = input("  Choose tactic (attack/defend/balanced): ")

    if tactic == "attack":
        chance = strength + forward + morale * 0.5
    elif tactic == "defend":
        chance = strength * 0.7 + defender + morale * 0.4
    elif tactic == "balanced":
        avg = (keeper + defender + midfielder + forward) / 4
        chance = strength * 0.5 + avg * 0.5 + morale * 0.4
    else:
        print("  Invalid tactic! Using balanced.")
        avg = (keeper + defender + midfielder + forward) / 4
        chance = strength * 0.5 + avg * 0.5 + morale * 0.4
        pass

    if goat == 1:
        chance = chance + 10
        print("  ★ GOAT effect inspires the team!")

    if injuries >= 3:
        print("  Too many injuries! Performance suffers.")
        chance = chance - 20

    # Calculate goals based on chance
    opp_idx = get_team_index(opponent)
    opp_str = teams[opp_idx][5]
    opp_def = teams[opp_idx][19]
    opp_keeper = teams[opp_idx][18]
    opp_power = opp_str * 0.3 + opp_def * 0.35 + opp_keeper * 0.35

    my_attack_roll = random.randint(1, 100) + chance * 0.3
    opp_attack_roll = random.randint(1, 100) + opp_power * 0.3

    if my_attack_roll > opp_attack_roll:
        my_goals = random.randint(1, 5)
        opp_goals = random.randint(0, my_goals - 1)
        print(f"  Result: {country} {my_goals} - {opp_goals} {opponent} ★ WIN!")
        wins = wins + 1
        morale = morale + 10
    else:
        my_goals = random.randint(0, 2)
        opp_goals = random.randint(my_goals + 1, 5)
        print(f"  Result: {country} {my_goals} - {opp_goals} {opponent} ★ LOSS")
        morale = morale - 8
        injuries = injuries + 1

    user_group_results.append([country, my_goals, opponent, opp_goals])
    user_matches_played = user_matches_played + 1

    if morale <= 0:
        print()
        print(f"  Morale has hit zero. {country} is eliminated!")
        break

    if user_matches_played < 3:
        rest = input("  Rest before next match? (y/n): ")
        if rest == "y":
            morale = morale + 5
            if injuries > 0:
                injuries = injuries - 1
                print("  One injury healed.")
        print()

# Auto-simulate the remaining matches in user's group (between the 3 opponents)
for i in range(3):
    for j in range(i + 1, 3):
        t1 = user_opponents[i]
        t2 = user_opponents[j]
        g1, g2 = auto_match(t1, t2)
        user_group_results.append([t1, g1, t2, g2])

all_group_results.insert(user_group_index, user_group_results)

# Print all group standings
print()
print("=" * 60)
print("   GROUP STAGE RESULTS")
print("=" * 60)

all_qualified = []
all_third_placed = []

for g in range(12):
    group = groups[g]
    results = all_group_results[g]
    standings = get_group_standings(group, results)
    print_standings(standings, group_names[g])
    all_qualified.append(standings[0][0])
    all_qualified.append(standings[1][0])
    all_third_placed.append(standings[2])

# Sort third-placed teams: points → GD → GS
all_third_placed.sort(key=lambda x: (x[8], x[7], x[5]), reverse=True)
for i in range(8):
    all_qualified.append(all_third_placed[i][0])

print()
print("  Teams qualified for Round of 32:")
print("  " + "-" * 60)
row = ""
for i in range(len(all_qualified)):
    row = row + f"  {i+1}. {all_qualified[i]}"
    if (i + 1) % 4 == 0:
        print(row)
        row = ""
if row != "":
    print(row)

# Check if user qualified
user_qualified = False
user_knockout_seed = -1
for q in range(len(all_qualified)):
    if all_qualified[q] == country:
        user_qualified = True
        user_knockout_seed = q
        break

if not user_qualified:
    print(f"\n  {country} did not qualify for knockout stage. Tournament over!")
    tournament_over = True
else:
    print(f"\n  ★ {country} qualified for knockout stage!")
    tournament_over = False


round_number = 0
user_in_tournament = user_qualified

# ==============================
# PHASE 3: KNOCKOUT STAGE
# ==============================
if tournament_over:
    pass
else:
    print()
    print("=" * 60)
    print("   PHASE 3: KNOCKOUT STAGE")
    print("=" * 60)

    # Set up knockout bracket for 32 teams
    # Round of 32 pairings: 1v32, 2v31, ..., 16v17
    round_of_32_pairs = []
    for i in range(16):
        round_of_32_pairs.append([all_qualified[i], all_qualified[31 - i]])

    rounds_knockout = ["Round of 32", "Round of 16", "Quarter-final", "Semi-final", "Final"]
    current_round_teams = all_qualified[:]
    user_in_tournament = user_qualified

    round_number = 0

    while round_number < 5 and user_in_tournament:
        current_round_name = rounds_knockout[round_number]
        print()
        print("  " + "=" * 56)
        print(f"   {current_round_name}")
        print("  " + "=" * 56)

        # Build pairings for this round
        if round_number == 0:
            pairs = round_of_32_pairs
        else:
            pairs = []
            for i in range(0, len(current_round_teams), 2):
                pairs.append([current_round_teams[i], current_round_teams[i + 1]])

        # Show all matchups
        print()
        print("  Matchups:")
        print("  " + "-" * 40)
        for p in range(len(pairs)):
            print(f"   {p+1}. {pairs[p][0]} vs {pairs[p][1]}")
        print("  " + "-" * 40)
        print()

        next_round_teams = []
        user_plays_in = -1

        # Find which match the user is in
        for p in range(len(pairs)):
            if pairs[p][0] == country or pairs[p][1] == country:
                user_plays_in = p
                break

        # Simulate all matches
        for p in range(len(pairs)):
            team1 = pairs[p][0]
            team2 = pairs[p][1]

            if p == user_plays_in:
                # User plays this match
                if strength > 100:
                    strength = 100
                if morale > 100:
                    morale = 100
                print(f"  ★ Your Match: {country} vs {team2 if team1 == country else team1}")
                print(f"  Morale: {morale}  |  Strength: {strength}  |  Injuries: {injuries}")

                if injuries >= 3:
                    print(f"  Critical injuries! {country} must skip this round.")
                    round_number = round_number + 1
                    continue

                intensity = input("  Choose intensity (normal/aggressive/conservative): ")

                if intensity == "aggressive":
                    win_chance = (strength + forward) * 1.2 + morale * 0.5 - (injuries * 10)
                    print(f"  {country} plays aggressively!")
                    if win_chance > 70:
                        print("  High risk pays off!")
                        morale = morale + 15
                    else:
                        print("  Aggression backfires!")
                        injuries = injuries + 2
                        morale = morale - 12
                elif intensity == "conservative":
                    win_chance = strength * 0.8 + defender + morale * 0.3 - (injuries * 5)
                    print(f"  {country} plays it safe.")
                    morale = morale + 5
                elif intensity == "normal":
                    avg = (keeper + defender + midfielder + forward) / 4
                    win_chance = strength * 0.5 + avg * 0.5 + morale * 0.4 - (injuries * 8)
                    print(f"  {country} plays a balanced game.")
                else:
                    print("  Invalid choice. Using normal.")
                    avg = (keeper + defender + midfielder + forward) / 4
                    win_chance = strength * 0.5 + avg * 0.5 + morale * 0.4 - (injuries * 8)
                    pass

                if goat == 1:
                    win_chance = win_chance + 10
                    print("  ★ GOAT effect lifts the team!")

                # Determine opponent's defense power
                opp_name = team2 if team1 == country else team1
                opp_idx = get_team_index(opp_name)
                opp_def_power = teams[opp_idx][5] * 0.3 + teams[opp_idx][19] * 0.35 + teams[opp_idx][18] * 0.35

                random_number = random.randint(1, 100)
                total = win_chance * 0.2 + random_number

                if total > 55:
                    my_goals = random.randint(1, 5)
                    opp_goals = random.randint(0, my_goals - 1)
                    print(f"  Result: {country} {my_goals} - {opp_goals} {opp_name} ★ WIN!")
                    morale = morale + 10
                    strength = strength + 3
                    next_round_teams.append(country)
                else:
                    my_goals = random.randint(0, 2)
                    opp_goals = random.randint(my_goals + 1, 5)
                    print(f"  Result: {country} {my_goals} - {opp_goals} {opp_name} ★ LOSS")
                    user_in_tournament = False
                    break

                if morale > 100:
                    morale = 100
                if strength > 100:
                    strength = 100

            else:
                # Auto-simulate this match
                g1, g2 = auto_match(team1, team2)
                if g1 > g2:
                    winner = team1
                    loser = team2
                elif g2 > g1:
                    winner = team2
                    loser = team1
                else:
                    # Draw - winner by penalties
                    if random.randint(0, 1) == 0:
                        winner = team1
                        loser = team2
                    else:
                        winner = team2
                        loser = team1
                    g1 = g1
                    g2 = g2
                next_round_teams.append(winner)
                print(f"   {team1} {g1} - {g2} {team2}  → {winner} advances")

        if not user_in_tournament:
            print(f"\n  {country} eliminated in the {current_round_name}. Tournament over!")
            tournament_over = True
            break

        # Show who advanced
        current_round_teams = next_round_teams
        print()
        print(f"  Teams advancing to next round:")
        for t in current_round_teams:
            print(f"    ★ {t}")
        round_number = round_number + 1

# ==============================
# FINAL RESULT
# ==============================
if strength > 100:
    strength = 100
if morale > 100:
    morale = 100

print()
print("=" * 60)
print("   TOURNAMENT RESULT")
print("=" * 60)
print()
print(f"  Team: {country}")
print(f"  FIFA Ranking: #{fifa_rank}")
print(f"  Final Strength: {strength}")
print(f"  Final Morale: {morale}")
print(f"  Total Injuries: {injuries}")
print()

if round_number == 5 and user_in_tournament:
    print("  ★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★")
    print(f"  ★       {country.upper()} WINS THE 2026 WORLD CUP!      ★")
    print("  ★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★")
    print("  Congratulations, champion manager!")
else:
    if user_qualified:
        print(f"  Eliminated in: {rounds_knockout[round_number]}")
    else:
        print("  Eliminated in: Group Stage")
    print("  Better luck next time!")

print()
print("  Thanks for playing!")
print("=" * 60)
print()
