from typing import Tuple
import numpy as np  # type: ignore

"""
dtype creates a data type which Numpy can use, which behaves similarly to a struct in a language like C. Our data type is made up of three parts:

ch: The character, represented in integer format. We’ll translate it from the integer into Unicode.
fg: The foreground color. “3B” means 3 unsigned bytes, which can be used for RGB color codes.
bg: The background color. Similar to fg.
"""
# Tile graphics structured type compatible with Console.tiles_rgb.
graphic_dt = np.dtype(
    [
        ("ch", np.int32),  # Unicode codepoint.
        ("fg", "3B"),  # 3 unsigned bytes, for RGB colors.
        ("bg", "3B"),
    ]
)

"""
This is yet another dtype, which we’ll use in the actual tile itself. It’s also made up of three parts:

walkable: A boolean that describes if the player can walk across this tile.
transparent: A boolean that describes if this tile does or does not block the field of view. Not used in this chapter, but will be in chapter 4.
dark: This uses our previously defined dtype, which holds the character to print, the foreground color, and the background color. Why is it called dark? Because later on, we’ll want to differentiate between tiles that are and aren’t in the field of view. dark will represent tiles that are not in the current field of view. Again, we’ll cover that in part 4.
"""
# Tile struct used for statically defined tile data.
tile_dt = np.dtype(
    [
        ("walkable", np.bool),  # True if this tile can be walked over.
        ("transparent", np.bool),  # True if this tile doesn't block FOV.
        ("dark", graphic_dt),  # Graphics for when this tile is not in FOV.
        ("light", graphic_dt),  # Graphics for when the tile is in FOV
    ]
)

"""
This is a helper function, that we’ll use in the next section to define our tile types. 
It takes the parameters walkable, transparent, and dark, which should look familiar, since they’re the same data points we used in tile_dt. It creates a Numpy array of just the one tile_dt element, and returns it.
"""


def new_tile(
        *,  # Enforce the use of keywords, so that parameter order doesn't matter.
        walkable: int,
        transparent: int,
        dark: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
        light: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
) -> np.ndarray:
    """Helper function for defining individual tile types """
    return np.array((walkable, transparent, dark, light), dtype=tile_dt)


# SHROUD represents unexplored, unseen tiles
SHROUD = np.array((ord(" "), (255, 255, 255), (0, 0, 0)), dtype=graphic_dt)

"""
floor is both walkable and transparent. Its dark attribute consists of the space character (feel free to change this to something else, a lot of roguelikes use “#") and defines its foreground color as white (won’t matter since it’s an empty space) and a background color.

wall is neither walkable nor transparent, and its dark attribute differs from floor slightly in its background color.
"""
floor = new_tile(
    walkable=True,
    transparent=True,
    dark=(ord(" "), (255, 255, 255), (50, 50, 150)),
    light=(ord(" "), (255, 255, 255), (200, 180, 50)),
)
wall = new_tile(
    walkable=False,
    transparent=False,
    dark=(ord(" "), (255, 255, 255), (0, 0, 100)),
    light=(ord(" "), (255, 255, 255), (130, 110, 50)),
)
