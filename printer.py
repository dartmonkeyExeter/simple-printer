# coords thingy gen.py
from PIL import Image, ImageOps
import pyautogui
from time import sleep

path = r"C:\Users\aaron\Documents\painter"
file = f"{path}\sample.png"

im = Image.open(file)
im = im.convert('1')
pixels = list(im.getdata())
width, height = im.size

pixels2d = []

for i in range(height):
    row = []
    for j in range(width):
        row.append(pixels[i * width + j])
    pixels2d.append(row)

last_colour = pixels2d[0][0]
first_of_colour = (0, 0)

instructions = []

for row_idx, row in enumerate(pixels2d):
    for pixel_idx, pixel in enumerate(row):
        if pixel != last_colour:
            if last_colour == 0:
                instructions.append((first_of_colour, (row_idx, pixel_idx)))
            first_of_colour = (row_idx, pixel_idx)
        last_colour = pixel

print("ALGORITHM STARTS IN TEN SECONDS, MOVE MOUSE TO CORRECT POSITION, PREFERABLY TOP LEFT OF PAINT WINDOW")
sleep(5)
start_pos = pyautogui.position()

print(instructions)

for idx, inst in enumerate(instructions):
    pyautogui.mouseDown(x=start_pos.x + inst[0][1], y=start_pos.y + inst[0][0])
    pyautogui.dragTo(x=start_pos.x + inst[1][1], y=start_pos.y + inst[1][0], duration=0.01)
    pyautogui.mouseUp()

print("PRINT COMPLETE")
