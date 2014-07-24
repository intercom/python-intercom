from describe import expect
from intercom.lib.flat_store import FlatStore


class DescribeIntercomFlatStore:

    def it_raises_if_you_try_to_set_or_merge_in_nested_hash_structures(self):
        data = FlatStore()
        with expect.raise_error(ValueError):
            data["thing"] = [1]
        with expect.raise_error(ValueError):
            data["thing"] = {1: 2}
        with expect.raise_error(ValueError):
            FlatStore(**{"1": {2: 3}})

    def it_raises_if_you_try_to_use_a_non_string_key(self):
        data = FlatStore()
        with expect.raise_error(ValueError):
            data[1] = "something"

    def it_sets_and_merges_valid_entries(self):
        data = FlatStore()
        data["a"] = 1
        data["b"] = 2
        expect(data["a"]) == 1
        expect(data["b"]) == 2
        data = FlatStore(a=1, b=2)
        expect(data["a"]) == 1
        expect(data["b"]) == 2
