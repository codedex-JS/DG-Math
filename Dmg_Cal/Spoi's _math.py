def calculate_base_damage(Level):
    

    Level_Mult = (Level - 1) * 0.02


    Stat_output = float(input("input stat: "))


    Stat_Mult = (Stat_output - 1) * 0.0045

  
    Total_Mult = Stat_Mult + Level_Mult + 1

   
    while True:
        if 1 <= Stat_output < 100:
            Move_dmg = float(input("input dmg: "))
        elif 100 <= Stat_output < 1000:
            Move_dmg = float(input("input dmg: "))
        elif 1000 <= Stat_output < 2000:
            Move_dmg = float(input("input dmg: "))
        elif 2000 <= Stat_output < 3000:
            Move_dmg = float(input("input dmg: "))
        else:
            Move_dmg = float(input("input dmg: "))

        
        Base_dmg = round(Move_dmg / Total_Mult, 3)

   
        print(f"Your move's base damage is {Base_dmg}.")


        repeat = input("Do you want to calculate for another move? (Y/N): ").lower()
        if repeat != 'y':
            break

Level = int(input("Script made by Beritrea. Please input DBOG level: "))


calculate_base_damage(Level)
