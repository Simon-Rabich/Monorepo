# Python3 Program to print BFS traversal
# from a given source vertex. BFS(int s)
# traverses vertices reachable from s.

from collections import defaultdict


class Person:
    next_id = 0

    def __init__(self, FullName, Addresses):
        self.FullName = Name(FullName.FirstName, FullName.LastName)
        self.Address = Address(Addresses.Street, Addresses.City)
        self.id = Person.next_id
        Person.next_id += 1

    def getFullName(self):
        return self.FullName

    def getAddress(self):
        return self.Address

    def setFullName(self, FullName):
        self.FullName = FullName

    def setAddress(self, Address):
        self.Address = Address


class Name:

    def __init__(self, FirstName, LastName):
        self.FirstName = FirstName
        self.LastName = LastName

    def getFirstName(self):
        return self.FirstName

    def getLastName(self):
        return self.LastName

    def setFirstName(self, FirstName):
        self.FirstName = FirstName

    def setLastName(self, LastName):
        self.LastName = LastName


class Address:

    def __init__(self, Street, City):
        self.Street = Street
        self.City = City

    def getStreet(self):
        return self.Street

    def getCity(self):
        return self.City

    def setStreet(self, Street):
        self.Street = Street

    def setCity(self, City):
        self.City = City


# This class represents a directed graph
# using adjacency list representation
class Graph:

    # Constructor
    def __init__(self):

        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    # function to add an edge to graph
    def Init(self, people):

        for person1 in people:
            for person2 in people:

                if person1.id != person2.id:

                    if (
                            person1.getFullName().getFirstName() is person2.getFullName().getFirstName() and person1.getFullName().getLastName() is person2.getFullName().getLastName()):
                        self.addEdge(person1.id, person2.id)
                        continue

                    if (
                            person1.getAddress().getStreet() == person2.getAddress().getStreet() and person1.getAddress().getCity() == person2.getAddress().getCity()):
                        self.addEdge(person1.id, person2.id)

    # Python implementation to find the
    # shortest path in the graph using
    # dictionaries

    # Function to find the shortest
    # path between two nodes of a graph
    def FindMinRelationLevel(self, personA, personB):

        personA = personA.id

        personB = personB.id

        explored = []

        # Queue for traversing the
        # graph in the BFS
        queue = [[personA]]

        # If the desired node is
        # reached
        if personA == personB:
            print("Same Node")
            return

        # Loop to traverse the graph
        # with the help of the queue
        while queue:
            path = queue.pop(0)
            node = path[-1]

            # Codition to check if the
            # current node is not visited
            if node not in explored:
                neighbours = self.graph[node]

                # Loop to iterate over the
                # neighbours of the node
                for neighbour in neighbours:
                    new_path = list(path)
                    new_path.append(neighbour)
                    queue.append(new_path)

                    # Condition to check if the
                    # neighbour node is the goal
                    if neighbour == personB:
                        print("Shortest path = ", *new_path)
                        return len(new_path) - 1
                explored.append(node)

                # Condition when the nodes
        # are not connected
        print("So sorry, but a connecting"
              "path doesn't exist :(")
        return -1


# Driver code

if __name__ == "__main__":
    per1 = Person(Name('Naum', 'Rabich'), Address('Rothschild', 'Haifa'))

    per2 = Person(Name('Simon', 'Rabich'), Address('Rothschild', 'Haifa'))

    per3 = Person(Name('Simon', 'Rabich'), Address('Rothschild', 'Tel-Aviv'))

    per4 = Person(Name('Naum', 'Rabich'), Address('Rothschild', 'Tel-Aviv'))

    per5 = Person(Name('Naum', 'Rabich'), Address('Rothschild', 'Tel-Aviv'))

    arr = [per1, per2, per3, per4, per5]

    # Create a graph given in
    # the above diagram
    g = Graph()
    g.Init(arr)

    print(g.FindMinRelationLevel(per3, per4))
