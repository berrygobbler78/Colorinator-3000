import time
import board
import digitalio
import pulseio
import busio
import simpleio

# Configure the sensor pins
s0 = digitalio.DigitalInOut(board.D12)
s0.direction = digitalio.Direction.OUTPUT

s1 = digitalio.DigitalInOut(board.D7)
s1.direction = digitalio.Direction.OUTPUT

s2 = digitalio.DigitalInOut(board.D8)
s2.direction = digitalio.Direction.OUTPUT

s3 = digitalio.DigitalInOut(board.D25)
s3.direction = digitalio.Direction.OUTPUT

out = pulseio.PulseIn(board.GP18, idle_state=True)

s0.value = True
s1.value = False

while True:
    s2.value = False
    s3.value = False

    time.sleep(0.01)

    while(out) == 0:
        pass
    
    out.pause()

    red_freq = out[0]
    red_color = simpleio.map_range(red_freq, 100, 530, 100, 0)

    out.clear()
    out.resume()

    s2.value = True
    s3.value = True

    time.sleep(0.01)

    # Wait for an active pulse
    while len(out) == 0:
        pass

    # Pause while we do something with the pulses
    out.pause()

    green_freq = out[0]
    green_color = simpleio.map_range(green_freq, 150, 700, 100, 0)

    out.clear()
    out.resume()

    s2.value = False
    s3.value = True

    time.sleep(0.01)

    # Wait for an active pulse
    while len(out) == 0:
        pass

    # Pause while we do something with the pulses
    out.pause()

    blue_freq = out[0]
    blue_color = simpleio.map_range(blue_freq, 70, 600, 100, 0)

    #print("{}\t{}\t{}".format(red_freq, green_freq, blue_freq))
    #print("{}\t{}\t{}".format(int(red_color), int(green_color), int(blue_color)))

    if red_color < 50 and green_color < 50 and blue_color < 50:
        color = "NONE "
    elif red_color > green_color and \
         red_color > blue_color:
        color = "RED  "
    elif green_color > red_color and \
         green_color > blue_color:
        color = "GREEN"
    elif blue_color > green_color and \
         blue_color > red_color:
        color = "BLUE "

    if color != prev_color:
        prev_color = color

        print(color)

    time.sleep(0.1)

    out.clear()
    out.resume()