import random

#""" B Y   M E S A B O on June 18 at 21:14:30 """
"""
    B1 : nombre de passagers sur B1
    B2 : nombre de passagers sur B2
    B3 : nombre de passagers sur B3
    B4 : nombre de passagers sur B4
    B5 : nombre de passagers sur B5
    B6 : nombre de passagers sur B6

    P1 : personnel disponible sur le trajet plateau-cocody
    P2 : personnel disponible sur le trajet plateau-treicheville
    P3 : personnel disponible sur le trajet plateau-yopougon


    m1 : Minute du voyage sur le trajet plateau-cocody
    m2 : Minute du voyage sur le trajet plateau-treicheville
    m3 : Minute du voyage sur le trajet plateau-yopougon

    m1_max : Minute maximale de tous les voyages sur le trajet plateau-cocody
    m2_max : Minute maximale de tous les voyages sur le trajet plateau-treicheville
    m3_max : Minute maximale de tous les voyages sur le trajet plateau-yopougon

    t_a : prix du trajet plateau-cocody
    t_b : prix du trajet plateau-treicheville
    t_c : prix du trajet plateau-yopougon

    r_A : recette minimale sur le trajet plateau-cocody par jour
    r_B : recette minimale sur le trajet plateau-treicheville par jour
    r_B : recette minimale sur le trajet plateau-yopougon par jour

    """


def resolution(t_a, t_b, t_c, A1, A2, A3, A4, A5, A6, m1, m2, m3, m1_max, m2_max, m3_max, P1, P2, P3, r_A, r_B, r_C):

    # fonction de determination de solution initiale
    L = []

    def determination():
        s = []
        fin = 1
        while fin == 1:
            n1A = random.randint(1, 20)
            n2A = random.randint(
                int((r_A-((n1A*t_a*A1)+(n1A*t_a*A3)))/(t_a*A2)), int((r_A-((n1A*t_a*A1)+(n1A*t_a*A3)))/(t_a*A2))+10)
            n3A = random.randint(
                int((r_A-((n1A*t_a*A1)+(n1A*t_a*A2)))/(t_a*A3)), int((r_A-((n1A*t_a*A1)+(n1A*t_a*A2)))/(t_a*A3))+10)

            n1B = random.randint(1, 20)
            n2B = random.randint(
                int((r_A-((n1B*t_a*A1)+(n1B*t_a*A3)))/(t_a*A2)), int((r_A-((n1B*t_a*A1)+(n1B*t_a*A3)))/(t_a*A2))+10)
            n3B = random.randint(
                int((r_A-((n1B*t_a*A1)+(n1B*t_a*A2)))/(t_a*A3)), int((r_A-((n1B*t_a*A1)+(n1B*t_a*A2)))/(t_a*A3))+10)

            n1C = random.randint(1, 20)
            n2C = random.randint(
                int((r_A-((n1C*t_a*A1)+(n1C*t_a*A3)))/(t_a*A2)), int((r_A-((n1C*t_a*A1)+(n1C*t_a*A3)))/(t_a*A2))+10)
            n3C = random.randint(
                int((r_A-((n1C*t_a*A1)+(n1C*t_a*A2)))/(t_a*A3)), int((r_A-((n1C*t_a*A1)+(n1C*t_a*A2)))/(t_a*A3))+10)

            if (n1A+n1B+n1C)*m1 <= m1_max and (n2A+n2B+n2C)*m2 <= m2_max and (n3A+n3B+n3C)*m3 <= m3_max:
                s.append(n1A)
                s.append(n2A)
                s.append(n3A)
                s.append(n1B)
                s.append(n2B)
                s.append(n3B)
                s.append(n1C)
                s.append(n2C)
                s.append(n3C)
                fin = 0
            else:
                fin = 1

        print("Solution initiale : ", s)
        return s

    # définition des voisins de s

    def voisin_1(s):
        return [s[0]+1, s[1]+1, s[2]+1, s[3]+1, s[4]+1, s[5]+1]

    def voisin_2(s):
        return [s[1]+1, s[0]+1, s[2]+1, s[3]+1, s[4]+1, s[5]+1]

    def voisin_3(s):
        return [s[1]+1, s[2]+1, s[0]+1,  s[3]+1, s[4]+1, s[5]+1]

    def voisin_4(s):
        return [s[1]+1, s[2]+1, s[3]+1, s[0]+1, s[4]+1, s[5]+1]

    def voisin_5(s):
        return [s[1]+1, s[2]+1, s[3]+1, s[4]+1, s[0]+1, s[5]+1]

    def voisin_6(s):
        return [s[1]+1, s[2]+1, s[3]+1, s[4]+1, s[5]+1, s[0]+1]

    # Définition des fonction objectifs (profit,minute,personnel,aggreatation)

    def profit(s):
        return (s[0]*t_a*A1 + s[1]*t_a*A2 + s[2]*t_a*A3) + (s[0]*t_b*A4 + s[1]*t_b*A5 + s[2]*t_b*A6)

    def duree(s):
        return (s[0]+s[2]+s[3])*m1 + (s[0]+s[1]+s[3])*m2 + (s[0]+s[1]+s[2])*m3

    def personnel(s):
        return (s[0]+s[2]+s[3])*P1 + (s[0]+s[1]+s[3])*P2 + (s[0]+s[1]+s[2])*P3

    def aggregation(s):
        return duree(s)+personnel(s)

    def cout(s):
        return profit(s)-aggregation(s)

    # Résolution - Algorithme de recherche tabout

    s = determination()
    X_k = 50
    X = 0
    l = 0
    i = 0
    while i <= X_k:
        for y in [voisin_1(s), voisin_2(s), voisin_3(s), voisin_4(s), voisin_5(s), voisin_6(s)]:
            if y not in L:
                C = cout(y)-cout(s)
                if C >= 0 and (s[0]*t_a*A1 + s[1]*t_a*A2 + s[2]*t_a*A3 + s[3]*t_a*A4 + s[4]*t_a*A5 + s[5]*t_a*A6) >= r_A and (s[0]*t_b*A1 + s[1]*t_b*A2 + s[2]*t_b*A3+s[3]*t_b*A4 + s[4]*t_b*A5 + s[5]*t_b*A6) >= r_B and (s[0]*t_c*A1 + s[1]*t_c*A2 + s[2]*t_c*A3+s[3]*t_c*A4 + s[4]*t_c*A5 + s[5]*t_c*A6) >= r_C and (s[0]+s[2]+s[3])*m1 <= m1_max and (s[0]+s[1]+s[3])*m2 <= m2_max and (s[0]+s[2]+s[1])*m3 <= m3_max:
                    L.append(s)
                    s = y

        i = i+1

    print("Solution optimale : ", s)
    print("profit maximal: ", profit(s), " Francs")
    print("Durée minimale totale: ", duree(s), " minutes")
    print("Nombre total de personnel minimal : ",
          personnel(s), " pour la journée\n")

    print("Nombre de passagers à transporter par jour sur la ligne PLATEAU-COCODY: ",
          s[0]*A1+s[1]*A2)
    print("Nombre de passagers à transporter par jour sur la ligne PLATEAU-TREICHEVILLE: ",
          s[2]*A1+s[3]*A2)
    print("Nombre de passagers à transporter par jour sur la ligne PLATEAU-YOPOUGON: ",
          s[3]*A1+s[1]*A2, "\n")
    print(
        "Nombre de passagers minimal/jour du bateau-bus 1 à transporter sur la ligne PLATEAU-COCODY : ", s[0]*A1)
    print(
        "Nombre de passagers minimal/jour du bateau-bus 1 à transporter sur la ligne PLATEAU-TREICHEVILLE : ", s[2]*A1)
    print(
        "Nombre de passagers minimal/jour du bateau-bus 1 à transporter sur la ligne PLATEAU-YOPOUGON : ", s[3]*A1, "\n")

    print(
        "Nombre de passagers minimal/jour du bateau-bus 2 à transporter sur la ligne PLATEAU-COCODY : ", s[0]*A2)
    print(
        "Nombre de passagers minimal/jour du bateau-bus 2 à transporter sur la ligne PLATEAU-TREICHEVILLE : ", s[1]*A2)
    print(
        "Nombre de passagers minimal/jour du bateau-bus 2 à transporter sur la ligne PLATEAU-YOPOUGON : ", s[3]*A2, "\n")

    print(
        "Nombre de passagers minimal/jour du bateau-bus 3 à transporter sur la ligne PLATEAU-COCODY : ", s[0]*A3)
    print(
        "Nombre de passagers minimal/jour du bateau-bus 3 à transporter sur la ligne PLATEAU-TREICHEVILLE : ", s[1]*A3)
    print(
        "Nombre de passagers minimal/jour du bateau-bus 3 à transporter sur la ligne PLATEAU-YOPOUGON : ", s[2]*A3, "\n")

    print(
        "Nombre de passagers minimal/jour du bateau-bus 4 à transporter sur la ligne PLATEAU-COCODY : ", s[0]*A4)
    print(
        "Nombre de passagers minimal/jour du bateau-bus 4 à transporter sur la ligne PLATEAU-TREICHEVILLE : ", s[1]*A4)
    print(
        "Nombre de passagers minimal/jour du bateau-bus 4 à transporter sur la ligne PLATEAU-YOPOUGON : ", s[2]*A4, "\n")

    print(
        "Nombre de passagers minimal/jour du bateau-bus 5 à transporter sur la ligne PLATEAU-COCODY : ", s[0]*A5)
    print(
        "Nombre de passagers minimal/jour du bateau-bus 5 à transporter sur la ligne PLATEAU-TREICHEVILLE : ", s[1]*A5)
    print(
        "Nombre de passagers minimal/jour du bateau-bus 5 à transporter sur la ligne PLATEAU-YOPOUGON : ", s[2]*A5, "\n")
    print(
        "Nombre de passagers minimal/jour du bateau-bus 6 à transporter sur la ligne PLATEAU-COCODY : ", s[0]*A6)
    print(
        "Nombre de passagers minimal/jour du bateau-bus 6 à transporter sur la ligne PLATEAU-TREICHEVILLE : ", s[1]*A6)
    print(
        "Nombre de passagers minimal/jour du bateau-bus 6 à transporter sur la ligne PLATEAU-YOPOUGON : ", s[2]*A6, "\n")

    print("-------------------fin-------------------------------")
    solution = [s, cout(s)]
    return solution


def main():
    # Test en génerant plusieurs solution initiale

    COUT = 0
    for i in range(10):
        c = resolution(500, 300, 200, 50, 75, 100, 70, 85, 90,
                       20, 25, 25, 250, 300, 325, 4, 4, 5, 300000, 25000, 180000)
        if c[1] > COUT:
            COUT = c[1]
            solution_finale = c

    print("∆∆∆∆∆∆∆∆∆ La meilleure solution est : ",
          solution_finale, " ∆∆∆∆∆∆∆∆∆")


main()
