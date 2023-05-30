# Movie Recommendation System

This is a movie recommendation system project that utilizes web scraping, exploratory data analysis (EDA), and content-based filtering to provide movie recommendations based on user preferences.

## Project Overview

The Movie Recommendation System project aims to create a personalized movie recommendation system by analyzing movie data and user preferences. The project incorporates the following steps:

- Web scraping: Data is scraped from IMDb or another movie database to gather movie information such as titles, genres, ratings, and cast.
- Data cleaning: The scraped data is cleaned by handling missing values, removing duplicates, and standardizing the format.
- Exploratory Data Analysis (EDA): The dataset is explored to gain insights into movie trends, popular genres, and average ratings.
- Data visualization: Visualizations are created to illustrate movie ratings, genre distributions, and other relevant patterns.
- Movie recommendation: A content-based filtering approach is implemented to recommend movies to users based on their preferences.
- Evaluation: The performance of the recommendation system can be assessed using metrics like precision, recall, or mean average precision.

## Installation

1. Clone the repository: [Movie-Recommendation-System-lessData-Analisisgreater](https://github.com/judinilson/Movie-Recommendation-System-lessData-Analisisgreater)


2. Install the required dependencies:
pip install -r requirements.txt


3. Run the main script:
python main.py


## Usage

1. Modify the web scraping code in `scrape_data.py` to scrape movie data from your preferred movie database.
2. Clean the scraped data and perform EDA in the `data_cleaning.ipynb` notebook.
3. Implement the content-based filtering recommendation system in the `recommendation.py` script.
4. Run the main script `main.py` to get movie recommendations for a given movie title.
5. Modify and extend the project as per your requirements.

## Contributing

Contributions to this project are welcome. Feel free to open an issue or submit a pull request with any improvements or additional features.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- [IMDb](https://www.imdb.com/) for providing the movie data.
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) and [Scrapy](https://scrapy.org/) for web scraping.
- [Pandas](https://pandas.pydata.org/) and [scikit-learn](https://scikit-learn.org/) for data manipula
