import requests
from bs4 import BeautifulSoup
# import mysql.connector
# import logging

# url = "https://www.imdb.com/chart/top/"

# logging.basicConfig(filename="imdb.log", level=logging.INFO,
#                     format="%(asctime)s:%(levelname)s:%(message)s")

# """ Database setup"""

# def create_table():
#     try:
#         mydb = mysql.connector.connect(
#             host="localhost",
#             user="root",
#             password="root",
#             database="imdb"
#         )
#         mycursor = mydb.cursor()

#         mycursor.execute("CREATE TABLE IF NOT EXISTS movie (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), rating FLOAT)")
#         mycursor.commit()
#         logging.info("Table created successfully")
#         mycursor.close()
#         mydb.close()

#     except Exception as e:
#         logging.error(f"Error creating table: {e}")


# def insert_data(name, rating):
#     try:
#         mydb = mysql.connector.connect(imdb.db)



URL = "https://www.imdb.com/chart/top/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

try:
    response = requests.get(URL )
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    movies = soup.select("li.ipc-metadata-list-summary-item")[:10]  # first 10

    if not movies:
        print("❌ Error: No movies found — IMDb changed structure OR request blocked.")
    else:
        for i, movie in enumerate(movies, start=1):
            title = movie.select_one("h3").get_text(strip=True)
            rating = movie.select_one("span.ipc-rating-star--rating")

            rating = rating.get_text(strip=True) if rating else "N/A"

            print(f"{title} ⭐ {rating}")

except Exception as e:
    print(f"⚠ Error: {e}")
