import sys 

class GameState():
    def __init__(self):
        self.score = 0
        self.lives = 5

    def kill_ast(self):
        self.score += 10
    
    def hit_ast(self):
        self.lives -= 1
        if self.lives <= 0:
            print("Game over!")
            sys.exit()

    def get_score(self):
        return self.score
    
    def get_lives(self):
        return self.lives