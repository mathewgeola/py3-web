import web


def test_cookies():
    cookies = {
        "package": "py3-web"
    }
    print(web.cookies.dict_to_str(cookies))


if __name__ == '__main__':
    test_cookies()
