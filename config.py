import os

# OpenAI API Key (or other LLM provider)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your_openai_api_key_here")

# Pinecone API Key and Environment
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY", "your_pinecone_api_key_here")
PINECONE_ENVIRONMENT = os.getenv("PINECONE_ENVIRONMENT", "your_pinecone_environment_here")

# AWS Credentials (if using AWS Lambda or other AWS services)
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID", "your_aws_access_key_id_here")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY", "your_aws_secret_access_key_here")
AWS_REGION = os.getenv("AWS_REGION", "us-east-1") # Example region

# Database Connection String (for Postgres/SQLite)
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@host:port/database")

# Other application-specific settings
APP_NAME = "Agentic AI Business Workflow Manager"
DEBUG_MODE = os.getenv("DEBUG_MODE", "True").lower() == "true"

# Example of how to load from .env file (install python-dotenv if needed)
# from dotenv import load_dotenv
# load_dotenv()
