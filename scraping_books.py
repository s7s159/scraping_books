import requests
from bs4 import BeautifulSoup
import pandas as pd

titles = []
prices = []
availabilities = []
ratings = []

page = 1
while page <= 50:
    #to get the url of every page in the website
    url = f"https://books.toscrape.com/catalogue/page-{page}.html"

    # fetch the html code from the webpage
    response = requests.get(url)

    # if the webpage got fetched it returns 200 if an error happened it returns 404
    if response.status_code == 200:
        print(f"Successfully fetched the webpage {page}\n")
    else:
        print("Unable to fetch the webpage\nClosing program...")
        quit()

    # it creates an object from beautifulsoup lib with the content of the webpage in html
    soup = BeautifulSoup(response.content, 'html.parser')

    # fetch all the books with the tag name 'article' and the argument 'product_pod'
    books = soup.find_all('article', class_='product_pod')

    # a loop to store data from every book
    for book in books:
        # search for an argument named "title" in tag name 'a' in 'h3' and returns the text in the title
        title = book.h3.a['title'] # title="some words"
        titles.append(title)

        # search for the class "price_color" within the tag name 'p' and returns the text after it
        price = book.find('p', class_='price_color').text # <p class=price_color>$50.77</p>
        prices.append(price[1:])

        availability = book.find('p', class_='instock availability').text.strip()
        availabilities.append(availability)

        # search for the tag name 'p' with class named "class" and returns the second word in the text
        rating = book.p['class'][1] # class="some words"
        ratings.append(rating)

    # to go to the next page
    page += 1

# to store data into a dataframe(rows and columns)
books_df = pd.DataFrame({
    'Title': titles,
    'Price': prices,
    'Availability': availabilities,
    'Rating': ratings
})

# converting and saving it in csv file
books_df.to_csv('Books.csv', index=False)
print("Data is exported successfully")