#!/bin/bash

# Install required packages
echo "Installing dependencies..."
pip install fastapi_poe uvicorn python-dotenv

# Create .env file with credentials
echo "Creating .env file..."
cat > .env << EOL
BOT_NAME=Db9UruEOCoATD4Tc3_TduQ==
ACCESS_KEY=BPnZOKJwEjcDgzWEcf9rop3dNSZ6l8qP2OlTCz1dgA==
EOL

# Make the script executable
chmod +x setup_bot.sh

# Run the server
echo "Starting the server..."
echo "Server will be available at http://localhost:8000"
uvicorn main:app --reload --port 8000