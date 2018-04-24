# this app takes a return delimited file (like a column from an Excel spreadsheet) and parses apart all of the
# related information from the cook county assessor's office

import bs4, requests, csv
from selenium import webdriver

# set all starting variables based on cook county site makeup
url = 'http://www.cookcountyassessor.com/Search/Property-Search.aspx'
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
neighborhood_select = "ctl00_phArticle_ctlPropertySearch_ctlNeighborhoodSearch_ddlNeighborhood"


def main():
    # create driver object, get the URL
    driver = webdriver.Chrome()
    driver.implicitly_wait(time_to_wait=15)
    driver.get(url)
    
    enter_menu = driver.find_element_by_link_text("Neighborhood Search")
    enter_menu.click()
    driver.execute_script("document.getElementById('ctl00_phArticle_ctlPropertySearch_ctlNeighborhoodSearch_ddlTownship').value = 32;")
    print("Checkpoint 1")


    # # pull listing of pins from the file
    # pinList = open('pinListing', mode='r').read()
    # # create CSV file to store home info
    # csv_file = open(file='testFile.csv', mode='w', newline='')
    # # loop through each PIN and pull the HTML info into the CSV. Use enumerate to track loops
    # for i, pins in enumerate(pinList.split()):
    #     # create an empty dictionary for tracking
    #     all_keys = {}
    #     pin_dict = {
    #         'pin': pins
    #     }
    #     # pull home info down based on PIN
    #     home = requests.get(url=url, params=pin_dict)
    #     home.raise_for_status()
    #     soup = bs4.BeautifulSoup(markup=home.text, features='html.parser')

    #     # print out the 'Property Information' section
    #     for k, v in property_info.items():
    #         val = soup.find(id=v)
    #         try:
    #             all_keys[k] = val.string
    #         except AttributeError:
    #             all_keys[k] = 'N/a'

    #     # print out the 'Assessed Valuation' section
    #     for k, v in assessed_valuation.items():
    #         val = soup.find(id=v)
    #         try:
    #             all_keys[k] = val.string
    #         except AttributeError:
    #             all_keys[k] = 'N/a'

    #     # print out the 'Property Characteristics' section
    #     for k, v in property_char.items():
    #         val = soup.find(id=v)
    #         try:
    #             all_keys[k] = val.string
    #         except AttributeError:
    #             all_keys[k] = 'N/a'

    #     # add the 'clean pin' without dashes into the dict
    #     all_keys['Num-Only Pin'] = all_keys.get('Pin').replace('-', '')
    #     if i == 0:
    #         # write a header section
    #         mycsv = csv.DictWriter(f=csv_file, fieldnames=all_keys.keys(), delimiter='|')
    #         mycsv.writeheader()
    #     else:
    #         mycsv.writerow(rowdict=all_keys)
    # csv_file.close()
    # print('All set!')


if __name__ == '__main__':
    main()