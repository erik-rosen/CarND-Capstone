#!/usr/bin/env python

import sys
import unittest

import roslib;

from tl_classifier import TLClassifier

class TestTrafficLightSegmentation(unittest.TestCase):
    def test_one_equals_one(self):  # only functions with 'test_'-prefix will be run!
        self.assertEquals(1, 1, "1!=1")

if __name__ == '__main__':
    import rostest

    rostest.unitrun("light_classification", 'test_traffic_segmentatin', 'src.tl_detector.light_classification.segmentation_test')