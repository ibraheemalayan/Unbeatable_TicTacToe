#from enums import X, O
X = 11
O = 12
# checks if a for must moves in a line
def critical_square_of_line(line, grid): 

    full_squares = []
    empty_square = None

    for i in line:
        if grid[i]:
            full_squares.append(i)
        else:
            empty_square = i
    
    if len(full_squares) == 2:
        if grid[ full_squares[0] ] == grid[ full_squares[1] ]:
            return empty_square

    return None



# check for a winning line with empty field
# each line that matches case 1, compare the 2 full squares

grid = [
    X    , X    , None,
    X    , O    , X,
    X    , X    , X
]

# TODO fill this with a script
winning_cases = [

    [0,1,2],
    [3,4,5],
    [6,7,8],

    [0,3,6],
    [1,4,7],
    [2,5,8],

    [0,4,8],
    [2,4,6]

]

for line in winning_cases:
    
    critic_square = critical_square_of_line(line, grid)

    if critic_square:
        print("line: " + str(line) + " is critical at " + str(critic_square) )

print()