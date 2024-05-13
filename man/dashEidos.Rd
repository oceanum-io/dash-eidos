% Auto-generated: do not edit by hand
\name{dashEidos}

\alias{dashEidos}

\title{DashEidos component}

\description{
DashEidos is a an EIDOS visualisation component for Dash.   It takes a EIDOS spec, converts it to a React component in a Plotly dash app,
}

\usage{
dashEidos(id=NULL, eidos=NULL, events=NULL, height=NULL,
lastevent=NULL, renderer=NULL, spectype=NULL, width=NULL)
}

\arguments{
\item{id}{Character. The ID used to identify this component in Dash callbacks.}

\item{eidos}{Named list. Eidos spec}

\item{events}{Unnamed list. List of EIDOS events to listen to. Can be any of:
['click']}

\item{height}{Numeric | character. Height of the map component container as pixels or CSS string
(optional) Default 500}

\item{lastevent}{Named list. The last event that was triggered. This is a read-only property.}

\item{renderer}{Character. The URL of the EIDOS renderer.}

\item{spectype}{A value equal to: "spec", "patch". The type of spec. Can be either 'spec' or 'patch'.}

\item{width}{Numeric | character. An array of tooltip objects that follows he pydeck tooltip specifcation.
An additonal 'layer' property can be added to the tooltip objects to restrict their action to that layer ID.}
}

\value{named list of JSON elements corresponding to React.js properties and their values}

