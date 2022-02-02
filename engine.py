from typing import Set, Iterable, Any

from tcod.context import Context
from tcod.console import Console

from actions import EscapeAction, MovementAction
from entity import Entity
from input_handlers import EventHandler

"""
entities is a set (of entities), which behaves kind of like a list that enforces uniqueness. That is, we can’t add an Entity to the set twice, whereas a list would allow that. In our case, having an entity in entities twice doesn’t make sense.
event_handler is the same event_handler that we used in main.py. It will handle our events.
player is the player Entity. We have a separate reference to it outside of entities for ease of access. We’ll need to access player a lot more than a random entity in entities.
"""


class Engine:
    def __init__(self, entities: Set[Entity], event_handler: EventHandler, player: Entity):
        self.entities = entities
        self.event_handler = event_handler
        self.player = player

    # iterates through events passed to it using self.event_handler
    def handle_events(self, events: Iterable[Any]) -> None:
        for event in events:
            action = self.event_handler.dispatch(event)

            if action is None:
                continue

            if isinstance(action, MovementAction):
                self.player.move(dx=action.dx, dy=action.dy)

            elif isinstance(action, EscapeAction):
                raise SystemExit()

    # iterates through self.entities and prints them to their proper locations, presents context, then clears the console
    def render(self, console: Console, context: Context) -> None:
        for entity in self.entities:
            console.print(entity.x, entity.y, entity.char, fg=entity.color)

        context.present(console)

        console.clear()
