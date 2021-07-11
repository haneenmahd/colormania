from main import useColor

for x in range(0, 200, 20):
    message = useColor("Goat messi", "135", "75", str(201 - x))

    print(message)