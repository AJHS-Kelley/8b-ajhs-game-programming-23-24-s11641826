# Example Game FUNCTIONS project, Albert Laguerre, v0.0
import random

def jumpBall():
    pass

def dribbleBall(param1):
    pass

def shootBall(param1):
    pass

def passBall(param1, param2, param3):
    pass

def catchBall(ThrowQuality, passCatchScore, weather):
    if ThrowQuality > 5.0 and passCatchScore >= 99 and weather == 'Sunny':
        ballCaught = True
    elif ThrowQuality > 4.0 and passCatchScore >= 75 and weather == 'Windy':
        ballCaught = False
    else:
        print('Oh, no, interceptiopn!\n')
        ballIntercepted = True
        return ballIntercepted
    return ballCaught

catchBall(4.25, 107, 'Rainy')



