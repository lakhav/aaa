def jug_simulation():
    jug_4 = 0
    jug_3 = 0
    Steps = []
    while jug_4 != 2:

        jug_3 = 3
        print("Jug 3 =", jug_3, "Jug 4 =", jug_4)

        pour = min(jug_3, 4 - jug_4)
        jug_3 -= pour
        jug_4 += pour
        print("Jug 3 =", jug_3, "Jug 4 =", jug_4)

        if jug_4 == 2 or jug_3 == 2:
            if jug_3 == 2 and jug_4 != 2:
                print ("Jug 3 =", jug_3, "Jug 4 = 0")
                print ("Jug 3 =", 0, "Jug 4 = 4")
            break

        if jug_3 == 0:
            jug_3 = 3
            print("Jug 3 =", jug_3, "Jug 4 =", jug_4)

        pour = min(jug_3, 4 - jug_4)
        jug_3 -= pour
        jug_4 += pour
        print("Jug 3 =", jug_3, "Jug 4 =", jug_4)


        if jug_4 == 2 or jug_3 == 2:
            if jug_3 == 2 and jug_4 != 2:
                jug_4=0
                print ("Jug 3 =", jug_3, "Jug 4 = ",jug_4)
                jug_4=2
                jug_3=0
                print ("Jug 3 =", jug_3, "Jug 4 = ",jug_4)
                # jug_3=
            break
    print("Final state:\nJug 4 =", jug_4, "liters | Jug 3 =", jug_3, "liters")

jug_simulation()