import sys
from support import SupportClass

print(SupportClass.get_workspace_path())

sys.path.insert(0, SupportClass.get_workspace_path())

print("SYS.PATH:",sys.path)

from my_first_class_dir.first_class import Addition


def test_add_fn():
    sum = Addition.add_fn(a=1,b=2)
    print("worked")
    assert sum == 3

if __name__ == "__main__":
    test_add_fn()