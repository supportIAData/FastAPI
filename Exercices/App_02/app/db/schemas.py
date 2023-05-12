from datetime import date
from typing import Union
from pydantic import BaseModel


class CaseBase(BaseModel):
    name: str
    active: bool


class CaseCreate(CaseBase):
    pass


class Case(CaseBase):
    id: int

    # class Config:
    #     orm_mode = True


# Schéma pour les données de https://disease.sh/v3/covid-19/countries
class CovidByCountrySchema(BaseModel):
    country: str
    cases: int
    deaths: int
    recovered: int
    active: Union[int, bool]
    population: int
    continent: str
    updated: int


# Schéma pour les données de https://covid.ourworldindata.org/data/owid-covid-data.csv
class CovidWorldwideSchema(BaseModel):
    iso_code: str
    continent: Union[str, None]
    location: str
    date: date
    total_cases: Union[int, None]
    new_cases: Union[int, None]
    new_cases_smoothed: Union[float, None]
    total_deaths: Union[int, None]
    new_deaths: Union[int, None]
    new_deaths_smoothed: Union[float, None]
    total_cases_per_million: Union[float, None]
    new_cases_per_million: Union[float, None]
    new_cases_smoothed_per_million: Union[float, None]
    total_deaths_per_million: Union[float, None]
    new_deaths_per_million: Union[float, None]
    new_deaths_smoothed_per_million: Union[float, None]
    reproduction_rate: Union[float, None]
    icu_patients: Union[int, None]
    icu_patients_per_million: Union[float, None]
    hosp_patients: Union[int, None]
    hosp_patients_per_million: Union[float, None]
    weekly_icu_admissions: Union[float, None]
    weekly_icu_admissions_per_million: Union[float, None]
    weekly_hosp_admissions: Union[float, None]
    weekly_hosp_admissions_per_million: Union[float, None]
    new_tests: Union[int, None]
    total_tests: Union[int, None]
    total_tests_per_thousand: Union[float, None]
    new_tests_per_thousand: Union[float, None]
    new_tests_smoothed: Union[int, None]
    new_tests_smoothed_per_thousand: Union[float, None]
    positive_rate: Union[float, None]
    tests_per_case: Union[float, None]
    tests_units: str
    total_vaccinations: Union[int, None]
    people_vaccinated: Union[int, None]
    people_fully_vaccinated: Union[Union[int, None]]
    new_vaccinations: Union[int, None]
    new_vaccinations_smoothed: Union[int, None]
    new_vaccinations_smoothed_per_million: Union[float, None]
    total_vaccinations_per_hundred: Union[float, None]
    people_vaccinated_per_hundred: Union[float, None]
    people_fully_vaccinated_per_hundred: Union[float, None]
    stringency_index: Union[float, None]
    population: Union[int, None]
    population_density: Union[float, None]
    median_age: Union[float, None]
    aged_65_older: Union[float, None]
    aged_70_older: Union[float, None]
    gdp_per_capita: Union[float, None]
    extreme_poverty: Union[float, None]
    cardiovasc_death_rate: Union[float, None]
    diabetes_prevalence: Union[float, None]
    female_smokers: Union[float, None]
    male_smokers: Union[float, None]
    handwashing_facilities: Union[float, None]
    hospital_beds_per_thousand: Union[float, None]
    life_expectancy: Union[float, None]
    human_development_index: Union[float, None]
