import unittest
import library

NUM_CORPUS = '''
On the 5th of May every year, Mexicans celebrate Cinco de Mayo. This tradition
began in 1845 (the twenty-second anniversary of the Mexican Revolution), and
is the 1st example of a national independence holiday becoming popular in the
Western Hemisphere. (The Fourth of July didn't see regular celebration in the
US until 15-20 years later.) It is celebrated by 77.9% of the population--
trending toward 80.                                                                
'''

class TestCase(unittest.TestCase):

    # Helper function
    def assert_extract(self, text, extractors, *expected):
        actual = [x[1].group(0) for x in library.scan(text, extractors)]
        self.assertEquals(str(actual), str([x for x in expected]))

    # First unit test; prove that if we scan NUM_CORPUS looking for mixed_ordinals,
    # we find "5th" and "1st".
    def test_mixed_ordinals(self):
        self.assert_extract(NUM_CORPUS, library.mixed_ordinals, '5th', '1st')

    # Second unit test; prove that if we look for integers, we find four of them.
    def test_integers(self):
        self.assert_extract(NUM_CORPUS, library.integers, '1845', '15', '20', '80')

    # Third unit test; prove that if we look for integers where there are none, we get no results.
    def test_no_integers(self):
        self.assert_extract("no integers", library.integers)

    def test_dates(self):

        fixtures = [
            ['I was born on 2015-07-25.', '2015-07-25'],
            ['I was born on 2015-07-25 18:22.', '2015-07-25 18:22'],
            ['I was born on 2015-07-25 18:22:19.', '2015-07-25 18:22:19'],
            ['I was born on 2015-07-25 18:22:19.123.', '2015-07-25 18:22:19.123'],
            ['I was born on 2015-07-25T18:22.', '2015-07-25T18:22'],
            ['I was born on 2015-07-25T18:22:19.', '2015-07-25T18:22:19'],
            ['I was born on 2015-07-25T18:22:19.123.', '2015-07-25T18:22:19.123'],
            ['I was born on 2015-07-25 18:22MDT.', '2015-07-25 18:22MDT'],
            ['I was born on 2015-07-25 18:22:19MDT.', '2015-07-25 18:22:19MDT'],
            ['I was born on 2015-07-25 18:22:19.123MDT.', '2015-07-25 18:22:19.123MDT'],
            ['I was born on 2015-07-25T18:22MDT.', '2015-07-25T18:22MDT'],
            ['I was born on 2015-07-25T18:22:19MDT.', '2015-07-25T18:22:19MDT'],
            ['I was born on 2015-07-25T18:22:19.123MDT.', '2015-07-25T18:22:19.123MDT'],
            ['I was born on 2015-07-25 18:22Z.', '2015-07-25 18:22Z'],
            ['I was born on 2015-07-25 18:22:19Z.', '2015-07-25 18:22:19Z'],
            ['I was born on 2015-07-25 18:22:19.123Z.', '2015-07-25 18:22:19.123Z'],
            ['I was born on 2015-07-25T18:22Z.', '2015-07-25T18:22Z'],
            ['I was born on 2015-07-25T18:22:19Z.', '2015-07-25T18:22:19Z'],
            ['I was born on 2015-07-25T18:22:19.123Z.', '2015-07-25T18:22:19.123Z'],
            ['I was born on 2015-07-25 18:22-0800.', '2015-07-25 18:22-0800'],
            ['I was born on 2015-07-25 18:22:19-0800.', '2015-07-25 18:22:19-0800'],
            ['I was born on 2015-07-25 18:22:19.123-0800.', '2015-07-25 18:22:19.123-0800'],
            ['I was born on 2015-07-25T18:22-0800.', '2015-07-25T18:22-0800'],
            ['I was born on 2015-07-25T18:22:19-0800.', '2015-07-25T18:22:19-0800'],
            ['I was born on 2015-07-25T18:22:19.123-0800.', '2015-07-25T18:22:19.123-0800'],
        ]

        for fixture in fixtures:
            self.assert_extract(fixture[0], library.dates_iso8601, fixture[1])

    def test_dates_fmt2(self):
        self.assert_extract('I was born on 25 Jan 2017.', library.dates_fmt2, '25 Jan 2017')

if __name__ == '__main__':
    unittest.main()
