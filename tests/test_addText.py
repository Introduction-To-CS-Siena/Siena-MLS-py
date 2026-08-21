import unittest
from siena_mls import addText, makePicture
from siena_mls import _load_fallback_font


class TestAddText(unittest.TestCase):
    def test_addText_zero_size_raises_value_error(self):
        pic = makePicture("tests/assets/siena-small-logo.png")
        with self.assertRaises(ValueError):
            addText(pic, 0, 0, "hello", size=0)

    def test_addText_negative_size_raises_value_error(self):
        pic = makePicture("tests/assets/siena-small-logo.png")
        with self.assertRaises(ValueError):
            addText(pic, 0, 0, "hello", size=-5)

    def test_load_fallback_font_returns_font(self):
        from PIL.ImageFont import FreeTypeFont
        font = _load_fallback_font(12)
        self.assertIsInstance(font, FreeTypeFont)


if __name__ == "__main__":
    unittest.main()
