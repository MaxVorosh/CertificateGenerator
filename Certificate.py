from PIL import Image, ImageDraw, ImageFont
import os


def size_to_pixels(size):
    return size * 3 // 4

class Certificate:
    def __init__(self, owner, width=2970, height=2100, type='Сертификат'):
        self.width = width
        self.height = height
        self.owner = owner
        self.bg = None
        self.nomination = ''
        self.content = []
        self.type = type

    def add_item(self, path, x, y, scale_x=1, scale_y=1, alpha=255, angle=0):
        item = Image.open(path)
        item.putalpha(alpha)
        item = item.rotate(angle, expand=True)
        item = item.resize((int(scale_x * item.size[0]), int(scale_y * item.size[1])))
        self.content.append([item, (x, y)])

    def set_nomination(self, text):
        self.nomination = text

    def set_bg(self, path):
        self.bg = Image.open(path)
        self.bg = self.bg.resize((self.width, self.height))

    def save(self, path):
        certificate = Image.new('RGBA', (self.width, self.height), 'White')
        certificate.paste(self.bg, (0, 0))
        for item in self.content:
            certificate.paste(item[0], item[1], item[0])
        draw = ImageDraw.Draw(certificate)
        text = [(self.type, 140), (self.nomination, 100), (self.owner, 100)]
        y = 200
        for line in text:
            font = ImageFont.truetype(os.path.join('font', 'font.ttf'), size=line[1])
            length = font.getlength(line[0])
            y += (font.getbbox(line[0])[3] - font.getbbox(line[0])[1]) + 50
            draw.text(((self.width - length) // 2, y), line[0], fill=(0, 0, 0), font=font)
        certificate = certificate.convert('RGB')
        certificate.save(path)
