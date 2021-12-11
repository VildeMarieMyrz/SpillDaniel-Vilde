import ctypes

class System:
    def __init__(self):
        user32 = ctypes.windll.user32
        
        self.screen_size = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)-70