'''visualization.py requires a list of boards, a list of boardlengths, and optionally a list of board values, the total value and a boolean that dictates if 
dimensioning lines should be added to the returned image. get_img() is the overarching funtion. First, a background is drawn, then each board is drawn upon it.
The colors are provided in color_reference.py. The globals can be used to change settings of how the image is displayed'''

import color_reference as col_ref
import cv2 as cv
import numpy as np

# CONFIGURATION: 
MARGIN = 27

BOARD_WIDTH = 25
BOARD_SCALAR = 12

VERTICAL_DIST_SCALAR = 3.8

VALUE_SPACE = 40
MARGIN_VALUE_DISP = 100

FONT = cv.FONT_HERSHEY_PLAIN
FONT_SCALE = 0.8
FONT_THICKNESS = 1

BLACK = (0,0,0)
WHITE = (255,255,255)

DIM_SPACE = 15
DIM_LINE = 8

DIM_CROSS_X = 3






def draw_background(boards, board_lens):
    n_of_boards = len(boards)
    background = np.zeros((int(VERTICAL_DIST_SCALAR * BOARD_WIDTH * (n_of_boards + 1)), max(board_lens) * BOARD_SCALAR + 5 * BOARD_WIDTH + VALUE_SPACE, 3),dtype='uint8')        
    return background

def draw_board_on_bg(board, canvas, board_lens, values, index, dimensioned):
    position = 0
    for section in board:
        length = section[1] * BOARD_SCALAR # Scaled, otherwise barely visible.
        quality = section[0]
        if quality in col_ref.color_table:
            r,g,b = col_ref.color_table[quality]
        else:
            r,g,b = (120,120,120)
        # Draw each section of the current board on the background. Index = board number, multiplied by scalar offsets the boards in y direction.
        x1 = position + MARGIN
        y1 = int(index * VERTICAL_DIST_SCALAR * BOARD_WIDTH + MARGIN)
        x2 = position + length + MARGIN
        y2 = int(index * VERTICAL_DIST_SCALAR * BOARD_WIDTH + BOARD_WIDTH + MARGIN)

        cv.rectangle(canvas, (x1, y1), (x2, y2), (r,g,b), thickness=-1) 
        cv.rectangle(canvas, (x1, y1), (x2, y2), WHITE, thickness= 1) 

        # Draw text.
        text = str(quality)
        textsize = cv.getTextSize(text, FONT, FONT_SCALE, FONT_THICKNESS)[0]
        x_pos_text = int((position + (length -textsize[0])/2) + MARGIN)
        y_pos_text = int(((BOARD_WIDTH + textsize[1])/2) + index * VERTICAL_DIST_SCALAR * BOARD_WIDTH + MARGIN)
        cv.putText(canvas, text,(x_pos_text, y_pos_text), FONT, FONT_SCALE, BLACK,FONT_THICKNESS) # textsize is to center the labels 

        if (dimensioned):
            # Draw dimension lines for sections.
            cv.line(canvas, (x1, y2 + DIM_SPACE), (x1, y2 + DIM_SPACE + DIM_LINE), WHITE)
            cv.line(canvas, (x1 + DIM_CROSS_X, y2 + DIM_SPACE), (x1 - DIM_CROSS_X, y2 + DIM_SPACE + DIM_LINE), WHITE)

        # Draw section lenghts.
        dim_text = str(int(length/BOARD_SCALAR))
        dim_size = cv.getTextSize(dim_text, FONT, FONT_SCALE, FONT_THICKNESS)[0]
        x_pos_dim = int((position + (length - dim_size[0])/2) + MARGIN)
        cv.putText(canvas, dim_text, (x_pos_dim, y2 + DIM_SPACE + DIM_LINE), FONT, FONT_SCALE, WHITE, FONT_THICKNESS)

        # Create space for next section.
        position += length 
    
    if (dimensioned):
            
        # Draw missing vertical dimensioning line.
        cv.line(canvas, (position + MARGIN, y2 + DIM_SPACE), (position + MARGIN, y2 + DIM_SPACE + DIM_LINE), WHITE)
        cv.line(canvas, (position + MARGIN + DIM_CROSS_X, y2 + DIM_SPACE), (position + MARGIN - DIM_CROSS_X, y2 + DIM_SPACE + DIM_LINE), WHITE)

    # Draw board length
    tot_len_text = 'L: ' + str(board_lens[index])
    tot_len_size = cv.getTextSize(tot_len_text, FONT, FONT_SCALE, FONT_THICKNESS)[0]
    x_pos_tot_len = int(((board_lens[index] * BOARD_SCALAR) - tot_len_size[0])/2 + MARGIN)
    cv.putText(canvas, tot_len_text, (x_pos_tot_len, y1 - DIM_SPACE), FONT, FONT_SCALE, WHITE, FONT_THICKNESS)

    # Draw value. 
    if (values): 
        cv.putText(canvas, 'VALUE: '+str(values[index]), (canvas.shape[1] - MARGIN_VALUE_DISP, y_pos_text), FONT, FONT_SCALE, WHITE, FONT_THICKNESS) 
    return canvas
     
    


def get_image(boards, board_lens, values = None, total_value = None, dimensioned = False):
    background = draw_background(boards, board_lens)

    for index, board in enumerate(boards): 
        img_with_boards = draw_board_on_bg(board, background, board_lens, values, index, dimensioned)
    

    if (total_value):
        cv.putText(img_with_boards, 'TOTAL VALUE : ' + str(total_value), (VALUE_SPACE + MARGIN, int((len(boards) ) * VERTICAL_DIST_SCALAR * BOARD_WIDTH + MARGIN)), FONT, FONT_SCALE, WHITE, FONT_THICKNESS)
    return img_with_boards
    

































# --------- FOR TESTING THIS MODULE AS A STAND-ALONE ------------------

# boards_before = [[[2,7],[1,5],[3,2]]]  # [quality, length]
# boards_after = [[[4, 2], ['2S', 5], ['1S', 5], [4, 2]]]

# draw_board(boards_before[0])
# draw_board(boards_after[0])

# image_of_boards_before = draw_image(boards_before)
# cv.imshow('Before', image_of_boards_before)

# image_of_boards_after = draw_image(boards_after)
# cv.imshow('After', image_of_boards_after)

# cv.waitKey(0)
# cv.destroyAllWindows()