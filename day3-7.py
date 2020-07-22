# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 15:46:55 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getTilePos()

mc.setSign(x,y,z,63,0,
           "[1,2,3]","[2,4,6]","[3,6,9]")















