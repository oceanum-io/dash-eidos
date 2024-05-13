# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Eidos(Component):
    """An Eidos component.


Keyword arguments:
"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_eidos'
    _type = 'Eidos'
    @_explicitize_args
    def __init__(self, width=Component.UNDEFINED, height=Component.UNDEFINED, events=Component.UNDEFINED, renderer=Component.UNDEFINED, **kwargs):
        self._prop_names = []
        self._valid_wildcard_attributes =            []
        self.available_properties = []
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(Eidos, self).__init__(**args)
