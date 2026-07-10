from concepts.recursion.dictionary_depth import dict_depth


def test_empty_dict_has_depth_zero():
    assert dict_depth({}) == 0


def test_flat_dict_with_scalar_values():
    assert dict_depth({"a": 1, "b": 2}) == 1


def test_single_nested_dict():
    assert dict_depth({"a": {"b": 1}}) == 2


def test_deeply_nested_dict():
    assert dict_depth({"a": {"b": {"c": 1}}}) == 3


def test_returns_deepest_branch():
    data = {"shallow": 1, "deep": {"x": {"y": 2}}}
    assert dict_depth(data) == 3


def test_non_dict_returns_current_depth():
    assert dict_depth(42) == 0


def test_nested_empty_dict():
    assert dict_depth({"a": {}}) == 1
