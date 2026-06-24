def classify_exit(
    surface
):

    if surface == "TOP":
        return "TOP_EXIT"

    if surface == "BOTTOM":
        return "BOTTOM_EXIT"

    return "EDGE_EXIT"