# Pet Pantry 🐾

Welcome to **Pet Pantry**, a Django-based web application designed to help manage and organize pet-related items efficiently. 

## 🌐 Live Application
The application is deployed and currently live! You can access it here:
**[https://pet-pantry-awdx.onrender.com](https://pet-pantry-awdx.onrender.com)**

*(Note: The application is hosted on Render's free tier. If the site hasn't been visited in the last 15 minutes, it may take 30-60 seconds to wake up on your first visit.)*

## 🛠️ Built With
* **Framework:** [Django](https://www.djangoproject.com/) (Python)
* **Database:** PostgreSQL (Production) / SQLite (Local)
* **Hosting:** [Render](https://render.com/)

## 🚀 Running Locally

If you'd like to run this project on your local machine, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/cimilcharly/Pet-Pantry.git
   cd Pet-Pantry
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Database Migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Start the Development Server:**
   ```bash
   python manage.py runserver
   ```
   *The application will be available at `http://127.0.0.1:8000/`*
