import time
import board
import pulseio

# Configure the sensor pins
s0 = pulseio.PWMOut(board.D12, frequency=1000, duty_cycle=2**15)
s1 = pulseio.PWMOut(board.D7, frequency=1000, duty_cycle=2**15)
s2 = pulseio.PWMOut(board.D8, frequency=1000, duty_cycle=2**15)
s3 = pulseio.PWMOut(board.D25, frequency=1000, duty_cycle=2**15)
sensor_out = pulseio.PWMOut(board.D24, frequency=1000, duty_cycle=2**15)

# Function to read color
def read_color():
    # Set frequency scaling to 2%
    s0.duty_cycle = 6554
    s1.duty_cycle = 6554
    # Red
    s2.duty_cycle = 0
    s3.duty_cycle = 0
    time.sleep(0.1)
    red = sensor_out.duty_cycle
    # Green
    s2.duty_cycle = 6554
    s3.duty_cycle = 0
    time.sleep(0.1)
    green = sensor_out.duty_cycle
    # Blue
    s2.duty_cycle = 0
    s3.duty_cycle = 6554
    time.sleep(0.1)
    blue = sensor_out.duty_cycle
    return red, green, blue

# Main loop
while True:
    r, g, b = read_color()
    # Print the RGB values
    print("Red: {}, Green: {}, Blue: {}".format(r, g, b))
    # Delay for a short while to prevent spamming the console
    time.sleep(1)