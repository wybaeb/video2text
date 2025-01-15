import whisper
import ffmpeg
import sys
import os

def convert_video_to_audio(video_path, audio_path):
    """Convert video file to audio using ffmpeg."""
    print(f"Converting video to audio: {video_path} -> {audio_path}")
    ffmpeg.input(video_path).output(audio_path).run()
    print("Conversion completed")

def transcribe_audio(audio_path, language="ru"):
    """Transcribe audio to text using whisper model."""
    print("Loading whisper model...")
    model = whisper.load_model("base")
    print("Transcribing audio...")
    result = model.transcribe(audio_path, language=language)
    print("Transcription completed")
    return result['text']

def transcribe_video(video_path):
    print(f"Starting transcription of: {video_path}")
    
    # Get the directory of the input video for temp file
    video_dir = os.path.dirname(os.path.abspath(video_path))
    audio_path = os.path.join(video_dir, "temp_audio.wav")
    
    try:
        # Convert video to audio
        convert_video_to_audio(video_path, audio_path)
        
        # Transcribe audio
        transcription = transcribe_audio(audio_path)
        
        # Write the transcription to a file
        output_filename = video_path.rsplit('.', 1)[0] + ".txt"
        print(f"Writing transcription to: {output_filename}")
        with open(output_filename, "w", encoding="utf-8") as f:
            f.write(transcription)
        
        print(f"Transcription saved to {output_filename}")
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        raise
    finally:
        # Clean up temp audio file
        if os.path.exists(audio_path):
            os.remove(audio_path)
            print("Temporary audio file removed")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python video2text.py <video_file>")
        sys.exit(1)
    
    video_path = os.path.abspath(sys.argv[1])
    print(f"Processing video file: {video_path}")
    transcribe_video(video_path)