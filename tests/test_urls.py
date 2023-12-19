import unittest
from ..urls import GameUrls, ManagerUrls, LeagueUrls


class GameUrlsTests(unittest.TestCase):
    def test_overview_returns_expected_url(self):
        self.assertEqual("https://fantasy.premierleague.com/api/bootstrap-static/", GameUrls().overview())

    def test_fixtures_returns_expected_url(self):
        self.assertEqual("https://fantasy.premierleague.com/api/fixtures/", GameUrls().fixtures())

    def test_player_stats_returns_expected_url(self):
        expected_url = "https://fantasy.premierleague.com/api/element-summary/123456/"
        self.assertEqual(expected_url, GameUrls().player_stats("123456"))
        self.assertEqual(expected_url, GameUrls().player_stats(123456))

    def test_gameweek_stats_returns_expected_url(self):
        expected_url = "https://fantasy.premierleague.com/api/event/123456/live/"
        self.assertEqual(expected_url, GameUrls().gameweek_stats("123456"))
        self.assertEqual(expected_url, GameUrls().gameweek_stats(123456))


class ManagerUrlsTests(unittest.TestCase):
    def test_overview_returns_expected_url(self):
        expected_url = "https://fantasy.premierleague.com/api/entry/123456/"
        self.assertEqual(expected_url, ManagerUrls().overview("123456"))
        self.assertEqual(expected_url, ManagerUrls().overview(123456))

    def test_transfer_history_returns_expected_url(self):
        expected_url = "https://fantasy.premierleague.com/api/entry/123456/transfers/"
        self.assertEqual(expected_url, ManagerUrls().transfer_history("123456"))
        self.assertEqual(expected_url, ManagerUrls().transfer_history(123456))

    def test_starting_lineup_returns_expected_url(self):
        expected_url = "https://fantasy.premierleague.com/api/entry/123/event/456/picks/"
        self.assertEqual(expected_url, ManagerUrls().starting_lineup("123", "456"))
        self.assertEqual(expected_url, ManagerUrls().starting_lineup("123", 456))
        self.assertEqual(expected_url, ManagerUrls().starting_lineup(123, "456"))
        self.assertEqual(expected_url, ManagerUrls().starting_lineup(123, 456))

    def test_performance_history_returns_expected_url(self):
        expected_url = "https://fantasy.premierleague.com/api/entry/123456/history/"
        self.assertEqual(expected_url, ManagerUrls().performance_history("123456"))
        self.assertEqual(expected_url, ManagerUrls().performance_history(123456))


class LeagueUrlsTests(unittest.TestCase):
    def test_overview_returns_expected_url(self):
        expected_url = "https://fantasy.premierleague.com/api/leagues-classic/123456/standings/"
        self.assertEqual(expected_url, LeagueUrls().overview("123456"))
        self.assertEqual(expected_url, LeagueUrls().overview(123456))


if __name__ == '__main__':
    unittest.main()
