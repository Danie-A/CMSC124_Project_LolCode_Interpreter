color = 'green'

def print_color_message(color):
    if color == 'green':
        message = 'The green color is fresh and invigorating.'
    elif color == 'blue':
        message = 'The blue color is calm and serene.'
    elif color == 'orange':
        message = 'The color orange is cheerful and energetic.'
    else:
        message = 'Purple color is romantic and mysterious.'
    print(message)

print_color_message(color)