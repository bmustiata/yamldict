from typing import Union, IO

import yaml
import yamldict
from yamldict.YamlIteratorWrapper import convert_type

YamlThing = Union[yamldict.YamlList, yamldict.YamlDict, int, float, bool, str, None]


def create(content: Union[str, IO[str]]) -> YamlThing:
    data = yaml.safe_load(content)
    return convert_type(property_name="", value=data)


def create_all(content: str) -> yamldict.YamlList:
    data = yaml.safe_load_all(content)
    return yamldict.YamlList(content=data)  # type: ignore
