#!/usr/bin/env python
# encoding: utf-8
"""
main.py

Created by Erik Evenson on 2012-03-22.
"""

import sys
import os
import fastener

FREECADPATH = '/usr/lib/freecad/lib'
SAVEPATH = '.'

def main():

	"""
	Shows how to invoke methods.
	"""
		
	sys.path.append(FREECADPATH)
	import FreeCAD
	name = "bolt"

	docName = name + "_doc" 
	fileName = SAVEPATH + "/" + name + ".FCStd"
	label = name

	doc=App.newDocument(docName)
	
	bolt = fastener.Fastener()
	bolt.add_freecad_rep(doc)

	App.getDocument(docName).FileName = fileName
	App.getDocument(docName).Label = label
	App.getDocument(docName).save()


if __name__ == '__main__':
	main()

