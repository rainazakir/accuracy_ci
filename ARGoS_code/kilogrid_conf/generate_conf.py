from datetime import datetime
import numpy as np
import sys
no = int(sys.argv[1])
noy = int(sys.argv[2])
nob = int(sys.argv[3])

conf_file_name = '/home/rzakir/Programs/argos3-kilogrid_recordq/conf_files/ASB_experiment_'+str(noy)+'_'+str(nob)+'_'+str(no)
number_of_options = 2
#342,342
option_1_quality = noy
option_2_quality = nob
option_3_quality = 646
option_4_quality = 171
option_5_quality = 58
option_6_quality = 58
option_7_quality = 57
option_8_quality = 57
option_9_quality = 57
option_10_quality = 57


wall_value = 42


module_grid = np.zeros((10, 20), dtype=np.uint8)
cell_grid = np.zeros((20, 40), dtype=np.uint8)

def make_walls(grid):
    grid[:, 0:1] = wall_value
    grid[:, -1:] = wall_value
    grid[0:1, :] = wall_value
    grid[-1:, :] = wall_value
#    print(grid)
    return grid

def distribute_tiles(grid):
    op1 = np.ones((option_1_quality,)) * 1
    op2 = np.ones((option_2_quality,)) * 2
    if number_of_options == 3:
        op3 = np.ones((option_3_quality,)) * 0
        op = np.concatenate((op1, op2, op3))
    elif number_of_options == 4:
        op3 = np.ones((option_3_quality,)) * 3
        op4 = np.ones((option_4_quality,)) * 4
        op = np.concatenate((op1, op2, op3, op4))
    elif number_of_options == 5:
        op3 = np.ones((option_3_quality,)) * 3
        op4 = np.ones((option_4_quality,)) * 4
        op5 = np.ones((option_5_quality,)) * 5
        op = np.concatenate((op1, op2, op3, op4, op5))
    elif number_of_options == 10:
        op3 = np.ones((option_3_quality,)) * 3
        op4 = np.ones((option_4_quality,)) * 4
        op5 = np.ones((option_5_quality,)) * 5
        op6 = np.ones((option_6_quality,)) * 6
        op7 = np.ones((option_7_quality,)) * 7
        op8 = np.ones((option_8_quality,)) * 8
        op9 = np.ones((option_9_quality,)) * 9
        op10 = np.ones((option_10_quality,)) * 10
        op = np.concatenate((op1, op2, op3, op4, op5, op6, op7, op8, op9, op10))
    else:
        op = np.concatenate((op1, op2))
    np.random.shuffle(op)
    op = np.reshape(op, (18, 38))
    grid[1:19, 1:39] = op
 ###   print(grid)
    return grid


if __name__ == "__main__":

    # set up module grid
    module_grid = make_walls(module_grid)

    # set up cell grid
    cell_grid = distribute_tiles(cell_grid)

    # write file
    with open(conf_file_name + '.kconf', 'w') as f:
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        print('# Experiment: ', conf_file_name, file=f)
        print('# Generation Time: ', dt_string, file=f)
        print('\n', file=f)

        # writing for each module
        for x in range(10):
            for y in range(20):
                # print header
                print('address', file=f)
                print('module:' + str(x) + '-' + str(y) + '\n', file=f)
                print('data', file=f)
                # fill with values ..
                print(hex(x), file=f)
                print(hex(y), file=f)
                #print(hex(module_grid[x, y]), file=f)

                if (x == 0) or (x == 9):
                    print(hex(42), file=f)
                #    print(hex(cell_grid[x * 2, y * 2 + 1]), file=f)
                #   print(hex(cell_grid[x * 2 + 1, y * 2 + 1]), file=f)
                # print(hex(cell_grid[x * 2, y * 2]), file=f)
                # print(hex(cell_grid[x * 2 + 1, y * 2]), file=f)

                elif (x == 1 and y == 0) or (x == 1 and y == 19) or (x == 2 and y == 0) or (x == 2 and y == 19) or (
                        x == 3 and y == 0) or (x == 3 and y == 19) or (x == 4 and y == 0) or (x == 4 and y == 19) or (
                        x == 5 and y == 0) or (x == 5 and y == 19) or (x == 6 and y == 0) or (x == 6 and y == 19) or (
                        x == 7 and y == 0) or (x == 7 and y == 19) or (x == 8 and y == 0) or (x == 8 and y == 19):
                    print(hex(62), file=f)

                else:
                        print(hex(module_grid[x, y]), file=f)
                ###print(hex(cell_grid[x * 2, y * 2]))
                print(hex(cell_grid[x * 2, y * 2 + 1]), file=f)
                print(hex(cell_grid[x * 2 + 1, y * 2 + 1]), file=f)
                print(hex(cell_grid[x * 2, y * 2]), file=f)
                print(hex(cell_grid[x * 2 + 1, y * 2]), file=f)
                # needed for structure
                print('', file=f)