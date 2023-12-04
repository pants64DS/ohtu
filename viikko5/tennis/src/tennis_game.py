
class TennisGame:
    def __init__(self, player1_name, player2_name):
        if player1_name == player2_name:
            raise ValueError("Players must have different names")

        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.m_score1 += 1
        elif player_name == self.player2_name:
            self.m_score2 += 1
        else:
            raise ValueError(f"Player \'{player_name}\' is not in the game")

    @staticmethod
    def __score_to_string(score):
        return ("Love", "Fifteen", "Thirty", "Forty")[score]

    def __get_even_score(self):
        if 0 <= self.m_score1 <= 2:
            return TennisGame.__score_to_string(self.m_score1) + "-All"
        else:
            return "Deuce"

    def __get_advantage_score(self):
        leading_player = int(self.m_score1 < self. m_score2) + 1;

        if abs(self.m_score1 - self. m_score2) == 1:
            return f"Advantage player{leading_player}"
        else:
            return f"Win for player{leading_player}"

    def get_score(self):
        if self.m_score1 == self.m_score2:
            return self.__get_even_score()

        if self.m_score1 >= 4 or self.m_score2 >= 4:
            return self.__get_advantage_score()

        return TennisGame.__score_to_string(self.m_score1) + "-" \
             + TennisGame.__score_to_string(self.m_score2)
