import DSDJ.OOP.Pytest.Custom_dict


class TestFunction:

    def test_instance_type(self):
        obj = DSDJ.OOP.Pytest.Custom_dict.ConfigDict('pickle_file.pkl')
        assert isinstance(obj, DSDJ.OOP.Pytest.Custom_dict.ConfigDict) == True