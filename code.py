import requests
from bs4 import BeautifulSoup

page_url = 'https://www.amazon.in/gp/product/B077Q42DTC/ref=s9_acss_bw_cg_CG1_5c1_w?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-1&pf_rd_r=MQNT096Q5JCVDBED33GS&pf_rd_t=101&pf_rd_p=bef577ce-86f4-4275-8ec2-85cbe6899e22&pf_rd_i=1389401031'

browser_agent = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}

product_page = requests.get(page_url,headers=browser_agent)

soup = BeautifulSoup(product_page.content,'html.parser')

#print(soup.prettify())

page_title = soup.find(id='title_feature_div').get_text()


page_price = soup.find(id='priceblock_ourprice').get_text()[2:8]



page_price = page_price.replace(',','')

final_price = float(page_price)

if (final_price<12999.0):


    send_email()

import smtplib

def send_email():

    s = smtplib.SMTP('smtp.gmail.com',587)

    s.starttls()


    s.login('sender_email_id','sender_email_id_password')


    message = 'hey price are down time to shop'


    s.sendmail('sender_email_id','receiver_email_id',message)

    s.quit()


    s.login('sender_email_id')




