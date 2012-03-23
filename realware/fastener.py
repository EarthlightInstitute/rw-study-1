#!/usr/bin/env python
# encoding: utf-8
"""
fastener.py

Created by Erik Evenson on 2012-03-22.
"""

import sys
import os

FREECADPATH = '/usr/lib/freecad/lib'
sys.path.append(FREECADPATH)

import FreeCAD
import Part

class Fastener():
	
	def __init__(self):

		self.name = "fastener"
		self.size = 10
	
	def add_freecad_rep(self,doc):
		
		"""
		Adds a FreeCAD representation of the fastener to doc.
		"""
		
		self.part = doc.addObject("Part::Feature",self.name)
		
		# Just create a simple object for now.
		self.shape = Part.makeBox(self.size, self.size, self.size)
		self.part.Shape = self.shape
		
		return
		
	def strength(self):
		
		"""
		Returns a dictionary of strength parameters.
		"""
		
		return {'axial': 10000, 'shear': 5000}


def main():
	
	"""
	Generates a sample default fastener.
	"""
	bolt = Fastener()
	print bolt


if __name__ == '__main__':
	main()

