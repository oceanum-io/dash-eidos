# AUTO GENERATED FILE - DO NOT EDIT

#' @export
dashEidos <- function(id=NULL, eidos=NULL, events=NULL, height=NULL, lastevent=NULL, renderer=NULL, spectype=NULL, width=NULL) {
    
    props <- list(id=id, eidos=eidos, events=events, height=height, lastevent=lastevent, renderer=renderer, spectype=spectype, width=width)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'DashEidos',
        namespace = 'dash_eidos',
        propNames = c('id', 'eidos', 'events', 'height', 'lastevent', 'renderer', 'spectype', 'width'),
        package = 'dashEidos'
        )

    structure(component, class = c('dash_component', 'list'))
}
