##Capitalize Name
def capitalizename(s):
    l=s.split(" ")
    for i in range(0,len(l)):
        l[i]=l[i].capitalize()
    name=" ".join(l)
    return name


##Using BeautifulSoup Object
tesla_revenue = pd.DataFrame(columns=["Date", "Revenue"])
for index, row in enumerate(soup.find_all('tbody')):
    if index == 1:
        for info in row.find_all('tr'):
            col = info.find_all('td')
            date = col[0].text
            revenue = col[1].text
            tesla_revenue = tesla_revenue.append({"Date":date, "Revenue":revenue}, ignore_index=True)    

