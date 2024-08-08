from chapter_11.city_functions import city_country


def test_city_country():
    city = city_country('santiago', 'chile')
    assert city == "Santiago, Chile"


def test_city_country_population():
    city = city_country('santiago', 'chile', 5000000)
    assert city == "Santiago, Chile - population 5000000"
