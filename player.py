class Player:
    def __init__(self, name, position, nationality):
        self.name = name
        self.position = position
        self.nationality = nationality
        self.goals_scored = 0
        self.assists = 0
        self.yellow_cards = 0
        self.red_cards = 0

    def score_goal(self, num_goals=1):
        self.goals_scored += num_goals

    def provide_assist(self, num_assists=1):
        self.assists += num_assists

    def receive_yellow_card(self, num_yellow_cards=1):
        self.yellow_cards += num_yellow_cards

    def receive_red_card(self, num_red_cards=1):
        self.red_cards += num_red_cards

    def get_stats(self):
        return {
            "Goals Scored": self.goals_scored,
            "Assists": self.assists,
            "Yellow Cards": self.yellow_cards,
            "Red Cards": self.red_cards
        }
