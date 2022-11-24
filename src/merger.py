from PIL import Image

# Combine two images of same canvas size
left = Image.open('left.png')
right = Image.open('right.png')

final = Image.alpha_composite(left, right)
final.save('final.png')

