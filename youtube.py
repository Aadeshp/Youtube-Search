#!/usr/bin/env python3

import sys, argparse

class YoutubeSearch:
    def __init__(self, to_search, filter=[], sort_by=None):
        self.to_search = to_search
        self.filter = filter
        self.sort_by = sort_by


    """A new tab of youtube video search page will open up, displaying the videos matching the specified arguments inputted"""
    def search(self):
        import webbrowser
        url = "https://www.youtube.com/results?search_query=" + '+'.join(self.to_search)
    
        """Check if args.filter array has items and if a sort_by argument was given"""
        if self.filter:
            url += "&filters=" + "%2C".join(self.filter)
        if self.sort_by:
            url += "&search_sort=" + self.sort_by
    
        webbrowser.open(url)


def initArgParse():
    """Create All Options"""
    parser = argparse.ArgumentParser()
    parser.add_argument("search", action="store", nargs='+',
                        help="Search Query")
    parser.add_argument("-u", "--upload-date", action="append",
                      help="Upload Date", dest="filter")
    parser.add_argument("-t", "--type", action="append", help="Video Type",
                      dest="filter")
    parser.add_argument("-d", "--duration", action="append",
                      help="Video Duration", dest="filter")
    parser.add_argument("-f", "--feature", action="append",
                      help="Specific Features", dest="filter")
    parser.add_argument("-s", "--sort", action="store", help="Sorting Pattern",
                      dest="sort_by")

    return parser.parse_args()

if __name__ == "__main__":
    """Check If Any Arguments Were Given"""
    if len(sys.argv) < 2:
        raise Exception("Error: Search Argument Required")

    args = initArgParse()
    s = YoutubeSearch(args.search, args.filter, args.sort_by)
    s.search()
