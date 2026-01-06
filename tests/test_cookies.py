import py3_web


def test_cookies():
    cookies = {
        "package": "py3-web"
    }
    print(py3_web.cookies.dict_to_str(cookies))


if __name__ == '__main__':
    test_cookies()
