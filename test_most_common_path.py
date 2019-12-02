from unittest import TestCase

from main import most_common_path


class TestMost_common_path(TestCase):

    def test_single_most_common_path(self):

        log = ["1,A", "1,B", "1,C", "1,D", "2,A", "2,B", "2,C"]
        expected_result = ["A->B->C"]

        result = most_common_path(log)

        self.assertCountEqual(result, expected_result)

    def test_multiple_common_path(self):

        log = ["1,A", "1,B", "1,C", "1,D", "2,A", "2,B", "2,C", "2,D"]
        expected_result = ["A->B->C", "B->C->D"]

        result = most_common_path(log)

        self.assertCountEqual(result, expected_result)

    def test_no_common_path(self):

        log = ["1,A", "2,B", "3,C"]
        expected_result = []

        result = most_common_path(log)

        self.assertCountEqual(result, expected_result)