# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 11:18:57 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getTilePos()
for i in range(3):
    mc.setBlock(x,y-1,z+i,41)
    mc.setBlock(x+3+i,y-1+i,z,41)

   








