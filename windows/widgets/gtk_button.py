import tkinter as tk
class RTkButton():
    def __init__(self, parent, width=125, height=35, radius=25, text='Button', font=('San Francisco', 10), 
                 color='#00cc00', hover_color='#00aa00', text_color='', bg_color='', image=None, compound='left', 
                 click_effect='resize', command=None):
        self.parent = parent
        self.width = width
        self.height = height
        self.radius = radius
        self.text = text
        self.font = font
        self.color = color
        self.hover_color = hover_color
        self.text_color = text_color
        self.bg_color = bg_color
        self.image = image
        self.compound = compound
        self.click_effect = click_effect
        self.command = command
        self.image_posx = self.width // 2
        self.image_posy = self.height // 2

        if not self.bg_color:
            window_color = self.parent.cget('bg')
            rgb_values = self.parent.winfo_rgb(window_color)
            hex_color = '#{:02x}{:02x}{:02x}'.format(
                rgb_values[0] // 256,
                rgb_values[1] // 256,
                rgb_values[2] // 256
            )
            self.bg_color = hex_color

        self.c = tk.Canvas(parent, width=width, height=height, bg=self.bg_color, highlightthickness=0)
        
        if not self.text_color:
            if self.color.count('f') > 3 or self.color.count('F') > 3:
                self.text_color = '#000000'
            else:
                self.text_color = '#FFFFFF'
        
        self.c.create_image(self.image_posx, self.image_posy, image=self.image, anchor='w', tags='btn_image')
        self.c.create_text(self.width // 2, self.height // 2, text=self.text, font=self.font, fill=self.text_color, tags='btn_text')
        self.c.create_rectangle(0, 0, width, height, fill='', outline='', tags='hitbox')

        self.c.bind('<Configure>', self.update_button_size)
        self.c.tag_bind('hitbox', '<Enter>', lambda e: self.btnHover('enter'))
        self.c.tag_bind('hitbox', '<Leave>', lambda e: self.btnHover('leave'))
        self.c.tag_bind('hitbox', '<Button-1>', lambda e: self.btnClick('click'))
        self.c.tag_bind('hitbox', '<ButtonRelease-1>', lambda e: self.btnClick('release'))

        self.update_button_size()

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

    def update_button_size(self, state='release', event=None):
        w, h = self.c.winfo_width(), self.c.winfo_height()
        self.c.delete('btn_rect')
        if state == 'click':
            if self.click_effect == 'resize':
                self.create_rounded_rectangle(self.c, 2, 2, w-4, h-4, radius=self.radius, fill=self.hover_color, tags='btn_rect')
            elif not self.click_effect:
                self.create_rounded_rectangle(self.c, 0, 0, w, h, radius=self.radius, fill=self.hover_color, tags='btn_rect')    
        else:
            self.create_rounded_rectangle(self.c, 0, 0, w, h, radius=self.radius, fill=self.hover_color, tags='btn_rect')
        if self.image:
            if self.compound == 'left': 
                self.image_posx = 5
            elif self.compound == 'center': 
                self.image_posx = w // 2
            elif self.compound == 'right': 
                self.image_posx = w - 5
            self.c.coords('btn_image', self.image_posx, self.image_posy)
        self.c.coords('btn_text', self.width // 2, self.height // 2)
        self.c.coords('hitbox', 0, 0, w, h)
        self.c.tag_raise('btn_image')   
        self.c.tag_raise('btn_text')
        self.c.tag_raise('hitbox')

    def btnHover(self, state):
        if state == 'enter':
            self.c.itemconfig('btn_rect', fill=self.hover_color)
        elif state == 'leave':
            self.c.itemconfig('btn_rect', fill=self.color)

    def btnClick(self, state):
        if state == 'click':
            self.update_button_size(state=state)
        elif state == 'release':
            self.update_button_size(state=state)
            if self.command:
                self.command()

    def pack(self, **kwargs):
        self.c.pack(**kwargs)
        self.update_button_size()

    def place(self, **kwargs):
        self.c.place(**kwargs)
        self.update_button_size()

    def grid(self, **kwargs):
        self.c.grid(**kwargs)
        self.update_button_size()