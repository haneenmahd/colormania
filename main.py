def useColor(message: str, red, green, blue):
    result_message = f"*033[38;2;{red};{green};{blue}m{message}*033[0m"

    return result_message