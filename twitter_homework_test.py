from twitter_homework import tentweets

def test_tentweets():
    testberkeley = tentweets('#berkeley')
    testberkeley = [x.lower() for x in testberkeley]
    assert '#berkeley' in testberkeley[0]


