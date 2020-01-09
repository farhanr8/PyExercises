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
        self.max_x = map_view.getMapSize()[0]
        self.max_y = map_view.getMapSize()[1]
        self.closest_zombie_x = self.max_x
        self.closest_zombie_y = self.max_y
        self.target_zombie = 0
        self.run = 0
        self.heal_count = 0

    def selectBehavior(self):

        self.game_frame += 1

        scan_results = self.getScanResults()

        x_off, y_off = 1, 1
        map_view = self.getMapView()
        size_x, size_y = map_view.getMapSize()
        x, y = self.getPos()

        ''' HEAL '''

        # If health is less than 80% and there's heal left
        if self.getHealth() < self.getInitHealth() * 0.2 and self.heal_count < 5:
            self.heal_count += 1
            return HealEvent(self)

        if self.run == 0:

            # If health is less than 50%, then heal with a 30% probability
            prob = random.random()
            prob_threshold = 0.3
            health_threshold = 0.5

            if prob < prob_threshold and self.getHealth() < self.getInitHealth() * health_threshold:
                self.heal_count += 1
                return HealEvent(self)

        ''' SCAN '''

        if self.game_frame == 1:
            return ScanEvent(self)

        if self.game_frame != 2 and self.game_frame % 2 == 0:
            self.closest_zombie_x = self.max_x
            self.closest_zombie_y = self.max_y
            return ScanEvent(self)

        # If no zombies nearby, go towards center
        if len(scan_results) == 0:
            mid_x = self.max_x / 2
            mid_y = self.max_y / 2

            if x - mid_x > 0:
                x_off = -1
            if y - mid_y > 0:
                y_off = -1

            return MoveEvent(self, x + x_off, y + y_off)

        # If there's zombie nearby, go to a safe distance and then attack
        for res in scan_results:
            pos = res.getPos()

            if pos[0] <= self.closest_zombie_x and pos[1] <= self.closest_zombie_y:
                self.closest_zombie_x = pos[0]
                self.closest_zombie_y = pos[1]
                self.target_zombie = res.getID()

        ''' ATTACK '''

        x_diff = abs(x - self.closest_zombie_x)
        y_diff = abs(y - self.closest_zombie_y)

        if (3 > x_diff > 0 and 3 > y_diff > 1) or (3 > y_diff > 0 and 3 > x_diff > 1):
                return AttackEvent(self, self.target_zombie)

        ''' MOVE '''

        # Run away. Too close to zombies
        if x_diff < 2 and y_diff < 2:
            self.run = 1
            if self.closest_zombie_x > x:
                x_off = -1
            if self.closest_zombie_y > y:
                y_off = -1
        else:
            self.run = 0

        # Going to safe distance to zombie
        if self.run == 0:
            if x - self.closest_zombie_x > 0:
                x_off = -1
            if y - self.closest_zombie_y > 0:
                y_off = -1

        # At the edge. If stuck ATTACK!!
        corner2 = False
        corner1 = False
        if x + x_off < 0 or x + x_off >= size_x:
            x_off = 0
            corner1 = True
        if y + y_off < 0 or y + y_off >= size_y:
            y_off = 0
            corner2 = True
        if corner1 and corner2:
            return AttackEvent(self, self.target_zombie)

        return MoveEvent(self, x + x_off, y + y_off)





