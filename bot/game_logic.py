from __future__ import annotations

import random
from typing import Dict, List, Optional, Set


DEFAULT_ROLES = [
    "engineer",
    "doctor",
    "scientist",
    "teacher",
    "chef",
]


class BunkerGame:
    """Simple game state container for the Bunker game."""

    def __init__(self, roles: Optional[List[str]] = None) -> None:
        self.players: Set[str] = set()
        self.started: bool = False
        self.roles: Dict[str, str] = {}
        self._available_roles = list(roles or DEFAULT_ROLES)

    def add_player(self, name: str) -> bool:
        """Add a player to the lobby.

        Returns True if the player was added, False if the player already exists.
        """
        if self.started:
            raise RuntimeError("Cannot join a game in progress")
        if name in self.players:
            return False
        self.players.add(name)
        return True

    def remove_player(self, name: str) -> bool:
        """Remove a player from the lobby."""
        if self.started:
            raise RuntimeError("Cannot leave a game in progress")
        if name not in self.players:
            return False
        self.players.remove(name)
        return True

    def start_game(self) -> None:
        """Start the game and assign roles."""
        if self.started:
            raise RuntimeError("Game already started")
        if not self.players:
            raise RuntimeError("No players to start the game")
        self.started = True
        roles = self._available_roles.copy()
        random.shuffle(roles)
        for player in self.players:
            role = roles.pop() if roles else random.choice(DEFAULT_ROLES)
            self.roles[player] = role

    def get_role(self, player: str) -> str:
        """Return player's assigned role."""
        if not self.started:
            raise RuntimeError("Game not started")
        return self.roles[player]

