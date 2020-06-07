from .utils import load_json_data

NJ_PARCELS_URL = "http://njparcels.com/property/"
NJ_PARCELS_API = "http://njparcels.com/api/v1.0/property/"
SHERIFF_SALES_BASE_URL = "https://salesweb.civilview.com"
SHERIFF_SALES_URL = "https://salesweb.civilview.com/Sales/SalesSearch?countyId="

NJ_DATA = load_json_data("json/NJ_Data.json")
COUNTY_LIST = sorted(list(NJ_DATA.keys()))
COUNTY_MAP = [NJ_DATA[county]['SheriffSale_ID'] for county in COUNTY_LIST if NJ_DATA[county]['SheriffSale_ID'] != '']

SUFFIX_ABBREVATIONS = {
    "Avenue": "Ave",
    "Building": "Bldg",
    "Boulevard": "Blvd",
    "Circle": "Cir",
    "Court": "Ct",
    "Drive": "Dr",
    "East": "E",
    "Lane": "Ln",
    "North": "N",
    "Place": "Pl",
    "Road": "Rd",
    "South": "S",
    "Square": "Sq",
    "Street": "St",
    "Terrace": "Terr",
    "West": "W",
}

ADDRESS_REGEX_SPLIT = [
    "Argyle",  # (Edge Case)
    "Ave",
    "Avenue",
    "Bay",
    "Boardwalk",
    "Boulevard",
    "Circle",
    "Condo",  # (Edge Case)
    "Cove",
    "Croft",
    "Court",
    "Drive",
    "Lane",
    "Highway",
    "Hollow",  # (Edge Case)
    "Mews",  # (Edge Case)
    "Pike",
    "Place",
    "Road",
    "Route [0-9]+",
    "Run",
    "Square",
    "Street",
    "Terrace",
    "Trail",
    "Village",
    "Way",
]

CITY_LIST = [
    "Aberdeen Twp",
    "Absecon",
    "Alexandria Twp",
    "Allamuchy Twp",
    "Allendale",
    "Allenhurst",
    "Allentown",
    "Alloway Twp",
    "Alpha",
    "Alpine",
    "Andover",
    "Andover Twp",
    "Asbury Park City",
    "Atlantic City",
    "Atlantic Highlands",
    "Audubon",
    "Audubon Park",
    "Avalon",
    "Avon-By-The-Sea",
    "Barnegat Light",
    "Barnegat Twp",
    "Barrington",
    "Bass River Twp",
    "Bay Head",
    "Bayonne City",
    "Beach Haven",
    "Beachwood",
    "Bedminster Twp",
    "Belleville Twp",
    "Bellmawr",
    "Belmar",
    "Belvidere Town",
    "Bergenfield",
    "Berkeley Heights Twp",
    "Berkeley Twp",
    "Berlin",
    "Berlin Twp",
    "Bernards Twp",
    "Bernardsville",
    "Bethlehem Twp",
    "Beverly City",
    "Blairstown Twp",
    "Bloomfield Twp",
    "Bloomingdale",
    "Bloomsbury",
    "Bogota",
    "Boonton Town",
    "Boonton Twp",
    "Bordentown City",
    "Bordentown Twp",
    "Bound Brook",
    "Bradley Beach",
    "Branchburg Twp",
    "Branchville",
    "Brick Twp",
    "Bridgeton City",
    "Bridgewater Twp",
    "Brielle",
    "Brigantine",
    "Brooklawn",
    "Buena",
    "Buena Borough",
    "Buena Vista Township",
    "Burlington City",
    "Burlington Twp",
    "Butler",
    "Byram Twp",
    "Caldwell",
    "Califon",
    "Camden City",
    "Cape May City",
    "Cape May Point",
    "Carlstadt",
    "Carneys Point Twp",
    "Carteret",
    "Cedar Grove Twp",
    "Chatham",
    "Chatham Twp",
    "Cherry Hill Twp",
    "Chesilhurst",
    "Chester",
    "Chester Twp",
    "Chesterfield Twp",
    "Cinnaminson Twp",
    "City Of Orange Twp",
    "Clark Twp",
    "Clayton",
    "Clementon",
    "Cliffside Park",
    "Clifton City",
    "Clinton Town",
    "Clinton Twp",
    "Closter",
    "Closter",
    "Collingswood",
    "Colts Neck Twp",
    "Commercial Twp",
    "Corbin City",
    "Cranbury Twp",
    "Cranford Twp",
    "Cresskill",
    "Deal",
    "Deerfield Twp",
    "Delanco Twp",
    "Delaware Twp",
    "Delran Twp",
    "Demarest",
    "Dennis Twp",
    "Denville Twp",
    "Deptford Twp",
    "Dover Town",
    "Downe Twp",
    "Dumont",
    "Dunellen",
    "Eagleswood Twp",
    "East Amwell Twp",
    "East Brunswick Twp",
    "East Greenwich Twp",
    "East Hanover Twp",
    "East Newark",
    "East Orange City",
    "East Rutherford",
    "East Windsor Twp",
    "Eastampton Twp",
    "Eatontown",
    "Edgewater",
    "Edgewater",
    "Edgewater Park Twp",
    "Edison Twp",
    "Egg Harbor City",
    "Egg Harbor Twp",
    "Egg Harbor Township",
    "Elizabeth",
    "Elk Twp",
    "Elmer",
    "Elmwood Park",
    "Elsinboro Twp",
    "Emerson",
    "Englewood",
    "Englewood City",
    "Englewood Cliffs",
    "Englishtown",
    "Essex Fells",
    "Estell Manor",
    "Evesham Twp",
    "Ewing Twp",
    "Fair Haven",
    "Fair Lawn",
    "Fairfield Twp",
    "Fair Lawn",
    "Fairview",
    "Fanwood",
    "Far Hills",
    "Farmingdale",
    "Fieldsboro",
    "Flemington",
    "Florence Twp",
    "Florham Park",
    "Folsom",
    "Fort Lee",
    "Frankford Twp",
    "Franklin",
    "Franklin Lakes",
    "Franklin Lakes",
    "Franklin Twp",
    "Fredon Twp",
    "Freehold",
    "Freehold Twp",
    "Frelinghuysen Twp",
    "Frenchtown",
    "Galloway",
    "Galloway Twp",
    "Galloway Township",
    "Garfield",
    "Garfield City",
    "Garwood",
    "Gibbsboro",
    "Glassboro",
    "Glen Gardner",
    "Glen Ridge",
    "Glen Rock",
    "Gloucester City",
    "Gloucester Twp",
    "Green Brook Twp",
    "Green Twp",
    "Greenwich Twp",
    "Guttenberg Town",
    "Hackensack",
    "Hackensack City",
    "Hackettstown Town",
    "Haddon Heights",
    "Haddon Twp",
    "Haddonfield",
    "Hainesport Twp",
    "Haledon",
    "Hamburg",
    "Hamilton Twp",
    "Hamilton Township",
    "Hammonton",
    "Hampton",
    "Hampton Twp",
    "Hanover Twp",
    "Harding Twp",
    "Hardwick Twp",
    "Hardyston Twp",
    "Harmony Twp",
    "Harrington Park",
    "Harrison Town",
    "Harrison Twp",
    "Harvey Cedars",
    "Hasbrouck Heights",
    "Hasbrouck Heights",
    "Haworth",
    "Hawthorne",
    "Hazlet Twp",
    "Helmetta",
    "Hi-Nella",
    "High Bridge",
    "Highland Park",
    "Highlands",
    "Hightstown",
    "Hillsborough Twp",
    "Hillsdale",
    "Hillside Twp",
    "Ho-Ho-Kus",
    "Hoboken City",
    "Holland Twp",
    "Holmdel Twp",
    "Hopatcong",
    "Hope Twp",
    "Hopewell",
    "Hopewell Twp",
    "Howell Twp",
    "Independence Twp",
    "Interlaken",
    "Irvington Twp",
    "Island Heights",
    "Jackson Twp",
    "Jamesburg",
    "Jefferson Twp",
    "Jersey City",
    "Keansburg",
    "Kearny Town",
    "Kenilworth",
    "Keyport",
    "Kingwood Twp",
    "Kinnelon",
    "Knowlton Twp",
    "Lacey Twp",
    "Lafayette Twp",
    "Lake Como",
    "Lakehurst",
    "Lakewood Twp",
    "Lambertville City",
    "Laurel Springs",
    "Lavallette",
    "Lawnside",
    "Lawrence Twp",
    "Lebanon",
    "Lebanon Twp",
    "Leonia",
    "Liberty Twp",
    "Lincoln Park",
    "Linden",
    "Lindenwold",
    "Linwood",
    "Little Egg Harbor Twp",
    "Little Falls Twp",
    "Little Ferry",
    "Little Silver",
    "Livingston Twp",
    "Loch Arbour Village",
    "Lodi",
    "Logan Twp",
    "Long Beach Twp",
    "Long Branch City",
    "Long Hill Twp",
    "Longport",
    "Lopatcong Twp",
    "Lower Alloways Creek Twp",
    "Lower Twp",
    "Lumberton Twp",
    "Lyndhurst",
    "Lyndhurst Twp",
    "Madison",
    "Magnolia",
    "Mahwah",
    "Mahwah Twp",
    "Manalapan Twp",
    "Manasquan",
    "Manchester Twp",
    "Mannington Twp",
    "Mansfield Twp",
    "Mantoloking",
    "Mantua Twp",
    "Manville",
    "Maple Shade Twp",
    "Maplewood Twp",
    "Margate",
    "Margate City",
    "Marlboro Twp",
    "Matawan",
    "Maurice River Twp",
    "Mays Landing",
    "Maywood",
    "Medford Lakes",
    "Medford Twp",
    "Mendham",
    "Mendham Twp",
    "Merchantville",
    "Metuchen",
    "Middle Twp",
    "Middlesex",
    "Middletown Twp",
    "Midland Park",
    "Milford",
    "Milford",
    "Millburn Twp",
    "Millstone",
    "Millstone Twp",
    "Milltown",
    "Millville City",
    "Mine Hill Twp",
    "Minotola",
    "Monmouth Beach",
    "Monroe Twp",
    "Montague Twp",
    "Montclair Twp",
    "Montgomery Twp",
    "Montvale",
    "Montville Twp",
    "Moonachie",
    "Moorestown Twp",
    "Morris Plains",
    "Morris Twp",
    "Morristown Town",
    "Mount Arlington",
    "Mount Ephraim",
    "Mount Holly Twp",
    "Mount Laurel Twp",
    "Mount Olive Twp",
    "Mountain Lakes",
    "Mountainside",
    "Mullica Township",
    "National Park",
    "Neptune City",
    "Neptune Twp",
    "Netcong",
    "Newtonville",
    "New Brunswick City",
    "New Hanover Twp",
    "New Milford",
    "New Providence",
    "Newark City",
    "Newfield",
    "Newton Town",
    "North Arlington",
    "North Bergen Twp",
    "North Brunswick Twp",
    "North Caldwell",
    "North Haledon",
    "North Hanover Twp",
    "North Plainfield",
    "North Wildwood City",
    "Northfield",
    "Northvale",
    "Norwood",
    "Nutley Twp",
    "Oakland",
    "Oaklyn",
    "Ocean City",
    "Ocean Gate",
    "Ocean Twp",
    "Oceanport",
    "Ogdensburg",
    "Old Bridge Twp",
    "Old Tappan",
    "Oldmans Twp",
    "Oradell",
    "Oxford Twp",
    "Palisades Park",
    "Palmyra",
    "Paramus",
    "Park Ridge",
    "Parsippany-Troy Hills Twp",
    "Passaic City",
    "Paterson City",
    "Paulsboro",
    "Peapack-Gladstone",
    "Pemberton",
    "Pemberton Twp",
    "Pennington",
    "Penns Grove",
    "Pennsauken Twp",
    "Pennsville Twp",
    "Pequannock Twp",
    "Perth Amboy City",
    "Phillipsburg Town",
    "Pilesgrove Twp",
    "Pine Beach",
    "Pine Hill",
    "Pine Valley",
    "Piscataway Twp",
    "Pitman",
    "Pittsgrove Twp",
    "Plainfield City",
    "Plainsboro Twp",
    "Pleasantville",
    "Plumsted Twp",
    "Pohatcong Twp",
    "Point Pleasant Beach",
    "Point Pleasant",
    "Pompton Lakes",
    "Port Republic",
    "Princeton",
    "Prospect Park",
    "Quinton Twp",
    "Rahway City",
    "Ramsey",
    "Randolph Twp",
    "Raritan",
    "Raritan Twp",
    "Readington Twp",
    "Red Bank",
    "Ridgefield",
    "Ridgefield Park",
    "Ridgefield Park Village",
    "Ridgewood",
    "Ridgewood Village",
    "Ringwood",
    "River Edge",
    "River Vale",
    "River Vale Twp",
    "Riverdale",
    "Riverside Twp",
    "Riverton",
    "Robbinsville Twp",
    "Rochelle Park",
    "Rochelle Park Twp",
    "Rockaway",
    "Rockaway Twp",
    "Rockleigh",
    "Rocky Hill",
    "Roosevelt",
    "Roseland",
    "Roselle",
    "Roselle Park",
    "Roxbury Twp",
    "Rumson",
    "Runnemede",
    "Rutherford",
    "Rutherford",
    "Saddle Brook",
    "Saddle Brook Twp",
    "Saddle River",
    "Salem City",
    "Sandyston Twp",
    "Sayreville",
    "Scotch Plains Twp",
    "Sea Bright",
    "Sea Girt",
    "Sea Isle City",
    "Seaside Heights",
    "Seaside Park",
    "Secaucus Town",
    "Shamong Twp",
    "Shiloh",
    "Ship Bottom",
    "Shrewsbury",
    "Shrewsbury Twp",
    "Somerdale",
    "Somers Point",
    "Somerville",
    "South Amboy City",
    "South Bound Brook",
    "South Brunswick Twp",
    "South Hackensack Twp",
    "South Harrison Twp",
    "South Orange Village Twp",
    "South Plainfield",
    "South River",
    "South Toms River",
    "Southampton Twp",
    "Sparta Twp",
    "Spotswood",
    "Spring Lake",
    "Spring Lake Heights",
    "Springfield Twp",
    "Stafford Twp",
    "Stanhope",
    "Stillwater Twp",
    "Stockton",
    "Stone Harbor",
    "Stow Creek Twp",
    "Stratford",
    "Summit",
    "Surf City",
    "Sussex",
    "Swedesboro",
    "Sweetwater",
    "Tabernacle Twp",
    "Tavistock",
    "Teaneck",
    "Teaneck Twp",
    "Tenafly",
    "Teterboro",
    "Tewksbury Twp",
    "Tinton Falls",
    "Toms River Twp",
    "Totowa",
    "Trenton City",
    "Tuckerton",
    "Union",
    "Union Beach",
    "Union Twp",
    "Upper Deerfield Twp",
    "Upper Freehold Twp",
    "Upper Pittsgrove Twp",
    "Upper Saddle River",
    "Upper Twp",
    "Ventnor City",
    "Vernon Twp",
    "Verona Twp",
    "Victory Gardens",
    "Vineland City",
    "Voorhees Twp",
    "Waldwick",
    "Wall Twp",
    "Wallington",
    "Walpack Twp",
    "Wanaque",
    "Wantage Twp",
    "Warren Twp",
    "Washington",
    "Washington Twp",
    "Washington Township",
    "Watchung",
    "Waterford Twp",
    "Wayne Twp",
    "Weehawken Twp",
    "Wenonah",
    "West Amwell Twp",
    "West Caldwell Twp",
    "West Cape May",
    "West Deptford Twp",
    "West Long Branch",
    "West Milford Twp",
    "West New York Town",
    "West Orange Twp",
    "West Wildwood",
    "West Windsor Twp",
    "Westampton Twp",
    "Westfield Town",
    "Westville",
    "Westwood",
    "Weymouth Twp",
    "Wharton",
    "White Twp",
    "Wildwood City",
    "Wildwood Crest",
    "Williamstown",
    "Willingboro Twp",
    "Winfield Twp",
    "Winslow Twp",
    "Wood Ridge",
    "Woodbine",
    "Woodbridge Twp",
    "Woodbury City",
    "Woodbury Heights",
    "Woodcliff Lake",
    "Woodland Park",
    "Woodland Twp",
    "Woodlynne",
    "Woodstown",
    "Woolwich Twp",
    "Wrightstown",
    "Wyckoff",
    "Wyckoff Twp",
]

CITY_LIST_SANITIZED = {
    "Atlanic City": "Atlantic City",
    "Buena": "Buena",
    "Buena Borough": "Buena",
    "Margate City": "Margate",
    "Pomona": "Galloway Township",
}
