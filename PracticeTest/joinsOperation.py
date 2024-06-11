import pandas as pd

def firstDataList():
    player = ['player1','player2','player3']
    points = [8,9,6]
    title = ['Game1', 'Game2', 'Game3']
    df1 = pd.DataFrame({'player':player,'points': points, 'title': title}, index=['L1','L2','L3'])
    # print(df1)
    return df1

def secondDataList():
    player = ['player1','player5','player6']
    power = ['Punch','Kick','Elbow']
    title = ['Game1', 'Game5', 'Game6']
    df2 = pd.DataFrame({'player':player,'power': power, 'title': title}, index=['L2','L3','L4'])
    # print(df2)
    return df2

def innerJoinOpe():
    fdl = firstDataList()
    sdl = secondDataList()
    print(fdl.join(sdl, lsuffix='-_caller', how='inner'))

def leftJoinOpe():
    fdl = firstDataList()
    sdl = secondDataList()
    print(fdl.join(sdl, lsuffix='-_caller', how='left'))

def rightJoinOpe():
    fdl = firstDataList()
    sdl = secondDataList()
    print(fdl.join(sdl, lsuffix='-_caller', how='right'))

def outerJoinOpe():
    fdl = firstDataList()
    sdl = secondDataList()
    print(fdl.join(sdl, lsuffix='-_caller', how='outer'))


outerJoinOpe()