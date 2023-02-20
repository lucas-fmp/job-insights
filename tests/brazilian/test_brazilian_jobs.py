from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    path = "tests/mocks/brazilians_jobs.csv"
    data = read_brazilian_file(path)
    expected_list = ["title", "salary", "type"]
    keys_list = []

    for dict in data:
        for key in dict:
            if key not in keys_list:
                keys_list.append(key)

    assert keys_list == expected_list
