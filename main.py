import car_breaker


def main(pX, pY, sizeX, sizeY, _window, _video):
    myCarBreaker = car_breaker.Car_breaker()
    window = False
    video = False

    if(_window == 'on'):
        window = True
    if(_video == 'on'):
        video = True
    
    myCarBreaker.start_detecting(pX, pY, sizeX, sizeY, window, video)

if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser(description='Get screen area to capture')
    parser.add_argument('pX', type=int,
                        help='X value of top left corner of screen area')
    parser.add_argument('pY', type=int,
                        help='Y value of top left corner of screen area')
    parser.add_argument('sizeX', type=int,
                        help='X size screen area')
    parser.add_argument('sizeY', type=int,
                        help='Y size screen area')

    parser.add_argument('--window', metavar='window', choices=['on','off'], default='off',
                        help='Open a window to show results?')
    parser.add_argument('--video', metavar='video', choices=['on','off'], default='off',
                        help='Save results as a video file?')

    args = parser.parse_args()

    main(int(args.pX), int(args.pY), int(args.sizeX), int(args.sizeY), args.window, args.video)
