class Team:
    def __init__(self, name, home_stadium):
        self.name = name
        self.home_stadium = home_stadium
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def remove_player(self, player):
        if player in self.players:
            self.players.remove(player)

    def get_team_stats(self):
        total_goals = sum(player.goals_scored for player in self.players)
        total_assists = sum(player.assists for player in self.players)
        total_yellow_cards = sum(player.yellow_cards for player in self.players)
        total_red_cards = sum(player.red_cards for player in self.players)

        return {
            "Team Name": self.name,
            "Home Stadium": self.home_stadium,
            "Total Goals": total_goals,
            "Total Assists": total_assists,
            "Total Yellow Cards": total_yellow_cards,
            "Total Red Cards": total_red_cards
        }
