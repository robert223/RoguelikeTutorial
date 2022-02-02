from typing import Optional

import tcod.event

from actions import Action, EscapeAction, MovementAction


class EventHandler(tcod.event.EventDispatch[Action]):
    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
        raise SystemExit()

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
        action: Optional[Action] = None

        key = event.sym

        """
        arrow keys
        """
        # up
        if key == tcod.event.K_UP:
            action = MovementAction(dx=0, dy=-1)
            # down
        elif key == tcod.event.K_DOWN:
            action = MovementAction(dx=0, dy=1)
            # left
        elif key == tcod.event.K_LEFT:
            action = MovementAction(dx=-1, dy=0)
            # right
        elif key == tcod.event.K_RIGHT:
            action = MovementAction(dx=1, dy=0)

        """
        vikeys
        """
        # up
        if key == tcod.event.K_k:
            action = MovementAction(dx=0, dy=-1)

            # down
        elif key == tcod.event.K_j:
            action = MovementAction(dx=0, dy=1)

            # left
        elif key == tcod.event.K_h:
            action = MovementAction(dx=-1, dy=0)

            # right
        elif key == tcod.event.K_l:
            action = MovementAction(dx=1, dy=0)

            # left-up
        elif key == tcod.event.K_y:
            action = MovementAction(dx=-1, dy=-1)

            # right-up
        elif key == tcod.event.K_u:
            action = MovementAction(dx=1, dy=-1)

            # left-down
        elif key == tcod.event.K_b:
            action = MovementAction(dx=-1, dy=1)

            # right-down
        elif key == tcod.event.K_n:
            action = MovementAction(dx=1, dy=1)

        elif key == tcod.event.K_ESCAPE:
            action = EscapeAction()

        # No valid key was pressed (moron)
        return action
