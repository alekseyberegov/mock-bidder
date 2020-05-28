from random import randint


class BidManager(object):
    def __init__(self, mean=2.5, sigma=0.5):
        self.bid_mean = mean
        self.bid_sigma = sigma

    def generate_bid(self):
        r = 1000
        return self.bid_mean * (1 + (randint(1, r) - self.bid_sigma * r) / r)
