import unittest

from siena_mls import (
    getSampleObjectAt,
    getSampleValueAt,
    makeEmptySound,
    setSampleValue,
    setSampleValueAt,
)


class TestSoundSampleValues(unittest.TestCase):
    def test_set_sample_value_at_clamps_to_int16_range(self):
        sound = makeEmptySound(1)

        setSampleValueAt(sound, 0, 40000)
        self.assertEqual(getSampleValueAt(sound, 0), 32767)

        setSampleValueAt(sound, 0, -40000)
        self.assertEqual(getSampleValueAt(sound, 0), -32768)

    def test_set_sample_value_clamps_to_int16_range(self):
        sound = makeEmptySound(1)
        sample = getSampleObjectAt(sound, 0)

        setSampleValue(sample, 40000)
        self.assertEqual(getSampleValueAt(sound, 0), 32767)
