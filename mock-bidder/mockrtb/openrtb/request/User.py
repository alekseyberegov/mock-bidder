from mockrtb.serialize.Serializable import Serializable
from mockrtb.serialize.String import String
from mockrtb.serialize.Field import Field


class User(Serializable):
    id = Field(String)
