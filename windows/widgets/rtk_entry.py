import tkinter as tk

class RTkEntry:
    def __init__(self, parent, width=140, height=28, radius=10, font=('San Francisco', 10),
                 color='#dddddd', border_color='#c3c3c3', border_width=2, text_color='', bg_color='', relief='flat'):
        self.parent = parent
        self.width = width
        self.height = height
        self.radius = radius
        self.font = font
        self.color = color
        self.border_color = border_color
        self.border_width = border_width
        self.text_color = text_color
        self.bg_color = bg_color
        self.relief = relief

        if not self.bg_color:
            window_color = self.parent.cget('bg')
            rgb_values = self.parent.winfo_rgb(window_color)
            hex_color = '#{:02x}{:02x}{:02x}'.format(
                rgb_values[0] // 256,
                rgb_values[1] // 256,
                rgb_values[2] // 256
            )
            self.bg_color = hex_color

        self.c = tk.Canvas(parent, width=self.width, height=self.height, bg=self.bg_color, highlightthickness=0)

        self.e = tk.Entry(relief=tk.FLAT, highlightthickness=0, bg=self.color)
        self.c.create_window(5, self.height // 2, window=self.e, anchor='w', tags='entry')

        self.update_entry()

    def create_rounded_rectangle(self, canvas, x1, y1, x2, y2, radius=25, **kwargs):
        points = [x1+radius, y1,
                  x1+radius, y1, x2-radius, y1,
                  x2-radius, y1, x2, y1,
                  x2, y1+radius, x2, y1+radius,
                  x2, y2-radius, x2, y2-radius,
                  x2, y2, x2-radius, y2,
                  x2-radius, y2, x1+radius, y2,
                  x1+radius, y2, x1, y2,
                  x1, y2-radius, x1, y2-radius,
                  x1, y1+radius, x1, y1+radius,
                  x1, y1]

        return canvas.create_polygon(points, **kwargs, smooth=True)
    
    def update_entry(self):
        w, h = self.c.winfo_width(), self.c.winfo_height()
        self.c.delete('entry_rect')
        self.c.delete('entry_border')
        if self.relief == 'flat':
            self.create_rounded_rectangle(self.c, 0, 0, self.width, self.height, radius=self.radius, fill=self.border_color, tags='entry_rect')
            self.create_rounded_rectangle(self.c, self.border_width, self.border_width, self.width-self.border_width, self.height-self.border_width, radius=self.radius, fill=self.color, tags='entry_border')
        elif self.relief == 'sunken':
            self.create_rounded_rectangle(self.c, 0, 0, self.width, self.height, radius=self.radius, fill=self.border_color, tags='entry_rect')
            self.create_rounded_rectangle(self.c, self.border_width, self.border_width, self.width, self.height, radius=self.radius, fill=self.color, tags='entry_border')
        else:
            raise ValueError('bad relief : must be flat or sunken')
        # self.c.coords('entry', w // 2, h // 2)
        # self.c.tag_raise('entry')

    def pack(self, **kwargs):
        self.c.pack(**kwargs)
        self.update_entry()

    def place(self, **kwargs):
        self.c.place(**kwargs)
        self.update_entry()

    def grid(self, **kwargs):
        self.c.grid(**kwargs)
        self.update_entry()