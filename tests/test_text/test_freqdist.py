# tests.test_text.test_freqdist
# Tests for the frequency distribution visualization
#
# Author:   Rebecca Bilbro <rbilbro@districtdatalabs.com>
# Created:  2017-03-22 15:27
#
# Copyright (C) 2017 District Data Labs
# For license information, see LICENSE.txt
#
# ID: test_freqdist.py [bd9cbb9] rebecca.bilbro@bytecubed.com $

"""
Tests for the frequency distribution text visualization
"""

##########################################################################
## Imports
##########################################################################

import unittest

from yellowbrick.text.freqdist import *
from tests.dataset import DatasetMixin
from sklearn.feature_extraction.text import CountVectorizer


##########################################################################
## FreqDist Tests
##########################################################################

class FreqDistTests(unittest.TestCase, DatasetMixin):

    def test_integrated_freqdist(self):
        """
        Assert no errors occur during freqdist integration
        """
        corpus     = self.load_data('hobbies')
        vectorizer = CountVectorizer()

        docs       = vectorizer.fit_transform(corpus.data)
        features   = vectorizer.get_feature_names()

        visualizer = FreqDistVisualizer()
        visualizer.fit(docs, features)
