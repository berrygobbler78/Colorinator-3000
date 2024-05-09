import time
import board
import pulseio

# Configure the sensor pins
s2 = pulseio.DigitalInOut(board.D2)
s3 = pulseio.DigitalInOut(board.D3)
sensor_out = pulseio.DigitalInOut(board.D4)

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