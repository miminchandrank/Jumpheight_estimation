# utils.py

def find_point(landmarks, point_id):
    for id, x, y in landmarks:
        if id == point_id:
            return (x, y)
    return None
