from bs4 import BeautifulSoup
import requests
import pandas as pd

years = [1930, 1934, 1938, 1950, 1954, 1958, 1962, 1966, 1970, 
                        1974, 1978, 1982, 1986, 1990, 1994, 1998, 2002, 2006, 
                        2010, 2014, 2018, 2022]


def get_matches(year):
    web = f'https://en.wikipedia.org/wiki/{year}_FIFA_World_Cup'
    response = requests.get(web)

    content = response.text

    soup = BeautifulSoup(content, 'lxml')

    matches = soup.find_all('div', class_='footballbox')

    home = []
    score = []
    away = []

    for match in matches:
        home.append(match.find('th', class_="fhome").get_text())
        score.append(match.find('th', class_="fscore").get_text())
        away.append(match.find('th', class_="faway").get_text())

    dict_football = {'home': home, 'score': score, "away":away}
    df_football = pd.DataFrame(dict_football)
    df_football['year'] = year
    return(df_football)


# print(get_matches('1990'))

fifa = [get_matches(year) for year in years]
df_fifa = pd.concat(fifa, ignore_index=True)
df_fifa.to_csv('fifa_worldcup_historical_data.csv', index=False)

# Note: Not every single wikipedia page follows the same HTML format so we have some missing data like in year 1982, so I will use selenium to handle that, and then clean/transform data later!
# Upon further research wikipedia has fixed most of this issue the only anamoly is year 1990