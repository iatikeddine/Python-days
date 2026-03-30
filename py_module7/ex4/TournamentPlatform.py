from typing import Dict, List
from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    def __init__(self) -> None:
        self.registered_cards = {}
        self.matches_played = 0

    def register_card(self, card: TournamentCard) -> str:
        if not isinstance(card, TournamentCard):
            raise ValueError("error: not a valid tournament card")
        self.registered_cards[card.id] = card
        return "card registered successfully"

    def create_match(self, card1_id: str, card2_id: str) -> Dict:
        if card1_id not in self.registered_cards:
            raise ValueError("error: card1 is not registered or invalid")
        if card2_id not in self.registered_cards:
            raise ValueError("error: card2 is not registered or invalid")

        card_1 = self.registered_cards.get(card1_id)
        card_2 = self.registered_cards.get(card2_id)
        card_1.defend(card_2.attack_dmg)
        card_2.defend(card_1.attack_dmg)
        if card_1.health > card_2.health:
            card_1.update_wins(1)
            card_2.update_losses(1)
            card_1.calculate_rating()
            card_2.calculate_rating()
            winner = card_1
            loser = card_2
        elif card_2.health > card_1.health:
            card_2.update_wins(1)
            card_1.update_losses(1)
            card_2.calculate_rating()
            card_1.calculate_rating()
            winner = card_2
            loser = card_1
        else:
            card_1.reset_health()
            card_2.reset_health()
            self.matches_played += 1
            return {
                "result": "draw"
            }
        self.matches_played += 1
        card_1.reset_health()
        card_2.reset_health()
        return {
            "winner": winner.id,
            "loser": loser.id,
            "winner_rating": winner.rating,
            "loser_rating": loser.rating
        }

    def get_leaderboard(self) -> List:
        leader_board = []
        for card in self.registered_cards.values():
            leader_board.append(card)

        def return_rating(card: TournamentCard) -> int:
            return card.rating

        leader_board = sorted(leader_board, key=return_rating, reverse=True)
        return leader_board

    def generate_tournament_report(self) -> Dict:
        cards = [card for card in self.registered_cards.values()]
        average = 0
        if len(cards) > 0:
            average = sum(card.rating for card in cards) / len(cards)
        return {
            "total_cards": len(self.registered_cards),
            "matches_played": self.matches_played,
            "avg_rating": average,
            "platform_status": "active"
        }
