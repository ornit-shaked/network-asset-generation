# This script is for Windows using PowerShell. It checks for uv, installs it if needed,
# and then uses it to install a list of Python packages.

# --- 1. Check for uv installation and install if not present ---
echo "Starting Python project setup with uv..."

# The PowerShell command checks if 'uv' exists in the PATH
# We are using 'powershell -c' to run this command from the bash script.
if ! command -v uv &> /dev/null
then
    echo "uv is not installed. Installing it now using PowerShell..."
    # The PowerShell command from your instructions to install uv
    powershell -ExecutionPolicy Bypass -c "irm https://astral.sh/uv/install.ps1 | iex"
    # Check if the installation was successful
    if [ $? -ne 0 ]; then
        echo "❌ Error: Failed to install uv via PowerShell."
        echo "Please run the command manually: powershell -ExecutionPolicy Bypass -c 'irm https://astral.sh/uv/install.ps1 | iex'"
        exit 1
    fi
    echo "✅ uv installed and should be on your PATH."
else
    echo "✅ uv detected."
fi

# --- 2. Verify uv installation by checking its version ---
echo "Verifying uv installation..."
uv --version

# Check the exit code of the version command
if [ $? -ne 0 ]; then
    echo "❌ Error: uv is not correctly installed or not on the PATH."
    exit 1
fi
echo "✅ uv version confirmed."

# --- 3. Define the list of packages to add and install in a single command ---
# This list is based on your request.
declare -a PACKAGES=(
    "langchain"
    "langchain-anthropic"
    "python-dotenv"
    "black"
    "isort"
    "langchain-community"
    "langchainhub"
    "langchain-ollama"
    "langchain-tavily"
    "flask"
    "langchain-aws"
    "boto3"
    "pydantic"
)

# --- 4. Add and install all packages in one go ---
echo "📦 Adding and installing all packages in one command..."
uv add "${PACKAGES[@]}"

# Check the exit code of the last command
if [ $? -ne 0 ]; then
    echo "❌ Error: Failed to add and install one or more packages."
    echo "Please check the error message above and try again."
    exit 1
fi

echo ""
echo "✨ All specified dependencies have been added and installed successfully!"
echo "Your `pyproject.toml` file has been updated."
echo "You can now run your project scripts."
