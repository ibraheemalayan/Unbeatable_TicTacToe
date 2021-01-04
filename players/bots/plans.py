
def generate_plans():

    plans = {}

    plans['lines'] = [
      [0,1,2],
      [3,4,5],
      [6,7,8],

      [0,3,6],
      [1,4,7],
      [2,5,8],

      [0,4,8],
      [2,4,6]
    ]

    plans['corners'] = [
      0, 2, 6, 8
    ]

    plans['edges'] = [
      1, 3, 5, 7
    ]

    plans['center'] = 5

    plans['opposite_corner_of']={
      0: 8, 2: 6, 6: 2, 8: 0
    }

    plans['far_edges'] = {
      0: [5, 7],
      2: [3, 7],
      6: [1, 5],
      8: [3, 1]
    }
    
    plans['near_edges'] = {
      8: [5, 7],
      6: [3, 7],
      2: [1, 5],
      0: [3, 1]
    }

    return plans

