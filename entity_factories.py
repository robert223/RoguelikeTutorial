from components.ai import HostileEnemy
from components.cards import Cards
from components import consumable, equippable
from components.equipment import Equipment
from components.deck import Deck
from components.fighter import Fighter
from components.inventory import Inventory
from components.level import Level
from entity import Actor, Item

player = Actor(
    char="@",
    color=(255, 255, 255),
    name="Player",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=30, base_defense=1, base_power=2),
    inventory=Inventory(capacity=26),
    level=Level(level_up_base=200),
    deck=Deck(card_list=[Cards("Player", 30, 5)])
)

orc = Actor(
    char="o",
    color=(63, 127, 63),
    name="Orc",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=10, base_defense=0, base_power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=35),
    deck=Deck(card_list=[Cards("Orc", 10, 3)])
)

troll = Actor(
    char="T",
    color=(0, 127, 0),
    name="Troll",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=16, base_defense=1, base_power=4),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=100),
    deck=Deck(card_list=[Cards("Troll", 16, 4)])
)

patrick_bateman = Actor(
    char="P",
    color=(255, 0, 0),
    name="Patrick Bateman (The America Psycho)",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=30, base_defense=2, base_power=6),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=500),
    deck=Deck(card_list=[Cards("Troll", 16, 4)])
)

azathoth = Actor(
    char="A",
    color=(255, 0, 200),
    name="Azathoth (from the hit game hp lovecraft)",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=6969, base_defense=50000, base_power=5000),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=50000),
    deck=Deck(card_list=[Cards("Troll", 16, 4)])
)

confusion_scroll = Item(
    char="~",
    color=(207, 63, 255),
    name="Confusion Scroll",
    consumable=consumable.ConfusionConsumable(number_of_turns=10),
)
fireball_scroll = Item(
    char="~",
    color=(255, 0, 0),
    name="Fireball Scroll",
    consumable=consumable.FireballDamageConsumable(damage=12, radius=3)
)

health_potion = Item(
    char="!",
    color=(127, 0, 255),
    name="Health Potion",
    consumable=consumable.HealingConsumable(amount=4)
)

lightning_scroll = Item(
    char="~",
    color=(255, 255, 0),
    name="Lightning Scroll",
    consumable=consumable.LightningDamageConsumable(damage=20, maximum_range=5),
)

dagger = Item(
    char="/", color=(0, 191, 255), name="Dagger", equippable=equippable.Dagger()
)

sword = Item(char="/", color=(0, 191, 255), name="Sword", equippable=equippable.Sword())

leather_armor = Item(
    char="[",
    color=(139, 69, 19),
    name="Leather Armor",
    equippable=equippable.LeatherArmor(),
)

chain_mail = Item(
    char="[", color=(139, 69, 19), name="Chain Mail", equippable=equippable.ChainMail()
)
