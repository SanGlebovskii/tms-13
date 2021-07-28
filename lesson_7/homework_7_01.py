while True:
    n = (int(input('''Выберите вариант перевода единиц измерений:
    1. Дюймы в сантиметры
    2. Сантиметры в дюймы
    3. Мили в километры
    4. Километры в мили
    5. Фунты в килограммы
    6. Килограммы в фунты
    7. Унции в граммы
    8. Граммы в унции
    9. Американский галлон в литры
    10. Английский галлон в литры
    11. Литры в американские галлоны
    12. Литры в английские галлоны
    13. Американская пинта в литры
    14. Английская пинта в литры
    15. Литры в американские пинты  
    16. Литры в английские пинты
    ''')))


    # 1. Дюймы в сантиметры:
    def inch_in_cm(values_SI):
        inch_coeff = 2.54
        cm = values_SI * inch_coeff

        return cm


    # 2. Сантиметры в дюймы:
    def cm_in_inch(values_SI):
        cm_coeff = 0.3937
        inch = values_SI * cm_coeff

        return inch


    # 3. Мили в километры:
    def miles_in_km(values_SI):
        km_coeff = 0.62137
        km = values_SI * km_coeff

        return km


    # 4. Километры в мили:
    def km_in_miles(values_SI):
        miles_coeff = 1.60934
        miles = values_SI * miles_coeff

        return miles


    # 5. Фунты в килограммы:
    def lb_in_kg(values_SI):
        kg_coeff = 0.454
        kg = values_SI * kg_coeff

        return kg


    # 6. Килограммы в фунты:
    def kg_in_lb(values_SI):
        lb_coeff = 2.205
        lb = values_SI * lb_coeff

        return lb


    # 7. Унции в граммы:
    def oz_in_gramm(values_SI):
        gramm_coeff = 28.3495
        gramm = values_SI * gramm_coeff

        return gramm


    # 8. Граммы в унции:
    def gramm_in_oz(values_SI):
        oz_coeff = 0.035
        oz = values_SI * oz_coeff

        return oz


    # 9. Американский галлон в литры:
    def usa_gallon_in_litres(values_SI):
        litr_coeff = 3.7854
        litr = values_SI * litr_coeff

        return litr


    # 10. Английский галлон в литры:
    def brit_gallon_in_litres(values_SI):
        litr_coeff = 4.546
        litr = values_SI * litr_coeff

        return litr


    # 11. Литры в американские галлоны:
    def litr_in_usa_gallon(values_SI):
        usa_gallon_coeff = 0.264
        usa_gallon = values_SI * usa_gallon_coeff

        return usa_gallon


    # 12. Литр в английский галлон:
    def litr_in_brit_gallon(values_SI):
        brit_gallon_coeff = 0.2199688
        brit_gallon = values_SI * brit_gallon_coeff

        return brit_gallon


    # 13. Американская пинта в литры:
    def usa_pint_in_litres(values_SI):
        litr_coeff = 0.47317
        litr = values_SI * litr_coeff

        return litr


    # 14. Английская пинта в литры:
    def brit_pint_in_litres(values_SI):
        litr_coeff = 0.56826
        litr = values_SI * litr_coeff

        return litr


    # 15. Литр в американские пинты:
    def litr_in_usa_pint(values_SI):
        usa_pint_coeff = 2.11337
        usa_pint = values_SI * usa_pint_coeff

        return usa_pint


    # 16. Литр в английскую пинту:
    def litr_in_brit_pint(values_SI):
        brit_pint_coeff = 1.75975
        brit_pint = values_SI * brit_pint_coeff

        return brit_pint

    if n == 0:
        break
    values_SI = int(input('Введите численное значение '))
    if n == 1:
        print(inch_in_cm(values_SI), 'сантиметров')
    elif n == 2:
        print(cm_in_inch(values_SI), 'дюймов')
    elif n == 3:
        print(miles_in_km(values_SI), 'километров')
    elif n == 4:
        print(km_in_miles(values_SI), 'миль')
    elif n == 5:
        print(lb_in_kg(values_SI), 'килограмм')
    elif n == 6:
        print(kg_in_lb(values_SI), 'фунт')
    elif n == 7:
        print(oz_in_gramm(values_SI), 'грамм')
    elif n == 8:
        print(gramm_in_oz(values_SI), 'унций')
    elif n == 9:
        print(usa_gallon_in_litres(values_SI), 'литров')
    elif n == 10:
        print(brit_gallon_in_litres(values_SI), 'литров')
    elif n == 11:
        print(litr_in_usa_gallon(values_SI), 'американских галлонов')
    elif n == 12:
        print(litr_in_brit_gallon(values_SI), 'английских галлонов')
    elif n == 13:
        print(usa_pint_in_litres(values_SI), 'литров')
    elif n == 14:
        print(brit_pint_in_litres(values_SI), 'литров')
    elif n == 15:
        print(litr_in_usa_pint(values_SI), 'американских пинт')
    elif n == 16:
        print(litr_in_brit_pint(values_SI), 'британских пинт')

