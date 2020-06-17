from train import Train
train = Train()

f = open("example_file_input.txt", "r")

info = f.readlines()

# show tracks
tracks = info[0].strip('\n').split(", ")
print("here is tracks given: ")
train.add_tracks(tracks)
train.show_graph()


# show distance
track = info[1].strip('\n')
print("get distance for {}".format(track))
distance = train.get_distance(track)
print("distance = {}".format(distance))


# get trips max limit stops
information = info[2].strip('\n').split(" ")
track = information[0]
stops = information[1]
print("get trips  max limit of {} stops for {}".format(stops, track ))
trips  = train.get_trips_max_limit(track[0], track[1], int(stops))
print("trips count = {}".format(trips))


# get trips equal certain stops  
information = info[3].strip('\n').split(" ")
track = information[0]
stops = information[1]
print("get trips with {} stops for {}".format(stops, track ))
trips  = train.get_trips_equal(track[0], track[1], int(stops))
print("trips count = {}".format(trips))



# get shortest route distance
track = info[4].strip('\n')
print("get shortest route for for {}".format(track))
distance = train.get_shortest_route(track[0], track[1])
print("shortest distance = {}".format(distance))


# get number of diff rounts under total
information = info[5].strip('\n').split(" ")
track = information[0]
limit = information[1]
print("get route count with total under {} for {}".format(limit, track ))
trips  = train.get_route_count(track[0], track[1], int(limit))
print("number of different routes  = {}".format(trips))


