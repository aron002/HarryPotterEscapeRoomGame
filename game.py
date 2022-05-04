import pygame
import random
import math
from spell import Spell
from line import Line


def _create_lines(spell):
    new_lines = []
    for line in spell.rough_lines:
        new_line = Line(CENTERS[line[0]], CENTERS[line[1]], COLORS[spell.color])
        new_lines.append(new_line)
    return new_lines


def _setup_spells(spells):
    for spell in spells:
        spell.lines = _create_lines(spell)


def create_spells():
    spells = []
    spells.append(Spell('Avada Kedavra', [(0,4), (4,2), (2,3), (3,5)], 'green'))
    spells.append(Spell('Expelliarmus', [(0,1), (1,2), (2,5), (5,4), (4,3), (3,0)], 'red'))
    spells.append(Spell('Incendio', [(3,2), (2,5), (5,4), (4,3), (3,0), (0,4)], 'purple'))
    spells.append(Spell('Stupefy', [(2,5), (5,0), (0, 4), (4,3)], 'blue'))
    spells.append(Spell('Expulso', [(1,4), (4,2), (2,3), (3,2), (2,5)], 'green'))
    spells.append(Spell('Deprimo', [(0,5), (5,0), (0,5), (5,0), (0,5)], 'yellow'))
    spells.append(Spell('Protego', [(2,3), (3,0), (0,5), (5,1), (1,4)], 'red'))
    spells.append(Spell('Rennervate', [(3,5), (5,0), (0,2), (2,3)], 'yellow'))
    spells.append(Spell('Tarantallegra', [(1,0), (0,3), (3,4), (4,5), (5,2)], 'purple'))
    spells.append(Spell('Bombarda', [(5,1), (1,4), (4,0), (0,3), (3,2)], 'blue'))
    _setup_spells(spells)
    return spells


def create_half_blood_spells(): # TODO
    spells = []
    spells.append(Spell('Avada Kedavra', [(1,4), (4,2), (2,3), (3,5)], 'green'))
    spells.append(Spell('Expelliarmus', [(0,3), (3,4), (4,5), (5,2), (2,1), (1,0)], 'red'))
    spells.append(Spell('Incendio', [(3,1), (1,5), (5,4), (4,3), (3,0), (0,4)], 'purple'))
    spells.append(Spell('Stupefy', [(2,5), (5,0), (0,4), (4,1)], 'blue'))
    spells.append(Spell('Expulso', [(0,4), (4,2), (2,3), (3,2), (2,5)], 'green'))
    spells.append(Spell('Deprimo', [(5,0), (0,5), (5,0), (0,5), (5,0)], 'yellow'))
    spells.append(Spell('Protego', [(2,3), (3,0), (0,5), (5,1), (1,3)], 'red'))
    spells.append(Spell('Rennervate', [(5,0), (0,2), (2,3), (3,5)], 'yellow'))
    spells.append(Spell('Tarantallegra', [(2,5), (5,4), (4,3), (3,0), (0,1)], 'purple'))
    spells.append(Spell('Bombarda', [(0,1), (1,4), (4,0), (0,3), (3,2)], 'blue'))
    _setup_spells(spells)
    return spells


def create_spells_dict(spells):
    spells_dict = {}
    for spell in spells:
        spells_dict[spell.name] = spell
    return spells_dict


def create_wands():
    wands = {}
    wand_names = ['dynol', 'forma', 'lingua', 'kyden']
    for wand_name in wand_names:
        # wand = resource_path('assets/' + wand_name + '.png')
        wand = pygame.image.load('assets/' + wand_name + '.png')
        # wand = pygame.image.load(wand)
        wand = pygame.transform.scale(wand, (POINTER_SIZE, POINTER_SIZE))
        wands[wand_name[0].upper()+wand_name[1:]] = wand
    return wands


def create_icons():
    icons = {}
    text_names = ['dynol', 'forma', 'lingua', 'kyden', 'clear', 'select', 'start']
    # clear = pygame.image.load('assets/clear.png')
    # icons['Clear'] = clear
    # avada_kedavra = pygame.image.load('assets/avada_kedavra.png')
    # icons['Avada Kedavra'] = avada_kedavra
    for spell in SPELLS:
        name = spell.name.replace(' ', '_').lower()
        # spell_img = resource_path('assets/' + name + '.png')
        spell_img = pygame.image.load('assets/' + name + '.png')
        # spell_img = pygame.image.load(spell_img)
        icons[spell.name] = spell_img
    for text_name in text_names:
        # text_img = resource_path('assets/' + text_name + '_text.png')
        text_img = pygame.image.load('assets/' + text_name + '_text.png')
        # text_img = pygame.image.load(text_img)
        icons[text_name[0].upper() + text_name[1:]+'_text'] = text_img
        if not text_name in ['clear', 'select', 'start']:
            # icon_img = resource_path('assets/' + text_name + '_icon.png')
            icon_img = pygame.image.load('assets/' + text_name + '_icon.png')
            # icon_img = pygame.image.load(icon_img)
            icon_img = pygame.transform.scale(icon_img, (WAND_BOX, WAND_BOX))
            icons[text_name[0].upper() + text_name[1:]+'_icon'] = icon_img
    return icons

    
def create_centers():
    centers = []
    for j in range(3):
        # center = (OFFSET_X, j*((HEIGHT-2*OFFSET_Y)//2)+OFFSET_Y)
        center = (OFFSET_X, j*((HEIGHT-OFFSET_Y)//2)+OFFSET_Y)
        centers.append(center)

    for j in range(3):
        # center = (WIDTH-OFFSET_X, j*((HEIGHT-2*OFFSET_Y)//2)+OFFSET_Y)
        center = (WIDTH-OFFSET_X, j*((HEIGHT-OFFSET_Y)//2)+OFFSET_Y)
        centers.append(center)
    return centers


def draw_circles():
    for center in CENTERS:
        pygame.draw.circle(gameDisplay, COLORS['black'], center, RADIUS)


def draw_line(selected, pos, color):
    pygame.draw.line(gameDisplay, color, selected, pos, LINE_WIDTH)


def draw_lines(lines):
    # draw all of the lines that have been made
    for line in lines:
        pygame.draw.line(gameDisplay, line.color, line.start, line.end, LINE_WIDTH)


def draw_dashboard():
    # draw clear box
    box = pygame.draw.rect(gameDisplay, COLORS['black'], (WIDTH-(BOX_WIDTH//2 + BOX_WIDTH), HEIGHT+(EXTRA_HEIGHT-BOX_HEIGHT)//2, BOX_WIDTH, BOX_HEIGHT), width = 2)
    # text = FONT.render('CLEAR', True, COLORS['black'])
    # textRect = text.get_rect()
    # textRect.center = box.center
    # gameDisplay.blit(text, textRect)
    clear = ICONS['Clear_text']
    clear_rect = clear.get_rect()
    clear_rect.center = box.center
    gameDisplay.blit(clear, clear_rect)

    # draw color boxes
    p_colors = list(COLORS.keys())
    for i in range(5):
        color = COLORS[p_colors[i]]
        box = pygame.draw.rect(gameDisplay, color, (BOX_WIDTH//2+i*(BOX_HEIGHT+BOX_OFFSET), HEIGHT+(EXTRA_HEIGHT-BOX_HEIGHT)//2, BOX_HEIGHT, BOX_HEIGHT))
        gameDisplay.fill(color, box)


def draw_spell_name(spell):
    # name = 'Malzahar used: ' + spell.name
    # text = FONT.render(name, True, COLORS['black'])
    text = ICONS[spell.name]
    textRect = text.get_rect()
    textRect.center = (WIDTH//2, 50)
    gameDisplay.blit(text, textRect)


def draw_timer(t):
    r_t = math.floor(t)
    str_t = str(MAX_TIME*(r_t//MAX_TIME+1) - r_t)
    text = FONT.render(str_t, True, COLORS['black'])
    textRect = text.get_rect()
    textRect.center = (textRect.width, textRect.height)
    gameDisplay.blit(text, textRect)


def draw_mouse_pointer(img, pos):
    img_rect = img.get_rect()
    img_rect.center = pos
    gameDisplay.blit(img, img_rect)


def draw_wands(wand):
    lingua_text = ICONS['Lingua_text']
    textRect = lingua_text.get_rect()
    textRect.center = (OFFSET_X+WAND_BOX//2, OFFSET_Y)
    gameDisplay.blit(lingua_text, textRect)
    lingua_wand = ICONS['Lingua_icon']
    imgRect = lingua_wand.get_rect()
    imgRect.center = (OFFSET_X+WAND_BOX//2, OFFSET_Y+textRect.height+WAND_BOX//2)
    color = COLORS['black']
    if wand == WANDS['Lingua']:
        color = COLORS['blue']
    pygame.draw.rect(gameDisplay, color, (OFFSET_X+10, OFFSET_Y+textRect.height, WAND_BOX, WAND_BOX), width = 2)
    gameDisplay.blit(lingua_wand, imgRect)

    dynol_text = ICONS['Dynol_text']
    textRect = dynol_text.get_rect()
    textRect.center = (WIDTH-(OFFSET_X+WAND_BOX//2), OFFSET_Y)
    gameDisplay.blit(dynol_text, textRect)
    dynol_wand = ICONS['Dynol_icon']
    imgRect = dynol_wand.get_rect()
    imgRect.center = (WIDTH-(OFFSET_X+WAND_BOX//2), OFFSET_Y+textRect.height+WAND_BOX//2)
    color = COLORS['black']
    if wand == WANDS['Dynol']:
        color = COLORS['blue']
    pygame.draw.rect(gameDisplay, color, (WIDTH-(OFFSET_X+WAND_BOX)+10, OFFSET_Y+textRect.height+3, WAND_BOX, WAND_BOX), width = 2)
    gameDisplay.blit(dynol_wand, imgRect)

    forma_text = ICONS['Forma_text']
    textRect = forma_text.get_rect()
    textRect.center = (OFFSET_X+WAND_BOX//2, HEIGHT-OFFSET_Y)
    gameDisplay.blit(forma_text, textRect)
    forma_wand = ICONS['Forma_icon']
    imgRect = forma_wand.get_rect()
    imgRect.center = (OFFSET_X+WAND_BOX//2, HEIGHT-OFFSET_Y+textRect.height+WAND_BOX//2)
    color = COLORS['black']
    if wand == WANDS['Forma']:
        color = COLORS['blue']
    pygame.draw.rect(gameDisplay, color, (OFFSET_X+10, HEIGHT-OFFSET_Y+textRect.height-5, WAND_BOX, WAND_BOX), width = 2)
    gameDisplay.blit(forma_wand, imgRect)

    kyden_text = ICONS['Kyden_text']
    textRect = kyden_text.get_rect()
    textRect.center = (WIDTH-(OFFSET_X+WAND_BOX//2), HEIGHT-OFFSET_Y)
    gameDisplay.blit(kyden_text, textRect)
    kyden_wand = ICONS['Kyden_icon']
    imgRect = kyden_wand.get_rect()
    imgRect.center = (WIDTH-(OFFSET_X+WAND_BOX//2), HEIGHT-OFFSET_Y+textRect.height+WAND_BOX//2)
    color = COLORS['black']
    if wand == WANDS['Kyden']:
        color = COLORS['blue']
    pygame.draw.rect(gameDisplay, color, (WIDTH-(OFFSET_X+WAND_BOX)+10, HEIGHT-OFFSET_Y+textRect.height+2, WAND_BOX, WAND_BOX), width = 2)
    gameDisplay.blit(kyden_wand, imgRect)


def draw_submit(wand):
    start = ICONS['Start_text']
    imgRect = start.get_rect()
    imgRect.center = (WIDTH//2, HEIGHT+EXTRA_HEIGHT//2)
    gameDisplay.blit(start, imgRect)
    pygame.draw.rect(gameDisplay, COLORS['black'], (WIDTH//2-imgRect.width//2-SUBMIT_OFFSET, HEIGHT+EXTRA_HEIGHT//2-imgRect.height//2-SUBMIT_OFFSET, imgRect.width+2*SUBMIT_OFFSET, imgRect.height+2*SUBMIT_OFFSET), width = 2)
    if wand is None:
        select = ICONS['Select_text']
        imgRect2 = select.get_rect()
        imgRect2.center = (WIDTH//2, HEIGHT+EXTRA_HEIGHT//2+imgRect.height+2*SUBMIT_OFFSET)
        gameDisplay.blit(select, imgRect2)


def calc_circle(pos):
    # find the circle
    x, y = pos
    for i in range(len(CENTERS)):
        circle_x, circle_y = CENTERS[i]
        dist_x = abs(x - circle_x)
        dist_y = abs(y - circle_y)
        if (dist_x**2 + dist_y**2) <= RADIUS**2:
            return i
    return None


def check_buttons(pos):
    x, y = pos
    p_colors = list(COLORS.keys())
    if (WIDTH-(BOX_WIDTH//2 + BOX_WIDTH)) <= x <= (WIDTH-(BOX_WIDTH//2)) and (HEIGHT+(EXTRA_HEIGHT-BOX_HEIGHT)//2) <= y <= (HEIGHT+(EXTRA_HEIGHT-BOX_HEIGHT)//2 + BOX_HEIGHT):
        return 'clear'
    elif (HEIGHT+(EXTRA_HEIGHT-BOX_HEIGHT)//2) <= y <= (HEIGHT+(EXTRA_HEIGHT-BOX_HEIGHT)//2+BOX_HEIGHT):
        for i in range(5):
            if (BOX_WIDTH//2+i*(BOX_HEIGHT+BOX_OFFSET)) <= x <= (BOX_WIDTH//2+i*(BOX_HEIGHT+BOX_OFFSET)+BOX_HEIGHT):
                return p_colors[i]
    return ''


def check_wands(pos):
    x, y = pos
    # (gameDisplay, COLORS['black'], (OFFSET_X+10, OFFSET_Y+textRect.height, WAND_BOX, WAND_BOX), width = 2)
    if OFFSET_X+10 <= x <= OFFSET_X+10+WAND_BOX and OFFSET_Y+33 <= y <= OFFSET_Y+33+WAND_BOX:
        return 'Lingua'
    # (gameDisplay, COLORS['black'], (WIDTH-(OFFSET_X+WAND_BOX)+10, OFFSET_Y+textRect.height+3, WAND_BOX, WAND_BOX), width = 2)
    if WIDTH-(OFFSET_X+WAND_BOX)+10 <= x <= WIDTH-(OFFSET_X+WAND_BOX)+10+WAND_BOX and OFFSET_Y+36 <= y <= OFFSET_Y+36+WAND_BOX:
        return 'Dynol'
    # (gameDisplay, COLORS['black'], (OFFSET_X+10, HEIGHT-OFFSET_Y+textRect.height-5, WAND_BOX, WAND_BOX), width = 2)
    if OFFSET_X+10 <= x <= OFFSET_X+10+WAND_BOX and HEIGHT-OFFSET_Y+28 <= y <= HEIGHT-OFFSET_Y+28+WAND_BOX:
        return 'Forma'
    # (gameDisplay, COLORS['black'], (WIDTH-(OFFSET_X+WAND_BOX)+10, HEIGHT-OFFSET_Y+textRect.height+2, WAND_BOX, WAND_BOX), width = 2)
    if WIDTH-(OFFSET_X+WAND_BOX)+10 <= x <= WIDTH-(OFFSET_X+WAND_BOX)+10+WAND_BOX and HEIGHT-OFFSET_Y+35 <= y <= HEIGHT-OFFSET_Y+35+WAND_BOX:
        return 'Kyden'
    return ''


def compare_lines(l1, l2):
    if len(l1) != len(l2):
        return False
    for i in range(len(l1)):
        if l1[i] != l2[i]:
            return False
    return True


def draw():
    # stop = False
    selected = None
    lines = []
    color = None
    clock = pygame.time.Clock()
    # used_spell = random.choice(SPELLS)
    # used_spell = SPELLS_DICT['Avada Kedavra']
    # spell = SPELLS_DICT[COUNTERS[used_spell.name]]
    used_spell = None
    spell = None
    score = 0
    wand = None # default doesnt matter
    screen = 'main'
    # while not stop:
    while True:
        gameDisplay.fill(COLORS['white'])
        pos = pygame.mouse.get_pos()
        if screen == 'main':
            pygame.mouse.set_visible(True)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # stop = True
                    return score
                if event.type == pygame.MOUSEBUTTONDOWN:
                    wnd = check_wands(pos)
                    if wnd != '':
                        wand = WANDS[wnd]
                    # (WIDTH//2-imgRect.width//2-SUBMIT_OFFSET, HEIGHT+EXTRA_HEIGHT//2-imgRect.height//2-SUBMIT_OFFSET, imgRect.width+2*SUBMIT_OFFSET, imgRect.height+2*SUBMIT_OFFSET)
                    elif wand and WIDTH//2-29-SUBMIT_OFFSET <= pos[0] <= WIDTH//2-29-SUBMIT_OFFSET+WIDTH//2-58-SUBMIT_OFFSET and HEIGHT+EXTRA_HEIGHT//2-16-SUBMIT_OFFSET <= pos[1] <= HEIGHT+EXTRA_HEIGHT//2-16-SUBMIT_OFFSET+33+2*SUBMIT_OFFSET:# when they click submit
                        screen = 'game'
                        start = pygame.time.get_ticks()
                        if wand == WANDS['Dynol']:
                            used_spell = random.choice(HALF_BLOOD_SPELLS)
                            spell = HALF_BLOOD_SPELLS_DICT[COUNTERS[used_spell.name]]
                        else:
                            used_spell = random.choice(SPELLS)
                            spell = SPELLS_DICT[COUNTERS[used_spell.name]]
            draw_wands(wand)
            draw_submit(wand)
        if screen == 'game':
            pygame.mouse.set_visible(False)
            seconds = (pygame.time.get_ticks() - start) / 1000
            if seconds >= MAX_TIME:
                # stop = True
                return score
            if compare_lines(lines, spell.lines):
                if wand == WANDS['Dynol']:
                    HALF_BLOOD_SPELLS.remove(used_spell)
                else:
                    SPELLS.remove(used_spell)
                score += 1
                start += seconds * 1000
                if len(SPELLS) > 0 and score < SCORE_NEEDED:
                    if wand == WANDS['Dynol']:
                        used_spell = random.choice(HALF_BLOOD_SPELLS)
                        spell = HALF_BLOOD_SPELLS_DICT[COUNTERS[used_spell.name]]
                    else:
                        used_spell = random.choice(SPELLS)
                        spell = SPELLS_DICT[COUNTERS[used_spell.name]]
                    lines = []
                else:
                    # stop = True
                    return score
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # stop = True
                    return score
                if event.type == pygame.MOUSEBUTTONDOWN:
                    btn = check_buttons(pos)
                    if btn == 'clear':
                        lines = []
                        selected = None
                    elif btn != '':
                        color = COLORS[btn]
                    else:
                        if color:
                            # if selected is not None:
                            #     # if a line has been started
                            #     new_selected = calc_circle(pos)
                            #     if new_selected is not None:
                            #         if new_selected != selected:
                            #             new_line = Line(CENTERS[selected], CENTERS[new_selected], color)
                            #             lines.append(new_line)
                            #             selected = None
                            # else:
                                # create new line from selected to mouse
                            selected = calc_circle(pos) # in else
                if event.type == pygame.MOUSEBUTTONUP:
                    # if a line has been started
                    new_selected = calc_circle(pos)
                    if color and selected is not None and new_selected is not None and new_selected != selected:
                        new_line = Line(CENTERS[selected], CENTERS[new_selected], color)
                        lines.append(new_line)
                    selected = None  
            if selected is not None:
                draw_line(CENTERS[selected], pos, color)
            draw_lines(lines)
            draw_circles()
            draw_dashboard()
            draw_spell_name(used_spell)
            draw_timer(seconds)
            draw_mouse_pointer(wand, pos)    
        pygame.display.update()
        clock.tick(30)


if __name__ == '__main__':
    WIDTH, HEIGHT = 700, 600 # 900, 800
    EXTRA_HEIGHT = 200
    RESOLUTION = WIDTH, HEIGHT + EXTRA_HEIGHT
    OFFSET_X = WIDTH//3//100 * 100 # 250
    OFFSET_Y = HEIGHT//4 # 150
    RADIUS = 20
    LINE_WIDTH = 5
    BOX_WIDTH = 115 # 150
    BOX_HEIGHT = 65 # 75
    BOX_OFFSET = (WIDTH - (WIDTH-(BOX_WIDTH//2 + BOX_WIDTH)) - BOX_WIDTH//2)//4
    COLORS = {'green': (73, 184, 72), 'red': (238, 55, 35), 'purple': (159, 55, 150), 'blue': (18, 126, 190), 'yellow': (243, 236, 24), 'black': (0, 0, 0), 'white': (255, 255, 255)}
    CENTERS = create_centers()
    SPELLS = create_spells()
    HALF_BLOOD_SPELLS = create_half_blood_spells()
    SPELLS_DICT = create_spells_dict(SPELLS)
    HALF_BLOOD_SPELLS_DICT = create_spells_dict(HALF_BLOOD_SPELLS)
    # Malzahar Used: Counter
    COUNTERS = {'Deprimo': 'Avada Kedavra', 'Avada Kedavra': 'Expelliarmus', 'Protego': 'Incendio', 'Expelliarmus': 'Stupefy', 'Stupefy': 'Expulso', 'Tarantallegra': 'Deprimo', 'Expulso': 'Protego', 'Bombarda': 'Rennervate', 'Rennervate': 'Tarantallegra', 'Incendio': 'Bombarda'}
    SCORE_NEEDED = 3
    MAX_TIME = 50
    POINTER_SIZE = 100
    WAND_BOX = 125
    WANDS = create_wands()
    ICONS = create_icons()
    SUBMIT_OFFSET = 10

    pygame.init()
    gameDisplay = pygame.display.set_mode(RESOLUTION)
    pygame.display.set_caption('Wand Duel')
    FONT = pygame.font.Font('freesansbold.ttf', 24)
    # TODO: Winner/Loser Screen
    if draw() == SCORE_NEEDED:
        print('YOU WON!!!')
    else:
        print('YOU LOSE!!!')
    pygame.quit()
