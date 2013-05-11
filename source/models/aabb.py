# -*- coding: utf-8 -*-

# import unittest

class AABB():
    """Boîte de collision AABB"""

    def __init__(self, x, y, w, h, vx, vy):
        """Give top-left corner position, width and height, velocity (all floats)"""
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.vx = vx
        self.vy = vy
        # note for Python: could use descriptors to get bottom / right positions easily

    # beware, it's a function!
    def sweptAABB(box1, box2):
        """
        Return the time of collision inside [0,1] (ratio of intended move in one frame before collision) or 1 if there is no collision (since the move is made at 100%)
        (asymmetric case: only box1 moves)
        and the normal vector of the collision side as a tuple ((0,0) if no collision)

        """

        if box1.vx > 0:
            # if collision is to happen on the right of box1
            # if box2 is actually on the left, dist will be negative ('box1 had collided box2 in the past')
            # if the boxes' widths overlap, only one can be negative
            x_entry_dist = box2.x - (box1.x + box1.w) # get close distance
            x_exit_dist = (box2.x + box2.w) - box1.x # get far sides distance
        else:
            # collision left to box1: use algebric distances (negative here)
            x_entry_dist = (box2.x + box2.w) - box1.x
            x_exit_dist = box2.x - (box1.x + box1.w)

        if box1.vy > 0:
            # if collision is to happen on the right of box1 (if anormal_y)
            y_entry_dist = box2.y - (box1.y + box1.h) # get close distance
            y_exit_dist = (box2.y + box2.h) - box1.y # get far sides distance
        else:
            # collision left to box1: use algebric distances (negative here)
            y_entry_dist = (box2.y + box2.h) - box1.y
            y_exit_dist = box2.y - (box1.y + box1.h)

        if box1.vx == 0:
            # if no move in the x direction, use infinite values to ensure they are not the min / max later
            x_entry_time = float("-inf")
            x_exit_time = float("+inf")
        else:
            x_entry_time = x_entry_dist / box1.vx
            x_exit_time = x_exit_dist / box1.vx

        if box1.vy == 0:
            # same with y
            y_entry_time = float("-inf")
            y_exit_time = float("+inf")
        else:
            y_entry_time = y_entry_dist / box1.vy
            y_exit_time = y_exit_dist / box1.vy

        entry_time = max(x_entry_time, y_entry_time)
        exit_time = min(x_exit_time, y_exit_time)

        # return entry_time, exit_time
        if entry_time > exit_time or x_entry_time < 0 and y_entry_time < 0 or x_entry_time > 1 or y_entry_time > 1:
            # no collision
            return 1, (0,0) # ratio is 1, no normal vector

        else:
            # collision (maybe just at t=1)
            if x_entry_time > y_entry_time:
                # so entry_time equals x_entry_time and it is an x collision
                normal_y = 0 # normal vector is in x
                if x_entry_dist < 0:
                    # box1 collides with box2 on its left side, so normal is directed to the left
                    normal_x = 1
                else:
                    # same with right
                    normal_x = -1
            else:
                # y collision
                normal_x = 0 # normal vector is in y
                if y_exit_dist < 0:
                    # box1 collides with box2 on its upper side, so normal is directed upwards
                    normal_y = 1
                else:
                    # same with lower / downwards
                    normal_y = -1

            return entry_time, (normal_x, normal_y) # ratio = time of collision, normal vector
