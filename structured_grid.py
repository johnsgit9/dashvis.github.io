import dash
import dash_vtk
from dash import html
from dash import dcc, callback
from dash.dependencies import Input, Output, State
import dash_daq as daq

import numpy as np
import pyvista as pv
from pyvista import examples

from vtk import vtkStructuredPointsReader
from dash_vtk.utils import to_mesh_state, preset_as_options


class Viz:
    def __init__(self):
        filename = 'structured_grid.vtk'

        reader = vtkStructuredPointsReader()
        reader.SetFileName(filename)
        reader.ReadAllVectorsOn()
        reader.ReadAllScalarsOn()
        reader.Update()
        self.mesh = to_mesh_state(reader.GetOutput())
        self.edgeVisibility = True
        
    def updateMeshVisiblility(self, value):
        self.edgeVisibility = value
    
    def getVtkMesh(self):
        return self.mesh

viz = Viz()

# Setup VTK rendering of PointCloud
app = dash.Dash(__name__)
server = app.server

#edgeVisibility = False

def vtk_view(edgeVisibility):
    return dash_vtk.View([
        dash_vtk.GeometryRepresentation([
                    dash_vtk.Mesh(id='simple_mesh',
                        state=viz.getVtkMesh())
                        ],
                        property={"edgeVisibility": edgeVisibility}
                    ),
        ])



app.layout = html.Div(
    style={"height": "calc(100vh - 16px)"},
    children=[
            daq.ToggleSwitch(
            id='my-toggle-switch',
            value=True,
            label="Add grid lines",
            labelPosition="top",
            ),
        html.Div(id='my-toggle-switch-output',
                 style={"height": "100%", "width": "100%"})
        ],
)

@callback(
            Output('my-toggle-switch-output', 'children'),
            Input('my-toggle-switch', 'value')
            )
def update_output(value):
    viz.updateMeshVisiblility(value)
    
    return vtk_view(viz.edgeVisibility)

if __name__ == "__main__":
    app.run(debug=True)
