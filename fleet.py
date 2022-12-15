from robot import Robot
from weapon import Weapon


class Fleet:
    def __init__(self):
        self.robots = []
        self.create_fleet()


    def create_fleet(self):
        weapon1 = Weapon("Hammer", 8)
        weapon2 = Weapon("Machete", 15)
        weapon3 = Weapon("Grenade", 50)

        robot1 = Robot("DumbleTron", weapon1)
        robot2 = Robot("LightYear", weapon2)
        robot3 = Robot("Grenada", weapon3)

        self.robots.append(robot1)
        self.robots.append(robot2)
        self.robots.append(robot3)