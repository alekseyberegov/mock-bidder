from mockrtb.http.utils import make_url, make_query_string


class AdURLFactory(object):
    def __init__(self, base_url):
        self.adm_url = make_url(base_url, bid='${AUCTION_PRICE}')

    def get_adm_url(self, **params):
        return self.adm_url + '&' + make_query_string(params)
