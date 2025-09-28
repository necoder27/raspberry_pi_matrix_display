import wifi
import time
import socketpool
import rtc
import adafruit_ntp

def sync_time():
    try:
        pool = socketpool.SocketPool(wifi.radio)
        ntp = adafruit_ntp.NTP(pool, tz_offset=2)
        rtc.RTC().datetime = ntp.datetime
        return True
    except Exception as e:
        print(e)
        return False

def get_time():
    t = time.localtime()
    return f"{t.tm_hour:02d}:{t.tm_min:02d}:{t.tm_sec:02d}"

def get_greeting():
    t = time.localtime()
    if (t.tm_hour < 12):
        return "morning"
    elif (t.tm_hour < 18):
       return "afternoon"
    else:
        return "evening"

def init():
    return sync_time()
