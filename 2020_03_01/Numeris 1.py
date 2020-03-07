'''
Turime gamybos liniją

Konvejeriu juda 50 vnt prekių metre su 0.5 m/s greičiu.
Pakuotojai turi jas sudėlioti į dėžes, dėliojimo greitis yra 8 vnt/s.
Dėžės talpa 100vnt.
Pakuotojas pasiekia 1m konvejerio

Užpildžius dėžes, pakuotojas  užtrunka 5min, kad ją užklijuoti
ir padėti ant kito konvejerio.

Parašyti funkciją, kuri apskaičiuotų reikalingą pakuotojų kiekį prie
prekių konvejerio.
'''


def apskaičiuoti_per_sekundę_pasiekiamų_prekių_kiekį(
        prekių_vnt_metre,
        konvejerio_greitis,
        pasiekiamas_plotis
):
    """
​
    :param prekių_vnt_metre: kiek prekių iš pradžių juda viename metre konvejerio diržo
    :param konvejerio_greitis: judėjimo greitis m/s
    :param pasiekiamas_plotis: pakuotojo pasiekiamas plotis, metrais
    :return: kiek vienetų pasiekiama vienam pakuotojui per sekundę
    """
    return prekių_vnt_metre * konvejerio_greitis * pasiekiamas_plotis


def pakuotojo_laikas_vienai_dėžei_supakiuoti(
        dežės_talpa,
        pakavimo_greitis,
        dežės_paruošimo_laikas
):
    """
​
    :param dežės_talpa: vienetai telpantys į dežę
    :param pakavimo_greitis: kiek vienetų per sekundę gali į dežę sudeda pakuotojas
    :param dežės_paruošimo_laikas: kiek laiko užtrunka dežę paruoši perdavimui (sekundėmis)
    :return:
    """
    return dežės_talpa / pakavimo_greitis + dežės_paruošimo_laikas


def apskaičiuoti_vidutinį_pakavimo_greitį(dežės_talpa, bendras_laikas):
    """
​
    :param dežės_talpa:
    :param laikas: kiek užtrunka pririnkti pilną dežę ir ją supakuoti
    :return: vienetų kiekis per sekundę
    """
    return dežės_talpa / bendras_laikas



def apskaičiuoti_pakuotojų_kiekį(pasiekiamas_kiekis, vidutinis_pakavimo_greitis):
    """

    :param pasiekiamas_kiekis: vienetai
    :param vidutinis_pakavimo_greitis: vienetai / sekundę
    :return:
    """
    return pasiekiamas_kiekis / vidutinis_pakavimo_greitis


DĖŽĖS_TALPA = 100
LINIJOS_VIENETŲ_KIEKIS_METRE = 50  # vnt/m
LINIJOS_GREITIS = 0.5   # m/s
PASIEKIAMAS_PLOTIS = 1  # m
PAKUOTOJO_GREITIS = 8  # vnt/s
DEŽĖS_PARUOŠIMO_LAIKAS = 5 * 60  # sekundės

kiekis = apskaičiuoti_per_sekundę_pasiekiamų_prekių_kiekį(LINIJOS_VIENETŲ_KIEKIS_METRE, LINIJOS_GREITIS,
                                                          PASIEKIAMAS_PLOTIS)
laikas = pakuotojo_laikas_vienai_dėžei_supakiuoti(DĖŽĖS_TALPA, PAKUOTOJO_GREITIS, DEŽĖS_PARUOŠIMO_LAIKAS)
vidutinis_greitis = apskaičiuoti_vidutinį_pakavimo_greitį(DĖŽĖS_TALPA, laikas)
pakuotojai = apskaičiuoti_pakuotojų_kiekį(kiekis, vidutinis_greitis)
print(pakuotojai)
