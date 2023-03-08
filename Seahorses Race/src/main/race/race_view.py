from box.box import Box

from race.race import Race

class RaceView:
    """In charge of displaying the race.""" 
    @classmethod
    def display_race(cls, race: Race) -> None:
        cls.display_race_lane(race)
        cls.display_step_mark()
        
    @classmethod
    def display_race_lane(cls, race: Race):
        print("Start: ", end='')
        race_lane = cls.render_race_lance(race.boxes)
        for step in race_lane:
            print(step, end=' ')
        print("Finish.")
    
    @classmethod
    def display_step_mark(cls):
        print("Mark:  ", end='|')
        for step_mark in range(1, 13):
            if step_mark < 10:
                print(f" {step_mark} ", end=' ')
            else:
                print(f" {step_mark} ", end='')
        print('|')
    
    @classmethod
    def render_race_lance(cls, boxes: list[Box]) -> None:
        original_race = ['___'] * 13
        original_race[0] = ''
        return cls.distribute_boxes(original_race, boxes)
    
    @classmethod
    def distribute_boxes(cls, original_race: list[str], boxes: list[Box]) -> list[str]:
        for box in boxes:
            box_pos = box.position
            box_type = box.box_type
            if box_type == 'mystery':
                original_race[box_pos] = '_?_'
            else:
                original_race[box_pos] = '_!_'
        return original_race
        