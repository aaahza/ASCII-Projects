from PIL import Image
import pygame
import sys

ASCII_CHARS = " `.-~:;=!+*>|)}]?6I;,:'^_1l()[]aweo#%$B@&8"

# Initialize Pygame
pygame.init()

# Get the dimensions of the screen
screen_info = pygame.display.Info()
screen_width = screen_info.current_w
screen_height = screen_info.current_h

# Create the Pygame screen (fullscreen)
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
pygame.display.set_caption("ASCII Art Display")

# Print screen dimensions
print(f"Screen width: {screen_info.current_w}")
print(f"Screen height: {screen_info.current_h}")

# Load the image
image_path = "eye.jpeg"
image = Image.open(image_path)
print(image.mode)

# Resize the image while maintaining aspect ratio
max_width = screen_width // 8
max_height = screen_height // 8
image.thumbnail((max_width, max_height))

# Convert image to grayscale
gray_image = image.convert("L")

ascii_ar = ""

# Generate ASCII art and overlay colors
pixels = gray_image.getdata()
for i, pixel in enumerate(pixels):
    ascii_char = ASCII_CHARS[int((pixel * (len(ASCII_CHARS) - 1)) / 255)]
    ascii_ar += ascii_char

    # Get color from the original image
    if image.mode == 'RGB':
        color = image.getpixel((i % gray_image.width, i // gray_image.width))
        r, g, b = color
        text_color = (r, g, b)
    elif image.mode == 'L':
        grayscale_value = pixel
        text_color = (grayscale_value, grayscale_value, grayscale_value)
    else:
        text_color = (255, 255, 255)

    # Render the character with the appropriate color
    font_size = 8
    font = pygame.font.Font("Consolas.ttf", font_size)
    text_surface = font.render(ascii_char, True, text_color)
    x = (i % gray_image.width) * font_size
    y = (i // gray_image.width) * font_size
    screen.blit(text_surface, (x, y))

    if (i + 1) % gray_image.width == 0:
        ascii_ar += "\n"

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
