import wikipedia,webbrowser

def getPage():
    #to randomly fetch 1 page from wikipedia and store it's title in wikipage 
    wikipage = wikipedia.random(1)
    #to get the contents, categories, coordinates, images, links and other metadata of a Wikipedia page
    wikiload = wikipedia.page(wikipage)
    #to get the original title of the wikipedia page
    print(wikiload.original_title)
    '''
    #to get all the links available on that wikipedia page
    print(wikiload.links)
    '''
    user_choice = input("Would you like to read about {} (Y/N/Q) :".format(wikipage)).lower().strip()
    
    if(user_choice == 'y' or user_choice == 'yes'):
        print("\nSummary:\n------\n")
        print(wikiload.summary)#to call the summary of loaded wikipage
        wikiopen = input("Open wikipage in browser? (Y/N) :").lower().strip()
        if(wikiopen == 'yes' or wikiopen == 'y'):
            webbrowser.open(wikiload.url,new=2)
        else:
            getPage()
        exit(0)

    elif(user_choice == 'q' or user_choice == 'quit'):
        exit(0)
    else:
        getPage()

getPage()