#!/bin/bash
export PATH="/opt/homebrew/bin:$PATH"
# Exit on error and print commands
set -e
set -x

# Path to the project directory
PROJECT_DIR="/Users/admin/Sites/video2text"
VENV_DIR="$PROJECT_DIR/venv"
PYTHON_SCRIPT="$PROJECT_DIR/video2text.py"

# Check if video file is provided
if [ $# -ne 1 ]; then
    echo "Usage: video2text.sh <video_file>"
    exit 1
fi

# Check if file exists
if [ ! -f "$1" ]; then
    echo "Error: File '$1' not found"
    exit 1
fi

# Get absolute path of the input file
VIDEO_FILE=$(realpath "$1")

echo "Processing video: $VIDEO_FILE"
echo "Using Python script: $PYTHON_SCRIPT"

# Check if virtual environment exists
if [ ! -d "$VENV_DIR" ]; then
    echo "Error: Virtual environment not found at $VENV_DIR"
    exit 1
fi

# Activate virtual environment and run the Python script
source "$VENV_DIR/bin/activate"

# Check if whisper is installed
if ! pip list | grep -q "openai-whisper"; then
    echo "Error: whisper is not installed in the virtual environment"
    exit 1
fi

# Run Python script with verbose output
python -u "$PYTHON_SCRIPT" "$VIDEO_FILE"
deactivate 