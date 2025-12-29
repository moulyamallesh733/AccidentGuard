def detect_accident(acceleration):
    threshold=15
    if acceleration>threshold:
        return True
    return False