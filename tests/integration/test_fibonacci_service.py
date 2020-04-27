from lib.fibonacci import fibonacci

def test_fibonacci_10_values(test_client):
    # client to get '/fibonacci/<n>'
    resp = test_client.get('/fibonacci/10')

    assert str(fibonacci(10)) in str(resp.data)
