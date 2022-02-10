from __future__ import annotations

from typing import Iterable, Optional, TYPE_CHECKING

import numpy as np  # type: ignore
from tcod.console import Console

import tile_types

if TYPE_CHECKING:
    from entity import Entity


class GameMap:
    """
    The initializer takes width and height integers and assigns them, in one line.

    The self.tiles line might look a little strange if you’re not used to Numpy. Basically, we create a 2D array, filled with the same values, which in this case, is the tile_types.floor that we created earlier. This will fill self.tiles with floor tiles.

    self.tiles[30:33, 22] = tile_types.wall creates a small, three tile wide wall at the specified location. We won’t normally hard-code walls like this, the wall is just for demonstration purposes. We’ll remove it in the next part.
    """

    def __init__(self, width: int, height: int, entities: Iterable[Entity] = ()):
        self.width, self.height = width, height
        self.entities = set(entities)
        self.tiles = np.full((width, height), fill_value=tile_types.wall, order="F")

        # array for tiles the player can currently see
        self.visible = np.full((width, height), fill_value=False, order="F")

        # array for tiles the player has in memory
        self.explored = np.full((width, height), fill_value=False, order="F")

    def get_blocking_entity_at_location(self, location_x: int, location_y: int) -> Optional[Entity]:
        for entity in self.entities:
            if entity.blocks_movement and entity.x == location_x and entity.y == location_y:
                return entity

    def in_bounds(self, x: int, y: int) -> bool:
        """Return True if x and y are inside of the bounds of this map."""
        return 0 <= x < self.width and 0 <= y < self.height

    """
    Using the Console class’s tiles_rgb method, we can quickly render the entire map. This method proves much faster than using the console.print method that we use for the individual entities.
    """

    def render(self, console: Console) -> None:
        """
        Renders the map.

        If a tile is in the "visible" array, then draw it with the "light" colors.
        If it isn't, but it's in the "explored" array, then draw it with the "dark" colors.
        Otherwise, the default is "SHROUD".
        """

        console.tiles_rgb[0:self.width, 0:self.height] = np.select(
            condlist=[self.visible, self.explored],
            choicelist=[self.tiles["light"], self.tiles["dark"]],
            default=tile_types.SHROUD
        )

        for entity in self.entities:
            # Only print entities that are in the FOV
            if self.visible[entity.x, entity.y]:
                console.print(entity.x, entity.y, entity.char, fg=entity.color)
