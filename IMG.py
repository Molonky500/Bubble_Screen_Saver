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

            'PowerBubble': {'Alpha': True, 'colorkey': None, 'surface': None},

        }
        for imgname, imgData in self.Bubble_imgDict.items():
            img = pg.image.load(pathlib.Path(self.folder).joinpath(f'{imgname}.png'))
            _:  Surface 
            for _ in imgData:
                if imgData['Alpha'] is True:
                    img = pg.Surface.convert_alpha(img)
                elif imgData['Alpha'] is False:
                    img = pg.Surface.convert(img)
                    if imgData['colorkey'] is not None:
                        img = img.set_colorkey((imgData['colorkey']))
                self.Bubble_imgDict[imgname] = img,
                # ic(self.Bubble_imgDict, "Image Loaded")
        self.OGPowerBubble = self.Bubble_imgDict['PowerBubble'][0]
        ic(self.Bubble_imgDict, "Image Loaded")
# Deprecated
#  def IMG load(self, Image_Name, Alpha = bool, colorkey = None ):
#      ic(pathlib.Path(self.folder).joinpath(f'{Image_Name}.png'))
#      self.Alpha = Alpha
#      self.ColorKey = colorkey
#      if self.Alpha is True:
#          self.IMG = pg.image.load(pathlib.Path(self.folder).joinpath(f'{Image_Name}.png'))
#          self.IMG = pg.Surface.convert_alpha(self.IMG)
#          ic(self.Alpha,"surface converted")
#      elif colorkey is not None:
#          self.IMG = pg.image.load(f'{Image_Name}.png')
#          self.IMG = pg.Surface.convert(self.IMG)
#          self.IMG = self.IMG.set_colorkey((self.ColorKey))
#          ic(self.ColorKey, "surface converted")
# 'path': self.folder,
# 'path': self.folder,
# 'path': self.folder,
# 'path': self.folder,
# 'path': self.folder,
# 'path': self.folder,
# 'path': self.folder,
# 'path': self.folder,
#    #
#      self.Bubble_imgDict[Image_Name] = self.IMG,
#
#
#      #return self.IMG
