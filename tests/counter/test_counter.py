from src.pre_built.counter import count_ocurrences


def test_counter():
    word_count = count_ocurrences("data/jobs.csv", "Python")
    assert word_count == 1639
