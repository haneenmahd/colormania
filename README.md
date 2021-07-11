# ColorMania
Use RGB Colors in your terminal app

# Installation 
Just clone this repo Using git
```
git clone https://github.com/haneenmahd/colormania.git 
```

Now you could import the function names `useColor` from this directory because it would act as a package as it contains `__init__.py` inside this repo. 

# Usage
Currently, There is only one function that is written in this package. It is called `useColor`.

useColor accepts four arguments.Number one is the string that should be colored, Two the amount of red colour, Three the amount of green, and finally the amoun of blue colour (It uses RGB Format)

## Example
1) Simple Usage
```python
# Importing the package
from colormania.main import useColor

# Setting up the colored message
message = useColor("Hello World", "135", "75", "100")

# Printing the message to console
print(message)
```
2) Generate Linear Background <br>

![image](https://user-images.githubusercontent.com/72091386/125189007-cf1ed780-e253-11eb-9c6d-0d11b7a2d3c2.png)
```python
import colormania

for x in range(0, 200, 20):
    message = colormania.useColor("|||||||||||", "135", "75", str(200 - x))

    print(message)
```
## License
ColorMania is Licensed under MIT.
