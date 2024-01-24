from captcha.image import ImageCaptcha
import random

# List with the letters to be randomized
letras = list('abcdef')

# Create an instance of ImageCaptcha
image = ImageCaptcha(width=280, height=90)


for i in range(10):
    # Shuffle the list of letters
    random.shuffle(letras)

    # Join the shuffled letters back into a string
    captcha_text = ''.join(letras)

    # Generate the image with the text
    data = image.generate(captcha_text)

    # Write the image to a file
    image.write(captcha_text, f'src/captchas/captcha-{i}.png')
