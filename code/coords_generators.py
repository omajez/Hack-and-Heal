import random
from haversine import inverse_haversine, Direction
import gmplot

def generate_rand_refugee_camps_loc(gmap, lat_min, lat_max, long_min, long_max, n_markers=10, color="blue", title=None, label=None):
    """
    Generates and plots refugee camps in random locations within a predefined square/rectangle. The squre/rectangle must not be rotated.
    Returns all randomly generated refugee camp coords in this format: [(latitude, longitude), ...]
    """

    refugee_camps = []

    for _ in range(n_markers):
        # Generate random latitude and longitude for the marker
        rand_lat, rand_long = random.uniform(lat_min, lat_max), random.uniform(long_min, long_max)

        # Plot the random marker
        gmap.marker(rand_lat, rand_long, color=color, title=title, label="C")
        gmap.text(rand_lat, rand_long, label, color="white")

        # Append the coords to the list
        refugee_camps.append((rand_lat, rand_long))

    return refugee_camps

def generate_rand_bomb_loc(gmap, lat_min, lat_max, long_min, long_max, n_markers=10, radius_range=(20, 50), color="red"):
    """
    Generates and plots random points for bombs that have a random radius specified by the "radius_range" parameter. The location of these bombs
    will be within a predefined square which must not be rotated. Returns all randomly generated bomb coords and their radius in this 
    format: [(latitude, longitude, radius), ...]
    """

    bombs = []

    for _ in range(n_markers):
        # Generate random points for the center of the bomb.
        rand_lat, rand_long = random.uniform(lat_min, lat_max), random.uniform(long_min, long_max)

        # Generate random radius for the bomb
        radius = random.uniform(radius_range[0], radius_range[1])

        # Plot the random bomb
        gmap.circle(rand_lat, rand_long, radius=radius, color=color, face_alpha=0.5, edge_width=2)

        # Append the coords to the list
        bombs.append((rand_lat, rand_long, radius))

    return bombs

def generate_rand_marker(gmap, lat_min, lat_max, long_min, long_max, color="grey", title=None, label=None):
    """
    Generates a random marker within a predefined square that must not be rotated. The marker represents a person. Returns the coords
    of the random marker in this format: (latitude, longitude)
    """

    # Generate random latitude and longitude for the marker
    rand_lat, rand_long = random.uniform(lat_min, lat_max), random.uniform(long_min, long_max)

    # Plot the random marker
    gmap.marker(rand_lat, rand_long, color=color, title=title, label=label)

    return rand_lat, rand_long

def generate_gmap_sim_square(user, length, height, user_color="grey", user_label="You"):
    """
    Creates a GoogleMapPlotter object and generates a random square for the simulation. The coordinates of the user will always be inside the
    simulatoin square.

    params:
    user -> Coordinates of the user in latitude and longitude
    length -> Length of the square in KM
    height -> Height of the square in KM
    user_color -> Color of the user's marker
    user_label -> Label to be displayed for the user's marker

    returns a tuple containing the center of the square, coordinates of the bottom left corner square (because it has the minimum latitude and 
    longitude) and the coordinates of the top right corner of the square (because it has the maximum latitude and longitude)
    """

    # Calculate min and max for lat and long to generate a random sim square that ensures that the user's coords will be inside it
    min_lat = inverse_haversine(user, height*0.5, Direction.SOUTH)[0]
    max_lat = inverse_haversine(user, height*0.5, Direction.NORTH)[0]
    min_long = inverse_haversine(user, length*0.5, Direction.WEST)[1]
    max_long = inverse_haversine(user, length*0.5, Direction.EAST)[1]

    center = random.uniform(min_lat, max_lat), random.uniform(min_long, max_long)

    lats = []
    longs = []

    # Square corners
    bottom_left_corner = inverse_haversine(inverse_haversine(center, height*0.5, Direction.SOUTH), length*0.5, Direction.WEST)
    lats.append(bottom_left_corner[0])
    longs.append(bottom_left_corner[1])

    bottom_right_corner = inverse_haversine(bottom_left_corner, length, Direction.EAST)
    lats.append(bottom_right_corner[0])
    longs.append(bottom_right_corner[1])

    top_right_corner = inverse_haversine(bottom_right_corner, height, Direction.NORTH)
    lats.append(top_right_corner[0])
    longs.append(top_right_corner[1])

    top_left_corner = inverse_haversine(top_right_corner, length, Direction.WEST)
    lats.append(top_left_corner[0])
    longs.append(top_left_corner[1])

    gmap = gmplot.GoogleMapPlotter(center[0], center[1], 16, "hybrid")
    gmap.marker(user[0], user[1], color=user_color, label="Y")
    gmap.text(user[0], user[1], "You", color="white")
    gmap.polygon(lats, longs, color="cyan", edge_width=2, face_alpha=0)
    
    return gmap, bottom_left_corner, top_right_corner
