import sys
from unittest import TestCase, main
from tornado.testing import AsyncHTTPTestCase
from src.fibonacci import get_fibonacci_number
from tornado.web import Application
import src.app as fibonacci_app
sys.path.append("..")


class TestFib(TestCase):
    def test_plus(self) -> None:
        self.assertEqual(get_fibonacci_number(4), "3")  # add assertion here

    def test_plus1(self) -> None:
        self.assertEqual(get_fibonacci_number(9), "34")

    def test_null(self) -> None:
        self.assertEqual(get_fibonacci_number(0), "does not exist :<")

    def test_minus(self) -> None:
        self.assertEqual(get_fibonacci_number(-5), "does not exist :<")


class TestApp(AsyncHTTPTestCase):
    @property
    def url(self: AsyncHTTPTestCase) -> str:
        if not hasattr(self, '_url'):
            self._url = self.get_url('/get/fibonacci')
        return self._url  # type: ignore

    def get_app(self) -> Application:
        return fibonacci_app.get_app()

    def test_calculate_fibonacci_number_successfully(self) -> None:
        print(self.get_url('/get/fibonacci'))
        response = self.fetch('/get/fibonacci?index=4', method='GET')
        self.assertEqual(response.code, 200)
        self.assertEqual(
            str(response.body),
            "b'Fibonacci number with index 4: 3'"
        )

    def test_not_calculate_fibonacci_number(self) -> None:
        print(self.get_url('/get/fibonacci'))
        response = self.fetch('/get/fibonacci', method='GET')
        self.assertEqual(response.code, 400)


if __name__ == '__main__':
    main()
