#! /usr/bin/python

import vtk

reader=vtk.vtkXMLPolyDataReader()
reader.SetFileName("PelvisPhantom_mirror/FullPelvis_mirror.vtp")
reader.Update()
surface=reader.GetOutput()

reverse = vtk.vtkReverseSense()
reverse.SetInputData(surface)
reverse.SetInputData(surface)
reverse.ReverseNormalsOn()
reverse.ReverseCellsOn()
reverse.Update()
flipsurf=reverse.GetOutput()

writer=vtk.vtkXMLPolyDataWriter()
writer.SetFileName("PelvisPhantom_mirror/FullPelvis_mirror_flip.vtp")
writer.SetInputData(flipsurf)
writer.Update()

