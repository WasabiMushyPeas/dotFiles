import requests
from bs4 import BeautifulSoup


webiteListFile = open('./listOfWebsites.txt', 'r')
websites = webiteListFile.readlines()
webiteListFile.close()

currentWebsite = 0;
invalidWebsiteList = [];
for site in websites:
    line = site.split("}")
    url = line[0]
    newsHeader = line[1]
    newsHeaderClass = line[2]
    newsLink = line[3]
    newsLinkClass = line[4]
    newsDiscrition = line[5]
    newsDiscritionClass = line[6]

    print(line)

    canContinue = True;

    try:
        rawHTML = requests.get(url)
    except:
        print("Invalid website added")
        invalidWebsiteList.append(currentWebsite)
        canContinue = False;
    currentWebsite += 1

    print(rawHTML)

    #BeautifulSoup part
    if(canContinue):
        soup = BeautifulSoup(rawHTML.content, 'html.parser')
        headers = []
        links = []
        discriptions = []
        
        cleanTextFile = open('./' + soup.title.getText().strip().replace(".", "").replace("|", "").replace("/", "") + ".txt", 'w')

        if(newsHeaderClass == "."):
            for title in soup.find_all(newsHeader):
                cleanTextFile.write(title.getText() + "\n")
            cleanTextFile.write("n*e*w**l*i*n*e\n")
        else:
            for title in soup.find_all(newsHeader, {"class": newsHeaderClass}):
                cleanTextFile.write(title.getText() + "\n")
            cleanTextFile.write("n*e*w**l*i*n*e\n")

        if(newsLinkClass != "." and newsLink != "."):
            for link in soup.find_all(newsLink, {"class": newsLinkClass}):
                cleanTextFile.write(link['href'] + "\n")
        else:
            cleanTextFile.write("No link\n")
        cleanTextFile.write("n*e*w**l*i*n*e\n")


        print(newsDiscrition + "    " + newsDiscritionClass)
        if(newsDiscritionClass != "." and newsDiscrition != "."):
            for discription in soup.find_all(newsDiscrition, {"class": newsDiscritionClass}):
                print(discription)
                cleanTextFile.write(discription.getText().replace("\n", "").replace("\t", "") + "\n")
        else:
            cleanTextFile.write("No discription")
            
        cleanTextFile.close()

#Invalid request deletion
lines = []
with open('./listOfWebsites.txt', 'r') as fp:
    lines = fp.readlines()

with open('./listOfWebsites.txt', 'w') as fp:
    for number, line in enumerate(lines):
        if number not in invalidWebsiteList:
            fp.write(line)
