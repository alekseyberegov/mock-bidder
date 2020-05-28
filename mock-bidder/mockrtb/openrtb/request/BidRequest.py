from mockrtb.serialize.Field import Field
from mockrtb.serialize.String import String
from mockrtb.serialize.Array import Array
from mockrtb.serialize.Serializable import Serializable

from mockrtb.openrtb.request.Device import Device
from mockrtb.openrtb.request.User import User
from mockrtb.openrtb.request.Site import Site
from mockrtb.openrtb.request.Impression import Impression


class BidRequest(Serializable):
    id = Field(String, required=True)

    bcat = Field(Array(String))

    imp = Field(Array(Impression), required=True)

    site = Field(Site)

    user = Field(User)

    device = Field(Device)

    def __str__(self):
        return str(self.serialize())
