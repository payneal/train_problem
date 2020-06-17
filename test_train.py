import unittest
from train import Train

class Test_Train(unittest.TestCase):

    def setUp(self):
        self.train = Train()
        self.train.add_tracks([
            "AB5", "BC4", "CD8", "DC8", "DE6", "AD5", "CE2", "EB3", "AE7"]) 

    def tearDown(self):
        self.train = None

    def test_get_distance_a_b(self):
        distance = self.train.get_distance("AB")
        self.assertEqual(distance, 5)

    # The distance of the route A-B-C.
    # answer = 9
    def test_get_distance_a_b_c(self):
        distance = self.train.get_distance("ABC")
        self.assertEqual(distance, 9)
   
    # The distance of the route A-D
    # answer = 5
    def test_get_distance_a_d(self):
        distance = self.train.get_distance("AD")
        self.assertEqual(distance, 5)
  
    # The distance of the route A-D-C. 
    # answer = 13 
    def test_get_distance_a_d_c(self):
        distance = self.train.get_distance("ADC")
        self.assertEqual(distance, 13)
    
    
    # The distance of the route A-E-B-C-D
    # answer= 22
    def test_get_distance_a_e_b_c_d(self):
        distance = self.train.get_distance("AEBCD")
        self.assertEqual(distance, 22)
   
    
    # The distance of the route A-E-D
    def test_get_distance_a_e_d(self):
        distance = self.train.get_distance("AED")
        self.assertEqual(distance, "NO SUCH ROUTE")
 

    def test_get_no_such_nothing(self):
        distance = self.train.get_distance("XY")
        self.assertEqual(distance, "NO SUCH ROUTE")
    
    def test_get_no_such_with_graph(self):
        distance = self.train.get_distance("ABZ")
        self.assertEqual(distance, "NO SUCH ROUTE")
    
    # The number of trips starting at C and ending at C with a maximum of 3 stops.  
    # In the sample data below, there are two such trips: C-D-C (2 stops). 
    # and C-E-B-C (3 stops)
    # answer = 2
    def test_get_distance_c_c_with_max_3(self):
        trips  = self.train.get_trips_max_limit("C", "C", 3)
        self.assertEqual(trips, 2)

    
    # The number of trips starting at A and ending at C with exactly 4 stops.  
    # In the sample data below, there are three such trips: A to C (via B,C,D); 
    # A to C (via D,C,D); and A to C (via D,E,B).
    # answer = 3
    def test_get_distance_a_c_equal(self):
        trips  = self.train.get_trips_equal("A", "C", 4)
        self.assertEqual(trips, 3)


    # The length of the shortest route (in terms of distance to travel) from A to C
    # answer = 9
    def test_get_shortest_a_c(self):
        shortest = self.train.get_shortest_route("A", "C")
        self.assertEqual(shortest, 9)
 

    # The length of the shortest route (in terms of distance to travel) from B to B.
    # answer = 9 
    def test_get_shortest_b_b(self):
        shortest = self.train.get_shortest_route("B", "B")
        self.assertEqual(shortest, 9)
    
    # The number of different routes from C to C with a distance of less than 30.  
    # In the sample data, the trips are: CDC, CEBC, CEBCDC, CDCEBC, CDEBC, CEBCEBC, CEBCEBCEBC.
    def test_get_number_of_diff_routes_c_c_less_than_30(self):
        routes = self.train.get_route_count("C", "C", 30)
        self.assertEqual(routes, 7)
    

if __name__ == "__main__":
    unittest.main()
