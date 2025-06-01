import pygame, time

pygame.font.init()

class Clock():
    def __init__(self):
        self.start_time = None
        self.cur_time = 0
        self.font = pygame.font.SysFont('monospace', 35)
        self.m_color = pygame.Color('yellow')

    def start_timer(self):
        self.start_time = time.time()

    def update_timer(self):
        if self.start_time is not None:
            self.cur_time = time.time() - self.start_time

    def display_timer(self):
        secs = int(self.cur_time % 60)
        min = int(self.cur_time / 60)
        my_time = self.font.render(f"{min:02}:{secs:02}", True, self.m_color)
        return my_time

    def stop_timer(self):
        self.start_time = None