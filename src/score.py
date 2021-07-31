class Score:
    def __init__(self):
        self.curr_score = 0
        self.best_score = self.load_best_score()
        
    
    def load_best_score(self):
        """Load best score"""

        with open("..//pref.pref", "r") as f:
            return int(f.read())


    def save_best_score(self):
        """Save best score"""

        with open("..//pref.pref", "w") as f:
            f.write(str(self.best_score))


    def update_score(self):
        """Update score"""

        self.curr_score += 1

        if self.curr_score > self.best_score:
            self.best_score = self.curr_score
