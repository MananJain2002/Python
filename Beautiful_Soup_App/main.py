from bs4 import BeautifulSoup
import requests

# Send a GET request to the specified URL
response = requests.get("https://news.ycombinator.com/news")

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Find all the <span> elements with class 'titleline'
articles = soup.find_all(name='span', class_='titleline')

# Extract the <a> tags from each <span> element
anchor_tags = [article.find("a") for article in articles]

# Extract the text from each <a> tag
article_texts = [tag.getText() for tag in anchor_tags]

# Extract the 'href' attribute from each <a> tag
article_links = [link.get("href") for link in anchor_tags]

# Find all the <td> elements with class 'subtext'
upvotes = soup.find_all(name="td", class_="subtext")

# Extract the upvote count for each article
article_upvotes = [0 if upvote.find(name="span", class_="score") == None else int((upvote.find(name="span", class_="score").string).split(" ")[0]) for upvote in upvotes]

# Find the index of the article with the maximum upvotes
ind = article_upvotes.index(max(article_upvotes))

# Print the text, link, and upvote count of the article with the maximum upvotes
print(article_texts[ind])
print(article_links[ind])
print(article_upvotes[ind])