import bs4, requests, csv


url = 'http://www.cookcountyassessor.com/Property.aspx'
# enter your pin below for single use
params = {
    'pin': ''
}
property_info = {
    'Pin': 'ctl00_phArticle_ctlPropertyDetails_lblPropInfoPIN',
    'PropertyLocation': 'ctl00_phArticle_ctlPropertyDetails_lblPropInfoAddress',
    'City': 'ctl00_phArticle_ctlPropertyDetails_lblPropInfoCity',
    'Township': 'ctl00_phArticle_ctlPropertyDetails_lblPropInfoTownship',
    'PropertyClass': 'ctl00_phArticle_ctlPropertyDetails_lblPropInfoClassification',
    'SqFootage': 'ctl00_phArticle_ctlPropertyDetails_lblPropInfoSqFt',
    'Neighborhood': 'ctl00_phArticle_ctlPropertyDetails_lblPropInfoNBHD',
    'Taxcode': 'ctl00_phArticle_ctlPropertyDetails_lblPropInfoTaxcode'
}
assessed_valuation = {
    'LandAssessedValue_2017_FirstPass': 'ctl00_phArticle_ctlPropertyDetails_lblAsdValLandFirstPass',
    'BuildingAssessedValue_2017_FirstPass': 'ctl00_phArticle_ctlPropertyDetails_lblAsdValBldgFirstPass',
    'TotalAssessedValue_2017_FirstPass': 'ctl00_phArticle_ctlPropertyDetails_lblAsdValTotalFirstPass',
    'LandAssessedValue_2016_Certified': 'ctl00_phArticle_ctlPropertyDetails_lblAsdValLandCertified',
    'BuildingAssessedValue_2016_Certified': 'ctl00_phArticle_ctlPropertyDetails_lblAsdValBldgCertified',
    'TotalAssessedValue_2016_Certified': 'ctl00_phArticle_ctlPropertyDetails_lblAsdValTotalCertified'

}
property_char = {
    '2017_market_value': 'ctl00_phArticle_ctlPropertyDetails_lblPropCharMktValCurrYear',
    '2016_market_value': 'ctl00_phArticle_ctlPropertyDetails_lblPropCharMktValPrevYear',
    'Description': 'ctl00_phArticle_ctlPropertyDetails_lblPropCharDesc',
    'Residence Type': 'ctl00_phArticle_ctlPropertyDetails_lblPropCharResType',
    'Use': 'ctl00_phArticle_ctlPropertyDetails_lblPropCharUse',
    'Apartments': 'ctl00_phArticle_ctlPropertyDetails_lblPropCharApts',
    'Exterior Construction': 'ctl00_phArticle_ctlPropertyDetails_lblPropCharExtConst',
    'Full Baths': 'ctl00_phArticle_ctlPropertyDetails_lblPropCharFullBaths',
    'Half Baths': 'ctl00_phArticle_ctlPropertyDetails_lblPropCharHalfBaths',
    'Basement': 'ctl00_phArticle_ctlPropertyDetails_lblPropCharBasement',
    'Attic': 'ctl00_phArticle_ctlPropertyDetails_lblPropCharAttic',
    'Central Air': 'ctl00_phArticle_ctlPropertyDetails_lblPropCharCentAir',
    'Number of Fireplaces': 'ctl00_phArticle_ctlPropertyDetails_lblPropCharFrpl',
    'Garage Size/Type': 'ctl00_phArticle_ctlPropertyDetails_lblPropCharGarage',
    'Age': 'ctl00_phArticle_ctlPropertyDetails_lblPropCharAge',
    'Building Square Footage': 'ctl00_phArticle_ctlPropertyDetails_lblPropCharBldgSqFt',
    'Assessment Pass': 'ctl00_phArticle_ctlPropertyDetails_lblPropCharAsmtPass'
}
all_keys = {}


home = requests.get(url=url, params=params)
home.raise_for_status()
soup = bs4.BeautifulSoup(markup=home.text, features='html.parser')

# print out the 'Property Information' section
for k, v in property_info.items():
    val = soup.find(id=v)
    all_keys[k] = val.string

# print out the 'Assessed Valuation' section
for k, v in assessed_valuation.items():
    val = soup.find(id=v)
    all_keys[k] = val.string

# print out the 'Property Characteristics' section
for k, v in property_char.items():
    val = soup.find(id=v)
    all_keys[k] = val.string

# add the 'clean pin' without dashes into the dict
all_keys['Num-Only Pin'] = all_keys.get('Pin').replace('-', '')

# write csv file
file = open(file='testFile.csv', mode='w', newline='')
mycsv = csv.DictWriter(f=file, fieldnames=all_keys.keys(), delimiter='|')
mycsv.writeheader()
mycsv.writerow(rowdict=all_keys)
file.close()

print('All set!')
