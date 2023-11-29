import My_First_Class as MFS


def test_add_fn():
    sum = MFS.Addition.add_fn(a=1,b=2)
    assert sum == 3

if __name__ == "__main__":
    test_add_fn()