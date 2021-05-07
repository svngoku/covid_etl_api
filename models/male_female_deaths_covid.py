def male_female_deaths_covid_helper(male_female_deaths_covid_data):
    return {
        "id": str(male_female_deaths_covid_data["_id"]),
        "country": male_female_deaths_covid_data["country"],
        "case_death_data_by_sex": male_female_deaths_covid_data["case_death_data_by_sex"],
        "cases_male": male_female_deaths_covid_data["cases_male"]
    }