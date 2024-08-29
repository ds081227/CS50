import random
import fpdf
import sys
import requests
import os

def main():
    match = []
    match_schedule =[]
    top_6 = []
    bot_6 = []
    checker("teams.txt")
    top_6, bot_6 = reader("teams.txt")
    get_font()
    while True:
        match.clear()
        match_schedule.clear()
        match.extend(draw_in_same_group(top_6))
        match.extend(draw_in_same_group(bot_6))
        match.extend(draw_in_diff_group(top_6, bot_6))
        random.shuffle(match)
        match_schedule = schedule(match)
        if all(len(week) == 6 for week in match_schedule):
            break
    match_schedule.append(matching(top_6,bot_6))
    pdf_output(match_schedule)
    os.remove('msjh.pkl')
    os.remove('msjh.cw127.pkl')


def draw_in_same_group(teams):
    match = []
    times = {}
    loop_counter = 0
    times = {team: 0 for team in teams}
    while not all(times[team] == 2 for team in times):
        loop_counter += 1
        if loop_counter < 50:
            team1 = random.choice(teams)
            team2 = random.choice(teams)
            if team1 != team2 and times[team1] < 2 and times[team2] < 2:
                if f"{team1} vs {team2}" not in match and f"{team2} vs {team1}" not in match:
                    match.append(f"{team1} vs {team2}")
                    times[team1] += 1
                    times[team2] += 1
                    loop_counter += 1
                else:
                    continue
        else:
            match.clear()
            times = {team: 0 for team in teams}
            loop_counter = 0
    return match


def draw_in_diff_group(grp1,grp2):
    match = []
    times = {}
    loop_counter = 0
    times = {team: 0 for team in (grp1 + grp2)}
    while not all(times[team] == 2 for team in times):
        loop_counter += 1
        if loop_counter < 50:
            team1 = random.choice(grp1)
            team2 = random.choice(grp2)
            if times[team1] < 2 and times[team2] < 2:
                if f"{team1} vs {team2}" not in match and f"{team2} vs {team1}" not in match:
                    match.append(f"{team1} vs {team2}")
                    times[team1] += 1
                    times[team2] += 1
                    loop_counter += 1
        else:
            match.clear()
            loop_counter = 0
            times = {team: 0 for team in (grp1 + grp2)}
    return match

def schedule(match_list):
    matches = [[],[],[],[]]
    for week in matches:
        for match in match_list[:]:
            team1, team2 = match.split(" vs ")
            if not any(team1 in scheduled_match or team2 in scheduled_match for scheduled_match in week):
                week.append(match)
                match_list.remove(match)
    return matches

def matching(grp1,grp2):
    matches = []
    for i in range(0,len(grp1 + grp2),2):
        matches.append((f"{(grp1 + grp2)[i]} vs {(grp1 + grp2)[(i + 1)]}"))
    return matches

def checker(filename):
    with open(filename, "r") as file:
        line_number = 0
        for line in file:
            if not line.isspace():
                line_number += 1
        if line_number != 12:
            sys.exit("Invalid number of teams")
        else:
            return True

def get_font():
    response = requests.get("https://raw.githubusercontent.com/lenyi/Microsoft/master/libs/msjh.ttf")
    with open('msjh.ttf', 'wb') as file:
        file.write(response.content)

def reader(filename):
    top_6 = []
    bot_6 = []
    with open(filename , "r") as file:
        lines = file.readlines()
        for line in lines[:6]:
            top_6.append(line.strip())
        for line in lines[6:]:
            bot_6.append(line.strip())
        return top_6, bot_6

def pdf_output(schedule_list):
    pdf = fpdf.FPDF(format='letter')
    pdf.add_font('MSJH','','msjh.ttf',True)
    pdf.set_font('MSJH', '', 14)
    pdf.add_page()
    i = 0
    for weeks in schedule_list:
        pdf.write(15,f"Week{i + 1}")
        pdf.ln()
        i += 1
        for matches in weeks:
            team1, team2 = matches.split(" vs ")
            pdf.set_x(20)
            pdf.cell(0, 11, txt = team1)
            pdf.set_x(100)
            pdf.cell(0, 11, txt = "vs")
            pdf.set_x(130)
            pdf.cell(0, 11, txt = team2)
            pdf.ln()
    pdf.output("schedule.pdf")

if __name__ == "__main__":
    main()


