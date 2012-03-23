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

class Fastener():
	
	def representation(self):
		
		"""
		Returns a CAD representation of the fastener.  Defaults to a FreeCAD object.
		"""
		
		import FreeCAD
		import Part

		name = "fastener"
		size = 10
		part = FreeCAD.ActiveDocument.addObject("Part::Feature",name)
		
		# Just create a simple object for now.
		shape = Part.makeBox(size, size, size)
		part.Shape = shape

		return part
		
	def strength(self):
		
		"""
		Returns a dictionary of strength parameters.
		"""
		
		return {}


def main():
	
	"""
	Generates a sample default fastener.
	"""
	bolt = Fastener()
	print bolt


if __name__ == '__main__':
	main()

