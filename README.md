🎬 Movie Recommendation System
A Machine Learning-based Movie Recommendation System that suggests movies to users based on their preferences. This project uses Natural Language Processing (NLP) and Content-Based Filtering techniques to recommend similar movies using features like genre, cast, keywords, and overview.

🚀 Features
Recommend movies similar to a selected movie
Content-based recommendation using similarity score
NLP techniques for text processing
Fast and accurate suggestions
User-friendly interface
Works without user history

🧠 Technologies Used
Python
Machine Learning
Natural Language Processing (NLP)
Pandas
NumPy
Scikit-learn
NLTK
Streamlit / Flask (if used for UI)

📂 Dataset
The system uses a movie dataset containing:
Movie titles
Genres
Cast
Crew
Keywords
Overview
Dataset Source: TMDB Movie Dataset

⚙️ How It Works
Movie data is preprocessed and cleaned
Important features are combined into a single text column
NLP techniques (tokenization, stemming, etc.) are applied
Text is converted into numerical vectors using CountVectorizer
Cosine similarity is calculated between movies
Top similar movies are recommended to the user

💻 Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/naharaarushi/movie-recommendation-system.git
cd movie-recommendation-system
2️⃣ Install dependencies
pip install -r requirements.txt
3️⃣ Run the application
python app.py
(or)
streamlit run app.py

📸 Example Output
Input: Selected movie name
Output: List of recommended movies with high similarity

🎯 Applications
OTT platforms (Netflix-like systems)
E-commerce recommendations
Personalized content delivery
Entertainment apps

📌 Future Improvements
Collaborative filtering integration
Hybrid recommendation system
User login and history tracking
Real-time recommendations
Deployment on cloud
👩‍💻 Author
Aarushi Nahar
BCA Student | Machine Learning Enthusiast
GitHub: https://github.com/naharaarushi
