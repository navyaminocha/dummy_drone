from controller import drone_dummy as drone

def execute(gesture):
    if gesture == "UP":
        drone.move_up()
    elif gesture == "DOWN":
        drone.move_down()
    elif gesture == "TAKEOFF":
        drone.takeoff()
    elif gesture == "LAND":
        drone.land()

