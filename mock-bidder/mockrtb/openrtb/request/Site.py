from mockrtb.serialize.Serializable import Serializable
from mockrtb.serialize.String import String
from mockrtb.serialize.Field import Field
from mockrtb.serialize.Array import Array


class Site(Serializable):
    id = Field(String)

    cat = Field(Array(String))
