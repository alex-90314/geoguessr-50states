from PIL import ImageGrab

# Take a screenshot of the entire screen
image = ImageGrab.grab()

# Save the screenshot to a file
image.save("screenshot.png")
