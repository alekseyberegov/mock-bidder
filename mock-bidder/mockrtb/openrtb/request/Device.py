from mockrtb.serialize.Serializable import Serializable
from mockrtb.serialize.String import String
from mockrtb.serialize.Field import Field


class Device(Serializable):
    ua = Field(String)

    ip = Field(String)
