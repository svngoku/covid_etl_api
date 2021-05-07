def vaccine_covid_helper(vaccine_covid_data):
    return {
        "id": str(vaccine_covid_data["_id"]),
        "YearWeekISO": vaccine_covid_data["YearWeekISO"],
        "FirstDose": vaccine_covid_data["FirstDose"],
        "UnknownDose": vaccine_covid_data["UnknownDose"],
        "Region": vaccine_covid_data["Region"],
        "Population": vaccine_covid_data["Population"],
        "Vaccine": vaccine_covid_data["Vaccine"],
        "TargetGroup": vaccine_covid_data["TargetGroup"]
    }