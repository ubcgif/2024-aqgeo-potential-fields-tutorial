import numpy as np
import matplotlib.pyplot as plt


def plot_model(mesh, density, slice_loc_z=-500, bounds=None):
    from matplotlib.gridspec import GridSpec

    # Get maxabs for inverted model
    maxabs = np.max(np.abs(density))

    # Create fig and axes
    fig = plt.figure(figsize=(16, 6))
    gs = GridSpec(nrows=2, ncols=2, width_ratios=[1.4, 1])
    axes = [
        fig.add_subplot(gs[0, 0]),
        fig.add_subplot(gs[1, 0]),
        fig.add_subplot(gs[:, 1]),
    ]

    # Vertical slices
    for ax, dim in zip(axes[:2], ["x", "y"]):
        (tmp,) = mesh.plot_slice(
            density,
            ax=ax,
            normal=dim,
            clim=(-maxabs, maxabs),
            pcolor_opts=dict(cmap="RdBu_r"),
        )
        if dim == "y":
            ax.set_xlabel("y")

    # Horizontal slice
    (tmp,) = mesh.plot_slice(
        density,
        ax=axes[-1],
        slice_loc=slice_loc_z,
        normal="z",
        clim=(-maxabs, maxabs),
        pcolor_opts=dict(cmap="RdBu_r"),
    )
    axes[-1].set_ylabel("y")

    # Extra stuff
    plt.colorbar(tmp, ax=axes, label="g/cc")
    for ax in axes:
        ax.set_aspect("equal")
        ax.grid()

    # Set ax limits
    if bounds is not None:
        axes[0].set_xlim(*bounds[:2])
        axes[0].set_ylim(*bounds[4:])
        axes[1].set_xlim(*bounds[2:4])
        axes[1].set_ylim(*bounds[4:])
        axes[2].set_xlim(*bounds[:2])
        axes[2].set_ylim(*bounds[2:4])

    return axes


def plot_block(
    block_bounds, axes, facecolor="none", edgecolor="C2", linewidth=3, **kwargs
):
    """
    Plot the bounds of the synthetic block in the three slice axes.
    """
    from matplotlib.patches import Rectangle

    tmp = kwargs
    kwargs = dict(facecolor=facecolor, edgecolor=edgecolor, linewidth=linewidth)
    kwargs.update(tmp)

    # x
    ax = axes[0]
    xy = (block_bounds[0], block_bounds[4])
    width = block_bounds[1] - block_bounds[0]
    height = block_bounds[5] - block_bounds[4]
    rectangle = Rectangle(xy, width, height, **kwargs)
    ax.add_artist(rectangle)

    # y
    ax = axes[1]
    xy = (block_bounds[2], block_bounds[4])
    width = block_bounds[3] - block_bounds[2]
    height = block_bounds[5] - block_bounds[4]
    rectangle = Rectangle(xy, width, height, **kwargs)
    ax.add_artist(rectangle)

    # z
    ax = axes[2]
    xy = (block_bounds[0], block_bounds[2])
    width = block_bounds[1] - block_bounds[0]
    height = block_bounds[3] - block_bounds[2]
    rectangle = Rectangle(xy, width, height, **kwargs)
    ax.add_artist(rectangle)
