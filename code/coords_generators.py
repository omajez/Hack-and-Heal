import random

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
        gmap.marker(rand_lat, rand_long, color=color, title=title, label=label)

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
