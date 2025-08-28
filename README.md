# Search & Analysis Agent Project
This project provides an example of an autonomous agent built with LangChain and advanced search capabilities. The agent is designed to perform searches and analyze information on the web. The project uses the highly efficient uv package manager to handle its Python dependencies.

## ⚙️ Installation and Setup
You have two options to set up the project: automated or manual.

### Automated Installation
To get the project up and running quickly, you can execute the provided installation script, which will handle all necessary dependencies.

Save the Script: Ensure the installation script (e.g., install_uv.sh) is in your project directory.

Run the Script: Open Git Bash, PowerShell, or WSL in the project directory and run the following command:

bash install_uv.sh

### Manual Installation
If you prefer to install dependencies directly without the script, you can use the following uv commands. First, ensure uv is installed on your system.

* If uv is not installed on Windows, run the following from PowerShell:
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
* Verify uv is installed
uv --version
* Initialize a new uv environment
* You may need to configure your IDE (e.g., PyCharm) to use this interpreter.
uv init
* Add the core dependencies
uv add langchain
uv add langchain-anthropic
uv add python-dotenv
uv add black isort
uv add langchain-community
uv add langchainhub
uv add langchain-ollama
uv add langchain-tavily
uv add flask
uv add langchain-aws boto3 pydantic

## 📦 Project Contents
The project relies on several key libraries to function:

* uv: An extremely fast Python package manager used for installing and managing dependencies.

* langchain: The core library for building LLM-powered agent applications.

* langchain-anthropic / langchain-ollama: Integrations for large language models.

* langchain-tavily: A search tool that allows the agent to perform web searches for up-to-date information.

* pydantic: A library used for data validation and parsing search results into structured objects.

* flask: A lightweight web server used to expose the agent's functionality via a simple web interface.

* boto3 / langchain-aws: Integration with Amazon Web Services.

* python-dotenv: A utility for easily loading environment variables from a .env file to securely manage API keys.

## 🔗 Usage
The project's main entry point is app.py. This script contains the logic for the search agent and also serves a web application using Flask.

* To run the application, use the following command from your terminal:

uv run python app.py

* Once the server is running, you can access the application in your browser at:
http://127.0.0.1:5000