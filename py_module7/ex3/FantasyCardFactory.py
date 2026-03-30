from typing import Dict
from ex3.CardFactory import CardFactory
from ex0.Card import Rarity, Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
import random


class FantasyCardFactory(CardFactory):
    def __init__(self) -> None:
        self.creature_catalog = {
            "dragon": {
                "cost": 5, "rarity": Rarity.LEGENDARY.value,
                "attack": 7, "health": 5
            },
            "goblin": {
                "cost": 2, "rarity": Rarity.COMMON.value,
                "attack": 3, "health": 2
            }
        }
        self.spell_catalog = {
            "fireball": {
                "cost": 3, "rarity": Rarity.RARE.value,
                "effect_type": "damage"
            }
        }
        self.artifact_catalog = {
            "mana_ring": {
                "cost": 2, "rarity": Rarity.RARE.value,
                "durability": 3, "effect": "Permanent: +1 mana per turn"
            }
        }

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, str):
            if name_or_power in self.creature_catalog:
                new_card = CreatureCard(
                    name_or_power,
                    self.creature_catalog[name_or_power]["cost"],
                    self.creature_catalog[name_or_power]["rarity"],
                    self.creature_catalog[name_or_power]["attack"],
                    self.creature_catalog[name_or_power]["health"]
                    )
                return new_card
            else:
                raise ValueError("error: the requested card is not available")

        elif isinstance(name_or_power, int):
            for name, card in self.creature_catalog.items():
                if card["cost"] == name_or_power:
                    new_card = CreatureCard(
                        name, card["cost"], card["rarity"],
                        card["attack"], card["health"]
                    )
                    return new_card
            raise ValueError("error: the requested card is not available")

        elif name_or_power is None:
            stats = self.creature_catalog["dragon"]
            return CreatureCard("dragon", stats["cost"], stats["rarity"],
                                stats["attack"], stats["health"])

        raise ValueError("error: invalid card request")

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, str):
            if name_or_power in self.spell_catalog:
                new_card = SpellCard(
                    name_or_power,
                    self.spell_catalog[name_or_power]["cost"],
                    self.spell_catalog[name_or_power]["rarity"],
                    self.spell_catalog[name_or_power]["effect_type"],
                    )
                return new_card
            else:
                raise ValueError("error: the requested card is not available")

        elif isinstance(name_or_power, int):
            for name, card in self.spell_catalog.items():
                if card["cost"] == name_or_power:
                    new_card = SpellCard(
                        name, card["cost"], card["rarity"],
                        card["effect_type"]
                    )
                    return new_card
            raise ValueError("error: the requested card is not available")

        elif name_or_power is None:
            stats = self.spell_catalog["fireball"]
            return SpellCard("fireball", stats["cost"], stats["rarity"],
                             stats["effect_type"])

        raise ValueError("error: invalid card request")

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, str):
            if name_or_power in self.artifact_catalog:
                new_card = ArtifactCard(
                    name_or_power,
                    self.artifact_catalog[name_or_power]["cost"],
                    self.artifact_catalog[name_or_power]["rarity"],
                    self.artifact_catalog[name_or_power]["durability"],
                    self.artifact_catalog[name_or_power]["effect"]
                    )
                return new_card
            else:
                raise ValueError("error: the requested card is not available")

        elif isinstance(name_or_power, int):
            for name, card in self.artifact_catalog.items():
                if card["cost"] == name_or_power:
                    new_card = ArtifactCard(
                        name, card["cost"], card["rarity"],
                        card["durability"], card["effect"]
                    )
                    return new_card
            raise ValueError("error: the requested card is not available")

        elif name_or_power is None:
            stats = self.artifact_catalog["mana_ring"]
            return ArtifactCard("mana_ring", stats["cost"], stats["rarity"],
                                stats["durability"], stats["effect"])

        raise ValueError("error: invalid card request")

    def create_themed_deck(self, size: int) -> Dict:
        if not isinstance(size, int) or size <= 0:
            raise ValueError("error: invalid deck size")
        deck_cards = []
        catalogs = ["creature", "spell", "artifact"]

        for x in range(size):
            choice = random.choice(catalogs)
            if choice == "spell":
                card = self.create_spell("fireball")
                deck_cards.append(card)
            elif choice == "creature":
                creatures = ["dragon", "goblin"]
                card = self.create_creature(random.choice(creatures))
                deck_cards.append(card)
            elif choice == "artifact":
                card = self.create_artifact("mana_ring")
                deck_cards.append(card)
        return {
            "theme": "fantasy",
            "deck_size": size,
            "cards": deck_cards
        }

    def get_supported_types(self) -> Dict:
        return {
            "creatures": list(self.creature_catalog),
            "spells": list(self.spell_catalog),
            "artifacts": list(self.artifact_catalog)
        }

    def register_new_card(self, category: str, name: str, stats: Dict) -> None:
        if (
            not isinstance(category, str)
            or not isinstance(name, str)
            or not isinstance(stats, dict)
        ):
            raise ValueError("error: invalid registration data")

        category = category.lower()

        if category == "creature":
            required_keys = {"cost", "rarity", "attack", "health"}
            if not required_keys.issubset(stats.keys()):
                raise ValueError("error: missing required creature stats")
            self.creature_catalog[name] = stats

        elif category == "spell":
            required_keys = {"cost", "rarity", "effect_type"}
            if not required_keys.issubset(stats.keys()):
                raise ValueError("error: missing required spell stats")
            self.spell_catalog[name] = stats

        elif category == "artifact":
            required_keys = {"cost", "rarity", "durability", "effect"}
            if not required_keys.issubset(stats.keys()):
                raise ValueError("error: missing required artifact stats")
            self.artifact_catalog[name] = stats

        else:
            raise ValueError("error: unsupported card category")
