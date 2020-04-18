from flask import (
    render_template,
    url_for,
    request,
    redirect,
    session,
    make_response,
    jsonify,
)
from app import app, db
from app.models import SheriffSaleDB

from .scrapers.sheriff_sale import SheriffSale
from .scrapers.constants import COUNTY_LIST, CITY_LIST, NJ_DATA
from settings import FLASK_APP_DIR

import json
import os
import time
from urllib.parse import urlencode

sheriff_sale = SheriffSale("15")

@app.route("/api/home", methods=["GET"])
def home():
    db_path = FLASK_APP_DIR.joinpath("main.db")
    db_mod_date = time.ctime(os.path.getmtime(db_path))

    counties = COUNTY_LIST
    cities = CITY_LIST
    nj_data = NJ_DATA
    sale_dates = sheriff_sale.get_sale_dates()

    if request.method == "GET":
        return jsonify(
            dbModDate=db_mod_date,
            counties=counties,
            cities=cities,
            saleDates=sale_dates,
            NJData=nj_data
        )


@app.route("/api/check_for_update")
def check_for_update(methods=["POST"]):
    # 1) Get the sheriff id's currently on the website
    sheriff_sale_ids_current = sheriff_sale.get_sheriff_ids()

    # 2) Query the db to get all the sheriff id's in the db
    sheriff_sale_ids_db = SheriffSaleDB.query.with_entities(SheriffSaleDB.sheriff).all()

    # 3) Check for any differences in between
    difference = list(set(sheriff_sale_ids_current) - set(sheriff_sale_ids_db))

    return jsonify(difference)


@app.route("/api/update_database")
def update_database(methods=["GET", "POST", "PUT"]):
    # if request.method == "POST":
    sheriff_sale_data = sheriff_sale.sheriff_sale_dict()

    # for row in sheriff_sale_data:
    #     _sheriff_sale_data = SheriffSaleDB(
    #         sheriff=row.listing_details.sheriff,
    #         court_case=row.listing_details.court_case,
    #         sale_date=row.listing_details.sale_date,
    #         plaintiff=row.listing_details.plaintiff,
    #         defendant=row.listing_details.defendant,
    #         address=row.listing_details.address,
    #         priors=row.listing_details.priors,
    #         attorney=row.listing_details.attorney,
    #         judgment=row.listing_details.judgment,
    #         deed=row.listing_details.deed,
    #         deed_address=row.listing_details.deed_address,
    #         maps_url=row.maps_url,
    #         address_sanitized=row.sanitized.address,
    #         unit=row.sanitized.unit,
    #         secondary_unit=row.sanitized.secondary_unit,
    #         city=row.sanitized.city,
    #         zip_code=row.sanitized.zip_code,
    #     )
    #     db.session.add(_sheriff_sale_data)
    #     db.session.commit()

    return (
        jsonify(
            {
                "message": "Sheriff Sale Database Successfully Updated",
                "data": sheriff_sale_data,
            }
        ),
        200,
    )


# else:
#     return jsonify({'Updating the Sheriff Sale Database Failed'}), 401


@app.route("/api/table_data", methods=["POST"])
def table_data():
    data = request.get_json()
    print(data)

    query = SheriffSaleDB.query
    if data:
        for req in data:
            if data[req]:
                query = query.filter(getattr(SheriffSaleDB, req) == data[req])
                # query = query.order_by(SheriffSaleDB.city.asc()).all()

        return jsonify([i.serialize for i in query.all()])
    else:
        return jsonify({"message": "Data is null"})