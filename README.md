# Film Recommendation System

## Overview
This project features a personalised film recommendation system using a Python-based machine learning backend and a React front-end. The system uses collaborative filtering, specifically through a cosine similarity matrix, to provide film suggestions tailored to individual user preferences.

## Frontend
The frontend can be found here: https://millie-ellis.com/recosys
This site has links to the frontend repo

## Project Structure
- `api/`: Flask API handling backend requests.
- `Data/`: Contains movie metadata and user ratings.
- `models/`: Machine learning models and utilities.
- `tests/`: Test cases for API endpoints and data processing.
- `utils/`: Helper scripts for data preprocessing and other utilities.
- `main.py`: The main Flask application file that initialises the app and routes.
- `collab_recommendation.py`: Implementation of the collaborative filtering algorithm.

## Technologies Used
- **Languages**: Python for the backend, JavaScript (React) for the frontend.
- **Frameworks/Libraries**:
  - Flask for creating the API.
  - React for building the interactive frontend.
- **Data Sources**:
  - User ratings and movie metadata from [Kaggle's The Movies Dataset](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset).

## Setup and Installation
1. **Clone the Repository**:
    ```
    git clone https://github.com/milbot1992/film-recosys.git
    cd film-recosys
    ```

2. **Install Dependencies**:
    - Backend:
        ```
        pip install -r requirements.txt
        ```
    - Frontend (assuming a separate directory):
        ```
        cd path/to/frontend
        npm install
        ```

3. **Running the Backend**:
    - Start the Flask server:
        ```
        python main.py
        ```
    - This will host the API on `http://localhost:5000/`.

4. **Running the Frontend**:
    - Navigate to the frontend directory and start the React app:
        ```
        npm start
        ```
    - This will serve the frontend on `http://localhost:3000/`.

## API
- The backend functions as an API connecting to the React frontend.
- Endpoints include user creation, fetching recommendations, and accessing trending data.

## Live App
Explore the live app to see the recommendation system in action. You can change the user view using dropdown options to see different personalised recommendations.
Live app: https://millie-ellis.com/recosys


## GitHub Repositories
- **Python API Backend**: [Film Recommendation Backend Repo](https://github.com/milbot1992/film-recosys)
- **React Frontend**: [Frontend Repo](https://github.com/milbot1992/data-projects)
