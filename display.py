from sense_hat import SenseHat
import time

sense = SenseHat()

white = (255, 255, 255)
black = (0, 0, 0)

checkerboard = [
    white, black, white, black, white, black, white, black,
    black, white, black, white, black, white, black, white,
    white, black, white, black, white, black, white, black,
    black, white, black, white, black, white, black, white,
    white, black, white, black, white, black, white, black,
    black, white, black, white, black, white, black, white,
    white, black, white, black, white, black, white, black,
    black, white, black, white, black, white, black, white,
]

sense.set_pixels(checkerboard)

time.sleep(5)
sense.clear()
