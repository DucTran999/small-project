class DieView:    
    
    @classmethod
    def print_dice_face(cls, face: int):
        if face == 1:
            print("\t\t┌─────────┐\n",
                  "\t\t│         │\n",
                  "\t\t│    ●    │\n",
                  "\t\t│         │\n",
                  "\t\t└─────────┘\n")
        elif face == 2:
            print("\t\t┌─────────┐\n"
                  "\t\t│  ●      │\n"
                  "\t\t│         │\n"
                  "\t\t│      ●  │\n"
                  "\t\t└─────────┘\n")
        elif face == 3: 
            print("\t\t┌─────────┐\n"
                  "\t\t│  ●      │\n"
                  "\t\t│    ●    │\n"
                  "\t\t│      ●  │\n"
                  "\t\t└─────────┘\n")
        elif face == 4: 
            print("\t\t┌─────────┐\n"
                  "\t\t│  ●   ●  │\n"
                  "\t\t│         │\n"
                  "\t\t│  ●   ●  │\n"
                  "\t\t└─────────┘\n")
        elif face == 5: 
            print("\t\t┌─────────┐\n"
                  "\t\t│  ●   ●  │\n"
                  "\t\t│    ●    │\n"
                  "\t\t│  ●   ●  │\n"
                  "\t\t└─────────┘\n")
        elif face == 6: 
            print("\t\t┌─────────┐\n"
                  "\t\t│  ●   ●  │\n"
                  "\t\t│  ●   ●  │\n"
                  "\t\t│  ●   ●  │\n"
                  "\t\t└─────────┘\n")
    
        