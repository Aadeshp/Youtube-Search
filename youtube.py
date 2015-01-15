#!/usr/bin/env python3

import sys, argparse

"""Change Spaces to '+' for Search Query"""

class YoutubeSearch:
    def __init__(self):   
        self.initArgParse()

    def initArgParse(self):
        """Create All Options"""
        self.parser = argparse.ArgumentParser()
        self.addArgument("search", "store", "Search Query")
        self.addArgument("--upload-date", "append", "Upload Date", "filter")
        self.addArgument("--type", "append", "Video Type", "filter")
        self.addArgument("--duration", "append", "Video Duration", "filter")
        self.addArgument("--feature", "append", "Specific Features", "filter")
        self.addArgument("--sort", "store", "Sorting Pattern", "sort_by")

        self.args = self.parser.parse_args()
    
    """Adds an argument to the class argparser"""
    def addArgument(self, opt, action, help, dest=None):
        """Check If Creating Positional or Optional Argument"""
        if dest:
            self.parser.add_argument(
                "-" + opt[2],
                str(opt),
                action=action,
                dest=dest,
                help=help
            )
        else:
            self.parser.add_argument(
                str(opt),
                action=action,
                help=help
            )
    
    """A new tab of youtube video search page will open up, displaying the videos matching the specified arguments inputted"""
    def search(self):
        import webbrowser
        url = "https://www.youtube.com/results?search_query=" + self.toProperSearchQuery()
    
        """Check if args.filter array has items and if a sort_by argument was given"""
        if self.args.filter:
            url += "&filters=" + "%2C".join(self.args.filter)
        if self.args.sort_by:
            url += "&search_sort=" + self.args.sort_by
    
        webbrowser.open(url)
 
    """
    Change Spaces to Plus Signs
    Ex) "This Is My Search Text" -> "This+Is+My+Search+Text"
    """
    def toProperSearchQuery(self):
        words = self.args.search.split()
        return "+".join(words)

if __name__ == "__main__":
    """Check If Any Arguments Were Given"""
    if len(sys.argv) < 2:
        raise Exception("Error: Search Argument Required")
    else:
        s = YoutubeSearch()
        s.search()

"""
------Using getopt instead of argparse------

import getopt

def help():
    print("\n======OPTIONS======")
    print("\t--search\n\t--upload-date\n\t--type\n\t--duration\n\t--feature\n\t--sort-by")
    print("\nCommand Example:\n\tyoutube [OPTION] [ARGUMENT]")
   
    print("\n---------------------------------------------------------\n")
    print("=======Upload Date======")
    print("Appropriate Arguments:\n\thour\n\ttoday\n\tweek\n\tmonth\n\tyear")

    print("\n---------------------------------------------------------\n")
    print("======Type======")
    print("Appropriate Arguments:\n\tvideo\n\tchannel\n\tplaylist\n\tmovie\n\tshow")

    print("\n---------------------------------------------------------\n")
    print("======Duration======")
    print("Appropriate Arguments:\n\tshort\n\tlong")

    print("\n---------------------------------------------------------\n")
    print("======Feature======")
    print("Appropriate Arguments:\n\thd\n\tcc\n\tcreativecommons\n\t3d\n\tlive\n\tpurchased")

    print("\n---------------------------------------------------------\n")
    print("======Sort By======")
    print("Default Argument:\n\trelevance")
    print("Appropriate Arguments:\n\tvideo_date_uploaded\n\tvideo_view_count\n\tvideo_avg_rating")
     
def main():
    search = ""
    filters = []
    search_sort = ""

    try:
        opts, args = getopt.getopt(sys.argv[1:], ":s:d:t:l:f:", ["search=", "upload-date=", "type=", "duration=", "feature=", "sort-by="])
    except getopt.GetoptError as error:
        print (error)
        sys.exit(2)

    for opt, arg in opts:
        if opt == "--search":
            search = spaces(arg)
        elif opt in ("--upload-date", "--type", "--duration", "--feature"):
            filters.append(arg)
        elif opt == "--sort-by":
            search_sort = arg
        else:
            assert False, "Error:\n\tInvalid Option " + opt

    import webbrowser
    url = "https://www.youtube.com/results?search_query=" + search + "&filters=" + "%2C".join(filters)
    if len(search_sort) > 0:
        url += "&search_sort=" + search_sort

    webbrowser.open(url)
"""
