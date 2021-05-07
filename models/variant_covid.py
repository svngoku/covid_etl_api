def variant_covid_helper(vaccine_covid_data):
    return {
        "id": str(vaccine_covid_data["_id"]),
        "country": vaccine_covid_data["country"],
        "country_code": vaccine_covid_data["country_code"],
        "year_week": vaccine_covid_data["year_week"],
        "new_cases": vaccine_covid_data["new_cases"],
        "valid_denominator": vaccine_covid_data["valid_denominator"],
        "variant": vaccine_covid_data["variant"],
        "number_detections_variant": vaccine_covid_data["number_detections_variant"]
    }