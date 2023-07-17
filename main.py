from player import Player
from team import Team
from matches import Match

if __name__ == "__main__": #read more why this is important
    # Create player instances
    player1 = Player("Lionel Messi", "Forward", "Argentina")
    player2 = Player("Cristiano Ronaldo", "Forward", "Portugal")
    player3 = Player("Neymar Jr.", "Forward", "Brazil")
    player4 = Player("Sergio Ramos", "Defender", "Spain")

    # Create team instances
    team1 = Team("Barcelona", "Camp Nou")
    team2 = Team("Real Madrid", "Santiago Bernabeu")

    # Add players to the teams
    team1.add_player(player1)
    team1.add_player(player3)

    team2.add_player(player2)
    team2.add_player(player4)

    # Create a match between the two teams
    match_date = "2023-07-17"
    match = Match(team1, team2, match_date)

    # Simulate the match
    match.simulate_match()

    # Display the match result and team statistics
    print(match.get_match_result())
    print(match.comment_on_match())
    print("----")
    print("Team 1 Stats:")
    print(team1.get_team_stats())
    print("----")
    print("Team 2 Stats:")
    print(team2.get_team_stats())
    
    print(player1.name, player1.get_stats())
    print(player2.name, player2.get_stats())
    print(player3.name, player3.get_stats())
    print(player4.name, player4.get_stats())
