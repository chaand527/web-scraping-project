import requests
from bs4 import BeautifulSoup

#product details
products_to_track = [
    {
        "URL":"https://www.amazon.in/Test-Exclusive_2020_1157-Multi-3GB-Storage/dp/B089MV3Q2G/ref=rvi_7/257-7142733-2682751?pd_rd_w=3WtgH&pf_rd_p=952d3327-3a6f-4a5f-9074-89f45ae60137&pf_rd_r=QWBDWW87V071KYG4QBJG&pd_rd_r=a937c1d1-bc23-401b-a43c-5b71b5606f83&pd_rd_wg=HFwKS&pd_rd_i=B089MV3Q2G&psc=1",
        "name":"Redmi note 10pro",
        "target_price":20000
    },
    {
        "URL":"https://www.amazon.in/dp/B096VDR283/ref=sspa_dk_detail_0?psc=1&pd_rd_i=B096VDR283&pd_rd_w=rQpx8&pf_rd_p=3d347ba3-873a-4950-a530-1b4d5938343e&pd_rd_wg=4SHSG&pf_rd_r=7N45DTT1JV0VQ2CVKMR7&pd_rd_r=51fe0db8-db0d-4fa4-8782-0e56b08ed945&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFZVFJCVlc1VkpZSUImZW5jcnlwdGVkSWQ9QTA2MzQ5MTYzQ0NMVFpGR09DQjRGJmVuY3J5cHRlZEFkSWQ9QTAyNTcxNTkxM0w3QUVUVVY2RDM0JndpZGdldE5hbWU9c3BfZGV0YWlsJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==",
        "name":"Samsung M31",
        "target_price":19000
    },
    {
        "URL":"https://www.amazon.in/OPPO-Fantastic-Purple-128GB-Storage/dp/B08VB34KJ1/ref=pd_d_dss_r_1/257-7142733-2682751?pd_rd_w=fz6gI&pf_rd_p=7f3a23eb-6514-4509-ae29-a02f735fbe53&pf_rd_r=WZZRJ1WKN3J9N0V3EF2T&pd_rd_r=494e7901-b4bd-433a-aa0c-16592e759ff4&pd_rd_wg=i1hxn&pd_rd_i=B08VB34KJ1&psc=1",
        "name":"Oppo A74 5G",
        "target_price":15000
    },
    {
        "URL":"https://www.amazon.in/OnePlus-Nord-Sierra-128GB-Storage/dp/B097RDVDL2/ref=sr_1_2?dchild=1&qid=1628248505&refinements=p_89%3AOnePlus&rnid=3837712031&s=electronics&sr=1-2",
        "name":"One plus nord2 5G",
        "target_price":30000
    },
    {
        "URL":"https://www.amazon.in/Vivo-Y51A-Titanium-Sapphire-Additional/dp/B08LRDP2Q6/ref=pd_d_dss_r_3/257-7142733-2682751?pd_rd_w=fz6gI&pf_rd_p=7f3a23eb-6514-4509-ae29-a02f735fbe53&pf_rd_r=WZZRJ1WKN3J9N0V3EF2T&pd_rd_r=494e7901-b4bd-433a-aa0c-16592e759ff4&pd_rd_wg=i1hxn&pd_rd_i=B08LRDP2Q6&psc=1",
        "name":"Vivo Y51A",
        "target_price":15000
    }
]
def share_product_price(URL):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
    }

    page = requests.get(URL,headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    product_price = soup.find(id="priceblock_dealprice")
    if (product_price == None):
        product_price = soup.find(id="priceblock_ourprice")

    return product_price.getText()

result_file = open('result_file.txt', 'w')

try:
    for every_product in products_to_track:
        price_received = share_product_price(every_product.get("URL"))
        print(price_received + "--" + every_product.get("name"))
        my_product_price = price_received[1:]
        my_product_price = my_product_price.replace(',', '')
        my_product_price = int(float(my_product_price))

        if my_product_price < every_product.get("target_price"):
            print("is available at your price")
            result_file.write("Hey,"  + every_product.get("name") + '\t'+ "is now available at your best price of"+"-" + str(my_product_price)+'\n')

    else:
        print("price is still high")

finally:
    result_file.close()
