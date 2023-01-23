from dadata import Dadata
from dadata_package import const


class CustomDadata:
    """Basic class for data from api dadata."""
    def __init__(self, token, secret):
        """Inits CustomDadata with token and secret"""
        self.client = Dadata(token, secret)
        self.response = {}

    def dadata_response(self, address):
        """Gets response from dadata."""
        self.response = self.client.clean("address", address)
        return self.response

    def customized_data(self):
        """Main method for customizing data."""
        customized_response = self.response
        self.format_region_metro(customized_response)
        self.remove_empty_data(customized_response)
        return self.format_data(customized_response, const.AREAS_PARAMS)

    @staticmethod
    def format_region_metro(data):
        """Formats areas with region and metro."""
        if data.get('region_kladr_id'):
            data['region_kladr_id'] = data['region_kladr_id'][:2]  # need only two numbers
        if data.get('metro'):
            stations = []
            for item in data['metro']:
                stations.append(
                    f"{item['name']} ({item['line']}) - {item['distance']} км"
                )
            data['metro'] = '\n'.join(stations)

    @staticmethod
    def remove_empty_data(data):
        """Removes empty data with None."""
        for key in list(data):
            if data[key] is None:
                data.pop(key)

    @staticmethod
    def format_data(data, params_groups):
        """Final formats data for output."""
        result = []
        for params_group in params_groups.values():
            group_points = []
            for key in params_group.keys():
                if data.get(key):
                    group_points.append(f"{params_group[key]}: {data[key]}")
            if len(group_points) == 0:
                del group_points
            else:
                result.append('\n'.join(group_points))
        return '\n\n'.join(result)
