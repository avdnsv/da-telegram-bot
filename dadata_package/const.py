AREAS_PARAMS = {
    'general': {'result': 'Общий вид'},
    'country': {
        'country': 'Страна', 'federal_district': 'Федеральный округ',
        'region_with_type': 'Регион', 'region_kladr_id': 'Код региона',
        'area_with_type': 'Район в регионе', 'city_with_type': 'Город',
        'city_area': 'Административный округ', 'city_district_with_type': 'Район города',
        'settlement_with_type': 'Населенный пункт'
    },
    'house': {
        'house_cadnum': 'Кадастровый номер дома', 'street_with_type': 'Улица',
        'house': 'Номер дома', 'block': 'Номер корпуса'
    },
    'flat': {
        'flat_cadnum': 'Кадастровый номер квартиры', 'entrance': 'Подъезд',
        'floor': 'Этаж', 'flat': 'Номер квартиры', 'flat_area': 'Площадь квартиры',
        'flat_price': 'Рыночная стоимость квартиры'
    },
    'geo': {
        'postal_code': 'Индекс', 'timezone': 'Часовой пояс',
        'geo_lat': 'Координаты (широта)', 'geo_lon': 'Координаты (долгота)',
        'metro': 'Ближайшие станции метро'
    }
}

FAKE_RESPONSE = {
    "source": "мск Волхонка, 12", "result": "г Москва, ул Волхонка, д 12",
    "postal_code": "119019", "country": "Россия", "country_iso_code": "RU",
    "federal_district": "Центральный",
    "region_fias_id": "0c5b2444-70a0-4932-980c-b4dc0d3f02b5",
    "region_kladr_id": "7700000000000", "region_iso_code": "RU-MOW",
    "region_with_type": "г Москва", "region_type": "г", "region_type_full": "город",
    "region": "Москва", "area_fias_id": None, "area_kladr_id": None,
    "area_with_type": None, "area_type": None, "area_type_full": None, "area": None,
    "city_fias_id": None, "city_kladr_id": None, "city_with_type": None,
    "city_type": None, "city_type_full": None, "city": None, "city_area": "Центральный",
    "city_district_fias_id": None, "city_district_kladr_id": None,
    "city_district_with_type": "р-н Хамовники", "city_district_type": "р-н",
    "city_district_type_full": "район", "city_district": "Хамовники",
    "settlement_fias_id": None, "settlement_kladr_id": None,
    "settlement_with_type": None, "settlement_type": None, "settlement_type_full": None,
    "settlement": None, "street_fias_id": "7ea17642-e64b-43e9-be6f-d4c7220b5c1c",
    "street_kladr_id": "77000000000101100", "street_with_type": "ул Волхонка",
    "street_type": "ул", "street_type_full": "улица", "street": "Волхонка",
    "house_fias_id": None, "house_kladr_id": None, "house_cadnum": None,
    "house_type": "д", "house_type_full": "дом", "house": "12", "block_type": None,
    "block_type_full": None, "block": None, "entrance": None, "floor": None,
    "flat_fias_id": None, "flat_cadnum": None, "flat_type": None, "flat_type_full": None,
    "flat": None, "flat_area": None, "square_meter_price": None, "flat_price": None,
    "postal_box": None, "fias_id": "7ea17642-e64b-43e9-be6f-d4c7220b5c1c",
    "fias_code": "77000000000000010110000", "fias_level": "7", "fias_actuality_state": "0",
    "kladr_id": "77000000000101100", "capital_marker": "0", "okato": "45286590000",
    "oktmo": "45383000", "tax_office": "7704", "tax_office_legal": "7704",
    "timezone": "UTC+3", "geo_lat": "55.7474236", "geo_lon": "37.6048764",
    "beltway_hit": "IN_MKAD", "beltway_distance": None, "qc_geo": 0, "qc_complete": 10,
    "qc_house": 10, "qc": 0, "unparsed_parts": None, "metro": [{"name": "Кропоткинская",
    "line": "Сокольническая", "distance": 0.2}, {"name": "Боровицкая",
    "line": "Серпуховско-Тимирязевская", "distance": 0.4}, {"name": "Арбатская",
    "line": "Арбатско-Покровская", "distance": 0.6}]
}
