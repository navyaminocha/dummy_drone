# dummy_drone
The Hand Gesture Controlled Drone system is designed to create a natural interaction between humans and machines. Using advanced image processing and neural network-based classification, the drone responds to predefined gestures, allowing users to guide its movement through intuitive hand signals.

🚁 Hand-Gesture Controlled Drone (AIMS) 

An AI-powered drone navigation system that converts live hand gestures into precise flight commands using Computer Vision and Deep Learning. The system leverages MediaPipe for hand landmark detection and a Custom CNN model for accurate gesture classification.

📌 Project Summary

This application enables contactless drone operation through an intuitive gesture-based interface. By extracting and normalizing 21 hand landmarks, the model ensures consistent recognition independent of hand size, orientation, or frame position.

🚀 Core Features

• Real-Time Recognition: Ultra-low latency processing for smooth control
• Landmark Normalization: Scale and position invariant input data
• Dynamic Speed Adjustment: Thumb–index finger distance controls velocity
• 8 Gesture Commands: FORWARD, BACKWARD, LEFT, RIGHT, UP, DOWN, STOP, SPEED

🛠️ Technology Stack

• Programming Language: Python 3.8+
• Computer Vision: OpenCV, MediaPipe
• Deep Learning Framework: TensorFlow / Keras (Custom CNN Model)
• Data Processing: NumPy, Pandas
