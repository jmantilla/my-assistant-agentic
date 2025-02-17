# Configuration settings for the application
import os

class Config:
    DEBUG = os.getenv('DEBUG', 'False') == 'True'
    DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///default.db')
    API_KEY = os.getenv('API_KEY', 'your_api_key_here')
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key_here')
    # Add other configuration variables as needed

config = Config()