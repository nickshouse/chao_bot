from PIL import Image

# Open images
frontImage = Image.open('purple.png').convert("RGBA")
background = Image.open('canvas.png').convert("RGBA")

# Paste and save
background.paste(frontImage, (0, 0), frontImage)
background.save("merged.png", format="png")

