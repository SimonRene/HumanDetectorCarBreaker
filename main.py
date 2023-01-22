import car_breaker




def main():
    myCarBreaker = car_breaker.Car_breaker()
    myCarBreaker.start_detecting()

if __name__ == "__main__":

    
    #import argparse

    #parser = argparse.ArgumentParser(description='Create a ArcHydro schema')
    #parser.add_argument('--workspace', metavar='path', required=True,
    #                    help='the path to workspace')
    #parser.add_argument('--schema', metavar='path', required=True,
    #                    help='path to schema')
    #parser.add_argument('--dem', metavar='path', required=True,
    #                    help='path to dem')
    #args = parser.parse_args()

    #main(workspace=args.workspace, schema=args.schema, dem=args.dem)

    main()
