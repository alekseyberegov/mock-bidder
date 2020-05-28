import json
from mockrtb.bidder.BidManager import BidManager
from mockrtb.openrtb.request.BidRequest import BidRequest
from mockrtb.openrtb.response.Bid import Bid
from mockrtb.openrtb.response.BidResponse import BidResponse
from mockrtb.openrtb.response.SeatBid import SeatBid
from mockrtb.http.AdURLFactory import AdURLFactory


class HttpHandler(object):
    def __init__(self, base_url):
        self.bid_manager = BidManager()
        self.url_factory = AdURLFactory(base_url)

    def make_response(self, req: BidRequest) -> BidResponse:
        url = self.url_factory.get_adm_url(auction_uuid=req.id)
        res: BidResponse = BidResponse(
            id=req.id,
            cur="USD",
            seatbid=[
                SeatBid(
                    bid=[
                        Bid(
                            id=req.id,
                            impid=req.imp[0].id,
                            adm=url,
                            nurl=url,
                            price=self.bid_manager.generate_bid(),
                            w=1024,
                            x=768
                        )
                    ],
                )
            ]
        )
        return res

    def do_bid(self, payload):
        req = BidRequest.deserialize(json.loads(payload))
        res = self.make_response(req)
        return str(res.serialize())

