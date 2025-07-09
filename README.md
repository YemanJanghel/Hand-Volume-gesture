# Hand-Volume-gesture

Control your system volume with hand gestures using MediaPipe, OpenCV, and pycaw!

📁 Folder Structure
bash
Copy
Edit
HandVolumeControl/
├── handtrackmodule.py       # Custom hand tracking class using MediaPipe
├── handvolume.py            # Main script to control volume with hand gestures
├── requirements.txt         # All dependencies
└── README.md                # Project guide

📌 Features
Detects hands using MediaPipe

Tracks thumb and index finger to calculate distance

Maps distance to system volume level

Live feedback with OpenCV window

🧰 Requirements
Library	Version Suggestion
Python	✅ 3.10.x
OpenCV	opencv-python
MediaPipe	mediapipe
Pycaw	pycaw
comtypes	auto-installed with pycaw
numpy	numpy

🔧 Installation

1️⃣ Install Python 3.10
Download Python 3.10 from official site

2️⃣ Create Virtual Environment (Optional but recommended)
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate  # Windows

3️⃣ Install Required Libraries
bash
Copy
Edit
pip install -r requirements.txt
If you don’t have requirements.txt, create it with:

txt
Copy
Edit
opencv-python
mediapipe
pycaw
numpy
Or run manually:

bash
Copy
Edit
pip install opencv-python mediapipe numpy pycaw
▶️ How to Run
Make sure your webcam is working and accessible.

Run the main script:

bash
Copy
Edit
python handvolume.py
Show your thumb and index finger to the camera.

Bring them closer to decrease volume, move apart to increase.

Press s to stop the program.

🔍 Code Breakdown
handtrackmodule.py
Custom class handDetector built on top of MediaPipe

Methods:

findHands(image) → Detect and draw hands

findPosition(image) → Get landmarks (x, y) of all hand points

handvolume.py
Loads hand tracking module

Uses pycaw to control Windows volume

Maps distance between thumb and index finger to system volume using np.interp

🚨 Troubleshooting
❓ ModuleNotFoundError: No module named 'comtypes'
✅ Solution:

bash
Copy
Edit
pip install comtypes
❓ Webcam not showing
Make sure no other app is using it

Check with a simple OpenCV webcam test

💡 Ideas to Improve
Add gesture for mute/unmute

Add GUI with Tkinter or PyQt

Add hand recognition for user-specific settings

👨‍💻 Author
Yeman — Python Enthusiast, Data Analyst in Progress
“Gesture-controlled tech is the future!”

