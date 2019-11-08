import random
from util import Queue


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(numUsers):
            self.addUser(F'User {i+1}')

        # Create friendships
        # totalFriendships = avgFriendships * numUsers
        # Generate a list of all possible friendships
        possible_friendships = []
        # avoid duplicates by ensuring the first ID is smaller than the second
        for userID in self.users:
            for friendID in range(userID + 1, self.lastID + 1):
                possible_friendships.append((userID, friendID))
        # Shuffle the list
        random.shuffle(possible_friendships)

        total_friendships = avgFriendships * numUsers // 2
        # Slice off excess friendships, implement the rest
        for i in range(total_friendships):
            friendship = possible_friendships[i]
            self.addFriendship(friendship[0], friendship[1])

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME

        # Implement a queue and add an array of the first userID
        q = Queue()
        q.enqueue([userID])
        # While queue has items
        while q.size() > 0:
            # dequeue item
            route = q.dequeue()
            node = route[-1]
            # Add it to visted with last item as key and route array as value
            visited[node] = route
            # Find and Loop over neighbors
            for neighbor in self.friendships[node]:
                # if neighbor has not been visited
                if neighbor not in visited.keys():
                    # Make a copy of route array
                    new_route = route.copy()
                    # Append neighbor to route
                    new_route.append(neighbor)
                    # Add route to queue
                    q.enqueue(new_route)
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(1000, 5)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
