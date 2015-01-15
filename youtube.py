#!/usr/bin/env python3

import sys, argparse

"""Change Spaces to '+' for Search Query"""
def spaces(s):
    words = s.split()
    return "+".join(words)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "search", 
        action="store", 
        help="Search Query"
    )
    parser.add_argument(
        "--upload-date",
        action="append",
        dest="filter",
        default=[],
        help="Upload Date"
    )
    parser.add_argument(
        "--type",
        action="append",
        dest="filter",
        help="Video Type"
    )
    parser.add_argument(
        "--duration",
        action="append",
        dest="filter",
        help="Video Duration"
    )
    parser.add_argument(
        "--feature",
        action="append",
        dest="filter",
        help="Video Features"
    )
    parser.add_argument(
        "--sort-by",
        action="store",
        dest="sort_by",
        help="Default is Sort By Relevance"
    )

    args = parser.parse_args(sys.argv[1:])
  
    import webbrowser
    url = "https://www.youtube.com/results?search_query=" + spaces(args.search)
    
    """Check if args.filter array has items and if a sort_by argument was given"""
    if args.filter:
        url += "&filters=" + "%2C".join(args.filter)
    if args.sort_by:
        url += "&search_sort=" + args.sort_by
    
    webbrowser.open(url)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise Exception("Error: Search Argument Required")
    else:
        main()

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
