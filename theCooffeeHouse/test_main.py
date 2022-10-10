

import requests

LOCAL_URL = 'http://localhost:8000/'
def test_get_direction_dont_have_profile():
    resp = requests.get(f"{LOCAL_URL}demopy")
    assert resp.status_code == 200
    msg = resp.json()
    assert 'pyt4est' in msg['dat9']['dat4a']
