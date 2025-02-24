import sys
import requests


def get_match_year(date):
    """
    Returns year from the match date
    """
    return int(date.split('/')[-1])


def get_match_weightage(current_year, match_year):
    """
    Returns weightage of match played at specific yer
    """
    weightage = 10 - (current_year - match_year)
    if weightage < 0:
        weightage = 0.5
    return weightage


def get_team_score(scorecard):
    """
    Returns total team score from scorecard
    """
    total = 0
    for score in scorecard:
        total += score['score']
    return total


def get_winning_team(match):
    """
    Returns winning team of the match (return none if draw)
    """
    team1 = match['team1']
    team2 = match['team2']
    team1_score = get_team_score(match['scoreCardTeam1'])
    team2_score = get_team_score(match['scoreCardTeam2'])
    if team1_score > team2_score:
        winning_team = team1
    elif team2_score > team1_score:
        winning_team = team2
    else:
        winning_team = None
    return winning_team


def get_win_probability(matches, curren_year, teams):
    """
    Returns win probability of both teams given in the teams list
    """
    team1_weightage_points = 0
    team2_weightage_points = 0
    total_weightage_points = 0
    for match in matches:
        team1 = match['team1']
        team2 = match['team2']
        # Both input teams should be in the match
        if team1 not in teams or team2 not in teams:
            continue
        winning_team = get_winning_team(match)
        if winning_team is not None:
            match_year = get_match_year(match['date'])
            match_weightage = get_match_weightage(match_year)
            if team1 == winning_team:
                team1_weightage_points += match_weightage
            else:
                team2_weightage_points += match_weightage
            total_weightage_points += match_weightage
    win_probability = {}
    win_probability[team1] = (team1_weightage_points / total_weightage_points) * 100
    win_probability[team2] = (team2_weightage_points / total_weightage_points) * 100
    return win_probability


if __name__ == "__main__":
    with open(sys.argv[1], "r") as file:
        teams = file.readline().strip().split(',')
    api_url = "https://l0l6pp2i0k.execute-api.eu-north-1.amazonaws.com/default/icc_matches"
    current_year = 2024
    matches = requests.get(api_url)
    win_probability = get_win_probability(matches, current_year, teams)
    team1 = teams[0]
    team2 = teams[1]
    print(round(win_probability[team1], 2), round(win_probability[team2], 2))
