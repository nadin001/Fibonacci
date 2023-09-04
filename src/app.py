from tornado.ioloop import IOLoop
from tornado.web import Application, RequestHandler
from src.fibonacci import get_fibonacci_number

port = 8888


def get_app() -> Application:
    return Application([('/get/fibonacci', FibonacciHandler)])


class FibonacciHandler(RequestHandler):

    def get(self: RequestHandler) -> None:
        index_argument = self.get_query_argument("index")
        if index_argument is None:
            index = 0
        else:
            index = int(index_argument)
        result = get_fibonacci_number(index)
        self.write(f"Fibonacci number with index {index}: {result}")


if __name__ == '__main__':
    get_app().listen(port)
    IOLoop.current().start()
