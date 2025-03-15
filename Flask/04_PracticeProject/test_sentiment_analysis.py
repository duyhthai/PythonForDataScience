import unittest
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

class TestSentimentAnalyzer(unittest.TestCase):
    def test_sentiment_analyzer (self):
        expect_positive = sentiment_analyzer("I love working with Python")
        self.assertEqual(expect_positive['label'], 'SENT_POSITIVE')

        expect_negative = sentiment_analyzer("I hate working with Python")
        self.assertEqual(expect_negative['label'], 'SENT_NEGATIVE')

        expect_neutral = sentiment_analyzer("I am neutral on Python")
        self.assertEqual(expect_neutral['label'], 'SENT_NEUTRAL')

unittest.main()
