import json
import requests
import urllib
from bs4  import  BeautifulSoup

colors = """AliceBlue, DarkOliveGreen, Indigo, MediumPurple, Purple,
AntiqueWhite, DarkOrange, Ivory, MediumSeaGreen, Red,
Aqua, DarkOrchid, Khaki, MediumSlateBlue, RosyBrown,
AquaMarine, DarkRed, Lavender, MediumSpringGreen, RoyalBlue,
Azure, DarkSalmon, LavenderBlush, MediumTurquoise, SaddleBrown,
Beige, DarkSeaGreen, LawnGreen, MediumVioletRed, Salmon,
Bisque, DarkSlateBlue, LemonChiffon, MidnightBlue, SandyBrown,
Black, DarkSlateGray, LightBlue, MintCream, SeaGreen,
BlanchedAlmond, DarkTurquoise, LightCoral, MistyRose, SeaShell,
Blue, DarkViolet, LightCyan, Moccasin, Sienna,
BlueViolet, DeepPink, LightGoldenrodYellow, NavajoWhite, Silver,
Brown, DeepSkyBlue, LightGray, Navy, SkyBlue,
BurlyWood, DimGray, LightGreen, OldLace, SlateBlue,
CadetBlue, DodgerBlue, LightPink, Olive, SlateGray,
Chartreuse, FireBrick, LightSalmon, OliveDrab, Snow,
Chocolate, FloralWhite, LightSeaGreen, Orange, SpringGreen,
Coral, ForestGreen, LightSkyBlue, OrangeRed, SteelBlue,
CornFlowerBlue, Fuchsia, LightSlateGray, Orchid, Tan,
Cornsilk, Gainsboro, LightSteelBlue, PaleGoldenRod, Teal,
Crimson, GhostWhite, LightYellow, PaleGreen, Thistle,
Cyan, Gold, Lime, PaleTurquoise, Tomato,
DarkBlue, GoldenRod, LimeGreen, PaleVioletRed, Turquoise,
DarkCyan, Gray, Linen, PapayaWhip, Violet,
DarkGoldenRod, Green, Magenta, PeachPuff, Wheat,
DarkGray, GreenYellow, Maroon, Peru, White,
DarkGreen, HoneyDew, MediumAquaMarine, Pink, WhiteSmoke,
DarkKhaki, HotPink, MediumBlue, Plum, Yellow,
DarkMagenta, IndianRed, MediumOrchid, PowderBlue, YellowGreen"""

colorsArray = colors.split(',')

colorsJson = []

for color in colorsArray:
    colorName = color.strip().lower()
    url = "https://rgb.to/" + colorName

    r = requests.get(url)
    html = r.text

    soup = BeautifulSoup(html, features="html.parser")
    hsbValue = soup.find("input", {"id": "HSB"}).get('value')

    hsbValues = hsbValue.split(',')
    colorJson = {"name": colorName, 'hue': int(hsbValues[0].strip()), 'sat': int(hsbValues[1].strip()), 'bri': int(hsbValues[2].strip())}

    colorsJson.append(colorJson)

with open('colors.json', 'w') as out:
    out.write(json.dumps(colorsJson, indent=4))


