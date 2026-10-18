class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adjList = defaultdict(list)

        for depart, arrival in sorted(tickets, reverse=True):
            adjList[depart].append(arrival)

        flight_path = []

        def dfs(node):
            while adjList[node]:
                dfs(adjList[node].pop())
            flight_path.append(node)

        dfs("JFK")
        return flight_path[::-1]

        