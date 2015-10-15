"""
This is a test file for twitter_homework to ensure
the compiled list of tweets contains the query.
"""

from twitter_homework import tentweets

def test_tentweets():
    testberkeley = tentweets('#berkeley')
    testberkeley = [x.lower() for x in testberkeley]
    assert '#berkeley' in testberkeley[0]


