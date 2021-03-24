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
#transform.SetScale(1.,1.,-1.)
polyfilter=vtk.vtkTransformPolyDataFilter()
polyfilter.SetTransform(transform)
polyfilter.SetInputData(surface)
polyfilter.Update()

#flipsurf=polyfilter.GetOutput()

reverse = vtk.vtkReverseSense()
reverse.SetInputData(polyfilter.GetOutput())
#reverse.ReverseNormalsOn()
reverse.ReverseCellsOn()
reverse.Update()
flipsurf=reverse.GetOutput()

writer=vtk.vtkXMLPolyDataWriter()
writer.SetFileName("PelvisPhantom_mirror_flip/FullPelvis_mirror_flip.vtp")
writer.SetInputData(flipsurf)
writer.Update()

