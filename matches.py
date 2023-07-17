import random

class Match:
    def __init__(self, home_team, away_team, match_date):
        self.home_team = home_team
        self.away_team = away_team
        self.match_date = match_date
        self.home_goals = 0
        self.away_goals = 0

    def simulate_match(self):
        # Simulate the match using random numbers
        self.home_goals = random.randint(0, 5)
        self.away_goals = random.randint(0, 5)

        # Update player statistics based on match outcome
        self.update_player_stats(self.home_team, self.home_goals)
        self.update_player_stats(self.away_team, self.away_goals)

    def update_player_stats(self, team, goals_scored):
        for player in team.players:
            assists = random.randint(0, goals_scored)  # Random assists up to goals scored
            yellow_cards = random.randint(0, 1)  # Random number of yellow cards (0 or 1)
            red_cards = 0 if yellow_cards == 0 else random.randint(0, 1)  # Random number of red cards (0 or 1)

            player.score_goal(goals_scored)
            player.provide_assist(assists)
            player.receive_yellow_card(yellow_cards)
            player.receive_red_card(red_cards)

    def get_match_result(self):
        return f"{self.home_team.name} {self.home_goals} - {self.away_goals} {self.away_team.name}"

    def comment_on_match(self):
        if self.home_goals > self.away_goals:
            return "A thrilling victory for the home team!"
        elif self.home_goals < self.away_goals:
            return "The away team steals the victory!"
        else:
            return "It's a draw. Both teams performed well!"
