# Video to Text Transcriber

A command-line tool that transcribes video files to text using OpenAI's Whisper model. It automatically converts video to audio, performs transcription, and saves the result as a text file.

## Features

- Supports various video formats
- Automatically handles temporary audio conversion
- Creates text output in the same directory as the input video
- Cleans up temporary files automatically
- Uses Whisper's base model for transcription (Russian language by default)

## Prerequisites

- Python 3.8 or higher
- FFmpeg
- Homebrew (for Mac users)
- At least 2GB of free disk space (for Whisper models)
- CUDA-compatible GPU (optional, for faster processing)

## Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd video2text
```

2. Install FFmpeg (Mac):
```bash
brew install ffmpeg
```

3. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate
```

4. Install Python dependencies:
```bash
# Basic installation
pip install openai-whisper ffmpeg-python

# If you have CUDA-compatible GPU, install PyTorch with CUDA support first:
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

### Python Dependencies Details

The project requires the following Python packages:

- **openai-whisper**: OpenAI's automatic speech recognition system
  - Automatically downloads the required model files (~1GB for base model)
  - Supports multiple languages
  - CPU or GPU processing

- **ffmpeg-python**: Python bindings for FFmpeg
  - Handles video/audio conversion
  - Requires FFmpeg to be installed on the system

### Available Whisper Models

You can modify the model in `video2text.py` to use different Whisper models:

- `tiny`: Fastest, least accurate (~1GB RAM)
- `base`: Good balance of speed and accuracy (~1GB RAM)
- `small`: Better accuracy, slower (~2GB RAM)
- `medium`: High accuracy, slower (~5GB RAM)
- `large`: Best accuracy, slowest (~10GB RAM)

To change the model, modify this line in `video2text.py`:
```python
model = whisper.load_model("base")  # Change "base" to your preferred model
```

5. Configure the shell script:

Edit `video2text.sh` and update the paths to match your system:
```bash
# Path to the project directory - change this to your project location
PROJECT_DIR="/Users/admin/Sites/video2text"  # <- Change this path

# These paths are derived from PROJECT_DIR, no need to change them
VENV_DIR="$PROJECT_DIR/venv"
PYTHON_SCRIPT="$PROJECT_DIR/video2text.py"
```

For Mac M1/M2 users, ensure FFmpeg is accessible by keeping this line:
```bash
export PATH="/opt/homebrew/bin:$PATH"
```

6. Make the shell script executable:
```bash
chmod +x video2text.sh
```

7. Create a symbolic link (optional, for system-wide access):
```bash
# Replace /full/path/to with your actual project directory path
sudo ln -s "$PROJECT_DIR/video2text.sh" /usr/local/bin/video2text
```

## Usage

### Basic Usage

Convert a video file to text:
```bash
video2text video_file.mov
```

This will create `video_file.txt` in the same directory as the input video.

### File Support

Supports various video formats including:
- .mov
- .mp4
- .avi
- And other formats supported by FFmpeg

### Output

The script will:
1. Create a temporary audio file
2. Transcribe the audio using Whisper
3. Save the transcription to a .txt file
4. Clean up the temporary audio file

### Mac Automation Setup

You can integrate this script with Mac's Automator to create a Quick Action for transcribing videos directly from Finder:

1. Open Automator
2. Create a new Quick Action
3. Set "Workflow receives current" to "files or folders" in "Finder"
4. Add a "Run Shell Script" action
5. Set "Shell" to "/bin/bash"
6. Set "Pass input" to "as arguments"
7. Enter the following script:
```bash
# Process all selected files
for f in "$@"
do
    video2text "$f"
done
```
8. Save the Quick Action with a name like "Transcribe Video"

Now you can:
- Right-click any video file in Finder
- Select Quick Actions → Transcribe Video
- The transcription will be created in the same directory

## Project Structure

- `video2text.py` - Main Python script for transcription
- `video2text.sh` - Shell script wrapper for easy command-line usage
- `venv/` - Virtual environment directory
- `.gitignore` - Git ignore file

## Troubleshooting

If you encounter issues:

1. Ensure FFmpeg is installed:
```bash
ffmpeg -version
```

2. Verify the virtual environment is activated:
```bash
which python
```
Should point to your venv directory

3. Check if Whisper is installed:
```bash
pip list | grep openai-whisper
```

## License

This project is licensed under the MIT License - see [MIT License](https://opensource.org/licenses/MIT) for details.

## Contributing

If you'd like to contribute, please:
1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

Please mention [@wybaeb](https://github.com/wybaeb) in your pull request.