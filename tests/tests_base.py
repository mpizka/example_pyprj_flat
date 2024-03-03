"""This is a bunch of basic tests."""

import unittest

from timemachine import flux


class Tests(unittest.TestCase):
    """These are the tests in here."""

    def test_a(self):
        """Does the space time continuum still work as expected"""
        self.assertEqual(
            flux.whats_this(),
            flux.whats_this(),
            "The destruction of the space-time-continuum Marty!",
        )

    def test_b(self):
        """Is testing working"""

        # see how boumm is a helper, not a test method?
        self.assertRaises(
            KeyError,
            self.boumm,
        )

    def boumm(self):
        """Not a test since it's named boumm"""
        return {}["no_exist"]

    def test_c(self):
        """Is the output as expected"""
        self.assertEqual(
            "The Flux-Compensator, Marty!",
            flux.whats_this(),
            "The destruction of the space-time-continuum Marty!",
        )


if __name__ == "__main__":
    unittest.main()
