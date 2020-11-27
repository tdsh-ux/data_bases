# AUTO GENERATED FILE - DO NOT EDIT

export nx

"""
    nx(;kwargs...)

A NX component.
ExampleComponent is an example component.
It takes a property, `label`, and
displays it.
It renders an input with the property `value`
which is editable by the user.
Keyword arguments:
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
- `data` (Dict; required): Vega-lite specification of the plot.
- `tapNode` (Dict; optional): Node clicked.
"""
function nx(; kwargs...)
        available_props = Symbol[:id, :data, :tapNode]
        wild_props = Symbol[]
        return Component("nx", "NX", "nx_graph", available_props, wild_props; kwargs...)
end

