# Explination of my design

## specs
* python 3.7_61 

## file structure
* test_train.py =  test cases 
* train.py = class to complete Trains problem
* example_file_input.txt = how to test with file inputi example 
* file_input_tracks.py = uses example_file_input.txt to get results 

## how to use Train class 
```
    from train import Train

    # get class
    train = Train()
    
    # add tracks to be used
    train.add_tracks([
        "AB5", "BC4", "CD8", "DC8", "DE6", "AD5", "CE2", "EB3", "AE7"]) 
    
    # get direct distance from one point to another 
    distance = self.train.get_distance("AB")
    print("here is distance: {}".format(distance))

    distance = self.train.get_distance("AEBCD")
    print("here is distance: {}".format(distance))

    # if direct path is non existent
    distance = self.train.get_distance("AED")
    print("here is distance: {}".format(distance))
    # here is distance: NO SUCH ROUTE

    # get number of trips avalible from point to point with max stop limit
    trips = train.get_trips_max_limit("C", "C", 3)
    print("here is # of trips: {}".format(trips))
    
    # get number of trips avalible from point to point that have x stops
    trips  = self.train.get_trips_equal("A", "C", 4)
    print("here is # of trips: {}".format(trips))
    
    # get length of shortest route from point to point
    shortest = self.train.get_shortest_route("A", "C")
    print("shortest route is this long: {}".format(shortest))
    
    # get number of different rounts under x total distance
    routes = self.train.get_route_count("C", "C", 30)
    print("here is the route count: {}".format(routes))

```

## how to run test
```
    python test_train.py
```

## how to use file input
* edit file location in file_input_tracks.py
```
    python file_input_tracks.py
```

# assumtions with code:
* test cases given covered all edge cases

# Below is the chosen code challenge Instructions given

PROBLEM ONE: TRAINS

Problem:  The local commuter railroad services a number of towns in Kiwiland.  Because of monetary concerns, all of the tracks are 'one-way.'  That is, a route from Kaitaia to Invercargill does not imply the existence of a route from Invercargill to Kaitaia.  In fact, even if both of these routes do happen to exist, they are distinct and are not necessarily the same distance!

The purpose of this problem is to help the railroad provide its customers with information about the routes.  In particular, you will compute the distance along a certain route, the number of different routes between two towns, and the shortest route between two towns.

Input:  A directed graph where a node represents a town and an edge represents a route between two towns.  The weighting of the edge represents the distance between the two towns.  A given route will never appear more than once, and for a given route, the starting and ending town will not be the same town.

Output: For test input 1 through 5, if no such route exists, output 'NO SUCH ROUTE'.  Otherwise, follow the route as given; do not make any extra stops!  For example, the first problem means to start at city A, then travel directly to city B (a distance of 5), then directly to city C (a distance of 4). 

The distance of the route A-B-C.

The distance of the route A-D.

The distance of the route A-D-C.

The distance of the route A-E-B-C-D.

The distance of the route A-E-D.

The number of trips starting at C and ending at C with a maximum of 3 stops.  In the sample data below, there are two such trips: C-D-C (2 stops). and C-E-B-C (3 stops).

The number of trips starting at A and ending at C with exactly 4 stops.  In the sample data below, there are three such trips: A to C (via B,C,D); A to C (via D,C,D); and A to C (via D,E,B).

The length of the shortest route (in terms of distance to travel) from A to C.

The length of the shortest route (in terms of distance to travel) from B to B.

10. The number of different routes from C to C with a distance of less than 30.  In the sample data, the trips are: CDC, CEBC, CEBCDC, CDCEBC, CDEBC, CEBCEBC, CEBCEBCEBC.

Test Input:

For the test input, the towns are named using the first few letters of the alphabet from A to D.  A route between two towns (A to B) with a distance of 5 is represented as AB5.

Graph: AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7

Expected Output: 

Output #1: 9

Output #2: 5

Output #3: 13

Output #4: 22

Output #5: NO SUCH ROUTE

Output #6: 2

Output #7: 3

Output #8: 9

Output #9: 9

Output #10: 7

 ==========

