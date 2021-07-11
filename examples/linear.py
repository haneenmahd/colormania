import colormania

for x in range(0, 200, 20):
    message = colormania.useColor("|||||||||||", "135", "75", str(200 - x))

    print(message)