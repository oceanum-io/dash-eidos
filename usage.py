import os
import pydeck as pdk
import xarray as xr
import shapely as sh
import geopandas as gpd
import dash_eidos
from dash import Dash, callback, html, Input, Output

from oceanum.eidos import Eidos, Node, FeatureLayerSpec, Layer, EidosDatasource

layerSpec = FeatureLayerSpec(
    hoverInfo={"template": "{{name}}"},
    style={
        "getPointRadius": 10,
        "getFillColor": "red",
        "opacity": 1.0,
        "pointRadiusUnits": "pixels",
    },
)

points_layer = Layer(
    id="points",
    layerType="feature",
    dataId="points_data",
    visible=True,
    layerSpec=layerSpec,
)


points_data = gpd.GeoDataFrame(
    {"name": ["Null island"]}, geometry=[sh.geometry.Point(0, 0)]
)

e = Eidos(
    id="eidos_test",
    name="EIDOS Test",
    title="Test",
    data=[EidosDatasource("points_data", points_data)],
    rootNode=Node(
        id="my-map", name="Root", nodeType="world", nodeSpec={"layers": [points_layer]}
    ),
)

app = Dash(__name__)

app.layout = html.Div(
    [
        dash_eidos.DashEidos(
            id="eidos_test",
            eidos=e.model_dump(),
            spectype="spec",
            events=["click", "hover"],
            width="100%",
            height="800px",
            renderer="http://localhost:3001",
        ),
        html.Div(id="output"),
    ]
)


@callback(
    Output("eidos_test", "eidos"),
    Output("eidos_test", "spectype"),
    Input("eidos_test", "lastevent"),
    prevent_initial_call=True,
)
def update_point(lastevent):
    if not lastevent:
        return None, "null"
    points_data = gpd.GeoDataFrame(
        {"name": ["Null island"]},
        geometry=[sh.geometry.Point(lastevent.get("coordinate"))],
    )
    e.data = [EidosDatasource("points_data", points_data)]
    return e.patch(), "patch"


if __name__ == "__main__":
    app.run_server(debug=True)
