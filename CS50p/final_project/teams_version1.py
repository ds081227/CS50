import random
from fpdf import FPDF
from tabulate import tabulate

def main():
    matches =[]
    top_6 = ["team_1", "team_2", "team_3", "team_4", "team_5", "team_6"]
    bot_6 = ["team_7", "team_8", "team_9", "team_10", "team_11", "team_12"]
    for match in (draw_in_same_group(top_6)):
        matches.append(match)
    for match in (draw_in_same_group(bot_6)):
        matches.append(match)
    for match in (draw_in_diff_grp(top_6, bot_6)):
        matches.append(match)
    print(tabulate(sorted(matches), tablefmt = "grid"))
    print(len(matches))

def draw_in_same_group(teams):
    match = []
    temp_list = []
    i = 0
    for team in teams:
        while temp_list.count(team) < 2:
            temp_list.append(team)
    while i < 6:
        versus = sorted(random.sample(temp_list, k = 2))
        if versus[0] != versus[1] and versus not in match:
            match.append(versus)
            temp_list.remove(versus[0])
            temp_list.remove(versus[1])
            i += 1
    return match

def draw_in_diff_grp(grp1, grp2):
    i = 0
    match = []
    temp_top = []
    temp_bot = []
    for team in grp1:
        while temp_top.count(team) < 2:
            temp_top.append(team)
    for team in grp2:
        while temp_bot.count(team) < 2:
            temp_bot.append(team)
    while i < 12:
        team1 = random.choice(temp_top)
        team2 = random.choice(temp_bot)
        versus = [team1, team2]
        if versus not in match:
            match.append(versus)
            temp_top.remove(team1)
            temp_bot.remove(team2)
            i += 1
    return match


if __name__ == "__main__":
    main()
