import requests

import py3_web


def test_http_response():
    text = """jQuery5346819({"username":"py3-web"})"""
    print(py3_web.http.response.jsonp_to_json(text)["username"])

    text = """jsonp_31515591963415254({"username":"py3-web"})"""
    print(py3_web.http.response.jsonp_to_json(text)["username"])

    url = "https://api.flickr.com/services/feeds/photos_public.gne?format=json&jsoncallback=handleFlickr"
    text = requests.get(url).text
    print(py3_web.http.response.jsonp_to_json(text))


if __name__ == '__main__':
    test_http_response()
