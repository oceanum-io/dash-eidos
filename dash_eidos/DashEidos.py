# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DashEidos(Component):
    """A DashEidos component.
DashEidos is a an EIDOS visualisation component for Dash.
  It takes a EIDOS spec, converts it to a React component in a Plotly dash app,

Keyword arguments:

- id (string; required):
    The ID used to identify this component in Dash callbacks.

- eidos (dict; required):
    Eidos spec.

- events (list; default ["click"]):
    List of EIDOS events to listen to. Can be any of: ['click'].

- height (number | string; default 500):
    Height of the map component container as pixels or CSS string
    (optional) Default 500.

- lastevent (dict; optional):
    The last event that was triggered. This is a read-only property.

- renderer (string; default "https://render.eidos.oceanum.io"):
    The URL of the EIDOS renderer.

- spectype (a value equal to: "spec", "patch"; default "spec"):
    The type of spec. Can be either 'spec' or 'patch'.

- width (number | string; default "100%"):
    An array of tooltip objects that follows he pydeck tooltip
    specifcation. An additonal 'layer' property can be added to the
    tooltip objects to restrict their action to that layer ID."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_eidos'
    _type = 'DashEidos'
    @_explicitize_args
    def __init__(self, id=Component.REQUIRED, eidos=Component.REQUIRED, spectype=Component.UNDEFINED, width=Component.UNDEFINED, height=Component.UNDEFINED, events=Component.UNDEFINED, lastevent=Component.UNDEFINED, renderer=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'eidos', 'events', 'height', 'lastevent', 'renderer', 'spectype', 'width']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'eidos', 'events', 'height', 'lastevent', 'renderer', 'spectype', 'width']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['id', 'eidos']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(DashEidos, self).__init__(**args)
