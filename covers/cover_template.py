"""HomeProject cover template: same layout, own image + accent color per video. Title in 3:4 safe zone."""
import sys
from PIL import Image, ImageDraw, ImageFont
W, H = 1080, 1920; BG = (247, 246, 242); NAVY = (16, 42, 67)
F = "/home/claude/motor/engine/fonts/"
ANTON = lambda s: ImageFont.truetype(F + "Anton-Regular.ttf", s); BEB = lambda s: ImageFont.truetype(F + "BebasNeue-Regular.ttf", s)
logo = Image.open("/home/claude/hp/logo.png").convert("RGBA")


def make(out, kicker, title, accent, img, box):
    c = Image.new("RGB", (W, H), BG); d = ImageDraw.Draw(c)
    # kicker pill (accent) + title (navy), inside 3:4 safe zone (y 240..1680)
    f = BEB(84); tw = d.textlength(kicker, font=f); y = 330
    d.rounded_rectangle([(W - tw) / 2 - 36, y - 6, (W + tw) / 2 + 36, y + 92], radius=18, fill=accent)
    d.text(((W - tw) / 2, y), kicker, font=f, fill=(255, 255, 255))
    y = 470
    for line in title:
        s = 190
        while d.textlength(line, font=ANTON(s)) > W - 120: s -= 6
        tw = d.textlength(line, font=ANTON(s)); d.text(((W - tw) / 2, y), line, font=ANTON(s), fill=NAVY, stroke_width=6, stroke_fill=(255, 255, 255))
        y += int(s * 1.12)
    src = Image.open(img).convert("RGB").crop(box); bw = 900; bh = int(src.height * bw / src.width)
    if bh > 1640 - y - 30: bh = 1640 - y - 30; bw = int(src.width * bh / src.height)
    src = src.resize((bw, bh), Image.LANCZOS); c.paste(src, ((W - bw) // 2, y + 30))
    d.rectangle([0, 0, W, 26], fill=accent); d.rectangle([0, H - 26, W, H], fill=accent)
    c.save(out, quality=92); print(out)


if __name__ == "__main__":
    S = "/tmp/claude-0/-home-claude/bb496f05-7973-5de4-a57a-38e4179fb5e1/scratchpad/"
    make("/home/claude/covers/2026-10-26-impuesto.jpg", "IMPUESTO DE TU CASA", ["AHORRA 4%", "EN NOVIEMBRE"], (40, 140, 80), S + "i_13.5.png", (100, 690, 980, 1480))
    make("/home/claude/covers/2026-10-26-ventanas.jpg", "VENTANAS", ["¿AGUANTA UN", "HURACÁN?"], (200, 60, 50), S + "v_1.png", (40, 835, 1040, 1500))
