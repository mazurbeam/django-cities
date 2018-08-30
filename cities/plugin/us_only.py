class Plugin(object):
    # def city_pre(self, parser, import_dict):
    #     if import_dict['cc2'] != 'US':
    #         return False
    #     else:
    #         return

    def region_pre(self, parser, import_dict):
        if import_dict['geonameid'] != '6252001':
            return False
        else:
            return


    # this is already handled by the CITIES_POSTAL_CODES array in settings.py
    # def postal_code_pre(self, parser, import_dict):
    #     if import_dict['cc2'] != 'US':
    #         return False
    #     else:
    #         return