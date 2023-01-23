"""Class AllTypes is made for content type in bot function 'message'.
It allows to collect all types of telegram messages at once.
There is no need to make a long list.
"""


class AllTypes(list):
    def __contains__(self, item):
        return True
