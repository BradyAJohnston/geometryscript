import geometryscript as gs


@gs.tree("Repeat Grid")
def repeat_grid(geometry: gs.Geometry, width: gs.Int, height: gs.Int):
    g = gs.grid(
        size_x=width, size_y=height, vertices_x=width, vertices_y=height
    ).mesh.mesh_to_points()
    return g.instance_on_points(instance=geometry)


if __name__ == "__main__":
    repeat_grid()
