import argparse
from datetime import datetime


def get_args():
    # TODO: Add --start-date, --end-date and --output arguments
    #       Convert the two dates to datetime objects
    parser = argparse.ArgumentParser()
    parser.add_argument('--start-date',required = True,help="crawl start")
    parser.add_argument('--end-date',required = True)
    parser.add_argument('--output',help="output csv")
    args = parser.parse_args()
    args.start_date = datetime.strptime(args.start_date,'%Y-%m-%d')
    args.end_date = datetime.strptime(args.end_date,'%Y-%m-%d')
    return args
