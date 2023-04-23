# Kalkulator kredytowy

oprocentowanie_kredytu = float(input("podaj oprocentowanie kredytu"))


kwota_kredytu = int(input("podaj kwotę kredytu"))


rata_kredytu = float(input("podaj stałą wartość raty kredytu"))


szablon = "{miesiac} \n Twoja pozostała kwota kredytu to {zadluzenie}, to {roznica} mniej niż w poprzednim miesiącu"


Inflacja_1 = 1.59282448436825
Inflacja_2 = -0.453509101198007
Inflacja_3 = 2.32467171712441
Inflacja_4 = 1.26125440724877
Inflacja_5 = 1.78252628571251
Inflacja_6 = 2.32938454145522
Inflacja_7 = 1.50222984223283
Inflacja_8 = 1.78252628571251
Inflacja_9 = 2.32884899407637
Inflacja_10 = 0.616921348207244
Inflacja_11 = 2.35229588637833
Inflacja_12 = 0.337779545187098
Inflacja_13 = 1.57703524727525
Inflacja_14 = -0.292781442607648
Inflacja_15 = 2.48619659017508
Inflacja_16 = 0.267110317834564
Inflacja_17 = 1.41795267229799
Inflacja_18 = 1.05424326726375
Inflacja_19 = 1.4805201044812
Inflacja_20 = 1.57703524727525
Inflacja_21 = -0.077420690314702
Inflacja_22 = 1.16573339872354
Inflacja_23 = -0.404186717638335
Inflacja_24 = 1.49970852083123







pozostala_kwota_kredytu_1 = (1 + ((Inflacja_1 + oprocentowanie_kredytu)/1200)) * kwota_kredytu - rata_kredytu
pozostala_kwota_kredytu_2 = (1 + ((Inflacja_2 + oprocentowanie_kredytu)/1200)) * pozostala_kwota_kredytu_1 - rata_kredytu
pozostala_kwota_kredytu_3 = (1 + ((Inflacja_3 + oprocentowanie_kredytu)/1200)) * pozostala_kwota_kredytu_2 - rata_kredytu
pozostala_kwota_kredytu_4 = (1 + ((Inflacja_4 + oprocentowanie_kredytu)/1200)) * pozostala_kwota_kredytu_3 - rata_kredytu
pozostala_kwota_kredytu_5 = (1 + ((Inflacja_5 + oprocentowanie_kredytu)/1200)) * pozostala_kwota_kredytu_4 - rata_kredytu
pozostala_kwota_kredytu_6 = (1 + ((Inflacja_6 + oprocentowanie_kredytu)/1200)) * pozostala_kwota_kredytu_5 - rata_kredytu
pozostala_kwota_kredytu_7 = (1 + ((Inflacja_7 + oprocentowanie_kredytu)/1200)) * pozostala_kwota_kredytu_6 - rata_kredytu
pozostala_kwota_kredytu_8 = (1 + ((Inflacja_8 + oprocentowanie_kredytu)/1200)) * pozostala_kwota_kredytu_7 - rata_kredytu
pozostala_kwota_kredytu_9 = (1 + ((Inflacja_9 + oprocentowanie_kredytu)/1200)) * pozostala_kwota_kredytu_8 - rata_kredytu
pozostala_kwota_kredytu_10 = (1 + ((Inflacja_10 + oprocentowanie_kredytu)/1200)) * pozostala_kwota_kredytu_9 - rata_kredytu
pozostala_kwota_kredytu_11=(1 + ((Inflacja_11 + oprocentowanie_kredytu)/1200)) * pozostala_kwota_kredytu_10 - rata_kredytu
pozostala_kwota_kredytu_12=(1 + ((Inflacja_12 + oprocentowanie_kredytu)/1200)) * pozostala_kwota_kredytu_11 - rata_kredytu
pozostala_kwota_kredytu_13=(1 + ((Inflacja_13 + oprocentowanie_kredytu)/1200)) * pozostala_kwota_kredytu_12 - rata_kredytu
pozostala_kwota_kredytu_14=(1 + ((Inflacja_14 + oprocentowanie_kredytu)/1200)) * pozostala_kwota_kredytu_13 - rata_kredytu
pozostala_kwota_kredytu_15=(1 + ((Inflacja_15 + oprocentowanie_kredytu)/1200)) * pozostala_kwota_kredytu_14 - rata_kredytu
pozostala_kwota_kredytu_16=(1 + ((Inflacja_16 + oprocentowanie_kredytu)/1200)) * pozostala_kwota_kredytu_15 - rata_kredytu
pozostala_kwota_kredytu_17=(1 + ((Inflacja_17 + oprocentowanie_kredytu)/1200)) * pozostala_kwota_kredytu_16 - rata_kredytu
pozostala_kwota_kredytu_18=(1 + ((Inflacja_18 + oprocentowanie_kredytu)/1200)) * pozostala_kwota_kredytu_17 - rata_kredytu
pozostala_kwota_kredytu_19=(1 + ((Inflacja_19 + oprocentowanie_kredytu)/1200)) * pozostala_kwota_kredytu_18 - rata_kredytu
pozostala_kwota_kredytu_20=(1 + ((Inflacja_20 + oprocentowanie_kredytu)/1200)) * pozostala_kwota_kredytu_19 - rata_kredytu
pozostala_kwota_kredytu_21=(1 + ((Inflacja_21 + oprocentowanie_kredytu)/1200)) * pozostala_kwota_kredytu_20 - rata_kredytu
pozostala_kwota_kredytu_22=(1 + ((Inflacja_22 + oprocentowanie_kredytu)/1200)) * pozostala_kwota_kredytu_21 - rata_kredytu
pozostala_kwota_kredytu_23=(1 + ((Inflacja_23 + oprocentowanie_kredytu)/1200)) * pozostala_kwota_kredytu_22 - rata_kredytu
pozostala_kwota_kredytu_24=(1 + ((Inflacja_24 + oprocentowanie_kredytu)/1200)) * pozostala_kwota_kredytu_23 - rata_kredytu




roznica_od_ostatniej_kwoty_kredytu_1 = rata_kredytu-pozostala_kwota_kredytu_1
roznica_od_ostatniej_kwoty_kredytu_2 = pozostala_kwota_kredytu_1 - pozostala_kwota_kredytu_2
roznica_od_ostatniej_kwoty_kredytu_3 = pozostala_kwota_kredytu_2 - pozostala_kwota_kredytu_3
roznica_od_ostatniej_kwoty_kredytu_4 = pozostala_kwota_kredytu_3 - pozostala_kwota_kredytu_4
roznica_od_ostatniej_kwoty_kredytu_5 = pozostala_kwota_kredytu_4 - pozostala_kwota_kredytu_5
roznica_od_ostatniej_kwoty_kredytu_6 = pozostala_kwota_kredytu_5 - pozostala_kwota_kredytu_6
roznica_od_ostatniej_kwoty_kredytu_7 = pozostala_kwota_kredytu_6 - pozostala_kwota_kredytu_7
roznica_od_ostatniej_kwoty_kredytu_8 = pozostala_kwota_kredytu_7 - pozostala_kwota_kredytu_8
roznica_od_ostatniej_kwoty_kredytu_9 = pozostala_kwota_kredytu_8 - pozostala_kwota_kredytu_9
roznica_od_ostatniej_kwoty_kredytu_10 = pozostala_kwota_kredytu_9 - pozostala_kwota_kredytu_10
roznica_od_ostatniej_kwoty_kredytu_11 = pozostala_kwota_kredytu_10 - pozostala_kwota_kredytu_11
roznica_od_ostatniej_kwoty_kredytu_12 = pozostala_kwota_kredytu_11 - pozostala_kwota_kredytu_12
roznica_od_ostatniej_kwoty_kredytu_13 = pozostala_kwota_kredytu_12 - pozostala_kwota_kredytu_13
roznica_od_ostatniej_kwoty_kredytu_14 = pozostala_kwota_kredytu_13 - pozostala_kwota_kredytu_14
roznica_od_ostatniej_kwoty_kredytu_15 = pozostala_kwota_kredytu_14 - pozostala_kwota_kredytu_15
roznica_od_ostatniej_kwoty_kredytu_16 = pozostala_kwota_kredytu_15 - pozostala_kwota_kredytu_16
roznica_od_ostatniej_kwoty_kredytu_17 = pozostala_kwota_kredytu_16 - pozostala_kwota_kredytu_17
roznica_od_ostatniej_kwoty_kredytu_18 = pozostala_kwota_kredytu_17 - pozostala_kwota_kredytu_18
roznica_od_ostatniej_kwoty_kredytu_19 = pozostala_kwota_kredytu_18 - pozostala_kwota_kredytu_19
roznica_od_ostatniej_kwoty_kredytu_20 = pozostala_kwota_kredytu_19 - pozostala_kwota_kredytu_20
roznica_od_ostatniej_kwoty_kredytu_21 = pozostala_kwota_kredytu_20 - pozostala_kwota_kredytu_21
roznica_od_ostatniej_kwoty_kredytu_22 = pozostala_kwota_kredytu_21 - pozostala_kwota_kredytu_22
roznica_od_ostatniej_kwoty_kredytu_23 = pozostala_kwota_kredytu_22 - pozostala_kwota_kredytu_23
roznica_od_ostatniej_kwoty_kredytu_24 = pozostala_kwota_kredytu_23 - pozostala_kwota_kredytu_24







miesiac = "Styczeń"
print(szablon.format(miesiac = miesiac, zadluzenie = pozostala_kwota_kredytu_1, roznica = roznica_od_ostatniej_kwoty_kredytu_1))

miesiac = "Luty"
print(szablon.format(miesiac = miesiac, zadluzenie = pozostala_kwota_kredytu_2, roznica = roznica_od_ostatniej_kwoty_kredytu_2))


miesiac = "Marzec"
print(szablon.format(miesiac = miesiac, zadluzenie = pozostala_kwota_kredytu_3, roznica = roznica_od_ostatniej_kwoty_kredytu_3))


miesiac = "Kwiecień"
print(szablon.format(miesiac = miesiac, zadluzenie = pozostala_kwota_kredytu_4, roznica = roznica_od_ostatniej_kwoty_kredytu_4))


miesiac = "Maj"
print(szablon.format(miesiac = miesiac, zadluzenie = pozostala_kwota_kredytu_5, roznica = roznica_od_ostatniej_kwoty_kredytu_5))


miesiac = "Czerwiec"
print(szablon.format(miesiac = miesiac, zadluzenie = pozostala_kwota_kredytu_6, roznica = roznica_od_ostatniej_kwoty_kredytu_6))


miesiac = "lipiec"
print(szablon.format(miesiac = miesiac, zadluzenie = pozostala_kwota_kredytu_7, roznica = roznica_od_ostatniej_kwoty_kredytu_7))


miesiac = "Sierpień"
print(szablon.format(miesiac = miesiac, zadluzenie = pozostala_kwota_kredytu_8, roznica = roznica_od_ostatniej_kwoty_kredytu_8))


miesiac = "Wrzesień"
print(szablon.format(miesiac = miesiac, zadluzenie = pozostala_kwota_kredytu_9, roznica = roznica_od_ostatniej_kwoty_kredytu_9))

miesiac = "Październik"
print(szablon.format(miesiac = miesiac, zadluzenie = pozostala_kwota_kredytu_10, roznica = roznica_od_ostatniej_kwoty_kredytu_10))

miesiac = "Listopad"
print(szablon.format(miesiac = miesiac, zadluzenie = pozostala_kwota_kredytu_11, roznica = roznica_od_ostatniej_kwoty_kredytu_11))

miesiac = "Grudzień"
print(szablon.format(miesiac = miesiac, zadluzenie = pozostala_kwota_kredytu_12, roznica = roznica_od_ostatniej_kwoty_kredytu_12))

miesiac = "Styczeń"
print(szablon.format(miesiac = miesiac, zadluzenie = pozostala_kwota_kredytu_13, roznica = roznica_od_ostatniej_kwoty_kredytu_13))

miesiac = "Luty"
print(szablon.format(miesiac = miesiac, zadluzenie = pozostala_kwota_kredytu_14, roznica = roznica_od_ostatniej_kwoty_kredytu_14))

miesiac = "Marzec"
print(szablon.format(miesiac = miesiac, zadluzenie = pozostala_kwota_kredytu_15, roznica = roznica_od_ostatniej_kwoty_kredytu_15))

miesiac = "Kwiecień"
print(szablon.format(miesiac = miesiac, zadluzenie = pozostala_kwota_kredytu_16, roznica = roznica_od_ostatniej_kwoty_kredytu_16))

miesiac = "Maj"
print(szablon.format(miesiac = miesiac, zadluzenie = pozostala_kwota_kredytu_17, roznica = roznica_od_ostatniej_kwoty_kredytu_17))

miesiac = "Czerwiec"
print(szablon.format(miesiac = miesiac, zadluzenie = pozostala_kwota_kredytu_18, roznica = roznica_od_ostatniej_kwoty_kredytu_18))

miesiac = "Lipiec"
print(szablon.format(miesiac = miesiac, zadluzenie = pozostala_kwota_kredytu_19, roznica = roznica_od_ostatniej_kwoty_kredytu_19))

miesiac = "Sierpień"
print(szablon.format(miesiac = miesiac, zadluzenie = pozostala_kwota_kredytu_20, roznica = roznica_od_ostatniej_kwoty_kredytu_20))

miesiac = "Wrzesień"
print(szablon.format(miesiac = miesiac, zadluzenie = pozostala_kwota_kredytu_21, roznica = roznica_od_ostatniej_kwoty_kredytu_21))

miesiac = "Październik"
print(szablon.format(miesiac = miesiac, zadluzenie = pozostala_kwota_kredytu_22, roznica = roznica_od_ostatniej_kwoty_kredytu_22))

miesiac = "Listopad"
print(szablon.format(miesiac = miesiac, zadluzenie = pozostala_kwota_kredytu_23, roznica = roznica_od_ostatniej_kwoty_kredytu_23))

miesiac = "Grudzień"
print(szablon.format(miesiac = miesiac, zadluzenie = pozostala_kwota_kredytu_24, roznica = roznica_od_ostatniej_kwoty_kredytu_24))




