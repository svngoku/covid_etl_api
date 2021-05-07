def africa_covid_data_helper(africa_covid_data):
    return {
        "id": str(africa_covid_data["_id"]),
        "Pays": africa_covid_data["Pays"],
        "Nombre de cas detectes": africa_covid_data["Nombre de cas detectes"],
        "Nombre de deces": africa_covid_data["Nombre de deces"]
    }