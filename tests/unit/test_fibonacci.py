import lib.fibonacci as fibonacci

FIRST_10_FIBONACCI = (0, 1, 1, 2, 3, 5, 8, 13, 21, 34)

def test_fibonacci_length():
    for size in range(100):
        assert len(fibonacci.fibonacci(size)) == size

def test_fibonacci_10_values():
    assert tuple(fibonacci.fibonacci(10)) == FIRST_10_FIBONACCI
