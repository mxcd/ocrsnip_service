import time
import uuid

MAX_STORE_SIZE = 2000

images = {}
secrets = {}
times = {}


def add_image(img):
    id = uuid.uuid4().hex
    secret = uuid.uuid4().hex

    images[id] = img
    secrets[id] = secret
    times[id] = time.time()

    do_cleanup()

    return id, secret


def get_image(id, secret):
    if id in secrets:
        if secrets[id] == secret:
            return images[id]
        else:
            return None
    else:
        return None


def delete_image(id, secret):
    if id in secrets:
        if secrets[id] == secret:
            _delete_image(id)
            return True
        else:
            return False
    else:
        return False


def _delete_image(id):
    del images[id]
    del secrets[id]
    del times[id]


def do_cleanup():
    sorted_times = {k: v for k, v in sorted(times.items(), key=lambda item: item[1])}
    print(len(sorted_times))
    if len(sorted_times) > MAX_STORE_SIZE:
        for el in list(sorted_times.keys())[MAX_STORE_SIZE - len(sorted_times):]:
            _delete_image(el)
