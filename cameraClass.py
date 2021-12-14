class Camera:

    def __init__(self, x=0, y=0):

        self.x = x
        self.y = y

        self.move_speed = 15

        self.right = False
        self.left = False
        self.up = False
        self.down= False
    def scroll(self, player_pos_x, player_pos_y):
        x_scroll = (player_pos_x + self.x - 900)/25
        self.x -= x_scroll
        
        y_scroll = (player_pos_y + self.y - 500)/10
        self.y -= y_scroll

    def move(self):
        if self.right:
            self.x -= self.move_speed
        if self.left:
            self.x += self.move_speed
        if self.up:
            self.y += self.move_speed
        if self.down:
            self.y -= self.move_speed

    def move_right(self, state):
        self.right = state

    def move_left(self, state):
        self.left = state

    def move_up(self, state):
        self.up = state

    def move_down(self, state):
        self.down = state