import re
from .match_parser import match_parser
from ...constants import (
    ADDRESS_REGEX_SPLIT,
    CITY_LIST,
    SUFFIX_ABBREVATIONS,
)


def sanitize_address(address, county):
    """
    Returns lists of sanitized address data in the format of
        address,
        city,
        unit,
        secondary_unit,
        zip_code
    """
    regex_street = re.compile(r".*?(?:" + r"|".join(ADDRESS_REGEX_SPLIT) + r")\s")
    regex_city = re.compile(r"(" + "|".join(CITY_LIST) + ") (NJ|Nj)")
    regex_unit = re.compile(r"(Unit|Apt).([0-9A-Za-z-]+)")
    regex_secondary_unit = re.compile(r"(Building|Estate) #?([0-9a-zA-Z]+)")
    regex_zip_code = re.compile(r"\d{5}")

    street_match = match_parser(regex_street, address, match_type="street")
    city_match = match_parser(regex_city, address, match_type="city", regexGroup=1)
    unit_match = match_parser(regex_unit, address, match_type="unit", log=False)
    secondary_unit_match = match_parser(
        regex_secondary_unit, address, match_type="secondary_unit", log=False
    )
    zip_code_match = match_parser(
        regex_zip_code, address, match_type="zip_code", log=False
    )

    try:
        for key, value in SUFFIX_ABBREVATIONS.items():
            street_match = re.sub(key, value, street_match)
    except TypeError:
        pass

    return {
        "street": street_match,
        "city": city_match,
        "county": county,
        "zip_code": zip_code_match,
        "unit": unit_match,
        "unit_secondary": secondary_unit_match,
    }