import time

RATE_LIMIT = 5  # requests
WINDOW_SIZE = 60  # seconds

user_requests = {}

def check_rate_limit(user_id: str) -> bool:
    current_time = time.time()
    requests = user_requests.get(user_id, [])

    # Remove expired requests
    requests = [req for req in requests if current_time - req < WINDOW_SIZE]

    if len(requests) >= RATE_LIMIT:
        return False

    requests.append(current_time)
    user_requests[user_id] = requests
    return True
