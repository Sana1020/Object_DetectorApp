import os
import urllib.request
from pathlib import Path

# Base directory for models
BASE_DIR = r"C:\media_pipe\downloaded_models.py"  # Change this to your desired directory

# Model URLs and filenames
MODELS = {
    "face_landmarker.task": "https://storage.googleapis.com/mediapipe-models/face_landmarker/face_landmarker/float16/1/face_landmarker.task",
    "hand_landmarker.task": "https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/1/hand_landmarker.task",
    "pose_landmarker.task": "https://storage.googleapis.com/mediapipe-models/pose_landmarker/pose_landmarker_heavy/float16/1/pose_landmarker_heavy.task"
}

def download_model(filename, url):
    """Download a model if it doesn't exist."""
    filepath = os.path.join(BASE_DIR, filename)
    
    if os.path.exists(filepath):
        file_size = os.path.getsize(filepath)
        if file_size > 1000:  # At least 1KB
            print(f"✓ {filename} already exists ({file_size:,} bytes)")
            return True
        else:
            print(f"⚠ {filename} exists but seems corrupted, re-downloading...")
    
    print(f"⬇ Downloading {filename}...")
    try:
        urllib.request.urlretrieve(url, filepath)
        file_size = os.path.getsize(filepath)
        print(f"✓ Downloaded {filename} ({file_size:,} bytes)")
        return True
    except Exception as e:
        print(f"✗ Failed to download {filename}: {e}")
        return False

def main():
    print("=" * 60)
    print("MediaPipe Models Downloader")
    print("=" * 60)
    print(f"\nDownload directory: {BASE_DIR}\n")
    
    # Create directory if it doesn't exist
    os.makedirs(BASE_DIR, exist_ok=True)
    
    success_count = 0
    total_count = len(MODELS)
    
    for filename, url in MODELS.items():
        if download_model(filename, url):
            success_count += 1
        print()
    
    print("=" * 60)
    print(f"Download Summary: {success_count}/{total_count} models ready")
    print("=" * 60)
    
    if success_count == total_count:
        print("\n✓ All models downloaded successfully!")
        print("You can now run: python complete_integrated_app.py")
    else:
        print("\n⚠ Some models failed to download. Please check your internet connection.")
        print("You can also download them manually from:")
        print("https://developers.google.com/mediapipe/solutions/vision/pose_landmarker#models")

if __name__ == "__main__":
    main()
