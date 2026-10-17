class Twitter:

    def __init__(self):
        self.timestamp = 0
        self.posts = defaultdict(list) # {userId : List[(timestamp, tweetId)]}
        self.followers = defaultdict(set) # {followerId : Set{followeeId}}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((self.timestamp, tweetId))
        self.timestamp += 1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        res, minHeap = [], []

        for followeeId in self.followers[userId] | {userId}:
            if followeeId in self.posts:
                i = len(self.posts[followeeId]) - 1
                timestamp, tweetId = self.posts[followeeId][i]
                minHeap.append([-timestamp, tweetId, followeeId, i-1])

        heapq.heapify(minHeap)
        while minHeap and len(res) < 10:
            timestamp, tweetId, followeeId, i = heapq.heappop(minHeap)
            res.append(tweetId)
            if i >= 0:
                timestamp, tweetId = self.posts[followeeId][i]
                heapq.heappush(minHeap, [-timestamp, tweetId, followeeId, i-1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId)
        
