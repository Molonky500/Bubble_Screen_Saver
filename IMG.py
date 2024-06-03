import pathlib
import pygame as pg
from icecream import ic
# #image loader singleton
# to call loader
#  ImgLib. Lib.IMG load(image name, alpha true or false , color key if desired)
# noinspection SpellCheckingInspection


class Lib:
    def __init__(self):
        self.folder = r'Sprites'
        self.Bubble_imgDict = {
            'bubbleglowy': {'Alpha': True, 'colorkey': None, 'surface': None},
        }
        for imgname, imgData in self.Bubble_imgDict.items():
            img = pg.image.load(pathlib.Path(self.folder).joinpath(f'{imgname}.png'))
            for _ in imgData:
                if imgData['Alpha'] is True:
                    img = pg.Surface.convert_alpha(img)
                elif imgData['Alpha'] is False:
                    img = pg.Surface.convert(img)
                    if imgData['colorkey'] is not None:
                        img = img.set_colorkey((imgData['colorkey']))
                self.Bubble_imgDict[imgname] = img,
                # ic(self.Bubble_imgDict, "Image Loaded")
        self.og_bubble_glowy = self.Bubble_imgDict['bubbleglowy'][0]
        ic(self.Bubble_imgDict, "Image Loaded")
