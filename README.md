# dummy_drone
The Hand Gesture Controlled Drone system is designed to create a natural interaction between humans and machines. Using advanced image processing and neural network-based classification, the drone responds to predefined gestures, allowing users to guide its movement through intuitive hand signals.

 🚁🖐️🎙️Hand-Gesture Controlled Drone (AIMS)

An AI-powered drone navigation system that converts real-time hand gestures and voice commands into accurate flight instructions using Computer Vision and Deep Learning. The system integrates MediaPipe for hand landmark detection, a Custom CNN for gesture classification, and voice recognition for command and emergency control.

📌 Project Summary

This software provides a touchless and voice-enabled interface for drone operation. By normalizing 21 hand landmarks, the system ensures reliable gesture recognition regardless of hand size or position. Additionally, voice detection enables users to issue commands or trigger emergency actions instantly.

🚀 Core Features

• Real-Time Gesture Recognition: Low-latency command processing
• Voice Command Integration: Control drone using predefined voice inputs
• Emergency Voice Detection: Instant STOP or LAND on emergency keywords
• Landmark Normalization: Scale and position invariant recognition
• Dynamic Speed Control: Thumb–index finger distance adjusts velocity
• 8 Gesture Commands: FORWARD, BACKWARD, LEFT, RIGHT, UP, DOWN, STOP, SPEED

🛠️ Technology Stack

• Programming Language: Python 3.8+
• Computer Vision: OpenCV, MediaPipe
• Deep Learning: TensorFlow / Keras (Custom CNN Model)
• Voice Recognition: SpeechRecognition / PyAudio
• Data Processing: NumPy, Pandas
