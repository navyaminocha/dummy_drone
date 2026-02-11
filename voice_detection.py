import speech_recognition as sr
import time
from playsound import playsound

recognizer = sr.Recognizer()
microphone = sr.Microphone()

emergency_active = False
siren_play_obj = None

# Drone commands
commands = {
    'takeoff': lambda: print("Taking off"),
    'land': lambda: print("Landing"),
    'up': lambda: print("Going up"),
    'down': lambda: print("Going down"),
    'left': lambda: print("Moving left"),
    'right': lambda: print("Moving right"),
    'flip': lambda: print("Flipping"),
}

def emergency_procedure():
    global emergency_active
    emergency_active = True
    print("EMERGENCY ACTIVATED")
    commands['land']()
    playsound("siren.mp3")  
    print("Landing immediately")
           


print("Voice Drone Control Ready")
print(f"Available commands: {', '.join(commands.keys())}")
print("Press Ctrl+C to stop")


with microphone as source:
    recognizer.adjust_for_ambient_noise(source, duration=2)

try:
 while True:
    print("\nListening...")
    
    try:
        with microphone as source:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=3)
        
        text = recognizer.recognize_google(audio).lower()
        print(f" You said: '{text}'")
        
        if "emergency" in text:
                emergency_procedure()
                continue
        
        if emergency_active:
                print("System locked due to emergency")
                continue
        # Check for commands
        for cmd in commands:
            if cmd in text:
                commands[cmd]()
                break
        else:
            print("Command not recognized")
            
    except sr.WaitTimeoutError:
        print("No speech detected")
    except sr.UnknownValueError:
        print("Could not understand audio")

except KeyboardInterrupt:
    print("\nExiting...")
    