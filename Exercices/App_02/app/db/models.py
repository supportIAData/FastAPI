from typing import Union
from datetime import date
from .database import Base
from pydantic import BaseModel, Field
from sqlalchemy import Boolean, Column, Integer, String
#from sqlalchemy.orm import relationship
# Rename of 01_App and 02_App into App_01 and App_02 to be able to get path to those folders
from FastAPI.Exercices.App_02.app.static.helpers import camel_to_snake


class Case(Base):
    __tablename__ = "cases"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200))
    active = Column(Boolean)


class CovidByCountryModel(BaseModel):
    updated: int
    country: str = Field(..., alias="country_name")
    cases: int
    deaths: int
    recovered: int
    active: Union[int, bool]
    population: int
    continent: str

    class Config:
        # Permet de mapper les noms des attributs aux noms des colonnes de la base de données
        orm_mode = True
        schema_extra = {
            "example": {
                "updated": 1620763895224,
                "country": "Afghanistan",
                "cases": 61755,
                "deaths": 2689,
                "recovered": 54039,
                "active": 5036,
                "population": 39835428,
                "continent": "Asia"
            }
        }


class CovidWorldwideModel(BaseModel):
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
    people_fully_vaccinated: Union[Union[int, None], None]
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

    class Config:
        # Permet de mapper les noms des attributs aux noms des colonnes de la base de données
        orm_mode = True
        # Use underscore_case instead of camelCase for database column names
        alias_generator = camel_to_snake
        # Utilisation du camelCase au lieu du snake_case pour les clés JSON
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "iso_code": "AFG",
                "continent": "Asia",
                "location": "Afghanistan",
                "date": "2021-05-11",
                "total_cases": 62403,
                "new_cases": 188,
                "total_deaths": 2698,
                "new_deaths": 3,
                "total_cases_per_million": 1595.676,
                "new_cases_per_million": 4.791,
                "total_deaths_per_million": 68.793,
                "new_deaths_per_million": 0.077,
                "reproduction_rate": 1.02,
                "icu_patients": None
            }
        }
