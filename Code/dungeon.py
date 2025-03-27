import pygame
import os 

class Dungeon:
    def __init__(self, width, height, tileset_image, tile_size = 16):
        self.width = width
        self.height = height
        self.tile_size = tile_size
        self.tiles = self.load_tiles(tileset_image)
    
    def load_tiles(self, tileset_image):
        tiles = {
            'wall': {
                'top': [tileset_image.subsurface((16, 0, self.tile_size, self.tile_size)),
                        tileset_image.subsurface((32, 0, self.tile_size, self.tile_size)),
                        tileset_image.subsurface((48, 0, self.tile_size, self.tile_size))],
                'bottom': [tileset_image.subsurface((16, 0, self.tile_size, self.tile_size))]
            }
        }