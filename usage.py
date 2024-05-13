import os
import pydeck as pdk
import xarray as xr
import dash_eidos
from dash import Dash, callback, html, Input, Output

from oceanum.eidos import Eidos, Node


e = Eidos(
    id="eidos_test",
    name="EIDOS Test",
    title="Test",
    data=[],
    rootNode=Node(id="my-map", name="Root", nodeType="world", nodeSpec={}),
)

app = Dash(__name__)

app.layout = html.Div(
    [
        dash_eidos.DashEidos(
            id="Eidos",
            eidos=e.model_dump(),
            events=["click", "hover"],
            width="100%",
            height="800px",
            renderer="http://localhost:3001",
        ),
        html.Div(id="output"),
    ]
)


@callback(Output("output", "children"), Input("Eidos", "lastevent"))
def display_output(value):
    return "Mouse event: {}".format(value)


if __name__ == "__main__":
    app.run_server()
