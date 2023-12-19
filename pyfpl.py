from urls import *

import requests


class PyFPL:
    @staticmethod
    def _make_get_request(url):
        response = requests.get(url)
        response.raise_for_status()
        return response

    class Game:
        @staticmethod
        def get_overview():
            return PyFPL._make_get_request(GameUrls.overview()).json()

        @staticmethod
        def get_fixtures():
            return PyFPL._make_get_request(GameUrls.fixtures()).json()

        @staticmethod
        def get_player_stats(player_id):
            return PyFPL._make_get_request(GameUrls.player_stats(player_id)).json()

        @staticmethod
        def get_gameweek_stats(gameweek):
            return PyFPL._make_get_request(GameUrls.gameweek_stats(gameweek)).json()

    class Manager:
        @staticmethod
        def get_overview(team_id):
            return PyFPL._make_get_request(ManagerUrls.overview(team_id)).json()

        @staticmethod
        def get_transfer_history(team_id):
            return PyFPL._make_get_request(ManagerUrls.transfer_history(team_id)).json()

        @staticmethod
        def get_starting_lineup(team_id, gameweek):
            return PyFPL._make_get_request(ManagerUrls.starting_lineup(team_id, gameweek)).json()

        @staticmethod
        def get_performance_history(team_id):
            return PyFPL._make_get_request(ManagerUrls.performance_history(team_id)).json()

    class League:
        @staticmethod
        def get_overview(league_id):
            return PyFPL._make_get_request(LeagueUrls.overview(league_id)).json()
