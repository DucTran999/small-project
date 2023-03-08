from box.box import Box


class BoxView:
    """In charge of display box"""
    @classmethod
    def display_box(cls, box: Box):
        cls.display_box_icon(box.box_type)
        print(box)
    
    @classmethod
    def display_box_icon(cls, box_type: str):
        box_art = {
            'mystery': ("\t\t┌───────────┐",
                        "\t\t│───────────│",
                        "\t\t│  Mystery  │",
                        "\t\t│  ? ? ? ?  │",
                        "\t\t└───────────┘"
                        ),
            'danger':  ("\t\t┌───────────┐",
                        "\t\t│───────────│",
                        "\t\t│   Danger  │",
                        "\t\t│   ! ! !   │",
                        "\t\t└───────────┘"
                        )
        }
        for art_line in box_art.get(box_type):
            print(art_line)
    