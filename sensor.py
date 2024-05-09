import time
import board
import digitalio

# Configure the sensor pins
s2 = digitalio.DigitalInOut(board.D2)
s2.direction = digitalio.Direction.OUTPUT
s3 = digitalio.DigitalInOut(board.D3)
s3.direction = digitalio.Direction.OUTPUT
sensor_out = digitalio.DigitalInOut(board.D4)
sensor_out.direction = digitalio.Direction.INPUT

# Function to read color
def read_color():
    # Red
    s2.value = False
    s3.value = False
    time.sleep(0.1)
    red = sensor_out.value
    # Green
    s2.value = True
    s3.value = False
    time.sleep(0.1)
    green = sensor_out.value
    # Blue
    s2.value = False
    s3.value = True
    time.sleep(0.1)
    blue = sensor_out.value
    return red, green, blue

# Main loop
while True:
    r, g, b = read_color()
    # Print the RGB values
    print("Red: {}, Green: {}, Blue: {}".format(r, g, b))
    # Delay for a short while to prevent spamming the console
    time.sleep(1)