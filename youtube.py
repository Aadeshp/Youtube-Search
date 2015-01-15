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
