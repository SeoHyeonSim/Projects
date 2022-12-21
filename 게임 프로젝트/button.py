import pygame

class Button():
    
    def __init__(self, image, x_pos, y_pos, text_input):
        self.image = image
        self.x_pos = x_pos
        self.y_pose = y_pos
        self.rect = self.image.get_rect(center=(self.x_pos,self.y_pose))
        self.text_input = text_input
        self.text = game_font.render(self.text_input, True, "white")
        self.text_rect = self.text.get_rect(center=(self.x_pos,self.y_pose))
        
    def update(self):
        screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            print("Button Press!")

    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = game_font.render(self.text_input, True, "yellow")
        else:
            self.text = game_font.render(self.text_input, True, "white")


