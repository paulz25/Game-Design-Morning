#Zara Paul 
#6/9/2022
#We are learning pygame basic functins, 
# creating screens, clrs, shape ,move 
# move  the square
# K_UP                  up arrow
# K_DOWN                down arrow
# K_RIGHT               right arrow
# K_LEFT                left arrow
#picture = pygame. image. load(filename)
#picture = pygame. transform. scale(picture, (1280, 720))
#bg=pygame.image.load('ClassStuff\CircleEatsSquare\Images\\bgSmaller.jpg')

import sys
from turtle import done, width
import pygame, time,os,random, math
pygame.init()#initialize the pygame package

# print(pygame.font.get_fonts())
# pygame.time.delay(10000)
TITLE_FONT = pygame.font.SysFont('comicsans', 40)
MENU_FONT = pygame.font.SysFont('comicsans', 20)

os.system('clear')
WIDTH=700 #like constant
HEIGHT=700
colors={"white":(255,255,255),"pink":(255,0,255),"blue":(0,0,255),"limeGreen":(153,255,51),
"RED" : (255, 0, 0),
"GREEN" : (0, 255, 0),
"BLUE" : (0, 0,255),
"BLACK" : (0, 0, 0),
"DARK_GREY" : (60, 60, 60),
"DARK_SLATE_GREY" : (47, 79, 79),
"DIM_GREY" : (105, 105, 105),
"FREE_SPEECH_GREY" : (99, 86, 136),
"GREY" : (190, 190, 190),
"GREY0" : (0, 0, 0),
"GREY1" : (3, 3, 3),
"GREY2" : (5, 5, 5),
"GREY3" : (8, 8, 8),
"GREY4" : (10, 10, 10),
"GREY5" : (13, 13, 13),
"GREY6" : (15, 15, 15),
"GREY7" : (18, 18, 18),
"GREY8" : (20, 20, 20),
"GREY9" : (23, 23, 23),
"GREY10" : (26, 26, 26),
"GREY11" : (28, 28, 28),
"GREY12" : (31, 31, 31),
"GREY13" : (33, 33, 33),
"GREY14" : (36, 36, 36),
"GREY15" : (38, 38, 38),
"GREY16" : (41, 41, 41),
"GREY17" : (43, 43, 43),
"GREY18" : (46, 46, 46),
"GREY19" : (48, 48, 48),
"GREY20" : (51, 51, 51),
"GREY21" : (54, 54, 54),
"GREY22" : (56, 56, 56),
"GREY23" : (59, 59, 59),
"GREY24" : (61, 61, 61),
"GREY25" : (64, 64, 64),
"GREY26" : (66, 66, 66),
"GREY27" : (69, 69, 69),
"GREY28" : (71, 71, 71),
"GREY29" : (74, 74, 74),
"GREY30" : (77, 77, 77),
"GREY31" : (79, 79, 79),
"GREY32" : (82, 82, 82),
"GREY33" : (84, 84, 84),
"GREY34" : (87, 87, 87),
"GREY35" : (89, 89, 89),
"GREY36" : (92, 92, 92),
"GREY37" : (94, 94, 94),
"GREY38" : (97, 97, 97),
"GREY39" : (99, 99, 99),
"GREY40" : (102, 102, 102),
"GREY41" : (105, 105, 105),
"GREY42" : (107, 107, 107),
"GREY43" : (110, 110, 110),
"GREY44" : (112, 112, 112),
"GREY45" : (115, 115, 115),
"GREY46" : (117, 117, 117),
"GREY47" : (120, 120, 120),
"GREY48" : (122, 122, 122),
"GREY49" : (125, 125, 125),
"GREY50" : (127, 127, 127),
"GREY51" : (130, 130, 130),
"GREY52" : (133, 133, 133),
"GREY53" : (135, 135, 135),
"GREY54" : (138, 138, 138),
"GREY55" : (140, 140, 140),
"GREY56" : (143, 143, 143),
"GREY57" : (145, 145, 145),
"GREY58" : (148, 148, 148),
"GREY59" : (150, 150, 150),
"GREY60" : (153, 153, 153),
"GREY61" : (156, 156, 156),
"GREY62" : (158, 158, 158),
"GREY63" : (161, 161, 161),
"GREY64" : (163, 163, 163),
"GREY65" : (166, 166, 166),
"GREY66" : (168, 168, 168),
"GREY67" : (171, 171, 171),
"GREY68" : (173, 173, 173),
"GREY69" : (176, 176, 176),
"GREY70" : (179, 179, 179),
"GREY71" : (181, 181, 181),
"GREY72" : (184, 184, 184),
"GREY73" : (186, 186, 186),
"GREY74" : (189, 189, 189),
"GREY75" : (191, 191, 191),
"GREY76" : (194, 194, 194),
"GREY77" : (196, 196, 196),
"GREY78" : (199, 199, 199),
"GREY79" : (201, 201, 201),
"GREY80" : (204, 204, 204),
"GREY81" : (207, 207, 207),
"GREY82" : (209, 209, 209),
"GREY83" : (212, 212, 212),
"GREY84" : (214, 214, 214),
"GREY85" : (217, 217, 217),
"GREY86" : (219, 219, 219),
"GREY87" : (222, 222, 222),
"GREY88" : (224, 224, 224),
"GREY89" : (227, 227, 227),
"GREY90" : (229, 229, 229),
"GREY91" : (232, 232, 232),
"GREY92" : (235, 235, 235),
"GREY93" : (237, 237, 237),
"GREY94" : (240, 240, 240),
"GREY95" : (242, 242, 242),
"GREY96" : (245, 245, 245),
"GREY97" : (247, 247, 247),
"GREY98" : (250, 250, 250),
"GREY99" : (252, 252, 252),
"LIGHT_GREY" : (211, 211, 211),
"SLATE_GREY" : (112, 128, 144),
"SLATE_GREY_1" : (198, 226, 255),
"SLATE_GREY_2" : (185, 211, 238),
"SLATE_GREY_3" : (159, 182, 205),
"SLATE_GREY_4" : (108, 123, 139),
"VERY_LIGHT_GREY" : (205, 205, 205),
"WHITE" : (255, 255,255),
 
 
"ALICE_BLUE" : (240, 248, 255),
"AQUA" : (0, 255, 255),
"AQUAMARINE" : (127, 255, 212),
"AQUAMARINE_1" : (127, 255, 212),
"AQUAMARINE_2" : (118, 238, 198),
"AQUAMARINE_3" : (102, 205, 170),
"AQUAMARINE_4" : (69, 139, 116),
"AZURE" : (240, 255, 255),
"AZURE_1" : (240, 255, 255),
"AZURE_2" : (224, 238, 238),
"AZURE_3" : (193, 205, 205),
"AZURE_4" : (131, 139, 139),
"BLUE_1" : (0, 0, 255),
"BLUE_2" : (0, 0, 238),
"BLUE_3" : (0, 0, 205),
"BLUE_4" : (0, 0, 139),
"BLUE_VIOLET" : (138, 43, 226),
"CADET_BLUE" : (95, 159, 159),
"CADET_BLUE_1" : (1152, 245, 255),
"CADET_BLUE_2" : (142, 229, 238),
"CADET_BLUE_3" : (122, 197, 205),
"CADET_BLUE_4" : (83, 134, 139),
"CORN_FLOWER_BLUE" : (66, 66, 111),
"CYAN" : (0, 255, 255),
"CYAN_1" : (0, 255, 255),
"CYAN_2" : (0, 238, 238),
"CYAN_3" : (0, 205, 205),
"CYAN_4" : (0, 139, 139),
"DARK_SLATE_BLUE" : (36, 24, 130),
"DARK_TURQUOISE" : (112, 147, 219),
"DEEP_SKY_BLUE" : (0, 191, 255),
"DEEP_SKY_BLUE_1" : (0, 191, 255),
"DEEP_SKY_BLUE_2" : (0, 178, 238),
"DEEP_SKY_BLUE_3" : (0, 154, 205),
"DEEP_SKY_BLUE_4" : (0, 104, 139),
"DODGER_BLUE" : (30, 144, 255),
"DODGER_BLUE_1" : (30, 144, 255),
"DODGER_BLUE_2" : (28, 134, 238),
"DODGER_BLUE_3" : (24, 116, 205),
"DODGER_BLUE_4" : (16, 78, 139),
"FREE_SPEECH_BLUE" : (65, 86, 197),
"LIGHT_BLUE" : (173, 216, 230),
"LIGHT_BLUE_1" : (191, 239, 255),
"LIGHT_BLUE_2" : (178, 223, 238),
"LIGHT_BLUE_3" : (154, 192, 205),
"LIGHT_BLUE_4" : (104, 131, 139),
"LIGHT_CYAN" : (224, 255, 255),
"LIGHT_CYAN_1" : (224, 255, 255),
"LIGHT_CYAN_2" : (209, 238, 238),
"LIGHT_CYAN_3" : (180, 205, 205),
"LIGHT_CYAN_4" : (122, 139, 139),
"LIGHT_SKY_BLUE" : (135, 206, 250),
"LIGHT_SKY_BLUE_1" : (176, 226, 255),
"LIGHT_SKY_BLUE_2" : (164, 211, 238),
"LIGHT_SKY_BLUE_3" : (141, 182, 205),
"LIGHT_SKY_BLUE_4" : (96, 123, 139),
"LIGHT_SLATE_BLUE" : (132, 112, 255),
"LIGHT_STEEL_BLUE" : (176, 196, 222),
"LIGHT_STEEL_BLUE_1" : (202, 225, 255),
"LIGHT_STEEL_BLUE_2" : (188, 210, 238),
"LIGHT_STEEL_BLUE_3" : (162, 181, 205),
"LIGHT_STEEL_BLUE_4" : (110, 123, 139),
"MEDIUM_BLUE" : (0, 0, 205),
"MEDIUM_SLATE_BLUE" : (123, 104, 238),
"MEDIUM_TURQUOISE" : (72, 209, 204),
"MIDNIGHT_BLUE" : (25, 25, 112),
"NAVY" : (0, 0, 128),
"NAVY_BLUE" : (0, 0, 128),
"NEON_BLUE" : (77, 77, 255),
"NEW_MIDNIGHT_BLUE" : (0, 0, 156),
"PALE_TURQUOISE" : (187, 255, 255),
"PALE_TURQUOISE_1" : (187, 255, 255),
"PALE_TURQUOISE_2" : (174, 238, 238),
"PALE_TURQUOISE_3" : (150, 205, 205),
"PALE_TURQUOISE_4" : (102, 139, 139),
"POWDER_BLUE" : (176, 224, 230),
"RICH_BLUE" : (89, 89, 171),
"ROYAL_BLUE" : (65, 105, 225),
"ROYAL_BLUE_1" : (72, 118, 255),
"ROYAL_BLUE_2" : (67, 110, 238),
"ROYAL_BLUE_3" : (58, 95, 205),
"ROYAL_BLUE_4" : (39, 64, 139),
"ROYAL_BLUE_5" : (0, 34, 102),
"SKY_BLUE" : (135, 206, 235),
"SKY_BLUE_1" : (135, 206, 255),
"SKY_BLUE_2" : (126, 192, 238),
"SKY_BLUE_3" : (108, 166, 205),
"SKY_BLUE_4" : (74, 112, 139),
"SLATE_BLUE" : (131, 111, 255),
"SLATE_BLUE_1" : (122, 103, 238),
"SLATE_BLUE_2" : (122, 103, 238),
"SLATE_BLUE_3" : (105, 89, 205),
"SLATE_BLUE_4" : (71, 60, 139),
"STEEL_BLUE" : (70, 130, 180),
"STEEL_BLUE_1" : (99, 184, 255),
"STEEL_BLUE_2" : (92, 172, 238),
"STEEL_BLUE_3" : (79, 148, 205),
"STEEL_BLUE_4" : (54, 100, 139),
"SUMMER_SKY" : (56, 176, 222),
"TEAL" : (0, 128, 128),
"TRUE_IRIS_BLUE" : (3, 180, 204),
"TURQUOISE" : (64, 224, 208),
"TURQUOISE_1" : (0, 245, 255),
"TURQUOISE_2" : (0, 229, 238),
"TURQUOISE_3" : (0, 197, 205),
"TURQUOISE_4" : (0, 134,139),
 
 
"BAKERS_CHOCOLATE" : (92, 51, 23),
"BEIGE" : (245, 245, 220),
"BROWN" : (166, 42, 42),
"BROWN_1" : (255, 64, 64),
"BROWN_2" : (238, 59, 59),
"BROWN_3" : (205, 51, 51),
"BROWN_4" : (139, 35, 35),
"BURLYWOOD" : (222, 184, 135),
"BURLYWOOD_1" : (255, 211, 155),
"BURLYWOOD_2" : (238, 197, 145),
"BURLYWOOD_3" : (205, 170, 125),
"BURLYWOOD_4" : (139, 115, 85),
"CHOCOLATE" : (210, 105, 30),
"CHOCOLATE_1" : (255, 127, 36),
"CHOCOLATE_2" : (238, 118, 33),
"CHOCOLATE_3" : (205, 102, 29),
"CHOCOLATE_4" : (139, 69, 19),
"DARK_BROWN" : (92, 64, 51),
"DARK_TAN" : (151, 105, 79),
"DARK_WOOD" : (133, 94, 66),
"LIGHT_WOOD" : (133, 99, 99),
"MEDIUM_WOOD" : (166, 128, 100),
"NEW_TAN" : (235, 199, 158),
"PERU" : (205, 133, 63),
"ROSY_BROWN" : (188, 143, 143),
"ROSY_BROWN_1" : (255, 193, 193),
"ROSY_BROWN_2" : (238, 180, 180),
"ROSY_BROWN_3" : (205, 155, 155),
"ROSY_BROWN_4" : (139, 105, 105),
"SADDLE_BROWN" : (139, 69, 19),
"SANDY_BROWN" : (244, 164, 96),
"SEMI_SWEET_CHOCOLATE" : (107, 66, 38),
"SIENNA" : (142, 107, 35),
"TAN" : (219, 147, 112),
"TAN_1" : (255, 165, 79),
"TAN_2" : (238, 154, 73),
"TAN_3" : (205, 133, 63),
"TAN_4" : (139, 90, 43),
"VERY_DARK_BROWN" : (92, 64,51),
 
"CHARTREUSE" : (127, 255, 0),
"CHARTREUSE_1" : (127, 255, 0),
"CHARTREUSE_2" : (118, 238, 0),
"CHARTREUSE_3" : (102, 205, 0),
"CHARTREUSE_4" : (69, 139, 0),
"DARK_GREEN" : (47, 79, 47),
"DARK_GREEN_COPPER" : (74, 118, 110),
"DARK_KHAKI" : (189, 183, 107),
"DARK_OLIVE_GREEN" : (85, 107, 47),
"DARK_OLIVE_GREEN_1" : (202, 255, 112),
"DARK_OLIVE_GREEN_2" : (188, 238, 104),
"DARK_OLIVE_GREEN_3" : (162, 205, 90),
"DARK_OLIVE_GREEN_4" : (110, 139, 61),
"DARK_SEA_GREEN" : (143, 188, 143),
"DARK_SEA_GREEN_1" : (193, 255, 193),
"DARK_SEA_GREEN_2" : (180, 238, 180),
"DARK_SEA_GREEN_3" : (155, 205, 155),
"DARK_SEA_GREEN_4" : (105, 139, 105),
"FOREST_GREEN" : (34, 139, 34),
"FREE_SPEECH_GREEN" : (9, 249, 17),
"GREEN_1" : (0, 255, 0),
"GREEN_2" : (0, 238, 0),
"GREEN_3" : (0, 205, 0),
"GREEN_4" : (0, 139, 0),
"GREEN_YELLOW" : (173, 255, 47),
"KHAKI" : (240, 230, 140),
"KHAKI_1" : (255, 246, 143),
"KHAKI_2" : (238, 230, 133),
"KHAKI_3" : (205, 198, 115),
"KHAKI_4" : (139, 134, 78),
"LAWN_GREEN" : (124, 252, 0),
"LIGHT_SEA_GREEN" : (32, 178, 170),
"LIME" : (0, 255, 0),
"MEDIUM_SEA_GREEN" : (60, 179, 113),
"MEDIUM_SPRING_GREEN" : (0, 250, 154),
"MINT_CREAM" : (245, 255, 250),
"OLIVE" : (128, 128, 0),
"OLIVE_DRAB" : (107, 142, 35),
"OLIVE_DRAB_1" : (192, 255, 62),
"OLIVE_DRAB_2" : (179, 238, 58),
"OLIVE_DRAB_3" : (154, 205, 50),
"OLIVE_DRAB_4" : (105, 139, 34),
"PALE_GREEN" : (152, 251, 152),
"PALE_GREEN_1" : (154, 255, 154),
"PALE_GREEN_2" : (144, 238, 144),
"PALE_GREEN_3" : (124, 205, 124),
"PALE_GREEN_4" : (84, 139, 84),
"SEA_GREEN" : (46, 139, 87),
"SEA_GREEN_1" : (84, 255, 159),
"SEA_GREEN_2" : (78, 238, 148),
"SEA_GREEN_3" : (67, 205, 128),
"SEA_GREEN_4" : (46, 139, 87),
"SPRING_GREEN" : (0, 255, 127),
"SPRING_GREEN_1" : (0, 255, 127),
"SPRING_GREEN_2" : (0, 238, 118),
"SPRING_GREEN_3" : (0, 205, 102),
"SPRING_GREEN_4" : (0, 139, 69),
"YELLOW_GREEN" : (154, 205,50),
"BISQUE" : (255, 228, 196),
"BISQUE_1" : (255, 228, 196),
"BISQUE_2" : (238, 213, 183),
"BISQUE_3" : (205, 183, 158),
"BISQUE_4" : (139, 125, 107),
"CORAL" : (255, 127, 0),
"CORAL_1" : (255, 114, 86),
"CORAL_2" : (238, 106, 80),
"CORAL_3" : (205, 91, 69),
"CORAL_4" : (139, 62, 47),
"DARK_ORANGE" : (255, 140, 0),
"DARK_ORANGE_1" : (255, 127, 0),
"DARK_ORANGE_2" : (238, 118, 0),
"DARK_ORANGE_3" : (205, 102, 0),
"DARK_ORANGE_4" : (139, 69, 0),
"DARK_SALMON" : (233, 150, 122),
"HONEYDEW" : (240, 255, 240),
"HONEYDEW_1" : (240, 255, 240),
"HONEYDEW_2" : (224, 238, 224),
"HONEYDEW_3" : (193, 205, 193),
"HONEYDEW_4" : (131, 139, 131),
"LIGHT_CORAL" : (240, 128, 128),
"LIGHT_SALMON" : (255, 160, 122),
"LIGHT_SALMON_1" : (255, 160, 122),
"LIGHT_SALMON_2" : (238, 149, 114),
"LIGHT_SALMON_3" : (205, 129, 98),
"LIGHT_SALMON_4" : (139, 87, 66),
"MANDARIN_ORANGE" : (142, 35, 35),
"ORANGE" : (255, 165, 0),
"ORANGE_1" : (255, 165, 0),
"ORANGE_2" : (238, 154, 0),
"ORANGE_3" : (205, 133, 0),
"ORANGE_4" : (139, 90, 0),
"ORANGE_RED" : (255, 36, 0),
"PEACH_PUFF" : (255, 218, 185),
"PEACH_PUFF_1" : (255, 218, 185),
"PEACH_PUFF_2" : (238, 203, 173),
"PEACH_PUFF_3" : (205, 175, 149),
"PEACH_PUFF_4" : (139, 119, 101),
"SALMON" : (250, 128, 114),
"SALMON_1" : (255, 140, 105),
"SALMON_2" : (238, 130, 98),
"SALMON_3" : (205, 112, 84),
"SALMON_4" : (139, 76, 57),
"SIENNA_1" : (255, 130, 71),
"SIENNA_2" : (238, 121, 66),
"SIENNA_3" : (205, 104, 57),
"SIENNA_4" : (139, 71, 38),
"DEEP_PINK," : (255, 20, 147),
"DEEP_PINK_1" : (255, 20, 147),
"DEEP_PINK_2" : (238, 18, 137),
"DEEP_PINK_3" : (205, 16, 118),
"DEEP_PINK_4" : (139, 10, 80),
"DUSTY_ROSE" : (133, 99, 99),
"FIREBRICK" : (178, 34, 34),
"FIREBRICK_1" : (255, 48, 48),
"FIREBRICK_2" : (238, 44, 44),
"FIREBRICK_3" : (205, 38, 38),
"FIREBRICK_4" : (139, 26, 26),
"FELDSPAR" : (209, 146, 117),
"FLESH" : (245, 204, 176),
"FREE_SPEECH_MAGENTA" : (227, 91, 216),
"FREE_SPEECH_RED" : (192, 0, 0),
"HOT_PINK" : (255, 105, 180),
"HOT_PINK_1" : (255, 110, 180),
"HOT_PINK_2" : (238, 106, 167),
"HOT_PINK_3" : (205, 96, 144),
"HOT_PINK_4" : (139, 58, 98),
"INDIAN_RED" : (205, 92, 92),
"INDIAN_RED_1" : (255, 106, 106),
"INDIAN_RED_2" : (238, 99, 99),
"INDIAN_RED_3" : (205, 85, 85),
"INDIAN_RED_4" : (139, 58, 58),
"LIGHT_PINK" : (255, 182, 193),
"LIGHT_PINK_1" : (255, 174, 185),
"LIGHT_PINK_2" : (238, 162, 173),
"LIGHT_PINK_3" : (205, 140, 149),
"LIGHT_PINK_4" : (139, 95, 101),
"MEDIUM_VIOLET_RED" : (199, 21, 133),
"MISTY_ROSE" : (255, 228, 225),
"MISTY_ROSE_1" : (255, 228, 225),
"MISTY_ROSE_2" : (238, 213, 210),
"MISTY_ROSE_3" : (205, 183, 181),
"MISTY_ROSE_4" : (139, 125, 123),
"ORANGE_RED_1" : (255, 69, 0),
"ORANGE_RED_2" : (238, 64, 0),
"ORANGE_RED_3" : (205, 55, 0),
"ORANGE_RED_4" : (139, 37, 0),
"PALE_VIOLET_RED" : (219, 112, 147),
"PALE_VIOLET_RED_1" : (255, 130, 171),
"PALE_VIOLET_RED_2" : (238, 121, 159),
"PALE_VIOLET_RED_3" : (205, 104, 137),
"PALE_VIOLET_RED_4" : (139, 71, 93),
"PINK" : (255, 192, 203),
"PINK_1" : (255, 181, 197),
"PINK_2" : (238, 169, 184),
"PINK_3" : (205, 145, 158),
"PINK_4" : (139, 99, 108),
"RED_1" : (255, 0, 0),
"RED_2" : (238, 0, 0),
"RED_3" : (205, 0, 0),
"RED_4" : (139, 0, 0),
"SCARLET" : (140, 23, 23),
"SPICY_PINK" : (255, 28, 174),
"TOMATO" : (255, 99, 71),
"TOMATO_1" : (255, 99, 71),
"TOMATO_2" : (238, 92, 66),
"TOMATO_3" : (205, 79, 57),
"TOMATO_4" : (139, 54, 38),
"VIOLET_RED" : (208, 32, 144),
"VIOLET_RED_1" : (255, 62, 150),
"VIOLET_RED_2" : (238, 58, 140),
"VIOLET_RED_3" : (205, 50, 120),
"VIOLET_RED_4" : (139, 34, 82),
 
"DARK_ORCHID," : (153, 50, 204),
"DARK_ORCHID_1" : (191, 62, 255),
"DARK_ORCHID_2" : (178, 58, 238),
"DARK_ORCHID_3" : (154, 50, 205),
"DARK_ORCHID_4" : (104, 34, 139),
"DARK_PURPLE" : (135, 31, 120),
"DARK_VIOLET" : (148, 0, 211),
"FUCHSIA" : (255, 0, 255),
"LAVENDER" : (230, 230, 250),
"LAVENDER_BLUSH" : (255, 240, 245),
"LAVENDER_BLUSH_1" : (255, 240, 245),
"LAVENDER_BLUSH_2" : (238, 224, 229),
"LAVENDER_BLUSH_3" : (205, 193, 197),
"LAVENDER_BLUSH_4" : (139, 131, 134),
"MAGENTA" : (255, 0, 255),
"MAGENTA_1" : (255, 0, 255),
"MAGENTA_2" : (238, 0, 238),
"MAGENTA_3" : (205, 0, 205),
"MAGENTA_4" : (139, 0, 139),
"MAROON" : (176, 48, 96),
"MAROON_1" : (255, 52, 179),
"MAROON_2" : (238, 48, 167),
"MAROON_3" : (205, 41, 144),
"MAROON_4" : (139, 28, 98),
"MEDIUM_ORCHID" : (186, 85, 211),
"MEDIUM_ORCHID_1" : (224, 102, 255),
"MEDIUM_ORCHID_2" : (209, 95, 238),
"MEDIUM_ORCHID_3" : (180, 82, 205),
"MEDIUM_ORCHID_4" : (122, 55, 139),
"MEDIUM_PURPLE" : (147, 112, 219),
"MEDIUM_PURPLE_1" : (171, 130, 255),
"MEDIUM_PURPLE_2" : (159, 121, 238),
"MEDIUM_PURPLE_3" : (137, 104, 205),
"MEDIUM_PURPLE_4" : (93, 71, 139),
"NEON_PINK" : (255, 110, 199),
"ORCHID" : (218, 112, 214),
"ORCHID_1" : (219, 112, 219),
"ORCHID_2" : (238, 122, 233),
"ORCHID_3" : (205, 105, 201),
"ORCHID_4" : (139, 71, 137),
"PLUM" : (221, 160, 221),
"PLUM_1" : (255, 187, 255),
"PLUM_2" : (238, 174, 238),
"PLUM_3" : (205, 150, 205),
"PLUM_4" : (139, 102, 139),
"PURPLE" : (160, 32, 240),
"PURPLE_1" : (155, 48, 255),
"PURPLE_2" : (145, 44, 238),
"PURPLE_3" : (125, 38, 205),
"PURPLE_4" : (85, 26, 139),
"THISTLE" : (216, 191, 216),
"THISTLE_1" : (255, 225, 255),
"THISTLE_2" : (238, 210, 238),
"THISTLE_3" : (205, 181, 205),
"THISTLE_4" : (139, 123, 139),
"VIOLET" : (238, 130, 238),
"VIOLET_BLUE" : (159, 95, 159),
 
"BLANCHED_ALMOND," : (255, 235, 205),
"DARK_GOLDENROD" : (184, 134, 11),
"DARK_GOLDENROD_1" : (255, 185, 15),
"DARK_GOLDENROD_2" : (238, 173, 14),
"DARK_GOLDENROD_3" : (205, 149, 12),
"DARK_GOLDENROD_4" : (139, 101, 8),
"LEMON_CHIFFON" : (255, 250, 205),
"LEMON_CHIFFON_1" : (255, 250, 205),
"LEMON_CHIFFON_2" : (238, 233, 191),
"LEMON_CHIFFON_3" : (205, 201, 165),
"LEMON_CHIFFON_4" : (139, 137, 112),
"LIGHT_GOLDENROD" : (238, 221, 130),
"LIGHT_GOLDENROD_1" : (255, 236, 139),
"LIGHT_GOLDENROD_2" : (238, 220, 130),
"LIGHT_GOLDENROD_3" : (205, 190, 112),
"LIGHT_GOLDENROD_4" : (139, 129, 76),
"LIGHT_GOLDENROD_YELLOW" : (250, 250, 210),
"LIGHT_YELLOW" : (255, 255, 224),
"LIGHT_YELLOW_1" : (255, 255, 224),
"LIGHT_YELLOW_2" : (238, 238, 209),
"LIGHT_YELLOW_3" : (205, 205, 180),
"LIGHT_YELLOW_4" : (139, 139, 122),
"PALE_GOLDENROD" : (238, 232, 170),
"PAPAYA_WHIP" : (255, 239, 213),
"CORNSILK" : (255, 248, 220),
"CORNSILK_1" : (255, 248, 220),
"CORNSILK_2" : (238, 232, 205),
"CORNSILK_3" : (205, 200, 177),
"CORNSILK_4" : (139, 236, 120),
"GOLDENROD" : (218, 165, 32),
"GOLDENROD_1" : (255, 193, 37),
"GOLDENROD_2" : (238, 180, 34),
"GOLDENROD_3" : (205, 155, 29),
"GOLDENROD_4" : (139, 105, 20),
"MOCCASIN" : (255, 228, 181),
"YELLOW" : (255, 255, 0),
"YELLOW_1" : (255, 255, 0),
"YELLOW_2" : (238, 238, 0),
"YELLOW_3" : (205, 205, 0),
"YELLOW_4" : (139, 139, 0),
"GOLD" : (255, 215, 0),
"GOLD_1" : (255, 215, 0),
"GOLD_2" : (238, 201, 0),
"GOLD_3" : (205, 173, 0),
"GOLD_4" : (139, 117, 0),
"MEDIUM_GOLDENROD" : (234, 234, 174),
"ANTIQUE_WHITE" : (250, 235, 215),
"ANTIQUE_WHITE_1" : (255, 239, 219),
"ANTIQUE_WHITE_2" : (238, 223, 204),
"ANTIQUE_WHITE_3" : (205, 192, 176),
"ANTIQUE_WHITE_4" : (139, 131, 120),
"FLORAL_WHITE" : (255, 250, 240),
"GHOST_WHITE" : (248, 248, 255),
"NAVAJO_WHITE" : (255, 222, 173),
"NAVAJO_WHITE_1" : (255, 222, 173),
"NAVAJO_WHITE_2" : (238, 207, 161),
"NAVAJO_WHITE_3" : (205, 179, 139),
"NAVAJO_WHITE_4" : (139, 121, 94),
"OLD_LACE" : (253, 245, 230),
"WHITE_SMOKE" : (245, 245, 245),
"GAINSBORO" : (220, 220, 220),
"IVORY" : (255, 255, 240),
"IVORY_1" : (255, 255, 240),
"IVORY_2" : (238, 238, 224),
"IVORY_3" : (205, 205, 193),
"IVORY_4" : (139, 139, 131),
"LINEN" : (250, 240, 230),
"SEASHELL" : (255, 245, 238),
"SEASHELL_1" : (255, 245, 238),
"SEASHELL_2" : (238, 229, 222),
"SEASHELL_3" : (205, 197, 191),
"SEASHELL_4" : (139, 134, 130),
"SNOW" : (255, 250, 250),
"SNOW_1" : (255, 250, 250),
"SNOW_2" : (238, 233, 233),
"SNOW_3" : (205, 201, 201),
"SNOW_4" : (139, 137, 137),
"WHEAT" : (245, 222, 179),
"WHEAT_1" : (255, 231, 186),
"WHEAT_2" : (238, 216, 174),
"WHEAT_3" : (205, 186, 150),
"WHEAT_4" : (139, 126, 102),
"QUARTZ" : (217, 217, 243),
}
clr=colors.get("limeGreen")
#create dispay wind with any name y like
screen=pygame.display.set_mode((WIDTH,HEIGHT)) 
pygame.display.set_caption("My First Game")  #change the title of my window

#images
bg=pygame.image.load('pygameFiles/Images/images/bgSmaller.jpeg')
char = pygame.image.load('pygameFiles/Images/images/PixelArtTutorial.png')
char = pygame.transform.scale(char, (50, 50))
# screen.blit(bg, (0,0))
# pygame.display.update()
# pygame.time.delay(5000)

#square Var
hb=50
wb=50
xb=100
yb=300

#character vars
charx = xb
chary = yb

#circle
cx=350
cy=350
rad=25

#inscribed box
ibox = rad*math.sqrt(2)
xig = cx-(ibox/2)
yig = cy-(ibox/2)

#mouse varuables
mx = 0
my = 0

#objects to draw
square=pygame.Rect(xb,yb,wb,hb)
insSquare=pygame.Rect(xig,yig,ibox,ibox)
mountainSqaure = pygame.Rect(250, 320, 180, 250)
#TIC TAC VARIA
x_wins = 0
o_wins = 0   

clock = pygame.time.Clock()
player=1
markers=[]      
lineWidth=10        
Game=True     
Gameover=False      
MxMy=(0,0)      
cirClr=colors.get("pink") 
xClr=colors.get("BLACK") 

#collors
squareClr=colors.get("pink")
circleClr=colors.get("blue")
backgrnd=colors.get("white")
buttoncolor=colors.get('pink')

#Game control
run = True
Game = False
speed=2

#Menu items
message = ["Instructions", "Settings", "Game 1", "Game 2", "Scoreboard", "Exit"]
#for game 2 
player=1
markers=[]
lineWidth=10
Game=True
gameOver=False
Xpoints= 0
Opoints= 0
MxMy=(0,0)
print(markers)  
cirClr=colors.get("blue")
xClr=colors.get("BLACK")
def input_name():
    # name variable
    user_name = "" #making sure no preset name is there 


    Title = TITLE_FONT.render("Input name", 1, colors.get("blue")) #input name 
    user_text = MENU_FONT.render(user_name,1, colors.get("BLACK"))

    #fills screen with white
    screen.fill(colors.get("white"))


    # renderig fonts to the screen
    xd = WIDTH//2 - (Title.get_width()//2)
    screen.blit(Title, (xd, 50))
    # text1_x = WIDTH//2 - (text1.get_width()//2)
    
    button_box_x = WIDTH//2 - WIDTH//4
    Button_box = pygame.Rect(button_box_x, 400, WIDTH//2, 50) #making this a changable button 
    pygame.draw.rect(screen, colors.get("pink"), Button_box)

    pygame.display.update() #notes we toook in class 
    run = True    
    while run: 
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    print(user_name) 
                    pygame.quit()
                    sys.exit()#exiting 

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mousePos = pygame.mouse.get_pos()
                    mx = mousePos[0]
                    my = mousePos[1]
                    

                if event.type == pygame.KEYDOWN:
                    if event.key ==  pygame.K_RETURN: # enter the name
                        run = False
                        print(user_name) 
                    if event.key == pygame.K_BACKSPACE: # remove the last letter of the name
                        user_name = user_name[0:len(user_name)-1]
                    elif event.key != pygame.K_RETURN: # add the character to the end of the string
                        user_name += event.unicode 

                    pygame.draw.rect(screen, colors.get("limeGreen"), Button_box)
                    user_text = MENU_FONT.render(user_name,1, colors.get("BLACK"))
                    screen.blit(user_text, (button_box_x + 20, 410))
                    pygame.display.update()       # updates the screen

def menu(): #doing the menu so much fun 
    screen.fill(backgrnd)
    ymenu = 155
    Title = TITLE_FONT.render("Home Page", 1, colors.get("blue"))
    xd = WIDTH//2 - (Title.get_width()//2)
    screen.blit(Title, (xd, 100))
    Bx = WIDTH//3

    Button_1 = pygame.Rect(Bx, 150, WIDTH//4, 40) #creating buttons for the menu and giving options on what to do 
    Button_2 = pygame.Rect(Bx, 200, WIDTH//4, 40) #creating buttons for the menu and giving options on what to do 
    Button_3 = pygame.Rect(Bx, 250, WIDTH//4, 40) #creating buttons for the menu and giving options on what to do 
    Button_4 = pygame.Rect(Bx, 300, WIDTH//4, 40) #creating buttons for the menu and giving options on what to do 
    Button_5 = pygame.Rect(Bx, 350, WIDTH//4, 40) #creating buttons for the menu and giving options on what to do 
    Button_6 = pygame.Rect(Bx, 400, WIDTH//4, 40) #creating buttons for the menu and giving options on what to do 
    pygame.draw.rect(screen,buttoncolor, Button_1) #drawing the buttons
    pygame.draw.rect(screen,buttoncolor, Button_2) #drawing the buttons
    pygame.draw.rect(screen,buttoncolor, Button_3) #drawing the buttons
    pygame.draw.rect(screen,buttoncolor, Button_4) #drawing the buttons
    pygame.draw.rect(screen,buttoncolor, Button_5) #drawing the buttons
    pygame.draw.rect(screen,buttoncolor, Button_6) #drawing the buttons

    for item in message:
        text = MENU_FONT.render(item, 1, colors.get('blue'))
        screen.blit(text, (Bx, ymenu)) #putting on the screen 
        pygame.display.update() 
        pygame.time.delay(50)
        ymenu += 50
    
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                mx = mousePos[0] #saying depending on where the button clicks 
                my = mousePos[1]
                if Button_1.collidepoint((mx, my)):
                    Instructions("Instructions", "pygameFiles/Images/instructions.txt") #opening instructions file 
                if Button_2.collidepoint((mx, my)):
                    settings()
                if Button_3.collidepoint((mx, my)): #opening the functions depending on that 
                    game1()
                if Button_4.collidepoint((mx, my)):
                    game2()
                if Button_5.collidepoint((mx, my)):
                    Instructions ("Scoreboard", "pythonFIles/scre.txt") #opening score file 
                if Button_6.collidepoint((mx, my)):
                    pygame.quit()
                    sys.exit()

def Instructions(TITLE,FILE):
    #rendering text objects
    Title = TITLE_FONT.render("Instructions", 1, colors.get("blue"))
    Title = TITLE_FONT.render(TITLE, 1, colors.get("blue"))

    #fills screen with white
    screen.fill(backgrnd)

    #creating button options
    #Button_1 = pygame.Rect(200, 400, 100, 50)
    #Button_2 = pygame.Rect(400, 400, 100, 50)
    #pygame.draw.rect(screen, colors.get("limeGreen"), Button_1)
    #pygame.draw.rect(screen, colors.get("limeGreen"), Button_2)

    #Instructions
    myFile = open(FILE, "r")
    content = myFile.readlines()

    #var to controll change of line
    yinstructions = 150
    for line in content:
        Instruc = MENU_FONT.render(line[0:-1], 1, colors.get("blue"))
        screen.blit(Instruc, (40, yinstructions))
        pygame.display.update()
        pygame.time.delay(50)
        yinstructions += 40

    myFile.close()

    #renderig fonts to the screen
    xd = WIDTH//2 - (Title.get_width()//2)
    #screen.blit(Title, (xd, 50))
    #screen.blit(text1, (Bx, 300)) #help 

    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                menu()
                print("Y quit")
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                mx = mousePos[0]
                my = mousePos[1]
                #if Button_1.collidepoint((mx, my)):
                    #return True 
def settings (): #settings for this 
    global WIDTH, HEIGHT, backgrnd, buttoncolor, screen, mx, my
    screen.fill(backgrnd)
    ymenu = 155
    Title = TITLE_FONT.render("Settings", 1, colors.get("blue"))
    xd = WIDTH//2 - (Title.get_width()//2)
    screen.blit(Title, (xd, 100))
    Bx = WIDTH//3
    colorRand = MENU_FONT.render("Randomize background color", 1, colors.get("blue")) #all the things you can do 
    bgcolor = MENU_FONT.render("Randomize button color", 1, colors.get("blue")) #all the things you can do 
    sizeincrease = MENU_FONT.render("Increase screen size",1, colors.get ("blue")) #all the things you can do 
    sizedecrease = MENU_FONT.render("Decrease screen size",1, colors.get ("blue")) #all the things you can do 
    done = MENU_FONT.render("Done changing settings",1, colors.get ("blue")) #all the things you can do 

    Button_Background = pygame.Rect(Bx, 150, WIDTH//3, 40) #making buttons for option s
    Button_Characters = pygame.Rect(Bx, 200, WIDTH//3, 40) #making buttons for option s
    Button_ScreensizeIncrease = pygame.Rect(Bx, 250, WIDTH//3, 40) #making buttons for option s
    Button_ScreensizeDecrease = pygame.Rect(Bx, 300, WIDTH//3, 40) #making buttons for option s
    Button_Done = pygame.Rect(Bx, 350, WIDTH//3, 40) #making buttons for option s

    pygame.draw.rect(screen, buttoncolor, Button_Background) #drawing the buttons
    pygame.draw.rect(screen, buttoncolor, Button_Characters) #drawing the buttons
    pygame.draw.rect(screen, buttoncolor, Button_ScreensizeIncrease) #drawing the buttons
    pygame.draw.rect(screen, buttoncolor, Button_ScreensizeDecrease) #drawing the buttons
    pygame.draw.rect(screen, buttoncolor, Button_Done) #drawing the buttons

    screen.blit(colorRand, (WIDTH//2 - (colorRand.get_width()//2), 160)) #putting them on the screen
    screen.blit(bgcolor, (WIDTH//2 - (bgcolor.get_width()//2), 210)) #putting them on the screen
    screen.blit(sizeincrease, (WIDTH//2 - (sizeincrease.get_width()//2), 260)) #putting them on the screen
    screen.blit(sizedecrease, (WIDTH//2 - (sizedecrease.get_width()//2), 310)) #putting them on the screen
    screen.blit(done, (WIDTH//2 - (done.get_width()//2), 360))  #putting them on the screen
    pygame.display.update() #putting them on the screen

    while True: #now making the options work 
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                menu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousepos=pygame.mouse.get_pos()
                mx=mousepos[0]
                my=mousepos[1]
                if Button_Background.collidepoint(mx,my):
                    backgrnd=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
                    screen.fill(backgrnd) #randomizing the background colors 
                if Button_Characters.collidepoint(mx,my):
                    buttoncolor=(random.randint(0,255),random.randint(0,255),random.randint(0,255)) # doing the same but with all of the buttons 
                if Button_ScreensizeIncrease.collidepoint(mx,my)and WIDTH < 1100:
                    WIDTH+=100 #adding to wodth and decreasing width 
                    screen=pygame.display.set_mode((WIDTH,HEIGHT)) 
                if Button_ScreensizeDecrease.collidepoint(mx,my)and WIDTH > 500:
                    WIDTH-=100
                    screen=pygame.display.set_mode((WIDTH,HEIGHT))
                if Button_Done.collidepoint(mx,my): #returning to main menu 
                    return menu()
            pygame.display.update()
            settings() 
                    #creen size is plus and minus box 
                    #change width = 800 and redefine screen variables screen=pygame.display.set
def game1(): 

    global run, insSquare, charx, chary, cx, cy, rad
    while run:
        # screen.fill(backgrnd)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                menu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                mx = mousePos[0]
                my = mousePos[1]
                # print(mousePos)
        
        pygame.draw.rect(screen, colors.get("white"), mountainSqaure)
        screen.blit(bg, (0,0))
        keys= pygame.key.get_pressed() #this is a list
        #mve square
        if keys[pygame.K_RIGHT] and square.x < WIDTH -(wb):
            square.x += speed
            charx += speed
        if keys[pygame.K_LEFT] and  square.x > speed:
            square.x -= speed
            charx -= speed
        if keys[pygame.K_UP] and square.y >speed:   #means clser t 0
            square.y -= speed
            chary -= speed
        if keys[pygame.K_DOWN] and square.y <HEIGHT -hb:  #means clser t max value HEIGHT
            square.y += speed
            chary += speed
            #mve Circle
        if keys[pygame.K_d] and cx < WIDTH -(rad):
            cx += speed
            insSquare.x += speed
        if keys[pygame.K_a] and  cx > (speed+rad):
            cx -= speed
            insSquare.x -= speed
        if keys[pygame.K_w] and cy >(speed+rad):   #means clser t 0
            cy -= speed
            insSquare.y -= speed
        if keys[pygame.K_s] and cy <HEIGHT -(rad):  #means clser t max value HEIGHT
            cy += speed
            insSquare.y += speed

        if square.colliderect(insSquare):
            print("BOOM")
            rad+=1
            cx=random.randint(rad, WIDTH-rad)
            cy=random.randint(rad, HEIGHT-rad)
            ibox = rad*math.sqrt(2)
            xig = cx-(ibox/2)
            yig = cy-(ibox/2)
            insSquare=pygame.Rect(xig,yig,ibox,ibox)
        
        if square.colliderect(mountainSqaure):
            square.x = 10
            square.y = 10
            charx = 10
            chary = 10

        #rect(surface, color, rect) -> Rect
        pygame.draw.rect(screen, squareClr,square)
        screen.blit(char, (charx, chary))

        #circle(surface, color, center, radius)
        pygame.draw.rect(screen, squareClr, insSquare)
        pygame.draw.circle(screen, circleClr, (cx,cy), rad)

        pygame.display.update()
        pygame.time.delay(5)
        pygame.display.update()

    global markers, winner, Gameover       

    while True: #mkaing game work 
        player=1 
        lineWidth=10      
        Game=True       
        Gameover=False      
        MxMy=(0,0)     
        cirClr=colors.get("pink") #circles and boxes nd stuff
        xClr=colors.get("BLACK") 
        markers = [] 

        zero_Array()
        while Game:
            clock.tick(60)
            screen.fill(backgrnd) #filling background colors and drawing stff 
            draw_grid()
            draw_Markers()
            for event in pygame.event.get():
                if event.type==pygame.QUIT: # if wants to exit 
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    MxMy = pygame.mouse.get_pos()
                    cellx=MxMy[0]//(WIDTH//3)
                    celly=MxMy[1]//(HEIGHT//3) #the cells and clicks and appearance of the game 
                    if markers[cellx][celly]==0:
                        markers[cellx][celly]=player
                        player *=-1
                        
                        winner = checkWinner() #chechking winner so can add to file 
                        if Gameover: 
                            draw_Markers()
                            pygame.display.update()
                            pygame.time.delay(1000)
                            gameEnd(winner)
                            Game = False #if you want to play again 
                            play_again() 

def zero_Array(): #mrs suarez helped us with this 
    for x in range(3): #mrs suarez helped us with this 
        row= [0] *3 #mrs suarez helped us with this 
        markers.append(row) #mrs suarez helped us with this 

def draw_grid():#drawing the grid
    lineClr=colors.get("white") #color for the grid 
    for x in range(1,3):
        pygame.draw.line(screen,lineClr,(0,HEIGHT//3*x),(WIDTH,HEIGHT//3*x),lineWidth)  #lines with certain widths and lengths 
        pygame.draw.line(screen,lineClr,(WIDTH//3*x, 0),(WIDTH//3*x,HEIGHT),lineWidth) 
    pygame.time.delay(100) #to make sure theres a timer and stuff 

def draw_Markers():   #drawing X and O 
    xValue=0
    for x in markers:  # to drae our x's and o's on the screen 
        yValue=0 #have to set varibales to something 
        for y in x:  
            if y ==1:
                #drawing the X
                pygame.draw.line(screen,xClr,(xValue * WIDTH//3 + 15, yValue * HEIGHT//3 + 15), (xValue * WIDTH//3 + WIDTH//3-15, yValue * WIDTH//3 + WIDTH//3-15),lineWidth)
                pygame.draw.line(screen, xClr,(xValue*WIDTH//3 +WIDTH//3-15, yValue*HEIGHT//3+15),(xValue *WIDTH//3+15,yValue*HEIGHT//3+HEIGHT//3-15),lineWidth)
            if y==-1:# we did these equations during class, they were difficult for me to understand at firts 
                #drawing the O
                pygame.draw.circle(screen,cirClr,(xValue*WIDTH//3+WIDTH//6,yValue*HEIGHT//3 +HEIGHT//6),WIDTH//6-15, lineWidth)
            yValue +=1
        xValue +=1 
    pygame.display.update() 

def checkWinner(): #creating and functioning the game properly 
    global markers, Gameover, winner
    winner = 0
    length = len(markers) #finding length of line 
    for x in range(length):
        if (markers[x][0] + markers[x][1] + markers[x][2]) == 3: #we did this in class
            winner = 1 #winner wither has to be -1 or 1 for this to work because row will add to be -3 or 3
            Gameover = True #ending the game if this is the case
        if (markers[0][x] + markers[1][x] + markers[2][x]) == 3:
            winner = 1 #all of these are different variations of the ways X can win 
            Gameover = True
    if (markers[0][0] + markers[1][1]+ markers[2][2]) == 3: 
        winner = 1#all of these are different variations of the ways X can win 
        Gameover = True
    if (markers[2][0]+markers[1][1] +markers[0][2]) == 3: 
        winner = 1 #all of these are different variations of the ways X can win 
        Gameover = True
    for x in range(3):
        if (markers[x][0] + markers[x][1] + markers[x][2]) == -3: 
            winner = -1#all of these are different variations of the ways O can win 
            Gameover = True
        if (markers[0][x] + markers[1][x] + markers[2][x]) == -3:
            winner = -1 #all of these are different variations of the ways O can win 
            Gameover = True
    if (markers[0][0] + markers[1][1]+ markers[2][2]) == -3: 
        winner = -1 #all of these are different variations of the ways O can win 
        Gameover = True
    if (markers[2][0]+markers[1][1] +markers[0][2]) == -3: 
        winner = -1 #all of these are different variations of the ways O can win 
        Gameover = True #if thi sis case ending the game 
    if Gameover == False:
        Tie = True #tie meaning no one wins and nothing adds to -3 or 3
        for ROW in markers:
            for COL in ROW:
                if COL == 0:
                    Tie = False 
        if Tie:
            Gameover = True #ending the game as well 
            winner = 0   #not adding anything to the score          

    return winner    #adding points to score 
   
def gameEnd(win): #giving players score 
    global TITLE_FONT, x_wins, o_wins # making them global if someone wins 
    title_Y = 100
    if win == 1: #if adds to this in check winner function 
        x_wins +=1 #adding one to overall score 
        message = "X wins!"
        screen.fill("BROWN")
        Title = TITLE_FONT.render(message, 1, colors.get("blue")) #creating titles and text  
        title_X = WIDTH//2 - (Title.get_width()//2) #creating titles and text  
        screen.blit(Title, (title_X, title_Y)) #creating titles 
        score_message = "X won "+str(x_wins)+" games" #saying what player won what amount of games 
        print(score_message) #printing this 
        showme_score = MENU_FONT.render(score_message, 1, colors.get("BLACK"))
        showme_score_x = WIDTH//2 - (showme_score.get_width()//2)
        screen.blit(showme_score, (showme_score_x, 250))
        pygame.display.update()
        pygame.time.delay(2000)
        
    if win == -1: #if O wins 
        o_wins +=1 #adding one to the scoreboard 
        message = "O wins!" #sending a message 
        screen.fill("PURPLE") #the color of background 
        Title = TITLE_FONT.render(message, 1, colors.get("BLACK")) #txt color 
        title_X = WIDTH//2 - (Title.get_width()//2)
        screen.blit(Title, (title_X, title_Y))
        score_message = "O won "+str(o_wins)+" games" # telling players what variable won what games 
        print(score_message)
        showme_score = MENU_FONT.render(score_message, 1, colors.get("BLACK"))
        showme_score_X = WIDTH//2 - (showme_score.get_width()//2)
        screen.blit(showme_score, (showme_score_X, 250)) #telling you who won what 
        pygame.display.update()
        pygame.time.delay(2000)
    if win == 0: #meaning no on e won "tie" func 
        message = "You tied!"
        screen.fill("green") 
        Title = TITLE_FONT.render(message, 1, colors.get("BLACK")) #text color 
        title_X = WIDTH//2 - (Title.get_width()//2)
        screen.blit(Title, (title_X, title_Y)) #displaying on screen 
        pygame.display.update()
        pygame.time.delay(1000)     

def play_again(): #playing again and shwoing scpres


    play_again_titlefont = pygame.font.SysFont('comicsans', 50)
    buttons_font = pygame.font.SysFont('comicsans', 20)
    Title = play_again_titlefont.render("Want to play again?", 1, colors.get("BLACK")) #asking player if want to play again 
    text1 = buttons_font.render("yes", 1, colors.get("white")) #txt clr
    text2 = buttons_font.render("no", 1, colors.get("white"))

#making the yes and no values buttons 
    screen.fill(colors.get("blue"))
    Button_yes = pygame.Rect(150, 400, 130, 50)
    pygame.draw.rect(screen, colors.get("pink"), Button_yes)
    Button_no = pygame.Rect(400, 400, 130, 50) #making the yes and no values buttons 
    pygame.draw.rect(screen, colors.get("pink"), Button_no)

    xd = WIDTH//2 - (Title.get_width()//2)
    screen.blit(Title, (xd, 50)) #now putting all of these onto the screen 
    screen.blit(text1, (175, 410)) #now putting all of these onto the screen 
    screen.blit(text2, (425, 410)) #now putting all of these onto the screen 

    pygame.display.update() 
    while True:
        for event in pygame.event.get(): #if someone tries to get out of the game
            if event.type==pygame.QUIT: 
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos() 
                mx = mousePos[0] #returning to game and playomg again if yes 
                my = mousePos[1] #no if not hit 
                if Button_yes.collidepoint((mx, my)): 
                    return True 
                if Button_no.collidepoint((mx, my)): 
                    
                    if x_wins > o_wins: 
                        ending_ms = "X won more games" # wasn't sure if we were supposed to do this so I got help with this
                    elif x_wins < o_wins:
                        ending_ms = "O won more games" #essentially just telling you who won more ganes 
                    else:
                        ending_ms = "both players won the same number of games"        

                    screen.fill("BROWN") #filling the background 
                    bye_txt = MENU_FONT.render("Thanks for playing", 1, colors.get("BLACK")) #giving the players a thanks message 
                    bye_txt_x = WIDTH//2 - (bye_txt.get_width()//2)
                    screen.blit(bye_txt, (bye_txt_x, 350))
                    score_message = "X won "+str(x_wins)+" games and O won "+str(o_wins)+" games" #final score at the end 
                    print(score_message)
                    showme_score = MENU_FONT.render(score_message, 1, colors.get("BLACK"))
                    showme_score_x = WIDTH//2 - (showme_score.get_width()//2)
                    screen.blit(showme_score, (showme_score_x, 200))  #shwoing the score and winner
                    showme_winner = MENU_FONT.render(ending_ms, 1, colors.get("BLACK"))
                    showme_winner_x = WIDTH//2 - (showme_winner.get_width()//2) 
                    screen.blit(showme_winner, (showme_winner_x, 270)) #putting on the screen 
                    pygame.display.update() 
                    pygame.time.delay(5000) 
                    pygame.quit()
                    sys.exit()    

def game2():   
    global markers, winner, Gameover       

    while True: #summarizing game 2 and making this a function 
        #will be helpful for my menu 
        player=1 
        lineWidth=10      #lines
        Game=True       
        Gameover=False      
        MxMy=(0,0)     
        cirClr=colors.get("pink") #circle colors and stuff 
        xClr=colors.get("BLACK") #X color
        markers = [] 

        zero_Array()
        while Game:
            clock.tick(60) #creating a habit as Mrs. Suarez says !!
            screen.fill(backgrnd) #filling the background 
            draw_grid()
            draw_Markers()
            for event in pygame.event.get():
                if event.type==pygame.QUIT: #if someone tries to exit 
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    MxMy = pygame.mouse.get_pos() #pretty much placing the X's and O's where they are supposed to go 
                    cellx=MxMy[0]//(WIDTH//3)
                    celly=MxMy[1]//(HEIGHT//3)
                    if markers[cellx][celly]==0:
                        markers[cellx][celly]=player
                        player *=-1
                        
                        winner = checkWinner() #chechking winner, returning to this function 
                        if Gameover: 
                            draw_Markers()
                            pygame.display.update()
                            pygame.time.delay(1000)
                            gameEnd(winner)
                            Game = False
                            play_again() 
                    
            pygame.display.update()
                    
            pygame.display.update() 
input_name()
menu()