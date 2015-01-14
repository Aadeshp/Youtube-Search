#!/usr/bin/env python3

import sys, getopt

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
     
def spaces(s):
    arr = []
    for c in s:
        if c == " ":
            arr.append("+")
        else:
            arr.append(c)

    return "".join(arr)

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
        elif opt in ("--upload-date", "--type", "--duration", "--feature", "--sort-by"):
            filters.append(arg)
        else:
            assert False, "Error:\n\tInvalid Option opt"

    import webbrowser
    url = "https://www.youtube.com/results?search_query=" + search + "&filters=" + "%2C".join(filters)
    if len(search_sort) > 0:
        url += "&search_sort=" + search_short

    webbrowser.open(url)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise Exception("Error: Search Argument Required")
    elif sys.argv[1] == "help":
        help()
    else:
        main()
