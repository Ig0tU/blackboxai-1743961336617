
Built by https://www.blackbox.ai

---

```markdown
# Poe Multi-Model Bot

## Project Overview
The Poe Multi-Model Bot is a server bot built using the `fastapi_poe` library that integrates multiple AI models, specifically **Claude 3.7 Sonnet** and **Google Gemini Pro**. This bot is designed to allow users to interact with these advanced AI models seamlessly while ensuring that the inference costs are covered by the developer's Poe account.

## Installation
To set up the project, ensure you have Python 3.8 or higher installed on your system. Follow these steps to install the necessary dependencies:

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```
2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install the required dependencies:
   ```bash
   pip install fastapi_poe uvicorn python-dotenv
   ```

## Usage
1. Create a `.env` file in the root of your project with the following content:
   ```
   BOT_NAME=your_bot_name
   ACCESS_KEY=your_access_key
   ```
   Replace `your_bot_name` and `your_access_key` with your actual Poe bot credentials.

2. Start the server locally with:
   ```bash
   uvicorn main:app --reload
   ```

3. Access the bot through the endpoint provided by Uvicorn, typically at `http://127.0.0.1:8000`.

## Features
- **Multi-Model Support**: Leverage both Claude 3.7 Sonnet and Google Gemini Pro for enhanced user interactions.
- **Environment Variable Management**: Securely manage credentials using environment variables, preventing hardcoding sensitive information.
- **Dynamic Response Handling**: The bot can handle and yield responses from multiple models based on user input.

## Dependencies
The project relies on the following Python packages, which are specified in the `requirements.txt` or `setup.py`:
- `fastapi_poe`
- `uvicorn`
- `python-dotenv`

## Project Structure
The project consists of the following structure:
```
/<project-root>
│
├── .env                     # Environment variables configuration
├── main.py                  # Main application code
├── README.md                # Documentation of the project
└── venv/                    # Virtual environment directory
```

### `main.py`
This file contains the implementation of the `MultiModelBot` class. It handles user requests and manages responses from Claude 3.7 Sonnet and Google Gemini Pro. Key functionalities include:
- `get_response(request: QueryRequest)`: Asynchronously gets responses from both models and yields texts.
- `get_settings(setting: SettingsRequest)`: Sets up the bot’s dependencies and configurations.

## Running the Bot
To deploy the bot, you can use cloud platforms like Vercel or Heroku. Ensure to set your environment variables appropriately in the hosting platform.

1. **Deploy to Vercel**:
   - Create a `vercel.json` configuration file.
   - Use the Vercel CLI to deploy:
   ```bash
   vercel --prod
   ```

2. **Update Poe Settings**:
   - After deployment, update your bot's settings on the Poe platform to include the deployed server URL.

## Troubleshooting
- **Missing Environment Variables**: Ensure that your `.env` file has valid entries for `BOT_NAME` and `ACCESS_KEY`.
- **Response Issues**: Check that the models are correctly referenced in the bot's settings and responses.
- **Rate Limit Exceeded**: Ensure that you are staying within the usage limits of the Poe platform to avoid additional charges.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
```