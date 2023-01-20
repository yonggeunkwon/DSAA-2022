# -*- coding: utf8 -*-

import os
import sys
sys.executable

if os.environ.get('DISPLAY',''):
    print('no display found. Using :0.0')
    os.system('Xvfb :1 -screen 0 1600x1200x16  &')
    os.environ.__setitem__('DISPLAY', ':0.1')

import unittest
import os
import urllib.request
import pickle
from datetime import datetime


import miro_finder as mf
from pyamaze import maze,agent

class MyMifoFinder(unittest.TestCase):
    def test_get_maze_answer(self):
        map_list = [(5, 5), (3, 3), (10, 5), (8, 9)]
        for map_size in map_list:
            m=maze(*map_size)
            m.CreateMaze(loopPercent=0)
            #a=agent(m,filled=True,footprints=True)
            #m.tracePath({a:m.path})
            maze_map = m.maze_map
            print(maze_map)
            
            starting_point = map_size
            solution = []
            solution.append(starting_point)

            while m.path[starting_point] != (1, 1):
                starting_point = m.path[starting_point]
                solution.append(starting_point)
            solution.append(m.path[starting_point])
            print(solution)
            self.assertEqual(
                solution, mf.get_maze_answer(maze_map))

if __name__ == '__main__':  
    unittest.main()
