import urllib.request as urllib


def main(url):
    print("Checking Connecivity ")
    response = urllib.urlopen(url)
    print("Connected to", url, "successfully")
    print("Response code: ", response.getcode())
 

print('This is a Site Connectivity Checker Program.')
input_url = input("Enter the url: ")   

main(input_url)