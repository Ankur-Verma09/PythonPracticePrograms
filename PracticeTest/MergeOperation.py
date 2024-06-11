import pandas as pd

def firstDataList():
    # global df1
    player = ['player1','player2','player3']
    points = [8,9,6]
    title = ['Game1', 'Game2', 'Game3']
    df1 = pd.DataFrame({'player':player,'points': points, 'title': title})
    # print(df1)
    return df1

def secondDataList():
    # global df2
    player = ['player1','player5','player6']
    power = ['Punch','Kick','Elbow']
    title = ['Game1', 'Game5', 'Game6']
    df2 = pd.DataFrame({'player':player,'power': power, 'title': title})
    # print(df2)
    return df2

# Inner Merge
def innerMrg():
    fdl = firstDataList()
    sdl = secondDataList()
    inn1 = fdl.merge(sdl, on='player', how='inner')
    # OR
    inn = fdl.merge(sdl)
    print(inn)
    print('\n', inn1)

def leftMrg():
    fdl = firstDataList()
    sdl = secondDataList()
    inn = fdl.merge(sdl, on='player', how='left')
    print(inn)

def rightMrg():
    fdl = firstDataList()
    sdl = secondDataList()
    inn = fdl.merge(sdl, on='player', how='right')
    print(inn)

def outerMrg():
    fdl = firstDataList()
    sdl = secondDataList()
    inn = fdl.merge(sdl, on='player', how='outer')
    print(inn)

outerMrg()