from mockrtb.serialize.Serializable import Serializable
from mockrtb.serialize.String import String
from mockrtb.serialize.Field import Field


class Impression(Serializable):
    id = Field(String, required=True)
