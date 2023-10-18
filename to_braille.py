from sys import argv
from PIL import Image
from braille import dots_to_braille

def generate(path: str):
    im = Image.open(path)
    width = im.size[0]
    height = im.size[1]
    im = im.convert('RGB')

    def is_on(x: int, y: int) -> bool:
        if width>x and height>y:
            r, g, b = im.getpixel((x, y))
            return (r+g+b)/3 > 127
        return False

    lines = []
    for y in range(0, height, 5):
        line = ""
        for x in range(0, width, 3):
            braille = dots_to_braille(
                is_on(x, y),
                is_on(x, y+1),
                is_on(x, y+2),
                is_on(x+1, y),
                is_on(x+1, y+1),
                is_on(x+1, y+2),
                is_on(x, y+3),
                is_on(x+1, y+3)
            )
            line += braille
        lines.append(line)

    with open("output.txt", "w", encoding="utf8") as f:
        f.write("\n".join(lines))

match argv:
    case [_, path]:
        generate(path)
    case _:
        print("Please give a file to convert.")
