from collections import defaultdict
import heapq
class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.follows = defaultdict(list)
        self.recency = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.recency, tweetId])
        self.recency -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        followees = self.follows[userId].copy()
        followees.append(userId)

        all_tweets = []
        for f in followees:
            if self.tweets[f]:
                for tweet in self.tweets[f]:
                    all_tweets.append(tweet)

        heapq.heapify(all_tweets)

        i = 0
        res = []
        while i < 10 and all_tweets:
            _, tweetId = heapq.heappop(all_tweets)
            res.append(tweetId)
            i += 1
        
        seen = set()

        new_res = []
        for r in res:
            if r not in seen:
                new_res.append(r)
                seen.add(r)

        return new_res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        curr_follows = self.follows[followerId].copy()
        self.follows[followerId] = []
        for f in curr_follows:
            if followeeId != f:
                self.follows[followerId].append(followeeId)
