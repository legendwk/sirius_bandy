from pptx import Presentation
from pptx.dml.color import ColorFormat, RGBColor
from pptx.util import Inches, Pt
import general_functions


from get_stats import Stats
from get_data import Game

class PP:

    # class variables
    text_color = RGBColor(0, 0, 0)
    background_color = RGBColor(51, 51, 255) 


    # contructor
    def __init__(self, filename: str, stats: Stats) -> None:
        self.teams_title = ' '.join(stats.team_dict).title()
        self.filename = filename
        self.pres = Presentation()
        return
    
    # static methods
    # don't know if we'll have any
        
    # non-static methods

    def make_pres(self) -> None:
        '''calls the methods needed to make a presentation '''
        self.make_front_page()
        self.save_presentation()

    def make_front_page(self) -> None:
        '''makes the front page layout'''
        lyt=self.pres.slide_layouts[0]
        slide=self.pres.slides.add_slide(lyt)
        title=slide.shapes.title
        title.text = self.teams_title
        img = r'C:\Users\vikin\Documents\Sirius Bandy\sirius_bandy\bilder\IK_Sirius_logo.png'
        picture = slide.insert_picture(img)
        #add_picture(image_file, left, top, width=None, height=None)
        return 

    def save_presentation(self) -> None:
        '''saves the presentation'''
        if len(self.filename) < 6 or self.filename[-5:] != '.pptx':
            self.filename = self.filename + '.pptx'
        self.pres.save(self.filename)

