import bs4, requests, csv, pyperclip
 
 
clipUrl = pyperclip.paste()
homeUrl = 'http://www.cookcountyassessor.com/Property.aspx'
agent = {'User-Agent': 'Mozilla/5.0'}
prop_info = {
 	'Current Year Value' : 'ctl00_phArticle_ctlPropertyDetails_lblPropCharMktValCurrYear',
 	'Address' : 'ctl00_phArticle_ctlPropertyDetails_lblPropInfoAddress',
 	'City' : 'ctl00_phArticle_ctlPropertyDetails_lblPropInfoCity',
 	'Township' : 'ctl00_phArticle_ctlPropertyDetails_lblPropInfoTownship',
 	'Class' : 'ctl00_phArticle_ctlPropertyDetails_lblPropInfoClassification',
 	'Land Sq Footage' : 'ctl00_phArticle_ctlPropertyDetails_lblPropInfoSqFt',
 	'Neighborhood' : 'ctl00_phArticle_ctlPropertyDetails_lblPropInfoNBHD'
 }


def main():
	my_file = open(file='redfinPinPull.csv', mode='w', newline='')
	for i, clip in enumerate(clipUrl.split()):
		pin = getPin(clip)
		prop_arry = getHomeInfo(pin=pin)
		prop_arry['pin'] = pin
		prop_arry['URL'] = clip
		if i == 0:
			csv_file = writeHeader(file=my_file, prop_arry=prop_arry)
		writeFile(csv_file, prop_arry)
def getPin(url):
	'''Goes to Redfin site and grabs the PIN off the web
 	@ url - input to check redfin site for Pin (called APN)
 	returns - 10 digit PIN number '''
	site = requests.get(url=url,headers=agent)
	site.raise_for_status()
	soup = bs4.BeautifulSoup(markup=site.text, features='html.parser')
	table = soup.find(class_="table-label", string="APN")
	pin = table.nextSibling.next
	return pin
def getHomeInfo(pin): 
	''' Goes to cook county assessor site with PIN to return key housing info 
	@ pin - used as a parmeter for requests 
	returns - dictionary of values from assessor site ''' 
	params = {'pin': pin}
	all_keys ={}
	home = requests.get(url=homeUrl, params=params)
	home.raise_for_status()
	soup = bs4.BeautifulSoup(markup=home.text, features='html.parser')
	for k, v in prop_info.items():
		val = soup.find(id=v)
		try:
			all_keys[k] = val.string
		except AttributeError:
			all_keys[k] = 'N/a' 
	return all_keys
def writeHeader(file, prop_arry):
	csv_file = csv.DictWriter(f=file, fieldnames=prop_arry.keys(), delimiter='|')
	csv_file.writeheader()
	return csv_file
def writeFile(csv, prop_arry):
	csv.writerow(rowdict=prop_arry)
if __name__=='__main__':
 	main()
