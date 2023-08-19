from routes.routes import app


def runner() -> None:
    app.run("localhost", 8000, True)


if __name__ == '__main__':
    runner()
