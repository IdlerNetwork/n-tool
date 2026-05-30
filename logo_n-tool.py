from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.text import Text
from rich import box
import time
import os

class Colors:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    PRIMARY = '\033[38;5;141m'
    SECONDARY = '\033[38;5;117m'
    SUCCESS = '\033[38;5;120m'
    WARNING = '\033[38;5;221m'
    ERROR = '\033[38;5;210m'
    INFO = '\033[38;5;159m'
    ACCENT = '\033[38;5;183m'
    MUTED = '\033[38;5;250m'
    WHITE = '\033[97m'
    GRAY = '\033[38;5;242m'
    GOLD_1 = '\033[38;5;220m'
    GRAD1 = '\033[38;5;147m'
    GRAD2 = '\033[38;5;153m'
    GRAD3 = '\033[38;5;159m'
    ORANGE = '\033[38;5;208m'
    YELLOW = '\033[38;5;220m'
    TT8_GREEN_PRIMARY = '\033[38;5;114m'
    TT8_GREEN_SECONDARY = '\033[38;5;150m'
    TT8_GREEN_INFO = '\033[38;5;156m'
    TT8_GREEN_ACCENT = '\033[38;5;157m'
    TT9_BLUE_PRIMARY = '\033[38;5;39m'
    TT9_BLUE_SECONDARY = '\033[38;5;81m'
    TT9_BLUE_INFO = '\033[38;5;87m'
    TT9_BLUE_ACCENT = '\033[38;5;123m'
    CASTORICE_PRIMARY = '\033[38;5;141m'
    CASTORICE_SECONDARY = '\033[38;5;177m'
    CASTORICE_ACCENT = '\033[38;5;183m'
    CASTORICE_LIGHT = '\033[38;5;189m'
    CASTORICE_DARK = '\033[38;5;135m'
    SOFT_RED = '\033[38;5;211m'
    SOFT_RED_SECONDARY = '\033[38;5;217m'
    SOFT_RED_ACCENT = '\033[38;5;224m'
    AMETHYST_DARK = '\033[38;5;54m'
    AMETHYST_MID = '\033[38;5;99m'
    AMETHYST_LIGHT = '\033[38;5;189m'
    SAKURA_DEEP = '\033[38;5;204m'
    SAKURA_MID = '\033[38;5;218m'
    SAKURA_LIGHT = '\033[38;5;225m'
C = Colors()

time_str = time.strftime("%d/%m/%Y", time.localtime())

console = Console()

ASCII_ART = [
    f"{C.CASTORICE_DARK} __   __          ___________   ______     ______    __      ",
    f"{C.CASTORICE_PRIMARY}|  \\ |  |        |           | /  __  \\   /  __  \\  |  |     ",
    f"{C.CASTORICE_SECONDARY}|   \\|  |  ______`---|  |----`|  |  |  | |  |  |  | |  |     ",
    f"{C.CASTORICE_ACCENT}|  . `  | |______|   |  |     |  |  |  | |  |  |  | |  |     ",
    f"{C.CASTORICE_LIGHT}|  |\\   |            |  |     |  `--'  | |  `--'  | |  `----.",
    f"{C.CASTORICE_DARK}|__| \\__|            |__|      \\______/   \\______/  |_______|\n"
    f"{C.RESET}"
]

def IdlerOK(text, offset=0):
    castorice_colors_smooth = [
        '\033[38;5;93m', '\033[38;5;99m', '\033[38;5;135m', 
        '\033[38;5;141m', '\033[38;5;177m', '\033[38;5;183m', 
        '\033[38;5;189m', '\033[38;5;219m', '\033[38;5;189m', 
        '\033[38;5;183m', '\033[38;5;177m', '\033[38;5;141m', 
        '\033[38;5;135m', '\033[38;5;99m', '\033[38;5;93m'
    ]
    num_colors = len(castorice_colors_smooth)
    result = ""
    for i, char in enumerate(text):
        if char.isspace():
            result += char
            continue
        idx = (i + offset) % num_colors
        result += castorice_colors_smooth[idx] + char
    return result + '\033[0m'

_MINECRAFT_COLORS = {
    '0': '000000', '1': '0000AA', '2': '00AA00', '3': '00AAAA',
    '4': 'AA0000', '5': 'AA00AA', '6': 'FFAA00', '7': 'AAAAAA',
    '8': '555555', '9': '5555FF', 'a': '55FF55', 'b': '55FFFF',
    'c': 'FF5555', 'd': 'FF55FF', 'e': 'FFFF55', 'f': 'FFFFFF',
}

_MINECRAFT_FORMATS = {
    'l': '\033[1m',   # bold
    'm': '\033[9m',   # strikethrough
    'n': '\033[4m',   # underline
    'o': '\033[3m',   # italic
    'k': '',           # obfuscated — unsupported in terminal
    'r': '\033[0m',   # reset
}


def c_n(text: str) -> str:
    result = []
    i = 0
    n = len(text)

    while i < n:
        if text[i] == '&' and i + 1 < n:
            code = text[i + 1].lower()

            if code == 'x' and i + 14 <= n:
                hex_digits = []
                valid = True
                for j in range(6):
                    pos = i + 2 + j * 2
                    if pos + 1 < n and text[pos] == '&':
                        d = text[pos + 1]
                        if d.lower() in '0123456789abcdef':
                            hex_digits.append(d)
                        else:
                            valid = False
                            break
                    else:
                        valid = False
                        break
                if valid:
                    rgb = ''.join(hex_digits)
                    r = int(rgb[0:2], 16)
                    g = int(rgb[2:4], 16)
                    b = int(rgb[4:6], 16)
                    result.append(f'\033[38;2;{r};{g};{b}m')
                    i += 14
                    continue

            if code in _MINECRAFT_COLORS:
                rgb = _MINECRAFT_COLORS[code]
                r = int(rgb[0:2], 16)
                g = int(rgb[2:4], 16)
                b = int(rgb[4:6], 16)
                result.append(f'\033[38;2;{r};{g};{b}m')
                i += 2
                continue

            if code in _MINECRAFT_FORMATS:
                result.append(_MINECRAFT_FORMATS[code])
                i += 2
                continue

            # Unknown & — emit as literal
            result.append('&')
            i += 1
            continue
          
        result.append(text[i])
        i += 1

    result.append('\033[0m')
    return ''.join(result)

TITLE_COLORED = c_n(
    "&x&F&F&8&5&C&7&lI&x&F&C&9&2&C&C&ld&x&F&A&9&F&D&0&ll"
    "&x&F&7&A&C&D&5&le&x&F&5&B&9&D&9&lr"
    " &x&F&9&A&6&D&3&lH&x&F&F&8&5&C&7&la"
)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def ntool():
    clear()
    screen_width = console.size.width
    box_width = 75
    if screen_width < 79:
        box_width = max(screen_width - 2, 40)

    banner_content = Text.from_ansi("\n".join(ASCII_ART) + C.RESET)

    panel = Panel(
        Align.center(banner_content),
        title=Text.from_ansi(TITLE_COLORED),
        title_align="center",
        subtitle=f"[white] Version: v1.0.0 [black]|[/black] Date: {time_str} [/white]",
        subtitle_align="center",
        width=box_width,
        border_style="bold magenta",
        box=box.SQUARE,
    )

    console.print(Align.center(panel))
    print("")
    admin = Panel(
        Align.center(Text.from_ansi(
            f"{C.INFO}Admin: {C.BOLD}Idler Ha{C.RESET}\n"
            f"{C.INFO}GitHub: {C.PRIMARY}https://github.com/IdlerNetwork{C.RESET}"
        )),
        title="[bold cyan]Admin Information[/bold cyan]",
        title_align="center",
        width=box_width,
        border_style="bold cyan",
    )

    console.print(Align.center(admin))

if __name__ == "__main__":
    ntool()
