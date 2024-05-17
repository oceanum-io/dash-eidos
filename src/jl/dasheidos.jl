# AUTO GENERATED FILE - DO NOT EDIT

export dasheidos

"""
    dasheidos(;kwargs...)

A DashEidos component.
DashEidos is a an EIDOS visualisation component for Dash.
  It takes a EIDOS spec, converts it to a React component in a Plotly dash app,
Keyword arguments:
- `id` (String; required): The ID used to identify this component in Dash callbacks.
- `eidos` (Dict; optional): Eidos spec
- `events` (Array; optional): List of EIDOS events to listen to. Can be any of:
['click']
- `height` (Real | String; optional): Height of the map component container as pixels or CSS string
(optional) Default 500
- `lastevent` (Dict; optional): The last event that was triggered. This is a read-only property.
- `renderer` (String; optional): The URL of the EIDOS renderer.
- `spectype` (a value equal to: "spec", "patch", "null"; optional): The type of spec. Can be either 'spec' or 'patch'.
- `width` (Real | String; optional): An array of tooltip objects that follows he pydeck tooltip specifcation.
An additonal 'layer' property can be added to the tooltip objects to restrict their action to that layer ID.
"""
function dasheidos(; kwargs...)
        available_props = Symbol[:id, :eidos, :events, :height, :lastevent, :renderer, :spectype, :width]
        wild_props = Symbol[]
        return Component("dasheidos", "DashEidos", "dash_eidos", available_props, wild_props; kwargs...)
end

