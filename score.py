class Score:
    def __init__(self, word=None, special_tile=None) -> None:
        self.word = word
        self.special_tile = special_tile

    def cal_score(self):
        total_score = 0
        for tile in self.word:
            total_score += int(tile[1])
        if self.special_tile is not None:
            self.special_tile
            
