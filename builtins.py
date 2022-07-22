import tkinter as tk
import re
class char:
    def __init__(self,character=""[0]):
        if len(character)!=1:raise Exception("Characters must be 1 char long")
        #else pass
        self.char=character
    def __str__(self):return str(self.char)
    def __upper__(self): return self.char.upper()
    def __lower__(self): return self.char.lower()
    def __islower__(self): return self.char.islower()
    def __isupper__(self): return self.char.isupper()
    def __isnumeric(self): return self.char.isnumeric()
    def __ishex__(self):
        hexaPattern = re.compile(r'\s--([0-9a-fA-F]+)(?:--)?\s')
        m = re.search(hexaPattern, self.char)
        if m: return True
        else:return False
    def __isbinary__(self):
        if self.char=="1" or self.char =="0":return True
        else: return False
    def __int__(self):
        if self.__isnumeric(): return int(self.char)
        else: raise Exception("The Char is not an integer")
    def __float__(self):
        if self.__isnumeric():return float(self.char)
        else: raise Exception("The Char is not a float")

class chararray:
    def __init__(self,chars:list):
        for i in chars:
            if len(i)!=1:raise Exception(f"The list has more than one char in element {chars.index(i)}")
            else:continue
        self.chars=chars
    def __str__(self):return self.chars.__str__()
class string(str): pass


class integer(int): pass


class decimal(float): pass


class double(float): pass


class Colors:
    aqua: str = "#00ffff"
    black: str = "#000000"
    blue: str = "#0000ff"
    fuchsia: str = "#ff00ff"
    green: str = "#008000"
    gray: str = "#808080"
    lime: str = "#00ff00"
    maroon: str = "#800000"
    navy: str = "#000080"
    olive: str = "#808000"
    purple: str = "#800080"
    red: str = "#ff0000"
    silver: str = "#c0c0c0"
    teal: str = "#008080"
    white: str = "#ffffff"
    yellow: str = "#ffff00"
    aliceblue: str = "#f0f8ff"
    antiquewhite: str = "#faebd7"
    aquamarine: str = "#7fffd4"
    azure: str = "#f0ffff"
    beige: str = "#f5f5dc"
    bisque: str = "#ffe4c4"
    blanchedalmond: str = "#ffebcd"
    blueviolet: str = "#8a2be2"
    brown: str = "#a52a2a"
    burlywood: str = "#deb887"
    cadetblue: str = "#5f9ea0"
    chartreuse: str = "#7fff00"
    chocolate: str = "#d2691e"
    coral: str = "#ff7f50"
    cornflowerblue: str = "#6495ed"
    cornsilk: str = "#fff8dc"
    crimson: str = "#dc143c"
    cyan: str = "#00ffff"
    darkblue: str = "#00008b"
    darkcyan: str = "#008b8b"
    darkgoldenrod: str = "#b8860b"
    darkgray: str = "#a9a9a9"
    darkgrey: str = "#a9a9a9"
    darkgreen: str = "#006400"
    darkkhaki: str = "#bdb76b"
    darkmagenta: str = "#8b008b"
    darkolivegreen: str = "#556b2f"
    darkorange: str = "#ff8c00"
    darkorchid: str = "#9932cc"
    darkred: str = "#8b0000"
    darksalmon: str = "#e9967a"
    darkseagreen: str = "#8fbc8f"
    darkslateblue: str = "#483d8b"
    darkslategray: str = "#2f4f4f"
    darkslategrey: str = "#2f4f4f"
    darkturquoise: str = "#00ced1"
    darkviolet: str = "#9400d3"
    deeppink: str = "#ff1493"
    deepskyblue: str = "#00bfff"
    dimgray: str = "#696969"
    dimgrey: str = "#696969"
    dodgerblue: str = "#1e90ff"
    firebrick: str = "#b22222"
    floralwhite: str = "#fffaf0"
    forestgreen: str = "#228b22"
    gainsboro: str = "#dcdcdc"
    ghostwhite: str = "#f8f8ff"
    gold: str = "#ffd700"
    goldenrod: str = "#daa520"
    grey: str = "#808080"
    greenyellow: str = "#adff2f"
    honeydew: str = "#f0fff0"
    hotpink: str = "#ff69b4"
    indianred: str = "#cd5c5c"
    indigo: str = "#4b0082"
    ivory: str = "#fffff0"
    khaki: str = "#f0e68c"
    lavender: str = "#e6e6fa"
    lavenderblush: str = "#fff0f5"
    lawngreen: str = "#7cfc00"
    lemonchiffon: str = "#fffacd"
    lightblue: str = "#add8e6"
    lightcoral: str = "#f08080"
    lightcyan: str = "#e0ffff"
    lightgoldenrodyellow: str = "#fafad2"
    lightgray: str = "#d3d3d3"
    lightgrey: str = "#d3d3d3"
    lightgreen: str = "#90ee90"
    lightpink: str = "#ffb6c1"
    lightsalmon: str = "#ffa07a"
    lightseagreen: str = "#20b2aa"
    lightskyblue: str = "#87cefa"
    lightslategray: str = "#778899"
    lightslategrey: str = "#778899"
    lightsteelblue: str = "#b0c4de"
    lightyellow: str = "#ffffe0"
    limegreen: str = "#32cd32"
    linen: str = "#faf0e6"
    magenta: str = "#ff00ff"
    mediumaquamarine: str = "#66cdaa"
    mediumblue: str = "#0000cd"
    mediumorchid: str = "#ba55d3"
    mediumpurple: str = "#9370db"
    mediumseagreen: str = "#3cb371"
    mediumslateblue: str = "#7b68ee"
    mediumspringgreen: str = "#00fa9a"
    mediumturquoise: str = "#48d1cc"
    mediumvioletred: str = "#c71585"
    midnightblue: str = "#191970"
    mintcream: str = "#f5fffa"
    mistyrose: str = "#ffe4e1"
    moccasin: str = "#ffe4b5"
    navajowhite: str = "#ffdead"
    oldlace: str = "#fdf5e6"
    olivedrab: str = "#6b8e23"
    orange: str = "#ffa500"
    orangered: str = "#ff4500"
    orchid: str = "#da70d6"
    palegoldenrod: str = "#eee8aa"
    palegreen: str = "#98fb98"
    paleturquoise: str = "#afeeee"
    palevioletred: str = "#db7093"
    papayawhip: str = "#ffefd5"
    peachpuff: str = "#ffdab9"
    peru: str = "#cd853f"
    pink: str = "#ffc0cb"
    plum: str = "#dda0dd"
    powderblue: str = "#b0e0e6"
    rosybrown: str = "#bc8f8f"
    royalblue: str = "#4169e1"
    saddlebrown: str = "#8b4513"
    salmon: str = "#fa8072"
    sandybrown: str = "#f4a460"
    seagreen: str = "#2e8b57"
    seashell: str = "#fff5ee"
    sienna: str = "#a0522d"
    skyblue: str = "#87ceeb"
    slateblue: str = "#6a5acd"
    slategray: str = "#708090"
    slategrey: str = "#708090"
    snow: str = "#fffafa"
    springgreen: str = "#00ff7f"
    steelblue: str = "#4682b4"
    tan: str = "#d2b48c"
    thistle: str = "#d8bfd8"
    tomato: str = "#ff6347"
    turquoise: str = "#40e0d0"
    violet: str = "#ee82ee"
    wheat: str = "#f5deb3"
    whitesmoke: str = "#f5f5f5"
    yellowgreen: str = "#9acd32"


class button(tk.Button):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def show(self, *args, **kwargs): self.pack(*args, **kwargs)

    def hide(self): self.pack_forget()

    def setText(self, text: str): self.config(text=text)

    def setBackground(self, color: str): self.config(bg=color)

    def setForeground(self, color: str): self.config(fg=color)


class label(tk.Label):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def show(self, *args, **kwargs): self.pack(*args, **kwargs)

    def hide(self): self.pack_forget()

    def setText(self, text: str): self.config(text=text)

    def setBackground(self, color: str): self.config(bg=color)

    def setForeground(self, color: str): self.config(fg=color)


class entry(tk.Entry):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def show(self, *args, **kwargs): self.pack(*args, **kwargs)

    def hide(self): self.pack_forget()

    def empty(self): self.delete(0, tk.END)

    def addText(self, texts: str): self.insert(0, texts)

    def setBackground(self, color: str): self.config(bg=color)

    def setForeground(self, color: str): self.config(fg=color)


class text(tk.Text):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def show(self, *args, **kwargs): self.pack(*args, **kwargs)

    def hide(self): self.pack_forget()

    def empty(self): self.delete(0, tk.END)

    def addText(self, text: str): self.insert(0, text)

    def setBackground(self, color: str): self.config(bg=color)

    def setForeground(self, color: str): self.config(fg=color)


class app(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.controls = dict()

    def addControl(self, name, control):
        self.controls[name] = control
        return control

    def getControl(self, controlName):
        try:
            return self.controls[controlName]
        except:
            return None

    def run(self):
        self.mainloop()

    def hide(self):
        self.withdraw()

    def show(self):
        self.focus()
