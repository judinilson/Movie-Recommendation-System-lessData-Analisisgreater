import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

# Step 1: Web Scraping
movies_df = pd.read_csv('movies.csv')

# Step 2: Data Cleaning
# Handle missing values
movies_df.dropna(inplace=True)

# Remove duplicates
movies_df.drop_duplicates(subset='title', inplace=True)

# Standardize column formats (e.g., convert genres to lowercase)
movies_df['genres'] = movies_df['genres'].str.lower()

# Step 3: Exploratory Data Analysis (EDA)
# Perform descriptive statistics
print(movies_df['rating'].describe())

# Analyze relationships between variables
average_rating_by_genre = movies_df.groupby('genres')['rating'].mean()
print(average_rating_by_genre)

# Step 4: Data Visualization
# Visualize genre frequencies
genre_counts = movies_df['genres'].value_counts()
genre_counts.plot(kind='bar',
                  xlabel='Genre',
                  ylabel='Count',
                  title='Genre Frequencies')

# Visualize rating distributions
movies_df['rating'].plot(kind='hist',
                         bins=10,
                         xlabel='Rating',
                         ylabel='Count',
                         title='Rating Distribution')

# Step 5: Movie Recommendation
# Implement content-based filtering using movie genres
count_vectorizer = CountVectorizer()
genre_matrix = count_vectorizer.fit_transform(movies_df['genres'])

# Compute cosine similarity matrix based on genre_matrix
cosine_sim = cosine_similarity(genre_matrix, genre_matrix)


# Function to get movie recommendations based on title
def get_movie_recommendations(title, cosine_sim_matrix):
  indices = pd.Series(movies_df.index,
                      index=movies_df['title']).drop_duplicates()
  movie_index = indices[title]
  similarity_scores = list(enumerate(cosine_sim_matrix[movie_index]))
  similarity_scores = sorted(similarity_scores,
                             key=lambda x: x[1],
                             reverse=True)
  recommended_movie_indices = [i[0] for i in similarity_scores[1:6]]
  return movies_df['title'].iloc[recommended_movie_indices]


# Get movie recommendations for a given movie title
recommended_movies = get_movie_recommendations('When in Rome', cosine_sim)
print(recommended_movies)
