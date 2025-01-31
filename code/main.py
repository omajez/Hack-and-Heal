import gmplot
import helper_functions
import coords_generators




# "LATS" and "LONGS" can be changed to any square coords you want. The square must NOT be rotated
# If you change the "LATS" and "LONGS", you must change "center", "lat_min", "long_min", "lat_max" and "long_max"
# "center" is the coords of the center of the square
# "lat_min" and "long_min" are the coords of the lower left corner of the square
# "lat_max" and "long_max" are the coords of the upper right corner of the square
import geocoder
g = geocoder.ip("me")
# point = (25.323231431863274, 51.442453311430995)
point = g.latlng
gmap, (LAT_MIN, LONG_MIN), (LAT_MAX, LONG_MAX) = coords_generators.generate_gmap_sim_square(point, 0.75, 0.75)

# Generate points
refugee_camps = coords_generators.generate_rand_refugee_camps_loc(gmap=gmap, lat_min=LAT_MIN, lat_max=LAT_MAX, long_min=LONG_MIN, long_max=LONG_MAX, n_markers=5, label="Camp")
danger_zones = coords_generators.generate_rand_bomb_loc(gmap=gmap, lat_min=LAT_MIN, lat_max=LAT_MAX, long_min=LONG_MIN, long_max=LONG_MAX, n_markers=10, radius_range=(20, 50))

# Find nearest safe refugee camp
nearest_safe_camp = helper_functions.find_best_camp(point, refugee_camps, danger_zones, 0.01)

# Check if the camp is worth going to
worthiness = helper_functions.check_camp_worthiness(point, nearest_safe_camp, danger_zones)

if worthiness:
    gmap.marker(nearest_safe_camp[0], nearest_safe_camp[1], "green", label="C", info_window=f"<a href='https://www.google.com/maps?q={nearest_safe_camp[0]},{nearest_safe_camp[1]}' target=_blank>Google maps</a>")
else:
    gmap.marker(nearest_safe_camp[0], nearest_safe_camp[1], "red", label="C", info_window=f"<a href='https://www.google.com/maps?q={nearest_safe_camp[0]},{nearest_safe_camp[1]}' target=_blank>Google maps</a>")




gmap.draw(r"templates\map.html")
