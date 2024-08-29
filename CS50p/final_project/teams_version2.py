import random

def main():
    match = []
    schedule =[]
    top_6 = []
    bot_6 = []
    top_6, bot_6 = reader("teams.txt")
    while True:
        match.clear()
        schedule.clear()
        match.extend(shuffle(top_6))
        match.extend(shuffle(bot_6))
        match.extend(shuffle1(top_6, bot_6))
        schedule = schedule1(match)
        if all(len(week) == 7 for week in schedule):
            break
    writer(schedule)

def shuffle(teams):
    shuffled = []
    random.shuffle(teams)
    for i in range(len(teams)):
        shuffled.append((f"{teams[i]} vs {teams[(i + 1) % len(teams)]}"))
    return (shuffled)

def shuffle1(grp1, grp2):
    shuffled = []
    new_grp2 = random.sample(grp2, k = 6)
    while any(item1 == item2 for item1, item2 in zip(grp2, new_grp2)):
        new_grp2 = random.sample(grp2, k = 6)
    for i in range(len(grp1)):
        shuffled.append((f"{grp1[i]} vs {grp2[i]}"))
        shuffled.append((f"{grp1[i]} vs {new_grp2[i]}"))
    return shuffled

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


def writer(list):
    with open("schedule.txt", "w") as file:
        i = 0
        for item in list:
            file.write(f"Week{i + 1}")
            file.write(f"{item}\n")
            i += 1

def schedule1(match_list):
    matches = [[],[],[],[]]
    for week in matches:
        for match in match_list[:]:
            team1, team2 = match.split(" vs ")
            if not any(team1 in scheduled_match or team2 in scheduled_match for scheduled_match in week):
                week.append(match)
                match_list.remove(match)
    return matches

if __name__ == "__main__":
    main()


