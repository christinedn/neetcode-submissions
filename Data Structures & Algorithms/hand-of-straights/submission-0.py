class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize != 0:
            return False
        hand_dict = Counter(hand)
        while hand_dict:
            min_value = min(hand_dict)
            for i in range(groupSize):
                card = min_value + i
                if card not in hand_dict:
                    return  False
                hand_dict[card] -= 1

                if hand_dict[card] == 0:
                    del hand_dict[card]
        return True



