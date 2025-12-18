# dashvis

```{admonition} Download sources
:class: download

* {Download}`Python script<./axisymmetric_elasticity.py>`
```

Import relevant libraries

```python
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
```

[back](./)


