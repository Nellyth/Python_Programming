from unittest import TestCase
from Bouncy import Bouncy


class DummyTest(TestCase):
    data = Bouncy()

    def test_the_main_function_receives_a_whole_data(self):
        assert self.data.main('asd')
        print(self.data.main('asd'))

    def test_can_not_enter_a_null_value(self):
        assert self.data.main(None)
        print(self.data.main(None))

    def test_the_value_can_not_be_greater_than_100(self):
        assert self.data.main(101)
        print(self.data.main(101))

    def test_the_value_can_not_be_less_than_1(self):
        assert self.data.main(0)
        print(self.data.main(0))

    def test_the_returned_value_must_be_an_integer(self):
        assert self.data.main(99).isnumeric()
