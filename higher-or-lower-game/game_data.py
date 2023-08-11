import pandas as pd

def get_data():
    url = "https://www.sacnilk.com/news/List_of_MostFollowed_Instagram_Handle_in_World"
    tables = pd.read_html(url)
    df = tables[0]
    df = df[['Instagram Account', 'Followers [In Million]', 'Profession', 'Country/Continent']]
    data = df.values.tolist()
    return data
