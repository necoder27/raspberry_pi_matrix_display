import time
from adafruit_display_text import label
from screens.screen import BaseScreen
import get_time_through_wifi

class DefaultScreen(BaseScreen):
    def __init__(self, group, font, time_weather_group, row_group):
        super().__init__(group, font)
        self.time_weather_group = time_weather_group
        self.row_group = row_group
        self.greeting_label = label.Label(self.font, text="", color=0x5B17A3, x=2, y=4) #color=0xBA4FE3,
        self.name_label = label.Label(self.font, text="laetitia", color=0x5B17A3, x=2, y=10) #color=0xBA4FE3,
        self.time_label = label.Label(self.font, text="--:--:--", color=0xDB237B, x=2, y=22) # color=0xFF0088,
        self.weather_label = label.Label(self.font, text="uv0-17°sun", color=0xFC5538, x=2, y=28) # color=0xAAE3E5,
        self.get_time = get_time_through_wifi
        self.get_time.init()
        self.last_sync = time.monotonic()
        self.SYNC_INTERVAL = 3600

        self.time_weather_group.append(self.time_label)
        self.time_weather_group.append(self.weather_label)
        self.row_group.append(self.time_weather_group)
        self.group.append(self.greeting_label)
        self.group.append(self.name_label)
        self.group.append(self.row_group)

    def update(self):
        self.time_label.text = get_time_through_wifi.get_time()
        self.greeting_label.text = f"good {self.get_time.get_greeting()},"

        if time.monotonic() - self.last_sync > self.SYNC_INTERVAL:
            if self.get_time.sync_time():
                self.last_sync = time.monotonic()
