from haversine import haversine

def check_safety(camp, danger_zones, danger_distance=10):
    """
    Returns True if camp is considered safe. Otherwise, returns False. If the camp is inside a danger zone, it returns False. If the distance 
    between the camp and the danger zone is less than "danger_distance", it returns False. "danger_distance" (in KM) determines how close to 
    a danger zone is considered dangerous
    """

    for danger_zone in danger_zones:
        # danger_zone is in this format: (latitude, longitude, radius). The latitude and longitude represent the center of the danger zone
        danger_zone_center, radius = (danger_zone[0], danger_zone[1]), danger_zone[2]

        # Distance between camp and danger_zone
        distance = haversine(camp, danger_zone_center) - (radius/1000) # subtracting by radius (in KM) is done to calculate the distance bewteen the camp and the circle of the danger_zone

        if distance < danger_distance:
            return False
    
    return True

def find_best_camp(point, refugee_camps, danger_zones, danger_distance=10):
    """
    Finds the nearest safe refugee camp (best) from "point". "danger_distance" (in KM) determines how close to a danger zone is considered dangerous
    """
    
    nearest_safe_camp = None
    nearest_safe_camp_distance = float("inf")

    for camp in refugee_camps:
        safe = check_safety(camp, danger_zones, danger_distance)
        
        if not safe:
            continue

        # Distance from point to camp
        distance = haversine(point, camp)

        if distance < nearest_safe_camp_distance:
            nearest_safe_camp_distance = distance
            nearest_safe_camp = camp
    
    return nearest_safe_camp

def check_camp_worthiness(point, nearest_safe_camp, danger_zones):
    """
    Checks if the nearest safe camp (best camp) is worth going to. If the distance between the point and the nearest danger zone is greater than 
    the distance between the camp and the nearest danger zone, then its not worth going to the camp (returns False)
    """

    # Calculating the nearest danger zone to "point"
    # one "danger_zone" format is like this -> (latitude, longitude, radius)
    nearest_dzone_to_point_distance = min(list(map(lambda x: haversine(point, (x[0], x[1])) - (x[2]/1000), danger_zones))) # "x[2]/1000" converting radius to KM

    # Calculating the nearest danger zone to "nearest_safe_camp"
    nearest_dzone_to_camp_distance = min(list(map(lambda x: haversine(nearest_safe_camp, (x[0], x[1])) - (x[2]/1000), danger_zones))) # "x[2]/1000" converting radius to KM

    if nearest_dzone_to_point_distance > nearest_dzone_to_camp_distance:
        return False
    elif nearest_dzone_to_point_distance < nearest_dzone_to_camp_distance:
        return True
    else:
        return None
