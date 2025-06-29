# ~/display/display.py
class BaseScreen:
    def clear(self): pass
    def draw_image(self, path, position): pass
    def draw_text(self, text, position, size=16, color=(255, 255, 255)): pass
    def update(self): pass