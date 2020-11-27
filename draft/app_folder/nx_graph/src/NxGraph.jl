
module NxGraph
using Dash

const resources_path = realpath(joinpath( @__DIR__, "..", "deps"))
const version = "0.0.1"

include("nx.jl")

function __init__()
    DashBase.register_package(
        DashBase.ResourcePkg(
            "nx_graph",
            resources_path,
            version = version,
            [
                DashBase.Resource(
    relative_package_path = "nx_graph.min.js",
    external_url = "https://unpkg.com/nx_graph@0.0.1/nx_graph/nx_graph.min.js",
    dynamic = nothing,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "nx_graph.min.js.map",
    external_url = "https://unpkg.com/nx_graph@0.0.1/nx_graph/nx_graph.min.js.map",
    dynamic = true,
    async = nothing,
    type = :js
)
            ]
        )

    )
end
end
