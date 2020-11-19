# AUTO GENERATED FILE - DO NOT EDIT

nX <- function(id=NULL, data=NULL, tapNode=NULL) {
    
    props <- list(id=id, data=data, tapNode=tapNode)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'NX',
        namespace = 'nx_graph',
        propNames = c('id', 'data', 'tapNode'),
        package = 'nxGraph'
        )

    structure(component, class = c('dash_component', 'list'))
}
