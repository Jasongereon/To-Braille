def dots_to_braille(a: bool, b: bool, c: bool, d: bool, e: bool, f: bool, x: bool, y: bool) -> str:
    '''
    a d
    b e
    c f
    x y
    '''
    return chr(10240 + (a << 0) + (b << 1) + (c << 2) + (d << 3) + (e << 4) + (f << 5) + (x << 6) + (y << 7))

