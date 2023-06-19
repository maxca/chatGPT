from PIL import Image, ImageDraw
import tkinter as tk

# Constants
BG_COLOR = (255, 255, 255)
PASTEL_PINK = (255, 204, 204)
PASTEL_PURPLE = (204, 204, 255)
PASTEL_YELLOW = (255, 255, 204)
PASTEL_GREEN = (204, 255, 204)

# Get the screen dimensions
root = tk.Tk()
SCREEN_WIDTH = root.winfo_screenwidth()
SCREEN_HEIGHT = root.winfo_screenheight()
root.destroy()

# Create a blank image with a white background
image = Image.new("RGB", (SCREEN_WIDTH, SCREEN_HEIGHT), BG_COLOR)
draw = ImageDraw.Draw(image)

# Draw the flower petals
petal_radius = int(min(SCREEN_WIDTH, SCREEN_HEIGHT) * 0.2)
center_x = SCREEN_WIDTH // 2
center_y = SCREEN_HEIGHT // 2
num_petals = 8
angle_between_petals = 360 // num_petals

for i in range(num_petals):
    start_angle = i * angle_between_petals
    end_angle = start_angle + angle_between_petals
    draw.arc(
        (
            center_x - petal_radius,
            center_y - petal_radius,
            center_x + petal_radius,
            center_y + petal_radius,
        ),
        start_angle,
        end_angle,
        fill=PASTEL_PINK,
        width=petal_radius // 4,
    )

# Draw the flower center
center_radius = petal_radius // 4
draw.ellipse(
    (
        center_x - center_radius,
        center_y - center_radius,
        center_x + center_radius,
        center_y + center_radius,
    ),
    fill=PASTEL_YELLOW,
)

# Draw the stem
stem_width = int(min(SCREEN_WIDTH, SCREEN_HEIGHT) * 0.04)
stem_height = int(min(SCREEN_WIDTH, SCREEN_HEIGHT) * 0.4)
stem_start_x = center_x - stem_width // 2
stem_start_y = center_y + center_radius
stem_end_x = stem_start_x
stem_end_y = stem_start_y + stem_height
draw.rectangle(
    (stem_start_x, stem_start_y, stem_end_x + stem_width, stem_end_y),
    fill=PASTEL_GREEN,
)

# Show the image
image.show()
