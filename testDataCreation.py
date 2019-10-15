

import math


def matlabTestDataPrint(n):

    #For Matlab data
    #Data Format --> A = [0 0 57923 57840 57221 56885 25653 25087 54410 53069;0 0 57923 57840 57221 56885 25653 25087 54410 53069];
    i = 0
    print('E = [', end = '')
    while i < 100:
        print(round(math.sin((i * math.pi) / n), 4), end='')
        print(' ',end = '')
        i = i + 1
    print('];')

    #Seth's Test Data
    #12,6,3
    #E = [0.0 0.2588 0.5 0.7071 0.866 0.9659 1.0 0.9659 0.866 0.7071 0.5 0.2588 0.0 -0.2588 -0.5 -0.7071 -0.866 -0.9659 -1.0 -0.9659 -0.866 -0.7071 -0.5 -0.2588 -0.0 0.2588 0.5 0.7071 0.866 0.9659 1.0 0.9659 0.866 0.7071 0.5 0.2588 0.0 -0.2588 -0.5 -0.7071 -0.866 -0.9659 -1.0 -0.9659 -0.866 -0.7071 -0.5 -0.2588 -0.0 0.2588 0.5 0.7071 0.866 0.9659 1.0 0.9659 0.866 0.7071 0.5 0.2588 0.0 -0.2588 -0.5 -0.7071 -0.866 -0.9659 -1.0 -0.9659 -0.866 -0.7071 -0.5 -0.2588 -0.0 0.2588 0.5 0.7071 0.866 0.9659 1.0 0.9659 0.866 0.7071 0.5 0.2588 0.0 -0.2588 -0.5 -0.7071 -0.866 -0.9659 -1.0 -0.9659 -0.866 -0.7071 -0.5 -0.2588 -0.0 0.2588 0.5 0.7071 ];
    #F = [0.0 0.5 0.866 1.0 0.866 0.5 0.0 -0.5 -0.866 -1.0 -0.866 -0.5 -0.0 0.5 0.866 1.0 0.866 0.5 0.0 -0.5 -0.866 -1.0 -0.866 -0.5 -0.0 0.5 0.866 1.0 0.866 0.5 0.0 -0.5 -0.866 -1.0 -0.866 -0.5 -0.0 0.5 0.866 1.0 0.866 0.5 0.0 -0.5 -0.866 -1.0 -0.866 -0.5 -0.0 0.5 0.866 1.0 0.866 0.5 0.0 -0.5 -0.866 -1.0 -0.866 -0.5 -0.0 0.5 0.866 1.0 0.866 0.5 -0.0 -0.5 -0.866 -1.0 -0.866 -0.5 -0.0 0.5 0.866 1.0 0.866 0.5 0.0 -0.5 -0.866 -1.0 -0.866 -0.5 -0.0 0.5 0.866 1.0 0.866 0.5 -0.0 -0.5 -0.866 -1.0 -0.866 -0.5 -0.0 0.5 0.866 1.0 ];
    #G = [0.0 0.866 0.866 0.0 -0.866 -0.866 -0.0 0.866 0.866 0.0 -0.866 -0.866 -0.0 0.866 0.866 0.0 -0.866 -0.866 -0.0 0.866 0.866 0.0 -0.866 -0.866 -0.0 0.866 0.866 0.0 -0.866 -0.866 -0.0 0.866 0.866 -0.0 -0.866 -0.866 -0.0 0.866 0.866 0.0 -0.866 -0.866 -0.0 0.866 0.866 -0.0 -0.866 -0.866 -0.0 0.866 0.866 0.0 -0.866 -0.866 -0.0 0.866 0.866 0.0 -0.866 -0.866 -0.0 0.866 0.866 -0.0 -0.866 -0.866 0.0 0.866 0.866 0.0 -0.866 -0.866 -0.0 0.866 0.866 -0.0 -0.866 -0.866 -0.0 0.866 0.866 0.0 -0.866 -0.866 -0.0 0.866 0.866 0.0 -0.866 -0.866 0.0 0.866 0.866 0.0 -0.866 -0.866 -0.0 0.866 0.866 0.0 ];




def pythonTestDataPrint(n):

    #For Python data
    #Data Format --> A = [0,1,2,3,4,5,6,7,8]       E = np.array([A,B,C])
    i = 0
    print('E = [', end = '')
    while i < 100:

        print(round(math.sin((i*math.pi)/n),4), end = '')
        print(',', end='')
        i = i + 1
    print(']')

    # Seth's Test Data
    #E = [0.0,0.2588,0.5,0.7071,0.866,0.9659,1.0,0.9659,0.866,0.7071,0.5,0.2588,0.0,-0.2588,-0.5,-0.7071,-0.866,-0.9659,-1.0,-0.9659,-0.866,-0.7071,-0.5,-0.2588,-0.0,0.2588,0.5,0.7071,0.866,0.9659,1.0,0.9659,0.866,0.7071,0.5,0.2588,0.0,-0.2588,-0.5,-0.7071,-0.866,-0.9659,-1.0,-0.9659,-0.866,-0.7071,-0.5,-0.2588,-0.0,0.2588,0.5,0.7071,0.866,0.9659,1.0,0.9659,0.866,0.7071,0.5,0.2588,0.0,-0.2588,-0.5,-0.7071,-0.866,-0.9659,-1.0,-0.9659,-0.866,-0.7071,-0.5,-0.2588,-0.0,0.2588,0.5,0.7071,0.866,0.9659,1.0,0.9659,0.866,0.7071,0.5,0.2588,0.0,-0.2588,-0.5,-0.7071,-0.866,-0.9659,-1.0,-0.9659,-0.866,-0.7071,-0.5,-0.2588,-0.0,0.2588,0.5,0.7071]
    #F = [0.0,0.5,0.866,1.0,0.866,0.5,0.0,-0.5,-0.866,-1.0,-0.866,-0.5,-0.0,0.5,0.866,1.0,0.866,0.5,0.0,-0.5,-0.866,-1.0,-0.866,-0.5,-0.0,0.5,0.866,1.0,0.866,0.5,0.0,-0.5,-0.866,-1.0,-0.866,-0.5,-0.0,0.5,0.866,1.0,0.866,0.5,0.0,-0.5,-0.866,-1.0,-0.866,-0.5,-0.0,0.5,0.866,1.0,0.866,0.5,0.0,-0.5,-0.866,-1.0,-0.866,-0.5,-0.0,0.5,0.866,1.0,0.866,0.5,-0.0,-0.5,-0.866,-1.0,-0.866,-0.5,-0.0,0.5,0.866,1.0,0.866,0.5,0.0,-0.5,-0.866,-1.0,-0.866,-0.5,-0.0,0.5,0.866,1.0,0.866,0.5,-0.0,-0.5,-0.866,-1.0,-0.866,-0.5,-0.0,0.5,0.866,1.0]
    #G = [0.0,0.866,0.866,0.0,-0.866,-0.866,-0.0,0.866,0.866,0.0,-0.866,-0.866,-0.0,0.866,0.866,0.0,-0.866,-0.866,-0.0,0.866,0.866,0.0,-0.866,-0.866,-0.0,0.866,0.866,0.0,-0.866,-0.866,-0.0,0.866,0.866,-0.0,-0.866,-0.866,-0.0,0.866,0.866,0.0,-0.866,-0.866,-0.0,0.866,0.866,-0.0,-0.866,-0.866,-0.0,0.866,0.866,0.0,-0.866,-0.866,-0.0,0.866,0.866,0.0,-0.866,-0.866,-0.0,0.866,0.866,-0.0,-0.866,-0.866,0.0,0.866,0.866,0.0,-0.866,-0.866,-0.0,0.866,0.866,-0.0,-0.866,-0.866,-0.0,0.866,0.866,0.0,-0.866,-0.866,-0.0,0.866,0.866,0.0,-0.866,-0.866,0.0,0.866,0.866,0.0,-0.866,-0.866,-0.0,0.866,0.866,0.0]




pythonTestDataPrint(12)




