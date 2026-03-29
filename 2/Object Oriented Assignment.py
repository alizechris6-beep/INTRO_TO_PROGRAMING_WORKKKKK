# Define the Player class
class Player:
    def __init__(self, playerName, playerPosition):
        self.playerName = playerName
        self.playerPosition = playerPosition

    def __str__(self):
        return f"{self.playerName} - {self.playerPosition}"

# Define the NFLTeam class
class NFLTeam:
    def __init__(self, teamName, players):
        self.teamName = teamName
        self.players = players

    def display_team(self):
        print(f"Team: {self.teamName}")
        print("Players:")
        for player in self.players:
            print(f"  {player}")

# Create Player objects
player1 = Player("Joe Montana", "QB")
player2 = Player("Barry Sanders", "RB")
player3 = Player("Jerry Rice", "WR")
player4 = Player("Graham Gano", "K")

# Add players to a list
playerList = [player1, player2, player3, player4]

# Create NFLTeam object
team = NFLTeam("Smashmouth Football", playerList)

# Display team and players
team.display_team()