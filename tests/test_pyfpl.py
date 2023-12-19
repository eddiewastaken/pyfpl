import unittest
import requests.exceptions

from pyfpl import PyFPL


class PyFPLTests(unittest.TestCase):
    def test_make_get_request_throws_if_return_code_is_not_200(self):
        with self.assertRaises(requests.exceptions.HTTPError):
            PyFPL._make_get_request("https://google.com/someunreachablelocation")
            PyFPL._make_get_request("notaurl")


class PyFPLGameTests(unittest.TestCase):
    def test_get_overview_returns_expected_json(self):
        expected_keys = ["events", "game_settings", "phases", "teams", "total_players", "element_stats",
                         "element_types"]
        self.assertTrue(all(key in PyFPL.Game.get_overview().keys() for key in expected_keys))

    def test_get_fixtures_returns_expected_json(self):
        self.assertTrue(380 == len(PyFPL.Game.get_fixtures()))

    def test_player_stats_returns_expected_json(self):
        expected_keys = ["fixtures", "history", "history_past"]
        self.assertTrue(all(key in PyFPL.Game.get_player_stats(1).keys() for key in expected_keys))
        self.assertTrue(all(key in PyFPL.Game.get_player_stats("1").keys() for key in expected_keys))

    def test_gameweek_stats_returns_expected_json(self):
        self.assertGreater(500, len(PyFPL.Game.get_gameweek_stats(1)))
        self.assertGreater(500, len(PyFPL.Game.get_gameweek_stats("1")))


class PyFPLManagerTests(unittest.TestCase):
    def test_get_overview_returns_expected_json(self):
        expected_keys = ["id", "joined_time", "started_event", "favourite_team", "player_first_name", "player_last_name",
                         "player_region_id", "player_region_name", "player_region_iso_code_short",
                         "player_region_iso_code_long", "summary_overall_points", "summary_overall_rank",
                         "summary_event_points", "summary_event_rank", "current_event", "leagues", "name",
                         "name_change_blocked", "kit", "last_deadline_bank", "last_deadline_value",
                         "last_deadline_total_transfers"]
        self.assertTrue(all(key in PyFPL.Manager.get_overview(1).keys() for key in expected_keys))
        self.assertTrue(all(key in PyFPL.Manager.get_overview("1").keys() for key in expected_keys))

    def test_get_transfer_history_returns_expected_json(self):
        expected_keys = ["element_in", "element_in_cost", "element_out", "element_out_cost", "entry", "event", "time"]
        self.assertTrue(all(key in PyFPL.Manager.get_transfer_history(1)[0].keys() for key in expected_keys))
        self.assertTrue(all(key in PyFPL.Manager.get_transfer_history("1")[0].keys() for key in expected_keys))


class PyFPLLeagueTests(unittest.TestCase):
    def test_get_overview_returns_expected_json(self):
        expected_keys = ["new_entries", "league", "standings"]
        self.assertTrue(all(key in PyFPL.League.get_overview(1).keys() for key in expected_keys))


if __name__ == '__main__':
    unittest.main()
