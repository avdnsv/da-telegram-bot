from dadata_package.custom_dadata import CustomDadata
from dadata_package import const


class FakeDadata(CustomDadata):
    """Class FakeDadata is made for testing to format data."""
    def __init__(self):
        """Inits CustomDadata with nothing"""
        self.response = {}
        pass

    def dadata_response(self, address):
        """Takes response from const (it's already have a response)."""
        self.response = const.FAKE_RESPONSE
        return self.response


# d = FakeDadata()
# d.dadata_response('address')
# print(d.customized_data())
