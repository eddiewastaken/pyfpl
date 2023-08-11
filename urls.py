base_url = "https://fantasy.premierleague.com/api/"


class GameUrls:
    @staticmethod
    def overview():
        return base_url + "bootstrap-static/"

    @staticmethod
    def fixtures():
        return base_url + "fixtures/"

    @staticmethod
    def player_stats(player_id):
        return base_url + "element-summary/{player_id}/".format(player_id=player_id)

    @staticmethod
    def gameweek_stats(gameweek):
        return base_url + "event/{gameweek}/live/".format(gameweek=gameweek)


class ManagerUrls:
    @staticmethod
    def overview(team_id):
        return base_url + "entry/{team_id}/".format(team_id=team_id)

    @staticmethod
    def transfer_history(team_id):
        return base_url + "entry/{team_id}/transfers/".format(team_id=team_id)

    @staticmethod
    def starting_lineup(team_id, gameweek):
        return base_url + "entry/{team_id}/event/{gameweek}/picks/".format(team_id=team_id, gameweek=gameweek)

    @staticmethod
    def performance_history(team_id):
        return base_url + "entry/{team_id}/history/".format(team_id=team_id)


class LeagueUrls:
    @staticmethod
    def overview(league_id):
        return base_url + "leagues-classic/{league_id}/standings/".format(league_id=league_id)
