import random
import time
import math

class SoccerAgent:
    """
    An AI Agent representing a soccer striker using PEAS logic.
    """
    def __init__(self):
        # Environment Setup
        self.agent_pos = [0, 0]
        self.ball_pos = [random.randint(10, 30), random.randint(10, 30)]
        self.goal_pos = [50, 25]
        self.has_ball = False
        self.steps = 0

    def get_distance(self, pos1, pos2):
        # Sensor Logic: Euclidean Distance
        return math.sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)

    def move_towards(self, target):
        # Actuator Logic: Movement
        if self.agent_pos[0] < target[0]: self.agent_pos[0] += 1
        elif self.agent_pos[0] > target[0]: self.agent_pos[0] -= 1
        
        if self.agent_pos[1] < target[1]: self.agent_pos[1] += 1
        elif self.agent_pos[1] > target[1]: self.agent_pos[1] -= 1

    def run_simulation(self):
        print("--- Match Started ---")
        print(f"Goal is at: {self.goal_pos} | Ball is at: {self.ball_pos}")
        
        while True:
            self.steps += 1
            dist_to_ball = self.get_distance(self.agent_pos, self.ball_pos)
            
            if not self.has_ball:
                if dist_to_ball < 1:
                    self.has_ball = True
                    print(f"Step {self.steps}: [BALL ACQUIRED]")
                else:
                    self.move_towards(self.ball_pos)
                    print(f"Step {self.steps}: Moving to ball... {self.agent_pos}")
            
            else:
                dist_to_goal = self.get_distance(self.agent_pos, self.goal_pos)
                if dist_to_goal < 2:
                    print(f"Step {self.steps}: [SHOOTING ON GOAL]")
                    if random.random() > 0.1: # 90% success rate
                        print("GOAL!!! Simulation Complete.")
                        break
                    else:
                        print("Missed! Retrying...")
                else:
                    self.move_towards(self.goal_pos)
                    self.ball_pos = self.agent_pos # Ball moves with agent
                    print(f"Step {self.steps}: Dribbling to goal... {self.agent_pos}")
            
            time.sleep(0.1)

if __name__ == "__main__":
    striker = SoccerAgent()
    striker.run_simulation()
