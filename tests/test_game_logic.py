from bot.game_logic import BunkerGame


def test_add_and_remove_players():
    game = BunkerGame()
    assert game.add_player("Alice")
    assert not game.add_player("Alice"), "duplicate add should fail"
    assert game.remove_player("Alice")
    assert not game.remove_player("Alice"), "double remove should fail"


def test_start_game_assigns_roles():
    game = BunkerGame()
    game.add_player("Alice")
    game.add_player("Bob")
    game.start_game()
    assert game.started
    assert game.get_role("Alice") in game.roles.values()
    assert game.get_role("Bob") in game.roles.values()

