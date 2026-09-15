from python.chapter11.city_functions import location

def test_city_country():
    city_country = location("beijing", "china")
    assert city_country == "Beijing, China"

def test_city_country_population():
    city_information = location("santiago", "chile", population = 5000000)
    assert city_information == "Santiago, Chile – population 5000000"