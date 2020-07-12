import copy
import random
# Consider using the modules imported above.

class Hat:
    
    def __init__(self, **kwargs):
        self.contents = []
        for color, number in kwargs.items():
            self.contents.extend([color] * number)

    def draw(self, number):
        if number >= len(self.contents):
            balls = self.contents.copy()
            self.contents.clear()
        else:
            balls = random.sample(self.contents, number)
            for ball in balls:
                self.contents.remove(ball)
        return balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success_cnt = 0  # how many times drawn balls match expectations of experiment
    
    for _ in range(num_experiments):
        hat_cp = copy.deepcopy(hat)
        drawn_balls = hat_cp.draw(num_balls_drawn)
        
        for color, number in expected_balls.items():
            if drawn_balls.count(color) < number:
                break
        else:
            success_cnt += 1

    return success_cnt / num_experiments
