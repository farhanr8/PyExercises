import random
import math

from gamelib import *


class ZombieCharacter(ICharacter):
    def __init__(self, obj_id, health, x, y, map_view):
        ICharacter.__init__(self, obj_id, health, x, y, map_view)

    def selectBehavior(self):
        prob = random.random()

        # If health is less than 50%, then heal with a 10% probability
        if prob < 0.1 and self.getHealth() < self.getInitHealth() * 0.5:
            return HealEvent(self)

        # Pick a random direction to walk 1 unit (Manhattan distance)
        x_off = random.randint(-1, 1)
        y_off = random.randint(-1, 1)

        # Check the bounds
        map_view = self.getMapView()
        size_x, size_y = map_view.getMapSize()
        x, y = self.getPos()
        if x + x_off < 0 or x + x_off >= size_x:
            x_off = 0
        if y + y_off < 0 or y + y_off >= size_y:
            y_off = 0

        return MoveEvent(self, x + x_off, y + y_off)


class PlayerCharacter(ICharacter):
    def __init__(self, obj_id, health, x, y, map_view):
        ICharacter.__init__(self, obj_id, health, x, y, map_view)
        # You may add any instance attributes you find useful to save information between frames
        self.game_frame = 0
        self.closest_zombie_x = map_view.getMapSize()[0]
        self.closest_zombie_y = map_view.getMapSize()[1]
        self.target_zombie = 0

    def selectBehavior(self):

        self.game_frame += 1

        scan_results = self.getScanResults()

        x_off, y_off = 1, 1
        map_view = self.getMapView()
        size_x, size_y = map_view.getMapSize()
        x, y = self.getPos()

        # HEAL
        prob = random.random()

        # If health is less than 40%, then heal with a 30% probability
        if prob < 0.3 and self.getHealth() < self.getInitHealth() * 0.4:
            return HealEvent(self)

        # SCAN
        if self.game_frame == 1:
            return ScanEvent(self)
        if self.game_frame != 2 and self.game_frame % 2 == 0:
            return ScanEvent(self)

        # If no zombies nearby, don't do anything. TODO: Make it efficient
        if len(scan_results) == 0:
            return MoveEvent(self, x, y)

        for res in scan_results:
            pos = res.getPos()

            if pos[0] <= self.closest_zombie_x and pos[1] <= self.closest_zombie_y:
                self.closest_zombie_x = pos[0]
                self.closest_zombie_y = pos[1]
                self.target_zombie = res.getID()

        # ATTACK
        if 3 > abs(x - self.closest_zombie_x) > 0:
            if 3 > abs(y - self.closest_zombie_y) > 0:
                return AttackEvent(self, self.target_zombie)

        # MOVE

        # Run away. Too close to zombies    TODO: Fix this
        if abs(x - self.closest_zombie_x) < 1:
            if self.closest_zombie_x > x:
                x_off = -1
        if abs(y - self.closest_zombie_y) < 1:
            if self.closest_zombie_y > y:
                y_off = -1

        # At the edge
        if x + x_off < 0 or x + x_off >= size_x:
            x_off = 0
        if y + y_off < 0 or y + y_off >= size_y:
            y_off = 0

        return MoveEvent(self, x + x_off, y + y_off)





