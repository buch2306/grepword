#!/bin/bash
# Step 1: Define the directory where the code will be stored
INSTALL_DIR="$HOME/search-word-cli"

# Step 2: Clone the repository if it doesn't already exist
if [ ! -d "$INSTALL_DIR" ]; then
    echo "Cloning the repository..."
    git clone https://github.com/yourusername/search-word-cli.git "$INSTALL_DIR"
else
    echo "Repository already cloned."
fi

# Navigate to the source directory
cd "$INSTALL_DIR"

# Step 3: Install the required dependencies
echo "Installing dependencies..."
pip3 install -r requirements.txt

# Step 4: Create a simple executable bash script that runs the Python module
EXECUTABLE_PATH="$HOME/.local/bin/grepword"
mkdir -p "$(dirname "$EXECUTABLE_PATH")"

echo "Creating executable script at $EXECUTABLE_PATH"
cat > "$EXECUTABLE_PATH" << 'EOF'
#!/bin/bash
# This script runs the search_word_cli Python module
python3 -m search_word_cli.main "$@"
EOF

# Make the script executable
chmod +x "$EXECUTABLE_PATH"

# Step 5: Check if .local/bin is in PATH, add if necessary
if [[ ":$PATH:" != *":$HOME/.local/bin:"* ]]; then
    echo "Adding ~/.local/bin to your PATH"
    
    # Determine which shell configuration file to use
    SHELL_CONFIG=""
    if [ -f "$HOME/.bashrc" ]; then
        SHELL_CONFIG="$HOME/.bashrc"
    elif [ -f "$HOME/.bash_profile" ]; then
        SHELL_CONFIG="$HOME/.bash_profile"
    elif [ -f "$HOME/.zshrc" ]; then
        SHELL_CONFIG="$HOME/.zshrc"
    fi
    
    if [ -n "$SHELL_CONFIG" ]; then
        echo 'export PATH="$HOME/.local/bin:$PATH"' >> "$SHELL_CONFIG"
        echo "Added PATH update to $SHELL_CONFIG"
        echo "Please run: source $SHELL_CONFIG"
    else
        echo "Warning: Could not find shell configuration file."
        echo "Please manually add this line to your shell configuration:"
        echo 'export PATH="$HOME/.local/bin:$PATH"'
    fi
else
    echo "~/.local/bin is already in your PATH"
fi

# Create a symlink to the main Python file in the installation directory
# This ensures the module can be found regardless of current directory
echo "Setting up Python module..."
mkdir -p "$INSTALL_DIR/search_word_cli"
touch "$INSTALL_DIR/search_word_cli/__init__.py"

# If main.py exists but not in the proper module structure, move it
if [ -f "$INSTALL_DIR/main.py" ] && [ ! -f "$INSTALL_DIR/search_word_cli/main.py" ]; then
    echo "Moving main.py to the proper module structure..."
    cp "$INSTALL_DIR/main.py" "$INSTALL_DIR/search_word_cli/main.py"
fi

echo ""
echo "Installation complete! You can now use the 'grepword' command directly from anywhere."
echo "If the command is not found, make sure ~/.local/bin is in your PATH."
echo "You may need to restart your terminal or run: source ~/.bashrc (or your shell's config file)"