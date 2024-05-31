from bs4 import BeautifulSoup
import requests

def scrape_movies():
    """
    Scrapes the Empire Online website to get a list of the best movies.

    Returns:
        list: A list of movie titles.
    """
    # Send a GET request to the website
    response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
    response.raise_for_status()

    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all movie titles on the page and store them in a list
    movies = [movie.getText() for movie in soup.find_all(name="h3", class_="title")[::-1]]

    # Write the movie titles to a text file
    with open("movies.txt", mode="w", encoding="utf-8") as file:
        file.writelines("\n".join(movies))


# Call the function to scrape the movies
scrape_movies()
