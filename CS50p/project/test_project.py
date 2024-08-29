from project import draw_in_same_group, draw_in_diff_group, checker, reader
from unittest.mock import mock_open, patch
import pytest

top_6 = ["team_1", "team_2", "team_3", "team_4", "team_5", "team_6"]
bot_6 = ["team_7", "team_8", "team_9", "team_10", "team_11", "team_12"]

def test_checker():
    mock_file = mock_open(read_data='line1\nline2\nline3\n')
    with patch('builtins.open', mock_file):
        with pytest.raises(SystemExit) as e:
            checker('any_filename')
        assert str(e.value) == "Invalid number of teams"

def test_reader():
    top_6 = []
    bot_6 = []
    mock_file = mock_open(read_data='line1\nline2\nline3\nline4\nline5\nline6\nline7\nline8\nline9\nline10\nline11\nline12\n')
    with patch('builtins.open', mock_file):
         top_6, bot_6 = reader(mock_file)
    assert len(top_6) == 6
    assert len(bot_6) == 6

def test_draw_in_same_group():
    teams = ["team_1", "team_2", "team_3", "team_4", "team_5", "team_6"]
    matches = draw_in_same_group(top_6)
    assert len(matches) == 6
    for team in teams:
        assert sum(team in match.split(" vs ") for match in matches) == 2

def test_draw_in_diff_group():
    teams = ["team_1", "team_2", "team_3", "team_4", "team_5", "team_6", "team_7", "team_8", "team_9", "team_10", "team_11", "team_12"]
    matches = draw_in_diff_group(top_6, bot_6)
    assert len(matches) == 12
    print(matches)
    for team in teams:
        print(f"Checking {team}")
        assert sum(team in match.split(" vs ") for match in matches) == 2

