# Hack-and-Heal
Hackathon 25 project for crisis management.

This project is just a simulation before implementing it into the real world. coords_generators.py contains all the code to generate random points and plot them into google maps using the gmplot library. helper_functions.py contains all of the logical code like finding the best refugee camp. In main.py, a gmplot.GoogleMapPlotter object is created with coordinates that form a square. These coordinates are the boundaries which specify where the simulation will take place. You can change these coordinates to any coordinates as long as they form a square/rectangle with no or little rotation.

If you want to change the the predefined coordinates, you need a coordinate for the center of the square/rectangle in this form: (latitude, longitude) in degrees, the variable in main.py is called "CENTER". Then, create a list for the latitude coordinates of the square/rectangle corners and create another list for the longitude coordinates. In main.py, these lists are called "LATS" and "LONGS". After that, you need to define the latitude coordinate for the lower left corner of the square and the upper right corner of the square, these are called "LAT_MIN" and "LAT_MAX" in main.py. Do the same thing for longitude coordinates. All variables mentioned for this part is in uppercase in main.py

Use the functions in point_generators.py to generate coordinates for the user, refugee camps and danger zones. All of these coordinates are randomly generated.

Once the coordinates are gathered, use the helper_functions.py to find the nearest and safest camp (best camp) and to check if it's worth going to. The find_best_camp function does not plot the best camp, it returns the coordinates of the best camp. After getting the coordinates, it is recommended to put it into the check_camp_worthiness function to see if going to the best camp is worth it or not based on how far the nearest danger zone to the point is and nearest danger zone to the best camp is.

coords_generators.py functions:
  generate_rand_refugee_camps_loc(gmap, lat_min, lat_max, long_min, long_max, n_markers=10, color="blue", title=None, label=None)
    This Generates and plots refugee camps in random locations within a predefined square/rectangle. The squre/rectangle must not be rotated. Returns a list of all randomly generated refugee camp coords in this       format: (latitude, longitude)

  generate_rand_bomb_loc(gmap, lat_min, lat_max, long_min, long_max, n_markers=10, radius_range=(20, 50), color="red")
    Generates and plots random points for bombs that have a random radius specified by the "radius_range" parameter. The location of these bombs will be within a predefined square which must not be rotated.           Returns a list of all randomly generated bomb coords and their radius in this format: (latitude, longitude, radius)

  generate_rand_marker(gmap, lat_min, lat_max, long_min, long_max, color="grey", title=None, label=None)
    Generates a random marker within a predefined square that must not be rotated. The marker represents a person. Returns the coords of the random marker in this format: (latitude, longitude)


helper_functions.py functions:
  check_safety(camp, danger_zones, danger_distance=10)
    Returns True if camp is considered safe. Otherwise, returns False. If the camp is inside a danger zone, it returns False. If the distance between the camp and the danger zone is less than "danger_distance",       it returns False. "danger_distance" (in KM) determines how close to a danger zone is considered dangerous

  find_best_camp(point, refugee_camps, danger_zones, danger_distance=10)
    Finds the nearest safe refugee camp (best) from "point". "danger_distance" (in KM) determines how close to a danger zone is considered dangerous

  check_camp_worthiness(point, nearest_safe_camp, danger_zones)
    Checks if the nearest safe camp (best camp) is worth going to. If the distance between the point and the nearest danger zone is greater than the distance between the camp and the nearest danger zone, then its     not worth going to the camp (returns False)
