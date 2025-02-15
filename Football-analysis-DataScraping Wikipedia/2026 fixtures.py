import pandas as pd

# Defining sample data for the 2026 FIFA World Cup fixtures
fixtures_2026 = [
    ["USA", "Match 1", "Mexico", 2026],
    ["Canada", "Match 2", "Costa Rica", 2026],
    ["USA", "Match 18", "Canada", 2026],
    ["Mexico", "Match 19", "Costa Rica", 2026],
    ["Costa Rica", "Match 35", "Canada", 2026],
    ["Mexico", "Match 36", "USA", 2026],
    ["Brazil", "Match 3", "Argentina", 2026],
    ["France", "Match 4", "Germany", 2026],
    ["Germany", "Match 17", "Argentina", 2026],
    ["Brazil", "Match 20", "France", 2026],
    ["Germany", "Match 33", "Brazil", 2026],
    ["Argentina", "Match 34", "France", 2026],
    ["Spain", "Match 8", "Japan", 2026],
    ["England", "Match 7", "Portugal", 2026],
    ["Portugal", "Match 22", "Japan", 2026],
    ["Spain", "Match 24", "England", 2026],
    ["Portugal", "Match 39", "Spain", 2026],
    ["Japan", "Match 40", "England", 2026],
    ["Netherlands", "Match 6", "Denmark", 2026],
    ["Italy", "Match 5", "Belgium", 2026],
    ["Denmark", "Match 21", "Belgium", 2026],
    ["Italy", "Match 23", "Netherlands", 2026],
    ["Belgium", "Match 37", "Netherlands", 2026],
    ["Denmark", "Match 38", "Italy", 2026],
    ["Winners Group A", "Match 49", "Runners-up Group B", 2026],
    ["Winners Group C", "Match 50", "Runners-up Group D", 2026],
    ["Winners Group D", "Match 52", "Runners-up Group C", 2026],
    ["Winners Group B", "Match 51", "Runners-up Group A", 2026],
    ["Winners Match 57", "Match 61", "Winners Match 58", 2026],
    ["Winners Match 59", "Match 62", "Winners Match 60", 2026],
    ["Losers Match 61", "Match 63", "Losers Match 62", 2026],
    ["Winners Match 61", "Match 64", "Winners Match 62", 2026]
]

# Creating a DataFrame
df_fixtures_2026 = pd.DataFrame(fixtures_2026, columns=["home", "score", "away", "year"])

df_fixtures_2026.to_csv("clean_fifa_worldcup_fixture.csv", index=False)
