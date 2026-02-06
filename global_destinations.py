"""
Global Countries and States Database
Comprehensive mapping of all countries and their administrative divisions
"""

GLOBAL_DESTINATIONS = {
    # ASIA
    "Afghanistan": {
        "states": ["Kabul", "Kandahar", "Herat", "Mazar-i-Sharif", "Jalalabad"],
        "region": "Asia",
        "description": "Mountainous country with ancient Silk Road heritage"
    },
    "Albania": {
        "states": ["Tirana", "Durrës", "Vlorë", "Shkodër", "Korçë"],
        "region": "Europe",
        "description": "Balkan country with Adriatic beaches and mountain heritage"
    },
    "Algeria": {
        "states": ["Algiers", "Oran", "Constantine", "Annaba", "Blida"],
        "region": "Africa",
        "description": "North African nation with Sahara desert and Mediterranean coast"
    },
    "Andorra": {
        "states": ["Andorra la Vella", "Escaldes-Engordany", "La Massana"],
        "region": "Europe",
        "description": "Pyrenees mountain principality"
    },
    "Angola": {
        "states": ["Luanda", "Benguela", "Huambo", "Kuando Kubango"],
        "region": "Africa",
        "description": "Southern African country with diverse wildlife"
    },
    "Argentina": {
        "states": ["Buenos Aires", "Córdoba", "Rosario", "Mendoza", "Salta", "Bariloche"],
        "region": "South America",
        "description": "South American nation known for tango, wine, and Patagonia"
    },
    "Australia": {
        "states": ["Sydney NSW", "Melbourne VIC", "Brisbane QLD", "Perth WA", "Adelaide SA", "Hobart TAS", "Darwin NT", "Canberra ACT"],
        "region": "Oceania",
        "description": "Island continent with unique wildlife and beach culture"
    },
    "Austria": {
        "states": ["Vienna", "Salzburg", "Innsbruck", "Linz", "Graz"],
        "region": "Europe",
        "description": "Alpine nation famous for music, culture, and imperial heritage"
    },
    "Azerbaijan": {
        "states": ["Baku", "Ganja", "Sumgait", "Sheki", "Quba"],
        "region": "Asia",
        "description": "Caucasus country on Caspian Sea"
    },
    "Bahamas": {
        "states": ["Nassau", "Freeport", "Marsh Harbour", "George Town"],
        "region": "Caribbean",
        "description": "Caribbean archipelago with clear waters and beaches"
    },
    "Bahrain": {
        "states": ["Manama", "Muharraq", "Riffa", "Isa Town"],
        "region": "Asia",
        "description": "Arabian Gulf island nation"
    },
    "Bangladesh": {
        "states": ["Dhaka", "Chittagong", "Sylhet", "Khulna", "Rajshahi"],
        "region": "Asia",
        "description": "South Asian nation with Ganges Delta and river culture"
    },
    "Barbados": {
        "states": ["Bridgetown", "Oistins", "Speightstown", "Bathsheba"],
        "region": "Caribbean",
        "description": "Caribbean island nation with colonial architecture"
    },
    "Belarus": {
        "states": ["Minsk", "Brest", "Grodno", "Vitebsk", "Mogilev"],
        "region": "Europe",
        "description": "Eastern European country with forests and lakes"
    },
    "Belgium": {
        "states": ["Brussels", "Antwerp", "Ghent", "Bruges", "Liège"],
        "region": "Europe",
        "description": "Western European nation with medieval cities and Belgian beer"
    },
    "Belize": {
        "states": ["Belmopan", "Belize City", "San Pedro", "Dangriga"],
        "region": "Central America",
        "description": "Central American country with Mayan ruins and barrier reef"
    },
    "Benin": {
        "states": ["Cotonou", "Porto-Novo", "Abomey", "Parakou"],
        "region": "Africa",
        "description": "West African nation with colonial history"
    },
    "Bhutan": {
        "states": ["Thimphu", "Paro", "Punakha", "Trongsa", "Jakar"],
        "region": "Asia",
        "description": "Himalayan kingdom focused on happiness over GDP"
    },
    "Bolivia": {
        "states": ["La Paz", "Sucre", "Santa Cruz", "Cochabamba", "Potosí"],
        "region": "South America",
        "description": "Andean nation with ancient ruins and salt flats"
    },
    "Bosnia and Herzegovina": {
        "states": ["Sarajevo", "Mostar", "Banja Luka", "Trebinje"],
        "region": "Europe",
        "description": "Balkan nation with Ottoman and Habsburg heritage"
    },
    "Botswana": {
        "states": ["Gaborone", "Francistown", "Maun", "Kasane"],
        "region": "Africa",
        "description": "Southern African nation famous for Okavango Delta wildlife"
    },
    "Brazil": {
        "states": ["Rio de Janeiro", "São Paulo", "Salvador", "Manaus", "Brasília", "Recife", "Florianópolis"],
        "region": "South America",
        "description": "Largest South American country with Amazon rainforest and carnival"
    },
    "Brunei": {
        "states": ["Bandar Seri Begawan", "Kuala Belait", "Tutong"],
        "region": "Asia",
        "description": "Small sultanate on Borneo island"
    },
    "Bulgaria": {
        "states": ["Sofia", "Plovdiv", "Varna", "Burgas", "Ruse"],
        "region": "Europe",
        "description": "Eastern European nation with Black Sea resorts and mountain culture"
    },
    "Burkina Faso": {
        "states": ["Ouagadougou", "Bobo-Dioulasso", "Koudougou", "Ouahigouya"],
        "region": "Africa",
        "description": "West African Sahel nation"
    },
    "Burundi": {
        "states": ["Gitega", "Bujumbura", "Muyinga", "Ngozi"],
        "region": "Africa",
        "description": "East African nation on Lake Tanganyika"
    },
    "Cambodia": {
        "states": ["Phnom Penh", "Siem Reap", "Sihanoukville", "Battambang"],
        "region": "Asia",
        "description": "Southeast Asian nation with Angkor Wat temples"
    },
    "Cameroon": {
        "states": ["Yaoundé", "Douala", "Buéa", "Kumba"],
        "region": "Africa",
        "description": "Central African nation with diverse landscapes"
    },
    "Canada": {
        "states": ["Toronto ON", "Vancouver BC", "Montreal QC", "Calgary AB", "Ottawa ON", "Quebec City QC", "Banff", "Niagara Falls"],
        "region": "North America",
        "description": "North American country with Rocky Mountains and Niagara Falls"
    },
    "Cape Verde": {
        "states": ["Praia", "Mindelo", "Santa Maria", "Tarrafal"],
        "region": "Africa",
        "description": "Atlantic island nation off West Africa"
    },
    "Central African Republic": {
        "states": ["Bangui", "Berbérati", "Carnot"],
        "region": "Africa",
        "description": "Central African nation"
    },
    "Chad": {
        "states": ["N'Djamena", "Sarh", "Moundou", "Abeché"],
        "region": "Africa",
        "description": "Sahel region nation"
    },
    "Chile": {
        "states": ["Santiago", "Valparaíso", "Antofagasta", "Puerto Montt", "Punta Arenas"],
        "region": "South America",
        "description": "South American nation with Atacama Desert and Patagonia"
    },
    "China": {
        "states": ["Beijing", "Shanghai", "Xi'an", "Chengdu", "Guilin", "Hong Kong", "Hangzhou", "Suzhou"],
        "region": "Asia",
        "description": "East Asian nation with Great Wall and ancient civilization"
    },
    "Colombia": {
        "states": ["Bogotá", "Medellín", "Cartagena", "Santa Marta", "Cali"],
        "region": "South America",
        "description": "South American country with coffee culture and Caribbean coast"
    },
    "Comoros": {
        "states": ["Moroni", "Mutsamudu", "Domoni"],
        "region": "Africa",
        "description": "Indian Ocean island nation"
    },
    "Congo": {
        "states": ["Brazzaville", "Pointe-Noire", "Dolisie"],
        "region": "Africa",
        "description": "Central African nation on Congo River"
    },
    "Costa Rica": {
        "states": ["San José", "Liberia", "Puerto Limón", "Manuel Antonio"],
        "region": "Central America",
        "description": "Central American country famous for eco-tourism and wildlife"
    },
    "Croatia": {
        "states": ["Zagreb", "Dubrovnik", "Split", "Zadar", "Rovinj"],
        "region": "Europe",
        "description": "Balkan nation with Adriatic coast and medieval cities"
    },
    "Cuba": {
        "states": ["Havana", "Varadero", "Santiago de Cuba", "Trinidad"],
        "region": "Caribbean",
        "description": "Caribbean island with colonial architecture and cigars"
    },
    "Cyprus": {
        "states": ["Nicosia", "Limassol", "Larnaca", "Paphos"],
        "region": "Europe",
        "description": "Mediterranean island nation"
    },
    "Czech Republic": {
        "states": ["Prague", "Brno", "Plzeň", "Ústí nad Labem"],
        "region": "Europe",
        "description": "Central European nation with Prague castles and beer culture"
    },
    "Denmark": {
        "states": ["Copenhagen", "Aarhus", "Odense", "Aalborg"],
        "region": "Europe",
        "description": "Scandinavian nation known for design and hygge"
    },
    "Djibouti": {
        "states": ["Djibouti City", "Arta", "Tadjourah"],
        "region": "Africa",
        "description": "Horn of Africa nation on Red Sea"
    },
    "Dominica": {
        "states": ["Roseau", "Portsmouth", "Marigot"],
        "region": "Caribbean",
        "description": "Caribbean island with rainforests"
    },
    "Dominican Republic": {
        "states": ["Santo Domingo", "Santiago", "Punta Cana", "La Romana"],
        "region": "Caribbean",
        "description": "Caribbean nation with beaches and colonial architecture"
    },
    "Ecuador": {
        "states": ["Quito", "Guayaquil", "Cuenca", "Galápagos"],
        "region": "South America",
        "description": "South American nation with Galápagos Islands and Amazon"
    },
    "Egypt": {
        "states": ["Cairo", "Alexandria", "Luxor", "Aswan", "Giza"],
        "region": "Africa",
        "description": "North African nation with pyramids and Nile River"
    },
    "El Salvador": {
        "states": ["San Salvador", "Santa Ana", "San Miguel"],
        "region": "Central America",
        "description": "Central American nation with volcanoes"
    },
    "Equatorial Guinea": {
        "states": ["Malabo", "Bata"],
        "region": "Africa",
        "description": "Central African nation"
    },
    "Eritrea": {
        "states": ["Asmara", "Massawa", "Keren"],
        "region": "Africa",
        "description": "Horn of Africa nation on Red Sea"
    },
    "Estonia": {
        "states": ["Tallinn", "Tartu", "Narva"],
        "region": "Europe",
        "description": "Baltic nation with digital innovation"
    },
    "Ethiopia": {
        "states": ["Addis Ababa", "Dire Dawa", "Adama", "Hawassa"],
        "region": "Africa",
        "description": "East African nation with ancient Christian heritage"
    },
    "Fiji": {
        "states": ["Suva", "Nadi", "Lautoka", "Labasa"],
        "region": "Oceania",
        "description": "South Pacific island nation"
    },
    "Finland": {
        "states": ["Helsinki", "Turku", "Tampere", "Rovaniemi"],
        "region": "Europe",
        "description": "Nordic country with lakes and Northern Lights"
    },
    "France": {
        "states": ["Paris", "Lyon", "Marseille", "Toulouse", "Nice", "Strasbourg", "Bordeaux"],
        "region": "Europe",
        "description": "Western European nation with culture, wine, and cuisine"
    },
    "Gabon": {
        "states": ["Libreville", "Port-Gentil", "Franceville"],
        "region": "Africa",
        "description": "Central African nation with rainforests"
    },
    "Gambia": {
        "states": ["Banjul", "Serekunda", "Bakau"],
        "region": "Africa",
        "description": "West African nation on Atlantic coast"
    },
    "Georgia": {
        "states": ["Tbilisi", "Batumi", "Kutaisi", "Gori"],
        "region": "Asia",
        "description": "Caucasus nation with mountains and wine culture"
    },
    "Germany": {
        "states": ["Berlin", "Munich", "Hamburg", "Cologne", "Frankfurt", "Dresden", "Heidelberg"],
        "region": "Europe",
        "description": "Central European nation with history, beer, and Oktoberfest"
    },
    "Ghana": {
        "states": ["Accra", "Kumasi", "Sekondi", "Cape Coast"],
        "region": "Africa",
        "description": "West African nation with gold and slave castle heritage"
    },
    "Greece": {
        "states": ["Athens", "Thessaloniki", "Mykonos", "Santorini", "Crete", "Rhodes"],
        "region": "Europe",
        "description": "Mediterranean nation with ancient ruins and islands"
    },
    "Grenada": {
        "states": ["St. George's", "Gouyave", "Grenville"],
        "region": "Caribbean",
        "description": "Caribbean island known for spices"
    },
    "Guatemala": {
        "states": ["Guatemala City", "Antigua", "Lake Atitlán", "Chichicastenango"],
        "region": "Central America",
        "description": "Central American nation with Mayan culture"
    },
    "Guinea": {
        "states": ["Conakry", "Kindia", "Mamou"],
        "region": "Africa",
        "description": "West African nation"
    },
    "Guinea-Bissau": {
        "states": ["Bissau", "Cacheu"],
        "region": "Africa",
        "description": "West African nation"
    },
    "Guyana": {
        "states": ["Georgetown", "Linden", "New Amsterdam"],
        "region": "South America",
        "description": "South American nation with rainforests"
    },
    "Haiti": {
        "states": ["Port-au-Prince", "Cap-Haïtien", "Les Cayes"],
        "region": "Caribbean",
        "description": "Caribbean nation with colonial history"
    },
    "Honduras": {
        "states": ["Tegucigalpa", "San Pedro Sula", "Copán"],
        "region": "Central America",
        "description": "Central American nation with Mayan ruins"
    },
    "Hong Kong": {
        "states": ["Central", "Kowloon", "New Territories", "Victoria Peak"],
        "region": "Asia",
        "description": "Asian financial hub with skyscrapers and harbor"
    },
    "Hungary": {
        "states": ["Budapest", "Debrecen", "Szeged", "Lake Balaton"],
        "region": "Europe",
        "description": "Central European nation with thermal baths"
    },
    "Iceland": {
        "states": ["Reykjavik", "Akureyri", "Ísafjörður", "Blue Lagoon"],
        "region": "Europe",
        "description": "Nordic island nation with geysers and waterfalls"
    },
    "India": {
        "states": ["Delhi", "Mumbai", "Bangalore", "Kolkata", "Chennai", "Jaipur", "Goa", "Kerala", "Agra"],
        "region": "Asia",
        "description": "South Asian nation with ancient culture and spices"
    },
    "Indonesia": {
        "states": ["Jakarta", "Bali", "Yogyakarta", "Bandung", "Surabaya", "Medan"],
        "region": "Asia",
        "description": "Southeast Asian archipelago with temples and beaches"
    },
    "Iran": {
        "states": ["Tehran", "Isfahan", "Shiraz", "Tabriz", "Mashhad"],
        "region": "Asia",
        "description": "Middle Eastern nation with Persian culture"
    },
    "Iraq": {
        "states": ["Baghdad", "Basra", "Mosul", "Erbil"],
        "region": "Asia",
        "description": "Middle Eastern nation with Mesopotamian heritage"
    },
    "Ireland": {
        "states": ["Dublin", "Cork", "Galway", "Limerick", "Cliffs of Moher"],
        "region": "Europe",
        "description": "European island nation with Celtic culture and whiskey"
    },
    "Israel": {
        "states": ["Jerusalem", "Tel Aviv", "Haifa", "Eilat", "Dead Sea"],
        "region": "Asia",
        "description": "Middle Eastern nation with ancient holy sites"
    },
    "Italy": {
        "states": ["Rome", "Venice", "Florence", "Milan", "Naples", "Sicily", "Amalfi Coast"],
        "region": "Europe",
        "description": "Southern European nation with Renaissance art and cuisine"
    },
    "Jamaica": {
        "states": ["Kingston", "Montego Bay", "Negril", "Port Antonio"],
        "region": "Caribbean",
        "description": "Caribbean island with reggae music and beaches"
    },
    "Japan": {
        "states": ["Tokyo", "Osaka", "Kyoto", "Hiroshima", "Yokohama", "Hokkaido", "Mount Fuji"],
        "region": "Asia",
        "description": "East Asian island nation with ancient temples and modern technology"
    },
    "Jordan": {
        "states": ["Amman", "Petra", "Dead Sea", "Wadi Rum"],
        "region": "Asia",
        "description": "Middle Eastern nation with Petra ruins"
    },
    "Kazakhstan": {
        "states": ["Almaty", "Astana", "Aktobe", "Karaganda"],
        "region": "Asia",
        "description": "Central Asian nation with steppes"
    },
    "Kenya": {
        "states": ["Nairobi", "Mombasa", "Kisumu", "Nakuru"],
        "region": "Africa",
        "description": "East African nation famous for safari and wildlife"
    },
    "Kiribati": {
        "states": ["Tarawa", "Kiritimati"],
        "region": "Oceania",
        "description": "Pacific island nation"
    },
    "Kosovo": {
        "states": ["Pristina", "Prizren", "Gjakovë"],
        "region": "Europe",
        "description": "Balkan nation"
    },
    "Kuwait": {
        "states": ["Kuwait City", "Salmiya", "Ahmadi"],
        "region": "Asia",
        "description": "Arabian Gulf nation"
    },
    "Kyrgyzstan": {
        "states": ["Bishkek", "Osh", "Issyk-Kul"],
        "region": "Asia",
        "description": "Central Asian mountain nation"
    },
    "Laos": {
        "states": ["Vientiane", "Luang Prabang", "Pakse", "Savannakhet"],
        "region": "Asia",
        "description": "Southeast Asian nation with Mekong River"
    },
    "Latvia": {
        "states": ["Riga", "Daugavpils", "Liepaja"],
        "region": "Europe",
        "description": "Baltic nation"
    },
    "Lebanon": {
        "states": ["Beirut", "Tripoli", "Sidon", "Tyre"],
        "region": "Asia",
        "description": "Middle Eastern nation on Mediterranean coast"
    },
    "Lesotho": {
        "states": ["Maseru", "Teyateyaneng"],
        "region": "Africa",
        "description": "Southern African mountain kingdom"
    },
    "Liberia": {
        "states": ["Monrovia", "Gbarnga", "Kakata"],
        "region": "Africa",
        "description": "West African nation"
    },
    "Libya": {
        "states": ["Tripoli", "Benghazi", "Misrata"],
        "region": "Africa",
        "description": "North African nation on Mediterranean"
    },
    "Liechtenstein": {
        "states": ["Vaduz", "Schaan"],
        "region": "Europe",
        "description": "Alpine principality"
    },
    "Lithuania": {
        "states": ["Vilnius", "Kaunas", "Klaipėda"],
        "region": "Europe",
        "description": "Baltic nation"
    },
    "Luxembourg": {
        "states": ["Luxembourg City", "Esch-sur-Alzette"],
        "region": "Europe",
        "description": "Western European grand duchy"
    },
    "Madagascar": {
        "states": ["Antananarivo", "Antsirabe", "Toliara"],
        "region": "Africa",
        "description": "African island with unique wildlife"
    },
    "Malawi": {
        "states": ["Lilongwe", "Blantyre", "Mzuzu"],
        "region": "Africa",
        "description": "Southern African nation on Lake Malawi"
    },
    "Malaysia": {
        "states": ["Kuala Lumpur", "Penang", "Malacca", "Sabah", "Sarawak"],
        "region": "Asia",
        "description": "Southeast Asian nation with Petronas Towers"
    },
    "Maldives": {
        "states": ["Malé", "Hulhumale"],
        "region": "Asia",
        "description": "Indian Ocean island nation with atolls"
    },
    "Mali": {
        "states": ["Bamako", "Timbuktu", "Ségou"],
        "region": "Africa",
        "description": "West African Sahel nation"
    },
    "Malta": {
        "states": ["Valletta", "Sliema", "Mdina"],
        "region": "Europe",
        "description": "Mediterranean island nation"
    },
    "Marshall Islands": {
        "states": ["Majuro"],
        "region": "Oceania",
        "description": "Pacific island nation"
    },
    "Mauritania": {
        "states": ["Nouakchott", "Atar"],
        "region": "Africa",
        "description": "West African Saharan nation"
    },
    "Mauritius": {
        "states": ["Port Louis", "Curepipe", "Vacoas"],
        "region": "Africa",
        "description": "Indian Ocean island nation"
    },
    "Mexico": {
        "states": ["Mexico City", "Cancún", "Playa del Carmen", "Puerto Vallarta", "Guadalajara", "Oaxaca", "Mérida"],
        "region": "North America",
        "description": "North American nation with Mayan ruins and beaches"
    },
    "Micronesia": {
        "states": ["Pohnpei", "Chuuk"],
        "region": "Oceania",
        "description": "Pacific island nation"
    },
    "Moldova": {
        "states": ["Chișinău", "Bender"],
        "region": "Europe",
        "description": "Eastern European nation with wine regions"
    },
    "Monaco": {
        "states": ["Monaco"],
        "region": "Europe",
        "description": "Mediterranean principality"
    },
    "Mongolia": {
        "states": ["Ulaanbaatar", "Darkhan", "Gobi Desert"],
        "region": "Asia",
        "description": "Central Asian nation with steppes and nomadic culture"
    },
    "Montenegro": {
        "states": ["Podgorica", "Kotor", "Budva"],
        "region": "Europe",
        "description": "Balkan nation with Adriatic coast"
    },
    "Morocco": {
        "states": ["Casablanca", "Marrakech", "Fes", "Tangier", "Agadir"],
        "region": "Africa",
        "description": "North African nation with deserts and medinas"
    },
    "Mozambique": {
        "states": ["Maputo", "Beira", "Inhambane"],
        "region": "Africa",
        "description": "Southern African nation on Indian Ocean"
    },
    "Myanmar": {
        "states": ["Yangon", "Mandalay", "Bagan", "Inle Lake"],
        "region": "Asia",
        "description": "Southeast Asian nation with golden temples"
    },
    "Namibia": {
        "states": ["Windhoek", "Swakopmund", "Walvis Bay"],
        "region": "Africa",
        "description": "Southern African nation with Namib Desert"
    },
    "Nauru": {
        "states": ["Yaren"],
        "region": "Oceania",
        "description": "Pacific island nation"
    },
    "Nepal": {
        "states": ["Kathmandu", "Pokhara", "Everest Region", "Bhaktapur"],
        "region": "Asia",
        "description": "Himalayan nation with Mount Everest"
    },
    "Netherlands": {
        "states": ["Amsterdam", "Rotterdam", "Utrecht", "The Hague"],
        "region": "Europe",
        "description": "Western European nation with canals and tulips"
    },
    "New Zealand": {
        "states": ["Auckland", "Wellington", "Christchurch", "Queenstown"],
        "region": "Oceania",
        "description": "South Pacific island nation with mountains and fjords"
    },
    "Nicaragua": {
        "states": ["Managua", "Granada", "León"],
        "region": "Central America",
        "description": "Central American nation with lakes and volcanoes"
    },
    "Niger": {
        "states": ["Niamey", "Zinder", "Maradi"],
        "region": "Africa",
        "description": "West African Sahel nation"
    },
    "Nigeria": {
        "states": ["Lagos", "Abuja", "Port Harcourt", "Kano"],
        "region": "Africa",
        "description": "West African nation with diverse cultures"
    },
    "North Korea": {
        "states": ["Pyongyang", "Kaesong"],
        "region": "Asia",
        "description": "East Asian nation with limited tourism"
    },
    "North Macedonia": {
        "states": ["Skopje", "Ohrid"],
        "region": "Europe",
        "description": "Balkan nation"
    },
    "Norway": {
        "states": ["Oslo", "Bergen", "Tromsø", "Geirangerfjord"],
        "region": "Europe",
        "description": "Scandinavian nation with fjords and Northern Lights"
    },
    "Oman": {
        "states": ["Muscat", "Salalah", "Nizwa"],
        "region": "Asia",
        "description": "Arabian Peninsula nation on Indian Ocean"
    },
    "Pakistan": {
        "states": ["Islamabad", "Lahore", "Karachi", "Peshawar"],
        "region": "Asia",
        "description": "South Asian nation with mountains and ancient sites"
    },
    "Palau": {
        "states": ["Koror"],
        "region": "Oceania",
        "description": "Pacific island nation"
    },
    "Palestine": {
        "states": ["Ramallah", "Gaza City", "Bethlehem"],
        "region": "Asia",
        "description": "Middle Eastern territory"
    },
    "Panama": {
        "states": ["Panama City", "Bocas del Toro", "Boquete"],
        "region": "Central America",
        "description": "Central American nation with canal"
    },
    "Papua New Guinea": {
        "states": ["Port Moresby", "Lae"],
        "region": "Oceania",
        "description": "Pacific island nation"
    },
    "Paraguay": {
        "states": ["Asunción", "Ciudad del Este", "Encarnación"],
        "region": "South America",
        "description": "South American nation with Paraná River"
    },
    "Peru": {
        "states": ["Lima", "Cusco", "Machu Picchu", "Arequipa", "Puno"],
        "region": "South America",
        "description": "South American nation with Incan ruins"
    },
    "Philippines": {
        "states": ["Manila", "Cebu", "Davao", "Palawan", "Boracay"],
        "region": "Asia",
        "description": "Southeast Asian island nation with beaches"
    },
    "Poland": {
        "states": ["Warsaw", "Krakow", "Gdańsk", "Wrocław"],
        "region": "Europe",
        "description": "Central European nation with historical cities"
    },
    "Portugal": {
        "states": ["Lisbon", "Porto", "Sintra", "Algarve", "Azores"],
        "region": "Europe",
        "description": "Western European nation with maritime heritage"
    },
    "Qatar": {
        "states": ["Doha", "Al Wakrah"],
        "region": "Asia",
        "description": "Arabian Peninsula nation"
    },
    "Romania": {
        "states": ["Bucharest", "Brașov", "Sibiu", "Transylvania"],
        "region": "Europe",
        "description": "Eastern European nation with Carpathian mountains"
    },
    "Russia": {
        "states": ["Moscow", "St. Petersburg", "Sochi", "Vladivostok", "Novosibirsk"],
        "region": "Europe/Asia",
        "description": "Largest country spanning Europe and Asia"
    },
    "Rwanda": {
        "states": ["Kigali", "Butare", "Gisenyi"],
        "region": "Africa",
        "description": "East African nation with mountain gorillas"
    },
    "Saint Kitts and Nevis": {
        "states": ["Basseterre", "Charlestown"],
        "region": "Caribbean",
        "description": "Caribbean island nation"
    },
    "Saint Lucia": {
        "states": ["Castries", "Vieuxfort"],
        "region": "Caribbean",
        "description": "Caribbean island nation"
    },
    "Saint Vincent and the Grenadines": {
        "states": ["Kingstown"],
        "region": "Caribbean",
        "description": "Caribbean island nation"
    },
    "Samoa": {
        "states": ["Apia", "Savai'i"],
        "region": "Oceania",
        "description": "South Pacific island nation"
    },
    "San Marino": {
        "states": ["San Marino City"],
        "region": "Europe",
        "description": "European microstate"
    },
    "Sao Tome and Principe": {
        "states": ["São Tomé"],
        "region": "Africa",
        "description": "West African island nation"
    },
    "Saudi Arabia": {
        "states": ["Riyadh", "Jeddah", "Medina", "Mecca"],
        "region": "Asia",
        "description": "Arabian Peninsula nation with Islamic holy sites"
    },
    "Senegal": {
        "states": ["Dakar", "Saint-Louis", "Kaolack"],
        "region": "Africa",
        "description": "West African nation on Atlantic coast"
    },
    "Serbia": {
        "states": ["Belgrade", "Novi Sad", "Niš"],
        "region": "Europe",
        "description": "Balkan nation with vibrant nightlife"
    },
    "Seychelles": {
        "states": ["Victoria"],
        "region": "Africa",
        "description": "Indian Ocean island nation"
    },
    "Sierra Leone": {
        "states": ["Freetown", "Makeni"],
        "region": "Africa",
        "description": "West African nation"
    },
    "Singapore": {
        "states": ["Central", "East Coast", "Sentosa"],
        "region": "Asia",
        "description": "Southeast Asian city-state with modern skyline"
    },
    "Slovakia": {
        "states": ["Bratislava", "Banská Bystrica", "Košice"],
        "region": "Europe",
        "description": "Central European nation with mountains"
    },
    "Slovenia": {
        "states": ["Ljubljana", "Maribor", "Lake Bled"],
        "region": "Europe",
        "description": "Central European nation with Alps"
    },
    "Solomon Islands": {
        "states": ["Honiara"],
        "region": "Oceania",
        "description": "Pacific island nation"
    },
    "Somalia": {
        "states": ["Mogadishu", "Hargeisa"],
        "region": "Africa",
        "description": "Horn of Africa nation"
    },
    "South Africa": {
        "states": ["Cape Town", "Johannesburg", "Durban", "Pretoria"],
        "region": "Africa",
        "description": "Southern African nation with diverse wildlife"
    },
    "South Korea": {
        "states": ["Seoul", "Busan", "Daegu", "Jeju Island"],
        "region": "Asia",
        "description": "East Asian nation with K-pop and technology"
    },
    "South Sudan": {
        "states": ["Juba", "Wau"],
        "region": "Africa",
        "description": "East African nation"
    },
    "Spain": {
        "states": ["Madrid", "Barcelona", "Seville", "Valencia", "Málaga", "Granada"],
        "region": "Europe",
        "description": "Southern European nation with Mediterranean culture"
    },
    "Sri Lanka": {
        "states": ["Colombo", "Kandy", "Galle", "Nuwara Eliya"],
        "region": "Asia",
        "description": "South Asian island with tea plantations"
    },
    "Sudan": {
        "states": ["Khartoum", "Port Sudan"],
        "region": "Africa",
        "description": "North African nation on Nile River"
    },
    "Suriname": {
        "states": ["Paramaribo", "Lelydorp"],
        "region": "South America",
        "description": "South American nation with rainforests"
    },
    "Sweden": {
        "states": ["Stockholm", "Gothenburg", "Malmö"],
        "region": "Europe",
        "description": "Scandinavian nation with lakes and IKEA"
    },
    "Switzerland": {
        "states": ["Zurich", "Geneva", "Bern", "Lucerne", "Interlaken"],
        "region": "Europe",
        "description": "Central European nation with Alps and watches"
    },
    "Syria": {
        "states": ["Damascus", "Aleppo", "Homs"],
        "region": "Asia",
        "description": "Middle Eastern nation on Mediterranean"
    },
    "Taiwan": {
        "states": ["Taipei", "Taichung", "Kaohsiung"],
        "region": "Asia",
        "description": "East Asian island nation with tech industry"
    },
    "Tajikistan": {
        "states": ["Dushanbe", "Khujand"],
        "region": "Asia",
        "description": "Central Asian mountain nation"
    },
    "Tanzania": {
        "states": ["Dar es Salaam", "Arusha", "Zanzibar"],
        "region": "Africa",
        "description": "East African nation with Mount Kilimanjaro and Serengeti"
    },
    "Thailand": {
        "states": ["Bangkok", "Chiang Mai", "Phuket", "Krabi", "Pattaya"],
        "region": "Asia",
        "description": "Southeast Asian nation known for beaches and temples"
    },
    "Timor-Leste": {
        "states": ["Dili", "Baucau"],
        "region": "Asia",
        "description": "Southeast Asian island nation"
    },
    "Togo": {
        "states": ["Lomé", "Sokodé"],
        "region": "Africa",
        "description": "West African nation"
    },
    "Tonga": {
        "states": ["Nuku'alofa"],
        "region": "Oceania",
        "description": "South Pacific island nation"
    },
    "Trinidad and Tobago": {
        "states": ["Port of Spain", "San Fernando"],
        "region": "Caribbean",
        "description": "Caribbean island nation"
    },
    "Tunisia": {
        "states": ["Tunis", "Sfax", "Sousse", "Djerba"],
        "region": "Africa",
        "description": "North African nation with Mediterranean coast"
    },
    "Turkey": {
        "states": ["Istanbul", "Ankara", "Cappadocia", "Antalya", "Ephesus"],
        "region": "Europe/Asia",
        "description": "Transcontinental nation with ancient ruins"
    },
    "Turkmenistan": {
        "states": ["Ashgabat", "Turkmenabat"],
        "region": "Asia",
        "description": "Central Asian nation on Caspian Sea"
    },
    "Tuvalu": {
        "states": ["Funafuti"],
        "region": "Oceania",
        "description": "Pacific island nation"
    },
    "Uganda": {
        "states": ["Kampala", "Entebbe", "Jinja"],
        "region": "Africa",
        "description": "East African nation with mountain gorillas"
    },
    "Ukraine": {
        "states": ["Kyiv", "Kharkiv", "Odesa", "Lviv"],
        "region": "Europe",
        "description": "Eastern European nation on Black Sea"
    },
    "United Arab Emirates": {
        "states": ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"],
        "region": "Asia",
        "description": "Arabian Peninsula federation with skyscrapers"
    },
    "United Kingdom": {
        "states": ["London", "Edinburgh", "Cardiff", "Belfast", "Manchester", "Bath"],
        "region": "Europe",
        "description": "European island nation with royal heritage"
    },
    "United States": {
        "states": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "Miami", "San Francisco", "Boston", "Las Vegas", "Seattle", "Denver", "Orlando", "Honolulu"],
        "region": "North America",
        "description": "North American superpower with diverse landscapes"
    },
    "Uruguay": {
        "states": ["Montevideo", "Punta del Este", "Colonia"],
        "region": "South America",
        "description": "South American nation with progressive society"
    },
    "Uzbekistan": {
        "states": ["Tashkent", "Samarkand", "Bukhara"],
        "region": "Asia",
        "description": "Central Asian nation on Silk Road"
    },
    "Vanuatu": {
        "states": ["Port Vila", "Luganville"],
        "region": "Oceania",
        "description": "South Pacific island nation"
    },
    "Vatican City": {
        "states": ["Vatican City"],
        "region": "Europe",
        "description": "European microstate with St. Peter's Basilica"
    },
    "Venezuela": {
        "states": ["Caracas", "Margarita Island", "Canaima"],
        "region": "South America",
        "description": "South American nation with Angel Falls"
    },
    "Vietnam": {
        "states": ["Hanoi", "Ho Chi Minh City", "Hoi An", "Halong Bay", "Hue"],
        "region": "Asia",
        "description": "Southeast Asian nation with French colonial heritage"
    },
    "Yemen": {
        "states": ["Sana'a", "Aden", "Mukalla"],
        "region": "Asia",
        "description": "Arabian Peninsula nation on Red Sea"
    },
    "Zambia": {
        "states": ["Lusaka", "Livingstone", "Ndola"],
        "region": "Africa",
        "description": "Southern African nation with Victoria Falls"
    },
    "Zimbabwe": {
        "states": ["Harare", "Bulawayo", "Victoria Falls"],
        "region": "Africa",
        "description": "Southern African nation with wildlife"
    },
}

def get_all_countries():
    """Get all countries as a sorted list"""
    return sorted(GLOBAL_DESTINATIONS.keys())

def get_states(country):
    """Get states/cities for a country"""
    if country in GLOBAL_DESTINATIONS:
        return GLOBAL_DESTINATIONS[country].get("states", [])
    return []

def get_country_info(country):
    """Get full information about a country"""
    return GLOBAL_DESTINATIONS.get(country, {})

def search_destination(query):
    """Search for destinations by name"""
    query_lower = query.lower()
    results = []
    
    # Search countries
    for country, data in GLOBAL_DESTINATIONS.items():
        if query_lower in country.lower():
            results.append({"type": "country", "name": country, "data": data})
        else:
            # Search states/cities
            for state in data.get("states", []):
                if query_lower in state.lower():
                    results.append({"type": "state", "name": f"{state}, {country}", "data": data})
    
    return results

def get_destinations_by_region(region):
    """Get all destinations in a specific region"""
    destinations = {}
    for country, data in GLOBAL_DESTINATIONS.items():
        if data.get("region") == region:
            destinations[country] = data
    return destinations

def get_all_regions():
    """Get list of all unique regions"""
    regions = set()
    for data in GLOBAL_DESTINATIONS.values():
        regions.add(data.get("region"))
    return sorted(list(regions))
