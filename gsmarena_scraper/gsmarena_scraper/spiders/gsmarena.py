import scrapy

class GsmArenaSpider(scrapy.Spider):
    name = "gsmarena"
    allowed_domains = ["gsmarena.com"]
    start_urls = ["https://www.gsmarena.com/meizu-phones-74.php",
                  "https://www.gsmarena.com/asus-phones-46.php",
                  "https://www.gsmarena.com/alcatel-phones-5.php",
                  "https://www.gsmarena.com/zte-phones-62.php",
                  "https://www.gsmarena.com/microsoft-phones-64.php",
                  "https://www.gsmarena.com/umidigi-phones-135.php",
                  "https://www.gsmarena.com/coolpad-phones-105.php",
                  "https://www.gsmarena.com/cat-phones-89.php",
                  "https://www.gsmarena.com/sharp-phones-23.php",
                  "https://www.gsmarena.com/micromax-phones-66.php",
                  "https://www.gsmarena.com/infinix-phones-119.php",
                  "https://www.gsmarena.com/ulefone-phones-124.php",
                  "https://www.gsmarena.com/tecno-phones-120.php",
                  "https://www.gsmarena.com/doogee-phones-129.php",
                  "https://www.gsmarena.com/blackview-phones-116.php",
                  "https://www.gsmarena.com/cubot-phones-130.php",
                  "https://www.gsmarena.com/oukitel-phones-132.php",
                  "https://www.gsmarena.com/itel-phones-131.php",
                  "https://www.gsmarena.com/tcl-phones-123.php"
                  ] 
    def parse(self, response):

        phone_links = response.css('div.makers ul li a::attr(href)').getall()
        for phone in phone_links:
            if 'watch' in phone.lower():
                continue
            phone_url = response.urljoin(phone)  # Convert relative URL to absolute
            yield scrapy.Request(phone_url, callback=self.parse_phone)

        # Handle pagination (if next page exists)
        next_page = response.css('div.nav-pages a.prevnextbutton[title="Next page"]').attrib['href']
        next_page = response.urljoin(next_page)
        if next_page:
            yield response.follow(next_page, callback=self.parse)

    def parse_phone(self, response):

        containers = response.css('div.pricing')
        listofprices = []

        for container in containers:
            model_name = (container.css('span::text').get())
            model_price = (container.css('ul li a::text').get())
            listofprices.append({model_name : model_price})


        yield {

            "Name" : response.css('h1.specs-phone-name-title::text').get(),
            "Prices" : listofprices,


            "Network_Technology" : response.css('tr td.nfo a[data-spec="nettech"]::text').get(),
            "Network_2gbands" : response.css('td.nfo[data-spec="net2g"]::text').get(),
            "Network_3gbands" : response.css('td.nfo[data-spec="net3g"]::text').get(),
            "Network_4gbands" : response.css('td.nfo[data-spec="net4g"]::text').get(),
            "Network_Speed" : response.css('td.nfo[data-spec="speed"]::text').get(),

            "Body_Dimensions" : response.css('td.nfo[data-spec="dimensions"]::text').get(),
            "Body_Weight" : response.css('td.nfo[data-spec="weight"]::text').get(),
            "Body_Build" : response.css('td.nfo[data-spec="build"]::text').get(),
            "Body_SIM" : response.css('td.nfo[data-spec="sim"]::text').get(),

            "Display_Type" : response.css('td.nfo[data-spec="displaytype"]::text').get(),
            "Display_Type" : response.css('td.nfo[data-spec="displaysize"]::text').get(),
            "Display_Resolution" : response.css('td.nfo[data-spec="displayresolution"]::text').get(),

            "Platform_OS" : response.css('td.nfo[data-spec="os"]::text').get(),
            "Platform_Chipset" : response.css('td.nfo[data-spec="chipset"]::text').get(),
            "Platform_Cpu" : response.css('td.nfo[data-spec="cpu"]::text').get(),
            "Platform_Gpu" : response.css('td.nfo[data-spec="gpu"]::text').get(),


            "Memory_Cardslot" : response.css('td.nfo[data-spec="memoryslot"]::text').get(),
            "Memory_Internalmemory" : response.css('td.nfo[data-spec="internalmemory"]::text').get(),

            "MainCamera_Cameraspecs" : response.xpath('//td[@data-spec="cam1modules"]//text()').getall(),
            "MainCamera_Features" : response.xpath('//td[@data-spec="cam1features"]//text()').getall(),
            "MainCamera_Video" : response.xpath('//td[@data-spec="cam1video"]//text()').getall(),

            "SelfieCamera_Cameraspecs" : response.xpath('//td[@data-spec="cam2modules"]//text()').getall(),
            "SelfieCamera_Features" : response.xpath('//td[@data-spec="cam2features"]//text()').getall(),
            "SelfieCamera_Features" : response.xpath('//td[@data-spec="cam2video"]//text()').getall(),

            "Sound_Feature" : response.css('tr:contains("Sound") td.nfo::text').get(),
            "Sound_3.5mmjack" :  response.css('tr:contains("3.5mm jack") td.nfo::text').get(),

            "COMMS_WLAN" : response.css('tr:contains("Comms") td a::text').get() + response.css('td.nfo[data-spec="wlan"]::text').get(),
            "COMMS_Bluetooth" : response.css('tr td.nfo[data-spec="bluetooth"]::text').get(),
            "COMMS_NFC" : response.css('tr td.nfo[data-spec="nfc"]::text').get(),
            "COMMS_Radio" : response.css('tr td.nfo[data-spec="radio"]::text').get(),
            "COMMS_USB" : response.css('tr td.nfo[data-spec="usb"]::text').get(),

            "Battery_Type" : response.css('tr td.nfo[data-spec="batdescription1"]::text').get(),
            "Battery_Charging" : response.css('tr:contains("Charging") td.nfo::text').get(),

            "Colors" : response.css('tr td.nfo[data-spec="colors"]::text').get(),
            "Price" : response.css('tr td.nfo[data-spec="price"]::text').get()
        }