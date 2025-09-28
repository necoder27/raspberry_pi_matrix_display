import displayio
from screens.screen import BaseScreen

class CatAnimation(BaseScreen):
    def __init__(self, group, font):
        super().__init__(group, font)
        self.tiles = []
        self.current_index = 0
        self.special_sprite = False
        self.frames = [
            displayio.OnDiskBitmap("imgs/cat_sprite_1.bmp"),
            displayio.OnDiskBitmap("imgs/cat_sprite_2.bmp"),
            displayio.OnDiskBitmap("imgs/cat_sprite_3.bmp"),
            displayio.OnDiskBitmap("imgs/cat_sprite_4.bmp"),
            displayio.OnDiskBitmap("imgs/cat_sprite_5.bmp"),
            displayio.OnDiskBitmap("imgs/cat_sprite_3_2.bmp"),
        ]

        for frame in self.frames:
            tile = displayio.TileGrid(frame, pixel_shader=frame.pixel_shader)
            self.tiles.append(tile)

    def update(self):
        if self.tiles[self.current_index] in self.group:
            self.group.remove(self.tiles[self.current_index])
        self.current_index = (self.current_index + 1) % 5

        if not (self.special_sprite and self.current_index == 2):
            self.group.append(self.tiles[self.current_index])
        else:
            if self.tiles[5] in self.group:
                self.group.remove(self.tiles[5])
            self.group.append(self.tiles[5])

        if self.current_index == 4:
            self.special_sprite = not self.special_sprite
