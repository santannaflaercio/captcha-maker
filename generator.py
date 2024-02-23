from captcha.image import ImageCaptcha
import random

image = ImageCaptcha(width=280, height=90)

# Populate the list with letters and numbers
letters_and_numbers = (
    [chr(i) for i in range(97, 123)]
    + [chr(i) for i in range(65, 91)]
    + [str(i) for i in range(10)]
)

number_of_captchas = 10
number_of_characters = 6

for i in range(number_of_captchas):
    # Randomly select 6 characters from the list
    captcha_text = "".join(random.sample(letters_and_numbers, number_of_characters))
    # Generate the image with the text
    image.write(captcha_text, f"data/captchas/captcha-{i}.png")
