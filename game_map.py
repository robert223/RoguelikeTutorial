import numpy as np  # type: ignore
from tcod.console import Console

import tile_types


class GameMap:
    """
    The initializer takes width and height integers and assigns them, in one line.

    The self.tiles line might look a little strange if you’re not used to Numpy. Basically, we create a 2D array, filled with the same values, which in this case, is the tile_types.floor that we created earlier. This will fill self.tiles with floor tiles.

    self.tiles[30:33, 22] = tile_types.wall creates a small, three tile wide wall at the specified location. We won’t normally hard-code walls like this, the wall is just for demonstration purposes. We’ll remove it in the next part.
    """

    def __init__(self, width: int, height: int):
        self.width, self.height = width, height
        self.tiles = np.full((width, height), fill_value=tile_types.wall, order="F")

    def in_bounds(self, x: int, y: int) -> bool:
        """Return True if x and y are inside of the bounds of this map."""
        return 0 <= x < self.width and 0 <= y < self.height

    """
    Using the Console class’s tiles_rgb method, we can quickly render the entire map. This method proves much faster than using the console.print method that we use for the individual entities.
    """

    def render(self, console: Console) -> None:
        console.tiles_rgb[0:self.width, 0:self.height] = self.tiles["dark"]
