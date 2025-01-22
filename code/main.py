import gmplot
import helper_functions
import coords_generators




# "LATS" and "LONGS" can be changed to any square coords you want. The square must NOT be rotated
# If you change the "LATS" and "LONGS", you must change "center", "lat_min", "long_min", "lat_max" and "long_max"
# "center" is the coords of the center of the square
# "lat_min" and "long_min" are the coords of the lower left corner of the square
# "lat_max" and "long_max" are the coords of the upper right corner of the square
CENTER = (31.52878623989880, 34.44500081676887)
gmap = gmplot.GoogleMapPlotter(CENTER[0], CENTER[1], 17, "hybrid")
LATS = [31.531300443694477, 31.526476319426628, 31.526430548012474, 31.531295620240535]
LONGS = [34.44110336819361, 34.441125174979014, 34.44773415865575, 34.44776638214709]
gmap.polygon(LATS, LONGS, color="cyan", edge_width=5, face_alpha=0.1)

# Boundaries of the square
LAT_MIN, LONG_MIN = 31.526476319426628, 34.441125174979014
LAT_MAX, LONG_MAX, = 31.531295620240535, 34.44776638214709

# Generate points
point = coords_generators.generate_rand_marker(gmap=gmap, lat_min=LAT_MIN, lat_max=LAT_MAX, long_min=LONG_MIN, long_max=LONG_MAX, label="Person")
refugee_camps = coords_generators.generate_rand_refugee_camps_loc(gmap=gmap, lat_min=LAT_MIN, lat_max=LAT_MAX, long_min=LONG_MIN, long_max=LONG_MAX, n_markers=5, label="Camp")
danger_zones = coords_generators.generate_rand_bomb_loc(gmap=gmap, lat_min=LAT_MIN, lat_max=LAT_MAX, long_min=LONG_MIN, long_max=LONG_MAX, n_markers=10, radius_range=(20, 50))

# Find nearest safe refugee camp
nearest_safe_camp = helper_functions.find_best_camp(point, refugee_camps, danger_zones, 0.01)

# Check if the camp is worth going to
worthiness = helper_functions.check_camp_worthiness(point, nearest_safe_camp, danger_zones)

if worthiness:
    gmap.marker(nearest_safe_camp[0], nearest_safe_camp[1], "green", label="Camp")
elif not worthiness:
    gmap.marker(nearest_safe_camp[0], nearest_safe_camp[1], "red", label="Camp")
else:
    gmap.marker(nearest_safe_camp[0], nearest_safe_camp[1], "yellow", label="Camp")


gmap.draw("map.html")
