from pptx import Presentation
from pptx.dml.color import ColorFormat, RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches, Pt
import general_functions as gf
from get_stats import Stats
from get_data import Game
import os
import constants
from pptx.util import Pt
from pptx.enum.text import MSO_ANCHOR


class PP:
    # class variables
    # sirius specific colors
    text_color = RGBColor(0, 0, 0)
    background_color = RGBColor(190,190,190)  # (223,223,223) 
    third_color = RGBColor(250, 226, 12)
    halftime = 45

    # relative link to image folder
    image_link = "..\\..\\bilder\\logos\\"

    # contructor
    def __init__(self, stats: Stats) -> None:
        self.stats = stats
        self.pres = Presentation()
        self.make_pres()
        return
    
    # static methods
    def iter_cells(table):
        '''yeilds the cells of a table, 
            used to style them'''
        for row in table.rows:
            for cell in row.cells:
                yield cell

    # non-static methods
    def set_background_color(self, slide) -> None:
        '''sets the background color of current slide to match
            class variable background_color'''
        background = slide.background
        fill = background.fill
        fill.solid()
        fill.fore_color.rgb = PP.background_color
        #fill.fore_color.brightness = 0.1
        #fill.transparency = 0.1
        return    

    def add_logo_images(self, slide, from_left = 0.7, from_top = 0.4, width = 2) -> None:
        '''adds the logos of the teams to the slide
            units in Inches''' 
        for i, team in enumerate(list(self.stats.teams)):
            img = PP.image_link + constants.logos[team]
            if i != 0: 
                # converting to inches by dividing by 914400 ??????
                from_left = self.pres.slide_width/914400 - from_left - width 
            slide.shapes.add_picture(img, Inches(from_left), Inches(from_top), Inches(width))

    def make_front_page(self) -> None:
        '''makes the front page layout'''
        slide_register = self.pres.slide_layouts[0]
        slide = self.pres.slides.add_slide(slide_register)
        title = slide.shapes.title
        title.text = " - ".join(constants.nicknames[team]['full'] for team in self.stats.teams)
        title.text_frame.paragraphs[0].font.color.rgb = PP.text_color

        subtitle = slide.placeholders[1]
        subtitle.text = ' - '.join(str(self.stats.prints['score'][team]) for team in self.stats.prints['score']) 
        subtitle.text_frame.paragraphs[0].font.color.rgb = PP.third_color
        self.add_logo_images(slide, width = 2)
        self.set_background_color(slide)
        return 

    def make_overview_stats_page(self) -> None:
        '''makes the overview stats page layout'''
        slide_register = self.pres.slide_layouts[4]
        slide = self.pres.slides.add_slide(slide_register)
        self.add_logo_images(slide, width = 1.5)
        self.set_background_color(slide)
        title = slide.shapes.title
        title.text = 'Matchstatistik'
        bpb = slide.shapes

        for i, team in enumerate(self.stats.teams):
            bpb = slide.shapes
            bp1 = bpb.placeholders[(i + 1)*2-1] # first 1, then 3  
            bp1.text = constants.nicknames[team]['short']
            bp1.text_frame.paragraphs[0].font.color.rgb = constants.colors[team][0]

            bp2 = bpb.placeholders[(i + 1)*2]  # first 2, then 4
            res = bp2.text_frame.add_paragraph()
            res.text = f"Resultat: \n\t{self.stats.prints['score'][team]}"
            res.level = 0
            res.font.color.rgb = constants.colors[team][0]
            res = bp2.text_frame.add_paragraph()
            res.text = f"Skott på mål: \n\t{self.stats.prints['shots on goal'][team]}"
            res.level = 0
            res.font.color.rgb = constants.colors[team][0]
            res = bp2.text_frame.add_paragraph()
            res.text = f"Bollinnehav: \n\t{self.stats.prints['possession'][team]}"
            res.level = 0
            res.font.color.rgb = constants.colors[team][0]
  

    def make_shot_types_page(self) -> None:
        '''makes the shots types stats page'''
        slide_register = self.pres.slide_layouts[4]
        slide = self.pres.slides.add_slide(slide_register)
        self.add_logo_images(slide, width = 1.5)
        self.set_background_color(slide)
        title = slide.shapes.title
        title.text = 'Skottstatistik \nSkotttyper'
        # this is just all the shot types for both teams sorted in alphabetical order
        print_order = sorted(list({st for team in self.stats.prints['shot types'] for st in self.stats.prints['shot types'][team]}))
        for i, team in enumerate(self.stats.teams):
            bpb = slide.shapes
            bp1 = bpb.placeholders[(i + 1)*2-1] # first 1, then 3  
            bp1.text = f"{constants.nicknames[team]['short']} - skottförsök: {sum(self.stats.prints['shot types'][team].values())}"
            bp1.text_frame.paragraphs[0].font.color.rgb = constants.colors[team][0]

            bp2 = bpb.placeholders[(i + 1)*2]  # first 2, then 4
            for st in print_order:
                res = bp2.text_frame.add_paragraph()
                if st in self.stats.prints['shot types'][team]:
                    i = self.stats.prints['shot types'][team][st]
                else: 
                    i = 0
                res.text = f"{st.title()}: {i}"
                res.level = 0
                res.font.color.rgb = constants.colors[team][0]

    def make_duels_page(self) -> None:
        '''makes the duels stats page'''
        slide_register = self.pres.slide_layouts[4]
        slide = self.pres.slides.add_slide(slide_register)
        self.add_logo_images(slide, width = 1.5)
        self.set_background_color(slide)
        title = slide.shapes.title
        title.text = 'Bollvinster'

        for i, team in enumerate(self.stats.teams):
            bpb = slide.shapes
            bp1 = bpb.placeholders[(i + 1)*2-1] # first 1, then 3  
            bp1.text = constants.nicknames[team]['short']
            bp1.text_frame.paragraphs[0].font.color.rgb = constants.colors[team][0]

            bp2 = bpb.placeholders[(i + 1)*2]  # first 2, then 4
            res = bp2.text_frame.add_paragraph()
            res.text = f"Vunna närkamper: \n\t{self.stats.prints['scrimmages'][team]}"
            res.level = 0
            res.font.color.rgb = constants.colors[team][0]
            res = bp2.text_frame.add_paragraph()
            res.text = f"Brytningar: \n\t{self.stats.prints['interceptions'][team]}"
            res.level = 0
            res.font.color.rgb = constants.colors[team][0]
            res = bp2.text_frame.add_paragraph()
            res.text = f"Bolltapp: \n\t{self.stats.prints['lost balls'][team]}"
            res.level = 0
            res.font.color.rgb = constants.colors[team][0]


    def make_scimmages_page(self) -> None:
        '''makes the scrimmages stats page'''
        slide_register = self.pres.slide_layouts[4]
        slide = self.pres.slides.add_slide(slide_register)
        self.add_logo_images(slide, width = 1.5)
        self.set_background_color(slide)
        title = slide.shapes.title
        title.text = 'Närkampssituationer \noch deras utfall'

        for i, team in enumerate(self.stats.teams):
            bpb = slide.shapes
            bp1 = bpb.placeholders[(i + 1)*2-1] # first 1, then 3  
            bp1.text = constants.nicknames[team]['short']
            bp1.text_frame.paragraphs[0].font.color.rgb = constants.colors[team][0]
            bp2 = bpb.placeholders[(i + 1)*2]  # first 2, then 4
            res = bp2.text_frame.add_paragraph()
            res.text = f"Långvarig bollvinst: \n\t{self.stats.prints['possession changes'][team]['long']}"
            res.level = 0
            res.font.color.rgb = constants.colors[team][0]
            res = bp2.text_frame.add_paragraph()
            res.text = f"Kortvarig bollvinst: \n\t{self.stats.prints['possession changes'][team]['short']}"
            res.font.color.rgb = constants.colors[team][0]
            res.level = 0

    def make_shot_origins_page(self) -> None:
        '''makes the shots types stats page'''
        slide_register = self.pres.slide_layouts[4]
        slide = self.pres.slides.add_slide(slide_register)
        self.add_logo_images(slide, width = 1.5)
        self.set_background_color(slide)
        title = slide.shapes.title
        title.text = 'Skottstatistik \nSkottens ursprung'
        # this is the shot origins for both teams sorted 
        print_order = sorted(list({so for team in self.stats.prints['shot origins'] for so in self.stats.prints['shot origins'][team]}))


        for i, team in enumerate(self.stats.teams):
            bpb = slide.shapes
            bp1 = bpb.placeholders[(i + 1)*2-1] # first 1, then 3  
            bp1.text = f"{constants.nicknames[team]['short']} - skottförsök: {sum(self.stats.prints['shot origins'][team].values())}"
            bp1.text_frame.paragraphs[0].font.color.rgb = constants.colors[team][0]

            bp2 = bpb.placeholders[(i + 1)*2]  # first 2, then 4
            #bp2.text_frame.paragraphs[0].font.color.rgb = constants.colors[team][0]
            for so in print_order:
                res = bp2.text_frame.add_paragraph()
                if so in self.stats.prints['shot origins'][team]:
                    i = self.stats.prints['shot origins'][team][so]
                else: 
                    i = 0
                res.text = f"{so.title()}: {i}"
                res.level = 0
                res.font.color.rgb = constants.colors[team][0]
        
    def make_goals_stats_page(self) -> None:
        '''makes the goals stats page'''
        slide_register = self.pres.slide_layouts[1]
        slide = self.pres.slides.add_slide(slide_register)
        self.add_logo_images(slide)
        self.set_background_color(slide)
        title = slide.shapes.title
        title.text = 'Målen'
        bpb = slide.shapes

        bp1 = bpb.placeholders[1]
        for goal in self.stats.goals_info_list:
            res = bp1.text_frame.add_paragraph()
            # fixa det här med målens tid i andra halvlek
            res.text = f"{goal['time']}: {goal['origin']} -> {goal['shot type']} på {goal['attack time']}s."
            res.font.color.rgb = constants.colors[goal['team']][0]
            res.level = 0


    def make_before_and_after_table_page(self) -> None:
        '''creates the page with the table for the before and after possessions'''
        # THIS IS SO AWFUL :------)))))
        slide_register = self.pres.slide_layouts[5]
        slide = self.pres.slides.add_slide(slide_register)
        self.add_logo_images(slide, width = 1.5)
        self.set_background_color(slide)
        title = slide.shapes.title

        title.text = 'Närkamper \noch deras utfall'
        left_table = Inches(2)
        top_table = Inches(2.5)
        width_table = Inches(6)
        height_table = Inches(4)
        table_frame = slide.shapes.add_table(3,3, left_table, top_table, width_table, height_table)
        table = table_frame.table
        
        tbl =  table_frame._element.graphic.graphicData.tbl
        style_id = '{69CF1AB2-1976-4502-BF36-3FF5EA218861}'
        tbl[0][-1].text = style_id
        # första cellen ska inte 
        for i in range(3):
            fill = table.cell(i, i).fill
            fill.solid()
            if i == 0:
                fill.fore_color.rgb = PP.background_color
            else:
                fill.fore_color.rgb = constants.color_scale[3]

        for i, team in enumerate(self.stats.prints['before and after']):
            table.cell(i+1, 0).text = f"Före {constants.nicknames[team]['short']}"
            table.cell(0, i+1).text = f"Efter {constants.nicknames[team]['short']}"
            table.cell(i+1, i+1).text = f"{self.stats.prints['before and after'][team][team]}"
            # this solution is horrible : -)
            if i == 0:
                j,k = 1,2
            else:
                j,k = 2,1
            table.cell(j,k).text = f"{self.stats.prints['before and after'][team][self.stats.opposite_team(team)]}"
        
        for cell in PP.iter_cells(table):
            cell.vertical_anchor = MSO_ANCHOR.MIDDLE
            paragraph = cell.text_frame.paragraphs[0]
            paragraph.font.size = Pt(25)
            paragraph.font.bold = True
            paragraph.alignment = PP_ALIGN.CENTER
            # här kan vi ändra färg om vi vill.......
            #fill = cell.fill
            #fill.solid()
            #fill.fore_color.rgb = PP.background_color


        

    def make_pres(self) -> None:
        '''calls the methods needed to make a presentation '''
        self.make_front_page()
        self.make_overview_stats_page()
        self.make_duels_page()
        #self.make_scimmages_page()
        self.make_before_and_after_table_page()
        self.make_shot_types_page()
        self.make_shot_origins_page()
        self.make_goals_stats_page()

        self.save_presentation()

    def save_presentation(self) -> None:
        '''saves the presentation'''
        self.pres.save(self.stats.out[:-9] + '.pptx')

