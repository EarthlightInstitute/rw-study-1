#!/usr/bin/env python
# encoding: utf-8
"""
fastener.py

Created by Erik Evenson on 2012-03-22.
Copyright (c) 2012 3E Enterprises, LLC. All rights reserved.
"""

import sys
import os

FREECADPATH = '/usr/lib/freecad/lib'
SAVEPATH = '/mnt/hgfs/eevenson/Documents/Projects/FreeCADScripting'
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
		fastener = Part.makeBox(size, size, size)
		part.Shape = fastener

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
	fastener = Fastener()
	print fastener


if __name__ == '__main__':
	main()

