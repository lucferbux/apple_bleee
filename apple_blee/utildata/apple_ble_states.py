# Adapting script from https://github.com/hexway/apple_bleee
# Thanks to Dmitry Chastuhin @_chipik and https://hexway.io 

# not sure about 1b, 13, 0a, 1a, 17
phone_states = {'0b': 'Home screen',
                '1c': 'Home screen',
                '1b': 'Home screen',
                '11': 'Home screen',
                '03': 'Off',
                '18': 'Off',
                '09': 'Off',
                '13': 'Off',
                '0a': 'Off',
                '1a': 'Off',
                '01': 'Off',
                '07': 'Lock screen',
                '17': 'Lock screen',
                '4a': 'Lock screen',
                '57':'Lock screen',
                '47':'Lock screen',
                '0e': 'Calling',
                '1e': 'Calling',
                '5e': 'Calling',
                '4e':'Outgoing call',
                '4b': 'Home screen/Airdrop',
                '5b': 'Home screen/Airdrop',
                '5a': 'Off',
                '5e':'Incoming call',
                }



airpods_states = {
    '00': 'Case:Closed',
    '01': 'Case:All out',
    '02': 'L:out',
    '05': 'R:out',
    '03': 'L:out',
    '09': 'R:out',
    '0b': 'LR:in',
    '11': 'R:out',
    '13': 'R:in',
    '15': 'R:in case',
    '20': 'L:out',
    '21': 'Case:All out',
    '22': 'Case:L out',
    '23': 'R:out',
    '29': 'L:out',
    '2b': 'LR:in',
    '31': 'Case:L out',
    '33': 'Case:L out',
    '50': 'Case:open',
    '51': 'L:out',
    '53': 'L:in',
    '55': 'Case:open',
    '70': 'Case:open',
    '71': 'Case:R out',
    '73': 'Case:R out',
    '75': 'Case:open',
}

dev_types = ["iPad", "iPhone", "MacOS", "AirPods"]


dev_sig = {'02010': 'MacBook', '02011': 'iPhone/iPad'}


devices_models = {
    "i386": "iPhone Simulator",
    "x86_64": "iPhone Simulator",
    "iPhone1,1": "iPhone",
    "iPhone1,2": "iPhone 3G",
    "iPhone2,1": "iPhone 3GS",
    "iPhone3,1": "iPhone 4",
    "iPhone3,2": "iPhone 4 GSM Rev A",
    "iPhone3,3": "iPhone 4 CDMA",
    "iPhone5,1": "iPhone 5 (GSM)",
    "iPhone4,1": "iPhone 4S",
    "iPhone5,2": "iPhone 5 (GSM+CDMA)",
    "iPhone5,3": "iPhone 5C (GSM)",
    "iPhone5,4": "iPhone 5C (Global)",
    "iPhone6,1": "iPhone 5S (GSM)",
    "iPhone6,2": "iPhone 5S (Global)",
    "iPhone7,1": "iPhone 6 Plus",
    "iPhone7,2": "iPhone 6",
    "iPhone8,1": "iPhone 6s",
    "iPhone8,2": "iPhone 6s Plus",
    "iPhone8,3": "iPhone SE (GSM+CDMA)",
    "iPhone8,4": "iPhone SE (GSM)",
    "iPhone9,1": "iPhone 7",
    "iPhone9,2": "iPhone 7 Plus",
    "iPhone9,3": "iPhone 7",
    "iPhone9,4": "iPhone 7 Plus",
    "iPhone10,1": "iPhone 8",
    "iPhone10,2": "iPhone 8 Plus",
    "iPhone10,3": "iPhone X Global",
    "iPhone10,4": "iPhone 8",
    "iPhone10,5": "iPhone 8 Plus",
    "iPhone10,6": "iPhone X GSM",
    "iPhone11,2": "iPhone XS",
    "iPhone11,4": "iPhone XS Max",
    "iPhone11,6": "iPhone XS Max Global",
    "iPhone11,8": "iPhone XR",
    "MacBookPro15,1": "MacBook Pro 15, 2019",
    "MacBookPro15,2": "MacBook Pro 13, 2019",
    "MacBookPro15,1": "MacBook Pro 15, 2018",
    "MacBookPro15,2": "MacBook Pro 13, 2018",
    "MacBookPro14,3": "MacBook Pro 15, 2017",
    "MacBookPro14,2": "MacBook Pro 13, 2017",
    "MacBookPro14,1": "MacBook Pro 13, 2017",
    "MacBookPro13,3": "MacBook Pro 15, 2016",
    "MacBookPro13,2": "MacBook Pro 13, 2016",
    "MacBookPro13,1": "MacBook Pro 13, 2016",
    "MacBookPro11,4": "MacBook Pro 15, mid 2015",
    "MacBookPro11,5": "MacBook Pro 15, mid 2015",
    "MacBookPro12,1": "MacBook Pro 13, ear 2015",
    "MacBookPro11,2": "MacBook Pro 15, mid 2014",
    "MacBookPro11,3": "MacBook Pro 15, mid 2014",
    "MacBookPro11,1": "MacBook Pro 13, mid 2014",
    "MacBookPro11,2": "MacBook Pro 15, end 2013",
    "MacBookPro11,3": "MacBook Pro 15, end 2013",
    "MacBookPro10,1": "MacBook Pro 15, ear 2013",
    "MacBookPro11,1": "MacBook Pro 13, end 2013",
    "MacBookPro10,2": "MacBook Pro 13, ear 2013",
    "MacBookPro10,1": "MacBook Pro 15, mid 2012",
    "MacBookPro9,1": "MacBook Pro 15, mid 2012",
    "MacBookPro10,2": "MacBook Pro 15, mid 2012",
    "MacBookPro9,2": "MacBook Pro 15, mid 2012",
    "MacBookPro8,3": "MacBook Pro 17, end 2011",
    "MacBookPro8,3": "MacBook Pro 17, ear 2011",
    "MacBookPro8,2": "MacBook Pro 15, end 2011",
    "MacBookPro8,2": "MacBook Pro 15, ear 2011",
    "MacBookPro8,1": "MacBook Pro 13, end 2011",
    "MacBookPro8,1": "MacBook Pro 13, ear 2011",
    "MacBookPro6,1": "MacBook Pro 17, mid 2010",
    "MacBookPro6,2": "MacBook Pro 15, mid 2010",
    "MacBookPro7,1": "MacBook Pro 13, mid 2010",
    "MacBookPro5,2": "MacBook Pro 17, mid 2009",
    "MacBookPro5,2": "MacBook Pro 17, ear 2009",
    "MacBookPro5,3": "MacBook Pro 15, mid 2009",
    "MacBookPro5,3": "MacBook Pro 15, mid 2009",
    "MacBookPro5,5": "MacBook Pro 13, mid 2009",
    "MacBookPro5,1": "MacBook Pro 15, end 2008",
    "MacBookPro4,1": "MacBook Pro 17, ear 2008",
    "MacBookPro4,1": "MacBook Pro 15, ear 2008",
    "iPod1,1": "1st Gen iPod",
    "iPod2,1": "2nd Gen iPod",
    "iPod3,1": "3rd Gen iPod",
    "iPod4,1": "4th Gen iPod",
    "iPod5,1": "5th Gen iPod",
    "iPod7,1": "6th Gen iPod",
    "iPad1,1": "iPad",
    "iPad1,2": "iPad 3G",
    "iPad2,1": "2nd Gen iPad",
    "iPad2,2": "2nd Gen iPad GSM",
    "iPad2,3": "2nd Gen iPad CDMA",
    "iPad2,4": "2nd Gen iPad New Revision",
    "iPad3,1": "3rd Gen iPad",
    "iPad3,2": "3rd Gen iPad CDMA",
    "iPad3,3": "3rd Gen iPad GSM",
    "iPad2,5": "iPad mini",
    "iPad2,6": "iPad mini GSM+LTE",
    "iPad2,7": "iPad mini CDMA+LTE",
    "iPad3,4": "4th Gen iPad",
    "iPad3,5": "4th Gen iPad GSM+LTE",
    "iPad3,6": "4th Gen iPad CDMA+LTE",
    "iPad4,1": "iPad Air (WiFi)",
    "iPad4,2": "iPad Air (GSM+CDMA)",
    "iPad4,3": "1st Gen iPad Air (China)",
    "iPad4,4": "iPad mini Retina (WiFi)",
    "iPad4,5": "iPad mini Retina (GSM+CDMA)",
    "iPad4,6": "iPad mini Retina (China)",
    "iPad4,7": "iPad mini 3 (WiFi)",
    "iPad4,8": "iPad mini 3 (GSM+CDMA)",
    "iPad4,9": "iPad Mini 3 (China)",
    "iPad5,1": "iPad mini 4 (WiFi)",
    "iPad5,2": "4th Gen iPad mini (WiFi+Cellular)",
    "iPad5,3": "iPad Air 2 (WiFi)",
    "iPad5,4": "iPad Air 2 (Cellular)",
    "iPad6,3": "iPad Pro (9.7 inch, WiFi)",
    "iPad6,4": "iPad Pro (9.7 inch, WiFi+LTE)",
    "iPad6,7": "iPad Pro (12.9 inch, WiFi)",
    "iPad6,8": "iPad Pro (12.9 inch, WiFi+LTE)",
    "iPad6,11": "iPad (2017)",
    "iPad6,12": "iPad (2017)",
    "iPad7,1": "iPad Pro 2nd Gen (WiFi)",
    "iPad7,2": "iPad Pro 2nd Gen (WiFi+Cellular)",
    "iPad7,3": "iPad Pro 10.5-inch",
    "iPad7,4": "iPad Pro 10.5-inch",
    "iPad7,5": "iPad 6th Gen (WiFi)",
    "iPad7,6": "iPad 6th Gen (WiFi+Cellular)",
    "iPad8,1": "iPad Pro 3rd Gen (11 inch, WiFi)",
    "iPad8,2": "iPad Pro 3rd Gen (11 inch, 1TB, WiFi)",
    "iPad8,3": "iPad Pro 3rd Gen (11 inch, WiFi+Cellular)",
    "iPad8,4": "iPad Pro 3rd Gen (11 inch, 1TB, WiFi+Cellular)",
    "iPad8,5": "iPad Pro 3rd Gen (12.9 inch, WiFi)",
    "iPad8,6": "iPad Pro 3rd Gen (12.9 inch, 1TB, WiFi)",
    "iPad8,7": "iPad Pro 3rd Gen (12.9 inch, WiFi+Cellular)",
    "iPad8,8": "iPad Pro 3rd Gen (12.9 inch, 1TB, WiFi+Cellular)",
    "Watch1,1": "Apple Watch 38mm case",
    "Watch1,2": "Apple Watch 38mm case",
    "Watch2,6": "Apple Watch Series 1 38mm case",
    "Watch2,7": "Apple Watch Series 1 42mm case",
    "Watch2,3": "Apple Watch Series 2 38mm case",
    "Watch2,4": "Apple Watch Series 2 42mm case",
    "Watch3,1": "Apple Watch Series 3 38mm case (GPS+Cellular)",
    "Watch3,2": "Apple Watch Series 3 42mm case (GPS+Cellular)",
    "Watch3,3": "Apple Watch Series 3 38mm case (GPS)",
    "Watch3,4": "Apple Watch Series 3 42mm case (GPS)",
    "Watch4,1": "Apple Watch Series 4 40mm case (GPS)",
    "Watch4,2": "Apple Watch Series 4 44mm case (GPS)",
    "Watch4,3": "Apple Watch Series 4 40mm case (GPS+Cellular)",
    "Watch4,4": "Apple Watch Series 4 44mm case (GPS+Cellular)",
}

ble_packets_types = {'watch_c': '0b',
                     'handoff': '0c',
                     'wifi_set': '0d',
                     'hotspot': '0e',
                     'wifi_join': '0f',
                     'nearby': '10',
                     'airpods': '07',
                     'airdrop': '05',
                     }