#! /usr/bin/python

import vtk

reader=vtk.vtkPolyDataReader()
reader.SetFileName("PelvisPhantom/FullPelvis.vtk")
reader.Update()
surface=reader.GetOutput()

flipper=vtk.vtkMatrix4x4()
flipper.SetElement(2,2,-1.0)

transform=vtk.vtkTransform()
transform.SetMatrix(flipper)

polyfilter=vtk.vtkTransformPolyDataFilter()
polyfilter.SetTransform(transform)
polyfilter.SetInputData(surface)
polyfilter.Update()

flipsurf=polyfilter.GetOutput()

writer=vtk.vtkXMLPolyDataWriter()
writer.SetFileName("PelvisPhantom_mirror/FullPelvis_mirror.vtp")
writer.SetInputData(flipsurf)
writer.Update()


