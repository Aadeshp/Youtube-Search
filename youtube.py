#!/usr/bin/env python3

import sys, argparse

"""Change Spaces to '+' for Search Query"""


class YoutubeSearch:
    def __init__(self, filter, to_search=None, sort_by=None):
        self.filter = filter
        self.sort_by = sort_by
        self.to_search = to_search


    """A new tab of youtube video search page will open up, displaying the videos matching the specified arguments inputted"""
    def search(self):
        import webbrowser
        url = "https://www.youtube.com/results?search_query=" + self.toProperSearchQuery()
    
        """Check if args.filter array has items and if a sort_by argument was given"""
        if self.filter:
            url += "&filters=" + "%2C".join(self.filter)
        if self.sort_by:
            url += "&search_sort=" + self.sort_by
    
        webbrowser.open(url)
 
    """
    Change Spaces to Plus Signs
    Ex) "This Is My Search Text" -> "This+Is+My+Search+Text"
    """
    def toProperSearchQuery(self):
        words = self.to_search.split()
        return "+".join(words)

def initArgParse():
    """Create All Options"""
    parser = argparse.ArgumentParser()
    parser.add_argument("search", action="store", help="Search Query")
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
    s = YoutubeSearch(args.filter, args.search, args.sort_by)
    s.search()
