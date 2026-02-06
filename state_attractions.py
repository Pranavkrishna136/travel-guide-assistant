"""
State-Specific Travel Information
Comprehensive guides for destinations worldwide with specific attractions, cuisine, and details
"""

STATE_ATTRACTIONS = {
    "India": {
        "Kerala": {
            "must_visit": [
                "Munnar - Tea plantations & misty mountains",
                "Alleppey (Alappuzha) - Houseboat backwater cruises",
                "Kochi (Cochin) - Chinese fishing nets & spice markets",
                "Thekkady - Periyar National Park wildlife",
                "Varkala - Beach cliffs & Janardhana Swami Temple",
                "Kumarakom - Bird sanctuary & backwaters",
                "Fort Kochi - Colonial architecture & heritage",
                "Wayanad - Waterfalls, trekking & coffee plantations"
            ],
            "local_cuisine": [
                "Kerala Fish Curry - coconut-based spice blend",
                "Appam - rice cake with stew",
                "Puttu - bamboo steamed cake",
                "Biriyani - fragrant rice dish",
                "Prawn dishes - fresh seafood specialty",
                "Idiyappam - rice noodles",
                "Kerala Paratha - layered flatbread"
            ],
            "best_time": "June to September (monsoon), October to May (dry season)",
            "how_to_reach": {
                "by_air": "Kochi International Airport (COK) - 30km from city",
                "by_rail": "Kochi Railway Station - well connected to major cities",
                "by_road": "Highways connect to Tamil Nadu, Karnataka, and other states"
            },
            "accommodation": {
                "luxury": "₹5,000-15,000 per night",
                "mid_range": "₹2,000-5,000 per night",
                "budget": "₹500-2,000 per night"
            },
            "activities": [
                "Houseboat cruises in backwaters",
                "Ayurvedic spa & massages",
                "Spice plantation tours",
                "Tea estate visits",
                "Wildlife spotting",
                "Beach activities",
                "Temple visits",
                "Trekking in hill stations"
            ],
            "culture": "Blend of Hindu, Muslim, and Christian traditions. Known for Kathakali dance and Kerala school of painting."
        },
        "Goa": {
            "must_visit": [
                "Baga Beach - Popular beach with watersports",
                "Calangute Beach - Long sandy stretch",
                "Basilica of Bom Jesus - Historic church",
                "Fort Aguada - 17th century Portuguese fort",
                "Palolem Beach - South Goa paradise",
                "Dudhsagar Falls - Massive waterfall",
                "Old Goa - UNESCO heritage site",
                "Spice plantations - Tour & tasting"
            ],
            "local_cuisine": [
                "Fish Curry - Goan specialty with coconut",
                "Vindaloo - Spicy pork curry",
                "Feijoada - Black bean stew",
                "Poi - Sweet bread",
                "Fresh seafood - prawns, fish, crab"
            ],
            "best_time": "November to February (cool & dry)",
            "how_to_reach": {
                "by_air": "Dabolim Airport - 30km from Panaji",
                "by_rail": "Madgaon Railway Station",
                "by_road": "Well connected via NH highways"
            },
            "accommodation": {
                "luxury": "₹4,000-12,000 per night",
                "mid_range": "₹1,500-4,000 per night",
                "budget": "₹400-1,500 per night"
            },
            "activities": [
                "Beach relaxation & watersports",
                "Portuguese heritage tours",
                "Spice plantation visits",
                "Houseboat cruises",
                "Casino nights",
                "Dolphin spotting",
                "Church visits",
                "Night markets & shopping"
            ],
            "culture": "Portuguese colonial heritage with blend of Hindu and Catholic traditions. Vibrant nightlife and beach culture."
        },
        "Rajasthan": {
            "must_visit": [
                "Jaipur - City Palace & Hawa Mahal",
                "Udaipur - City Palace & Lake Pichola",
                "Pushkar - Holy lake & camel fair",
                "Jodhpur - Mehrangarh Fort & blue city",
                "Jaisalmer - Golden fort & desert safari",
                "Mount Abu - Hill station with temples",
                "Chittorgarh - Massive hill fort",
                "Ranakpur - Marble Jain temples"
            ],
            "local_cuisine": [
                "Daal Baati Churma - Rajasthani meal",
                "Gatte ki Sabzi - Gram flour vegetable",
                "Ker Sangri - Desert vegetables",
                "Malpoua - Sweet dessert",
                "Bajra roti - Millet bread"
            ],
            "best_time": "October to March (cool season)",
            "how_to_reach": {
                "by_air": "Jaipur International Airport",
                "by_rail": "Multiple railway stations",
                "by_road": "Good highway connectivity"
            },
            "accommodation": {
                "luxury": "₹6,000-20,000 per night",
                "mid_range": "₹2,500-6,000 per night",
                "budget": "₹800-2,500 per night"
            },
            "activities": [
                "Fort & palace tours",
                "Desert safari",
                "Camel trekking",
                "Temple visits",
                "Puppet shows",
                "Tie & dye workshops",
                "Local market exploration",
                "Photography tours"
            ],
            "culture": "Royal Rajasthani heritage with colorful festivals, traditional crafts, and warrior traditions."
        },
        "Delhi": {
            "must_visit": [
                "Red Fort - Mughal fortress",
                "Jama Masjid - India's largest mosque",
                "Raj Ghat - Mahatma Gandhi's memorial",
                "India Gate - Famous monument",
                "Qutub Minar - UNESCO world heritage",
                "Chandni Chowk - Historic market",
                "National Museum - Art & artifacts",
                "Lotus Temple - Bahai worship place"
            ],
            "local_cuisine": [
                "Chole Bhature - Chickpea bread meal",
                "Butter Chicken - Creamy chicken curry",
                "Aloo Paratha - Potato flatbread",
                "Chaat - Street snacks",
                "Tandoori items - Grilled specialties"
            ],
            "best_time": "October to March",
            "how_to_reach": {
                "by_air": "Indira Gandhi International Airport",
                "by_rail": "New Delhi Railway Station",
                "by_road": "National highways converge here"
            },
            "accommodation": {
                "luxury": "₹8,000-25,000 per night",
                "mid_range": "₹3,000-8,000 per night",
                "budget": "₹800-3,000 per night"
            },
            "activities": [
                "Historical monument tours",
                "Street food walk",
                "Museum visits",
                "Market shopping",
                "Temple/mosque visits",
                "Garden walks",
                "Metro exploration",
                "Nightlife in Hauz Khas"
            ],
            "culture": "Capital city blending ancient history, Mughal heritage, and modern India."
        },
        "Mumbai": {
            "must_visit": [
                "Gateway of India - Iconic arch",
                "Taj Mahal Hotel - Historic hotel",
                "Marine Drive - Coastal road",
                "Colaba Causeway - Market & shopping",
                "Chhatrapati Shivaji Terminus - Heritage railway station",
                "Haji Ali Dargah - Mosque on island",
                "Worli Sea Link - Engineering marvel",
                "Bollywood studios & Elephant Caves"
            ],
            "local_cuisine": [
                "Vada Pav - Fried lentil snack",
                "Pav Bhaji - Spiced vegetable curry",
                "Misal Pav - Spicy curry with bread",
                "Mumbai Biryani - Rice dish",
                "Seafood specialties - Fresh fish & prawns"
            ],
            "best_time": "October to May",
            "how_to_reach": {
                "by_air": "Mumbai International Airport",
                "by_rail": "Central & Western Railway stations",
                "by_road": "Well connected highways"
            },
            "accommodation": {
                "luxury": "₹7,000-20,000 per night",
                "mid_range": "₹2,500-7,000 per night",
                "budget": "₹700-2,500 per night"
            },
            "activities": [
                "Heritage walks",
                "Beach relaxation",
                "Bollywood studio tours",
                "Shopping at malls & markets",
                "Island visits (Elephanta)",
                "Pub & club nights",
                "Art gallery visits",
                "Food tours"
            ],
            "culture": "Bustling metropolis, Bollywood hub, financial capital with mix of old & new Mumbai."
        },
        "Jaipur": {
            "must_visit": [
                "City Palace - Still partly royal residence",
                "Hawa Mahal - Pink 5-story structure",
                "Jantar Mantar - Astronomical instruments",
                "Albert Hall Museum - Art & artifacts",
                "City Market - Traditional shopping",
                "Govind Dev Temple - Sacred temple",
                "Ram Niwas Garden - Green space",
                "Amer Fort - Hilltop fortification"
            ],
            "local_cuisine": [
                "Gatte ki Sabzi - Gram flour curry",
                "Lal Maas - Spicy meat curry",
                "Bajra Roti - Millet bread",
                "Mohan Maas - Meat preparation",
                "Ghargharhi - Sweet dish"
            ],
            "best_time": "October to March",
            "how_to_reach": {
                "by_air": "Jaipur International Airport",
                "by_rail": "Jaipur Railway Station",
                "by_road": "Well connected to Delhi & other states"
            },
            "accommodation": {
                "luxury": "₹5,000-15,000 per night",
                "mid_range": "₹2,000-5,000 per night",
                "budget": "₹600-2,000 per night"
            },
            "activities": [
                "Fort & palace tours",
                "Market shopping",
                "Temple visits",
                "Photography",
                "Tribal village tours",
                "Pottery workshops",
                "Hot air balloon rides",
                "Polo matches (seasonal)"
            ],
            "culture": "Pink city with royal Rajasthani heritage, famous for architecture, textiles, and gemstones."
        },
        "Chennai": {
            "must_visit": [
                "Marina Beach - 13km long sandy beach with sunset views",
                "Fort St. George - Historic British fort with museum",
                "San Thome Cathedral - Iconic Gothic-style cathedral",
                "Government Museum - Art collection and antiques",
                "Kapaleeshwar Temple - 400-year-old Shiva temple in Mylapore",
                "Parthasarathy Temple - Ancient Vaishnavite temple",
                "Brihadeeswarar Temple - UNESCO World Heritage Chola dynasty temple",
                "Thousand Lights Mosque - Historic mosque with colonial architecture"
            ],
            "local_cuisine": [
                "Dosa - Crispy rice & lentil crepe with sambar",
                "Idli - Fluffy steamed rice cake",
                "Sambar - Spiced lentil & vegetable stew",
                "Rasam - Hot & tangy tamarind soup",
                "Uttapam - Savory rice pancake with vegetables",
                "Payasam - Rice pudding dessert with jaggery",
                "Filter Coffee - Traditional strong South Indian coffee",
                "Appalam - Thin crispy wafer"
            ],
            "best_time": "October to March (cool & pleasant weather)",
            "how_to_reach": {
                "by_air": "Chennai International Airport - 16km from city center",
                "by_rail": "Chennai Central & Egmore Railway Stations",
                "by_road": "NH-44 and state highways well connected"
            },
            "accommodation": {
                "luxury": "₹5,000-15,000 per night",
                "mid_range": "₹2,000-5,000 per night",
                "budget": "₹600-2,000 per night"
            },
            "activities": [
                "Beach relaxation & sunset walks",
                "Museum exploration",
                "Heritage walks in Fort area",
                "Temple tours & prayers",
                "Street food sampling",
                "Colonial architecture tours",
                "Yoga & meditation centers",
                "Shopping in T.Nagar & Anna Salai"
            ],
            "culture": "Dravidian civilization with ancient temple traditions, Bharatanatyam classical dance, Tamil language heritage, British colonial influence, and coastal culture."
        },
        "Uttar Pradesh": {
            "must_visit": [
                "Taj Mahal - White marble mausoleum in Agra, UNESCO World Heritage",
                "Agra Fort - Red sandstone fortress with Mughal architecture",
                "Varanasi Ghats - Sacred river banks with pilgrimage sites",
                "Kashi Vishwanath Temple - Ancient temple on Ganges river",
                "Mathura - Krishna's birthplace with temples & pilgrimage sites",
                "Vrindavan - Krishna devotional temples & Radha-Krishna sites",
                "Lucknow - Mughal & British colonial architecture including Bara Imambara",
                "Sarnath - Buddhist pilgrimage site where Buddha preached"
            ],
            "local_cuisine": [
                "Biryani - Fragrant rice with meat or vegetables",
                "Seekh Kebab - Ground meat kebab grilled on skewer",
                "Galauti Kebab - Melt-in-mouth spiced meat kebab",
                "Sheermal - Saffron flavored flatbread",
                "Nihari - Slow-cooked meat stew",
                "Khees - Wheat pudding with ghee",
                "Paan - Betel leaf preparation",
                "Lucknowi Namkeen - Savory snacks"
            ],
            "best_time": "October to March (cool season)",
            "how_to_reach": {
                "by_air": "Agra & Lucknow airports - well connected to major cities",
                "by_rail": "Central & North Central Railways - excellent connectivity",
                "by_road": "National highways from Delhi & other states"
            },
            "accommodation": {
                "luxury": "₹5,500-16,000 per night",
                "mid_range": "₹2,000-5,500 per night",
                "budget": "₹500-2,000 per night"
            },
            "activities": [
                "Taj Mahal sunrise/sunset visits",
                "Spiritual pilgrimage walks",
                "Boat rides on Ganges",
                "Temple exploration tours",
                "Traditional Mughal cuisine tours",
                "Shopping in historic bazaars",
                "Photography of monuments",
                "Wildlife watching"
            ],
            "culture": "Religious pilgrimage hub with Mughal heritage, Krishna devotion centers, ancient Buddhist sites, and architectural wonders spanning centuries."
        },
        "Himachal Pradesh": {
            "must_visit": [
                "Shimla - Victorian hill station with Mall Road shopping",
                "Manali - Adventure hub with Beas River & Solang Valley",
                "Dharamshala - Home of Dalai Lama & Tibetan culture",
                "McLeod Ganj - Tibetan refugee settlement with monasteries",
                "Khajjiar - 'Mini Switzerland' with green meadows",
                "Dalhousie - Colonial hill town with pine forests",
                "Rohtang Pass - Mountain pass with scenic views",
                "Tirthan Valley - Trout fishing & adventure sports"
            ],
            "local_cuisine": [
                "Chole Bhature - Chickpea curry with fried bread",
                "Madra - Lentil curry with yogurt",
                "Chikhalwali - Gram flour pancake",
                "Aloo Parathas - Potato-filled flatbread",
                "Mittha - Sweet preparation",
                "Honey from Himalayas - Local specialty",
                "Trout Fish - Fresh mountain fish",
                "Siddu - Steamed bread with filling"
            ],
            "best_time": "March to June, September to October (pleasant weather)",
            "how_to_reach": {
                "by_air": "Shimla Airport or Chandigarh Airport nearby",
                "by_rail": "Narrow gauge railway from Chandigarh to Shimla",
                "by_road": "Good highways from Delhi & Punjab"
            },
            "accommodation": {
                "luxury": "₹6,000-18,000 per night",
                "mid_range": "₹2,500-6,000 per night",
                "budget": "₹800-2,500 per night"
            },
            "activities": [
                "Trekking in mountains",
                "Paragliding in Bir Billing",
                "Skiing in winter",
                "Monastery visits",
                "Adventure sports (rafting, zip-lining)",
                "Shopping at hill stations",
                "Photography walks",
                "Yoga & meditation retreats"
            ],
            "culture": "Himalayan hill stations with British colonial legacy, Tibetan Buddhist influence, adventure sports culture, and nature-loving community."
        },
        "Uttarakhand": {
            "must_visit": [
                "Rishikesh - Yoga capital with Ganges river & temples",
                "Haridwar - Holy pilgrimage city on Ganges",
                "Auli - Snow sports destination in winter",
                "Chopta - Green meadows & camping site",
                "Mussoorie - Queen of Hills with Ridge Walk",
                "Nainital - Lake town surrounded by mountains",
                "Corbett National Park - Tiger & wildlife sanctuary",
                "Tungnath - Highest Shiva temple in India"
            ],
            "local_cuisine": [
                "Momos - Tibetan dumplings",
                "Thukpa - Tibetan noodle soup",
                "Bhang ki Chutney - Hemp seed chutney",
                "Aloo Pie - Potato-filled pastry",
                "Phaanu - Sorghum bread",
                "Kafuli - Spinach bean dish",
                "Gahat ki Dal - Horse gram lentil",
                "Sweets with Jaggery - Traditional desserts"
            ],
            "best_time": "March to May, September to November (mild weather)",
            "how_to_reach": {
                "by_air": "Delhi Airport then road transport",
                "by_rail": "Haridwar Railway Station main hub",
                "by_road": "Well connected from Delhi & Himachal"
            },
            "accommodation": {
                "luxury": "₹5,000-15,000 per night",
                "mid_range": "₹2,000-5,000 per night",
                "budget": "₹600-2,000 per night"
            },
            "activities": [
                "Yoga & meditation at ashrams",
                "River rafting on Ganges",
                "Trekking to waterfalls & peaks",
                "Wildlife safari in Corbett",
                "Skiing at Auli",
                "Lake boating",
                "Adventure sports",
                "Religious pilgrimage tours"
            ],
            "culture": "Spiritual destination known for yoga, ashrams, Hindu pilgrimages, adventure sports, and Himalayan nature-based tourism."
        },
        "Bangalore": {
            "must_visit": [
                "Vidhana Soudha - Iconic government building with Neo-Dravidian architecture",
                "Cubbon Park - 300-acre park with trees, gardens & museums",
                "Tipu Sultan's Summer Palace - 18th century wooden palace",
                "Bangalore Palace - Tudor-style castle with gardens",
                "Bull Temple (Nandi Temple) - 16th century temple with granite bull statue",
                "Virupaksha Temple - Historic temple in Basavanagudi",
                "Lalbagh Botanical Garden - 200-year-old garden with flowers",
                "Glass House in Lalbagh - Victorian greenhouse with exotic plants"
            ],
            "local_cuisine": [
                "Idli - Steamed rice cakes",
                "Dosa - Crispy rice & lentil crepe with sambar",
                "Ragi Mudde - Finger millet dumpling",
                "Bisibelebath - Mixed rice with lentils & vegetables",
                "Chitranna - Lemon rice",
                "Coffee - Bangalore filter coffee culture",
                "Benne Dosa - Butter dosa",
                "Payasam - Rice pudding dessert"
            ],
            "best_time": "October to March (pleasant weather, cool evenings)",
            "how_to_reach": {
                "by_air": "Kempegowda International Airport - 40km from city",
                "by_rail": "Bangalore City Railway Station - Central location",
                "by_road": "NH-44 and state highways well connected"
            },
            "accommodation": {
                "luxury": "₹6,000-18,000 per night",
                "mid_range": "₹2,500-6,000 per night",
                "budget": "₹800-2,500 per night"
            },
            "activities": [
                "Park walks in Cubbon Park",
                "Palace & architecture tours",
                "Temple exploration",
                "Botanical garden visits",
                "Shopping in Brigade Road & MG Road",
                "Tech park tours",
                "Pub & nightlife culture",
                "Art galleries & cafes"
            ],
            "culture": "Garden City known for greenery, IT hub of India, cosmopolitan lifestyle, emerging startup culture, and pleasant climate."
        },
        "Mysore": {
            "must_visit": [
                "Mysore Palace - Opulent royal palace with intricate architecture",
                "Chamundeshwari Temple - 900-year-old hilltop temple",
                "St. Philomena's Cathedral - Gothic-style church with twin spires",
                "Government Museum - Art collection with ivory carvings",
                "Jayachamarajendra Art Gallery - Indian paintings & sculptures",
                "Karanji Lake - Scenic artificial lake with gardens",
                "Brindavan Garden - Royal garden with fountains",
                "Ranganathittu Bird Sanctuary - Island with bird species"
            ],
            "local_cuisine": [
                "Mysore Pak - Sweet made with ghee & gram flour",
                "Dosa - Rice & lentil crepe",
                "Idli - Steamed rice cake",
                "Sambar - Lentil vegetable stew",
                "Uttapam - Savory pancake",
                "Filter Coffee - South Indian coffee",
                "Mysore Rasam - Tangy soup",
                "Payasam - Rice pudding"
            ],
            "best_time": "October to February (cool season, Dasara festival)",
            "how_to_reach": {
                "by_air": "Bangalore Airport - 150km away",
                "by_rail": "Mysore Railway Station - South Western Railway",
                "by_road": "NH-44 and state highways - 3 hours from Bangalore"
            },
            "accommodation": {
                "luxury": "₹5,000-15,000 per night",
                "mid_range": "₹2,000-5,000 per night",
                "budget": "₹600-2,000 per night"
            },
            "activities": [
                "Palace tours with evening illumination",
                "Temple visits & prayers",
                "Chamundi Hill hiking",
                "Garden exploration",
                "Museum visits",
                "Bird sanctuary tours",
                "Shopping for silk & sandalwood",
                "Dasara festival participation (seasonal)"
            ],
            "culture": "Royal Mysore heritage with palace splendor, Dasara festival celebrations, silk weaving tradition, and classical arts."
        }
    },
    "Thailand": {
        "Bangkok": {
            "must_visit": [
                "Grand Palace - Royal residence & temples",
                "Temple of the Emerald Buddha - Sacred shrine",
                "Wat Arun - Temple of Dawn",
                "Floating Markets - Traditional boat markets",
                "Lumphini Park - Urban park",
                "Chatuchak Market - Weekend market",
                "Muay Thai Boxing - Sports experience",
                "Sky Bar - Rooftop bar with views"
            ],
            "local_cuisine": [
                "Pad Thai - Stir-fried noodles",
                "Green Curry - Spiced coconut curry",
                "Tom Yum - Hot & sour soup",
                "Pad Krapow - Basil stir-fry",
                "Satay - Grilled meat skewers",
                "Mango Sticky Rice - Dessert",
                "Fish Cakes - Fried patties"
            ],
            "best_time": "November to February (cool & dry)",
            "how_to_reach": {
                "by_air": "Suvarnabhumi International Airport",
                "by_rail": "Bangkok Railway Station",
                "by_road": "Highway network"
            },
            "accommodation": {
                "luxury": "3,000-10,000 THB per night",
                "mid_range": "1,000-3,000 THB per night",
                "budget": "300-1,000 THB per night"
            },
            "activities": [
                "Temple exploration",
                "Thai massage",
                "Muay Thai training",
                "River cruises",
                "Night market visits",
                "Shopping",
                "Nightlife",
                "Tuk-tuk tours"
            ],
            "culture": "Buddhist kingdom with strong temple culture, Muay Thai martial arts, and welcoming spirit."
        },
        "Phuket": {
            "must_visit": [
                "Patong Beach - Popular beach",
                "Phang Nga Bay - Limestone formations",
                "James Bond Island - Famous rock",
                "Big Buddha - 45-meter statue",
                "Old Phuket Town - Heritage buildings",
                "Similan Islands - Diving spot",
                "Kata Beach - Quiet beach",
                "Bangla Road - Entertainment"
            ],
            "local_cuisine": [
                "Pad Thai - Fried noodles",
                "Massaman Curry - Peanut curry",
                "Tom Kha - Coconut soup",
                "Fresh Seafood - Grilled fish",
                "Mango Sticky Rice - Dessert",
                "Green Papaya Salad - Som Tam",
                "Pad See Ew - Soy noodles"
            ],
            "best_time": "November to April (dry season)",
            "how_to_reach": {
                "by_air": "Phuket International Airport",
                "by_ferry": "From nearby islands",
                "by_road": "Highway from mainland"
            },
            "accommodation": {
                "luxury": "2,500-8,000 THB per night",
                "mid_range": "800-2,500 THB per night",
                "budget": "250-800 THB per night"
            },
            "activities": [
                "Beach swimming",
                "Scuba diving",
                "Island hopping",
                "Water sports",
                "Nightlife",
                "Spa & massage",
                "Hiking",
                "Photography"
            ],
            "culture": "Beach paradise with water sports, Buddhist temples, and tropical island lifestyle."
        }
    },
    "Indonesia": {
        "Bali": {
            "must_visit": [
                "Ubud - Arts & culture center with rice terraces",
                "Seminyak Beach - Popular beach with resorts",
                "Sanur Beach - Scenic beach town",
                "Sacred Monkey Forest - Jungle with temples",
                "Tegallalang Rice Terraces - Iconic green valleys",
                "Tanah Lot Temple - Coastal temple on rock",
                "Mount Batur - Volcano with sunrise hike",
                "Goa Gajah (Elephant Cave) - Ancient temple carved in rock"
            ],
            "local_cuisine": [
                "Nasi Goreng - Fried rice with egg",
                "Sate - Grilled meat skewers",
                "Gado-gado - Vegetable salad with peanut sauce",
                "Lumpia - Spring rolls",
                "Perkedel - Potato fritter",
                "Bakso - Meatball soup",
                "Bali Coffee - Local specialty",
                "Lawar - Traditional Balinese dish"
            ],
            "best_time": "April to October (dry season)",
            "how_to_reach": {
                "by_air": "Ngurah Rai International Airport",
                "by_ferry": "From Java island",
                "by_road": "Internal roads well maintained"
            },
            "accommodation": {
                "luxury": "800,000-3,000,000 IDR per night",
                "mid_range": "300,000-800,000 IDR per night",
                "budget": "100,000-300,000 IDR per night"
            },
            "activities": [
                "Rice terrace trekking",
                "Temple exploration",
                "Surfing & water sports",
                "Volcano hiking",
                "Spa & massage treatments",
                "Yoga retreats",
                "Diving & snorkeling",
                "Art & craft workshops"
            ],
            "culture": "Hindu-Buddhist island with spiritual temples, traditional dance performances, rice farming, and artistic heritage."
        }
    },
    "Japan": {
        "Tokyo": {
            "must_visit": [
                "Senso-ji Temple - Ancient Buddhist temple in Asakusa",
                "Tokyo Tower - Landmark with observation deck",
                "Shibuya Crossing - World's busiest intersection",
                "Meiji Shrine - Shinto shrine in forest",
                "Tsukiji Fish Market - Fresh seafood & food stalls",
                "Imperial Palace - Historic royal residence",
                "Akihabara - Electronics & anime district",
                "Harajuku - Fashion & youth culture center"
            ],
            "local_cuisine": [
                "Sushi - Raw fish with rice",
                "Ramen - Noodle soup",
                "Tempura - Battered fried vegetables & seafood",
                "Tonkatsu - Breaded pork cutlet",
                "Okonomiyaki - Savory pancake",
                "Matcha - Green tea",
                "Mochi - Rice cake",
                "Udon - Thick wheat noodles"
            ],
            "best_time": "March to May, September to November (mild weather)",
            "how_to_reach": {
                "by_air": "Narita or Haneda International Airports",
                "by_rail": "Shinkansen bullet train from cities",
                "by_subway": "Extensive metro network"
            },
            "accommodation": {
                "luxury": "¥20,000-50,000 per night",
                "mid_range": "¥8,000-20,000 per night",
                "budget": "¥3,000-8,000 per night"
            },
            "activities": [
                "Temple & shrine visits",
                "Shopping in Shibuya & Shinjuku",
                "Cherry blossom viewing (spring)",
                "Karaoke nights",
                "Tea ceremonies",
                "Anime/manga museum visits",
                "Garden walks",
                "Sumo wrestling matches"
            ],
            "culture": "Blending ancient traditions with cutting-edge technology, known for temples, pop culture, precision, and hospitality."
        },
        "Kyoto": {
            "must_visit": [
                "Fushimi Inari Shrine - Thousands of red torii gates",
                "Arashiyama Bamboo Grove - Serene bamboo forest",
                "Kinkaku-ji (Golden Pavilion) - Golden temple on water",
                "Kiyomizu-dera Temple - Ancient wooden temple",
                "Gion District - Historic geisha district",
                "Philosopher's Path - Canal-side walking path",
                "Maruyama Park - Scenic park with ancient trees",
                "Nijo Castle - Historic samurai castle"
            ],
            "local_cuisine": [
                "Kaiseki - Multi-course traditional dinner",
                "Yudofu - Hot pot with tofu",
                "Kyo-ryori - Kyoto-style cuisine",
                "Matcha Desserts - Green tea cakes",
                "Pickled vegetables - Local specialty",
                "Udon noodles - Thick wheat noodles",
                "Sukiyaki - Beef hot pot",
                "Green tea - Premium grade"
            ],
            "best_time": "April-May (spring), October-November (autumn)",
            "how_to_reach": {
                "by_rail": "Shinkansen from Tokyo (2.5 hours)",
                "by_bus": "Long-distance buses available",
                "by_car": "Rental car with driver"
            },
            "accommodation": {
                "luxury": "¥25,000-60,000 per night",
                "mid_range": "¥10,000-25,000 per night",
                "budget": "¥4,000-10,000 per night"
            },
            "activities": [
                "Temple & shrine exploration",
                "Geisha district walks",
                "Bamboo forest trekking",
                "Garden visits",
                "Traditional tea ceremony",
                "Kimono rental & wearing",
                "Traditional craft workshops",
                "Lantern festival (summer)"
            ],
            "culture": "Ancient capital with 2,000+ temples, geisha traditions, traditional arts, and preserved historic atmosphere."
        }
    },
    "China": {
        "Beijing": {
            "must_visit": [
                "Great Wall of China - Ancient fortification",
                "Forbidden City - Imperial palace complex",
                "Tiananmen Square - Large public plaza",
                "Summer Palace - Royal garden retreat",
                "Temple of Heaven - Iconic temple complex",
                "Ming Tombs - Imperial mausoleums",
                "Hutong neighborhoods - Traditional alleyways",
                "Bird's Nest Stadium - Olympic architecture"
            ],
            "local_cuisine": [
                "Peking Duck - Roasted duck specialty",
                "Jiaozi - Dumplings with filling",
                "Mapo Tofu - Spicy tofu dish",
                "Hot pot - Communal cooking",
                "Chow mein - Fried noodles",
                "Kung Pao Chicken - Spiced chicken",
                "Dim sum - Small portions variety",
                "Baozi - Steamed buns"
            ],
            "best_time": "April to May, September to October (mild weather)",
            "how_to_reach": {
                "by_air": "Beijing Capital International Airport",
                "by_rail": "High-speed trains from major cities",
                "by_road": "Highway network"
            },
            "accommodation": {
                "luxury": "¥800-2,000 per night",
                "mid_range": "¥300-800 per night",
                "budget": "¥100-300 per night"
            },
            "activities": [
                "Great Wall trekking",
                "Palace tours",
                "Temple exploration",
                "Hutong rickshaw rides",
                "Tea ceremonies",
                "Martial arts training",
                "Night markets",
                "Photography"
            ],
            "culture": "Ancient imperial capital with 3,000+ years of history, traditional architecture, philosophy, and UNESCO World Heritage sites."
        }
    },
    "Spain": {
        "Barcelona": {
            "must_visit": [
                "Sagrada Familia - Gaudi's unfinished basilica",
                "Park Güell - Colorful park with city views",
                "Gothic Quarter - Medieval architecture",
                "La Rambla - Famous tree-lined boulevard",
                "Casa Batlló - Gaudi's modernist house",
                "Montjuïc - Hill with museums & fountains",
                "Barceloneta Beach - City beach with bars",
                "Casa Vicens - Gaudi's first house"
            ],
            "local_cuisine": [
                "Paella - Rice dish with seafood",
                "Tapas - Small appetizers variety",
                "Pan con tomate - Tomato on bread",
                "Escalivada - Grilled vegetables",
                "Fideuà - Noodle paella",
                "Jamón ibérico - Cured ham",
                "Calcots - Roasted onions",
                "Crema Catalana - Caramel dessert"
            ],
            "best_time": "April to June, September to October (pleasant weather)",
            "how_to_reach": {
                "by_air": "Barcelona-El Prat Airport",
                "by_rail": "AVE high-speed trains",
                "by_subway": "Metro system"
            },
            "accommodation": {
                "luxury": "€200-600 per night",
                "mid_range": "€80-200 per night",
                "budget": "€30-80 per night"
            },
            "activities": [
                "Gaudi architecture tours",
                "Beach activities",
                "Museum visits",
                "Food market exploration",
                "Flamenco shows",
                "Mountain hiking",
                "Sailing & water sports",
                "Nightlife & clubs"
            ],
            "culture": "Catalan capital known for Gaudi's distinctive architecture, modern art, beach culture, food, and passionate locals."
        }
    },
    "Italy": {
        "Rome": {
            "must_visit": [
                "Colosseum - Ancient Roman amphitheater",
                "Vatican City - Pope's residence & museums",
                "Roman Forum - Ancient ruins & temples",
                "Pantheon - Dome temple with oculus",
                "Trevi Fountain - Baroque fountain",
                "Spanish Steps - Famous staircase",
                "Sistine Chapel - Michelangelo's ceiling",
                "Castel Sant'Angelo - Historic castle"
            ],
            "local_cuisine": [
                "Carbonara - Creamy pasta with guanciale",
                "Cacio e Pepe - Cheese & black pepper pasta",
                "Amatriciana - Tomato bacon sauce",
                "Risotto - Creamy rice dish",
                "Gelato - Italian ice cream",
                "Tiramisu - Coffee dessert",
                "Ravioli - Stuffed pasta",
                "Osso Buco - Braised veal shanks"
            ],
            "best_time": "April to June, September to October",
            "how_to_reach": {
                "by_air": "Leonardo da Vinci Airport",
                "by_rail": "Trenitalia train services",
                "by_subway": "Metro & tram network"
            },
            "accommodation": {
                "luxury": "€200-500 per night",
                "mid_range": "€80-200 per night",
                "budget": "€30-80 per night"
            },
            "activities": [
                "Ancient site exploration",
                "Museum & art gallery visits",
                "Vatican tours",
                "Fountain visits",
                "Food tours",
                "Italian cooking classes",
                "Wine tasting",
                "Evening walks"
            ],
            "culture": "Eternal City with 2,500+ years of history, Renaissance art, Catholic heritage, classical architecture, and culinary traditions."
        }
    },
    "Mexico": {
        "Mexico City": {
            "must_visit": [
                "Templo Mayor - Aztec pyramid ruins",
                "Palacio Nacional - Government palace with murals",
                "Frida Kahlo Museum - Artist's iconic house",
                "National Museum of Anthropology - Largest museum",
                "Xochimilco Floating Gardens - Ancient waterways",
                "Coyoacán - Charming colonial neighborhood",
                "Chapultepec Park - Large urban park",
                "Metropolitan Cathedral - Colonial church"
            ],
            "local_cuisine": [
                "Tacos - Soft tortillas with fillings",
                "Mole - Complex sauce with spices",
                "Tamales - Corn dough packets",
                "Chiles Rellenos - Stuffed peppers",
                "Guacamole - Avocado dip",
                "Ceviche - Raw fish salad",
                "Elote - Corn with mayo & cheese",
                "Churros - Fried pastry sticks"
            ],
            "best_time": "October to April (dry season)",
            "how_to_reach": {
                "by_air": "Mexico City International Airport",
                "by_rail": "Limited intercity rail",
                "by_bus": "Extensive bus network"
            },
            "accommodation": {
                "luxury": "MXN 3,000-8,000 per night",
                "mid_range": "MXN 1,000-3,000 per night",
                "budget": "MXN 400-1,000 per night"
            },
            "activities": [
                "Museum exploration",
                "Archaeological site tours",
                "Floating garden boat rides",
                "Art market visits",
                "Street food sampling",
                "Cooking classes",
                "Nightlife in Polanco",
                "Neighborhood walking tours"
            ],
            "culture": "Aztec & colonial heritage with indigenous traditions, vibrant art scene, street culture, and world-class cuisine."
        }
    },
    "United States": {
        "New York": {
            "must_visit": [
                "Statue of Liberty - Iconic symbol",
                "Times Square - Tourist center",
                "Central Park - Urban park",
                "Empire State Building - Skyscraper",
                "Brooklyn Bridge - Historic bridge",
                "Metropolitan Museum - Art museum",
                "One World Trade - Modern building",
                "Broadway - Theater district"
            ],
            "local_cuisine": [
                "New York Pizza - Thin crust",
                "Hot Dogs - Street food",
                "Bagels - Breakfast item",
                "Pastrami - Deli sandwich",
                "Cheesecake - Dessert",
                "Lobster Rolls - Seafood",
                "Soft Pretzels - Snack"
            ],
            "best_time": "April to October",
            "how_to_reach": {
                "by_air": "JFK & LaGuardia Airports",
                "by_rail": "Amtrak & commuter rail",
                "by_road": "Interstate highways"
            },
            "accommodation": {
                "luxury": "$300-800 per night",
                "mid_range": "$120-300 per night",
                "budget": "$50-120 per night"
            },
            "activities": [
                "Museum visits",
                "Theater shows",
                "Shopping",
                "Dining",
                "Park walks",
                "Photography",
                "Nightlife",
                "Sports events"
            ],
            "culture": "Global metropolis, finance hub, diverse cultures, museums, theater, and iconic landmarks."
        },
        "California": {
            "must_visit": [
                "Golden Gate Bridge - San Francisco",
                "Disneyland - Theme park",
                "Hollywood - Entertainment hub",
                "Yosemite - National park",
                "Venice Beach - Boardwalk",
                "Universal Studios - Movie park",
                "Redwoods - Tall trees",
                "Big Sur - Coastal scenic"
            ],
            "local_cuisine": [
                "In-N-Out Burger - Fast food",
                "Fish Tacos - Mexican-inspired",
                "Avocado Toast - California style",
                "Wine - Napa Valley",
                "Farm-to-Table - Fresh produce",
                "Sushi - Japanese cuisine",
                "BBQ - Grilled meats"
            ],
            "best_time": "March to May, year-round possible",
            "how_to_reach": {
                "by_air": "Los Angeles & San Francisco",
                "by_rail": "Amtrak Surfliner",
                "by_road": "Interstate 5"
            },
            "accommodation": {
                "luxury": "$250-600 per night",
                "mid_range": "$100-250 per night",
                "budget": "$40-100 per night"
            },
            "activities": [
                "Beach activities",
                "Theme parks",
                "Wine tasting",
                "Hiking",
                "Surfing",
                "Photography",
                "Road trips",
                "Cultural sites"
            ],
            "culture": "Entertainment capital, tech hub, beach culture, outdoor recreation, diverse cuisine."
        },
        "Florida": {
            "must_visit": [
                "Miami Beach - Popular beach with nightlife",
                "Walt Disney World - Theme park resort (Orlando)",
                "Universal Studios Florida - Movie-themed park (Orlando)",
                "Everglades - Wetland ecosystem with wildlife",
                "Key West - Island with sunset culture",
                "Kennedy Space Center - Space launch facility",
                "South Beach - Art Deco architecture",
                "Busch Gardens - Animal park (Tampa)"
            ],
            "local_cuisine": [
                "Cuban Sandwich - Roasted meat sandwich",
                "Stone Crab - Crustacean specialty",
                "Conch Salad - Seafood salad",
                "Key Lime Pie - Citrus dessert",
                "Fresh Seafood - Grouper, snapper, lobster",
                "Cuban Food - Rice & beans",
                "Citrus Smoothies - Orange juice drinks",
                "Grouper Sandwich - Fish sandwich"
            ],
            "best_time": "November to April (cool & dry)",
            "how_to_reach": {
                "by_air": "Miami, Orlando, Tampa airports",
                "by_rail": "Amtrak to select cities",
                "by_road": "Interstate highways throughout"
            },
            "accommodation": {
                "luxury": "$200-500 per night",
                "mid_range": "$80-200 per night",
                "budget": "$40-80 per night"
            },
            "activities": [
                "Beach activities & swimming",
                "Theme park visits",
                "Everglades airboat tours",
                "Water sports & diving",
                "Shopping & dining",
                "Nightlife & clubs",
                "Key West sunset watching",
                "Wildlife spotting"
            ],
            "culture": "Beach destination with Cuban heritage, theme parks, wetland ecosystem, and island culture."
        },
        "Hawaii": {
            "must_visit": [
                "Waikiki Beach - Famous sandy beach (Oahu)",
                "Diamond Head - Iconic crater hike (Oahu)",
                "Mauna Kea - Tallest volcano with observatory",
                "Hawaii Volcanoes National Park - Active volcanoes (Big Island)",
                "Kauai Napali Coast - Dramatic cliffs & valleys",
                "Lanikai Beach - Turquoise waters (Windward Oahu)",
                "Pearl Harbor - Historic WWII site (Oahu)",
                "Haleakala National Park - Sunrise crater (Maui)"
            ],
            "local_cuisine": [
                "Poke - Cubed raw fish salad",
                "Loco Moco - Rice with gravy & fried egg",
                "Kalua Pork - Roasted pig",
                "Spam Musubi - Rice & spam roll",
                "Acai Bowl - Blended berry bowl",
                "Hawaiian Shave Ice - Frozen dessert",
                "Macadamia Nuts - Local nut snack",
                "Poi - Taro root paste"
            ],
            "best_time": "April to October (warmer), anytime possible",
            "how_to_reach": {
                "by_air": "Honolulu International Airport main hub",
                "by_inter-island": "Inter-island flights between islands",
                "by_car": "Rental cars on each island"
            },
            "accommodation": {
                "luxury": "$300-800 per night",
                "mid_range": "$120-300 per night",
                "budget": "$60-120 per night"
            },
            "activities": [
                "Beach swimming & sunbathing",
                "Crater hiking",
                "Snorkeling & diving",
                "Whale watching (winter)",
                "Sunset viewing",
                "Water sports",
                "Pearl Harbor tour",
                "Volcano exploration"
            ],
            "culture": "Island paradise with Hawaiian culture, volcanoes, beaches, Polynesian traditions, and tropical biodiversity."
        }
    },
    "France": {
        "Paris": {
            "must_visit": [
                "Eiffel Tower - Iron monument",
                "Louvre Museum - Art museum",
                "Notre-Dame - Gothic cathedral",
                "Arc de Triomphe - Monumental arch",
                "Sacré-Cœur - White basilica",
                "Champs-Élysées - Shopping avenue",
                "Versailles - Royal palace",
                "Montmartre - Artistic area"
            ],
            "local_cuisine": [
                "Croissants - Pastries",
                "Baguettes - Bread",
                "Escargot - Cooked snails",
                "Coq au Vin - Wine chicken",
                "French Onion Soup - Broth",
                "Crème Brûlée - Custard dessert",
                "Cheese & Wine - Local items"
            ],
            "best_time": "April to June, September to October",
            "how_to_reach": {
                "by_air": "Charles de Gaulle & Orly",
                "by_rail": "Eurostar & TGV",
                "by_road": "European highways"
            },
            "accommodation": {
                "luxury": "€300-800 per night",
                "mid_range": "€100-300 per night",
                "budget": "€40-100 per night"
            },
            "activities": [
                "Museum visits",
                "Palace tours",
                "River cruises",
                "Shopping",
                "Café culture",
                "Photography",
                "Art galleries",
                "Theater"
            ],
            "culture": "Art & culture capital, romance, haute cuisine, fashion, literature, fine wines."
        }
    },
    "Germany": {
        "Berlin": {
            "must_visit": [
                "Brandenburg Gate - Iconic symbol of reunification",
                "Berlin Wall Memorial - Historical divide remains",
                "Reichstag - Government building with glass dome",
                "Museumsinsel - Museum island with 5 museums",
                "Checkpoint Charlie - Cold War crossing point",
                "Charlottenburg Palace - Royal baroque palace",
                "TV Tower - Landmark with observation deck",
                "East Side Gallery - Street art on remaining wall"
            ],
            "local_cuisine": [
                "Currywurst - Curried sausage",
                "Schnitzel - Breaded meat cutlet",
                "Pretzel - Twisted bread",
                "Sauerkraut - Fermented cabbage",
                "Spätzle - Egg noodles",
                "Schweinshaxe - Roasted pork leg",
                "German Beer - Local brewing tradition",
                "Bread Varieties - Dark pumpernickel"
            ],
            "best_time": "May to September (mild weather)",
            "how_to_reach": {
                "by_air": "Berlin Tegel & Schönefeld Airports",
                "by_rail": "Deutsche Bahn trains",
                "by_road": "European highway network"
            },
            "accommodation": {
                "luxury": "€150-400 per night",
                "mid_range": "€60-150 per night",
                "budget": "€25-60 per night"
            },
            "activities": [
                "Historical site tours",
                "Museum exploration",
                "Monument visits",
                "Beer garden visits",
                "Street art tours",
                "Nightlife & clubs",
                "Shopping districts",
                "River cruises"
            ],
            "culture": "WWII & Cold War history, divided past, modern reunification, technology hub, vibrant nightlife."
        }
    },
    "UK": {
        "London": {
            "must_visit": [
                "Big Ben & Houses of Parliament - Gothic architecture",
                "Tower of London - Historic fortress & crown jewels",
                "Tower Bridge - Iconic bascule bridge",
                "Buckingham Palace - Royal residence",
                "Westminster Abbey - Historic Gothic church",
                "British Museum - World's largest museum",
                "London Eye - Ferris wheel with city views",
                "St. Paul's Cathedral - Baroque masterpiece"
            ],
            "local_cuisine": [
                "Fish & Chips - Battered fish with fries",
                "Beef Wellington - Tenderloin in pastry",
                "Shepherd's Pie - Meat under potato",
                "Bangers & Mash - Sausages & gravy",
                "Tea & Scones - Cream tea tradition",
                "Pork Pie - Pastry-wrapped meat",
                "Roast Dinner - Sunday tradition",
                "Jam Roly-Poly - Steamed pudding"
            ],
            "best_time": "April to June, September to October",
            "how_to_reach": {
                "by_air": "Heathrow, Gatwick, Stansted Airports",
                "by_rail": "Eurostar from Europe, National Rail",
                "by_subway": "Extensive Underground network"
            },
            "accommodation": {
                "luxury": "£150-400 per night",
                "mid_range": "£60-150 per night",
                "budget": "£30-60 per night"
            },
            "activities": [
                "Palace & monument tours",
                "Museum visits",
                "Theater shows (West End)",
                "River Thames cruises",
                "Shopping districts",
                "Pub culture",
                "Street markets",
                "Nightlife & dining"
            ],
            "culture": "Capital city with royal heritage, Gothic architecture, Victorian era legacy, world museums, and cosmopolitan culture."
        }
    },
    "Greece": {
        "Athens": {
            "must_visit": [
                "Acropolis - Ancient citadel with Parthenon",
                "Parthenon Temple - Iconic Greek structure",
                "Acropolis Museum - Archaeological artifacts",
                "Ancient Agora - Historic marketplace ruins",
                "Panathenaic Stadium - Ancient Olympic venue",
                "Syntagma Square - Central public square",
                "National Archaeological Museum - Largest museum",
                "Plaka District - Historic neighborhood"
            ],
            "local_cuisine": [
                "Gyros - Grilled meat in flatbread",
                "Souvlaki - Grilled meat skewers",
                "Moussaka - Layered eggplant dish",
                "Feta Cheese - Local cheese specialty",
                "Spanakopita - Spinach pie",
                "Greek Salad - Tomato & feta",
                "Baklava - Honey pastry dessert",
                "Ouzo - Anise liqueur"
            ],
            "best_time": "April to May, September to October",
            "how_to_reach": {
                "by_air": "Athens International Airport",
                "by_ferry": "From Mediterranean islands",
                "by_road": "Highway network"
            },
            "accommodation": {
                "luxury": "€120-350 per night",
                "mid_range": "€50-120 per night",
                "budget": "€20-50 per night"
            },
            "activities": [
                "Ancient ruins exploration",
                "Museum visits",
                "Acropolis climbing",
                "Island hopping",
                "Greek food tours",
                "Nightlife in Gazi district",
                "Walking neighborhood tours",
                "Photography of monuments"
            ],
            "culture": "Birthplace of Western civilization with ancient Greek ruins, mythology, Mediterranean lifestyle, and island culture."
        }
    },
    "Australia": {
        "Sydney": {
            "must_visit": [
                "Sydney Opera House - Iconic performing arts venue",
                "Sydney Harbour Bridge - Iconic bridge with climbs",
                "Bondi Beach - Famous beach with lifeguards",
                "Blue Mountains - Scenic mountains with hikes",
                "Royal Botanic Gardens - Waterfront gardens",
                "Manly Beach - Beach with promenade",
                "The Rocks - Historic neighbourhood",
                "Taronga Zoo - Waterfront zoo with views"
            ],
            "local_cuisine": [
                "Lamingtons - Chocolate coconut cake",
                "Pavlova - Meringue dessert with berries",
                "Barramundi - Local fish",
                "Meat Pies - Savory pastries",
                "Anzac Biscuits - Oat cookies",
                "Tim Tams - Chocolate biscuits",
                "Vegemite Toast - Yeast spread on toast",
                "Coffee Culture - Flat whites"
            ],
            "best_time": "September to November, March to May (spring/autumn)",
            "how_to_reach": {
                "by_air": "Sydney Kingsford Smith Airport",
                "by_rail": "CityRail metropolitan network",
                "by_ferry": "Sydney Harbour ferries"
            },
            "accommodation": {
                "luxury": "AUD 250-600 per night",
                "mid_range": "AUD 100-250 per night",
                "budget": "AUD 50-100 per night"
            },
            "activities": [
                "Beach swimming & surfing",
                "Opera House tours",
                "Bridge climbing experiences",
                "Harbour cruises",
                "Blue Mountains hikes",
                "Wildlife encounters",
                "Nightlife in Kings Cross",
                "Coastal walks"
            ],
            "culture": "Modern harbourside city with Australian beach culture, Indigenous heritage, outdoor lifestyle, and cosmopolitan dining."
        }
    },
    "Brazil": {
        "Rio de Janeiro": {
            "must_visit": [
                "Christ the Redeemer - Iconic statue on mountain",
                "Sugarloaf Mountain - Cable car with views",
                "Copacabana Beach - Famous beach with culture",
                "Ipanema Beach - Upscale beach neighbourhood",
                "Carnival (seasonal) - World's largest festival",
                "Maracanã Stadium - Olympic & football venue",
                "Corcovado Train - Historic mountain railway",
                "Tijuca National Park - Rainforest within city"
            ],
            "local_cuisine": [
                "Feijoada - Black bean stew with pork",
                "Pão de Queijo - Cheese bread",
                "Caipirnha - Sugarcane spirit drink",
                "Açai Bowl - Blended purple berries",
                "Brigadeiro - Chocolate truffle",
                "Churrasco - Brazilian barbecue",
                "Moqueca - Seafood stew",
                "Empanada - Filled pastry"
            ],
            "best_time": "December to February (summer, Carnival season)",
            "how_to_reach": {
                "by_air": "Tom Jobim International Airport",
                "by_rail": "Limited rail service",
                "by_car": "Rental cars available"
            },
            "accommodation": {
                "luxury": "BRL 600-1,500 per night",
                "mid_range": "BRL 250-600 per night",
                "budget": "BRL 80-250 per night"
            },
            "activities": [
                "Beach days & swimming",
                "Statue viewing & hiking",
                "Cable car rides",
                "Carnival participation (seasonal)",
                "Football stadium tours",
                "Mountain hikes",
                "Nightlife & clubs",
                "Rainforest exploration"
            ],
            "culture": "Vibrant beach city with Carnival spirit, samba music, Portuguese heritage, tropical climate, and passionate inhabitants."
        }
    }
}

# Fallback generic data for countries/states without specific entries
GENERIC_DESTINATION_DATA = {
    "must_visit": [
        "City center & downtown",
        "Historical monuments",
        "Local museums",
        "Parks & gardens",
        "Markets & shopping",
        "Religious sites",
        "Viewpoints & scenic spots",
        "Tourist information"
    ],
    "local_cuisine": [
        "Local street food",
        "Traditional dishes",
        "Fresh local produce",
        "Regional specialties",
        "Desserts & sweets",
        "Local beverages",
        "Night market food"
    ],
    "best_time": "Check local weather and festival calendar for best season",
    "how_to_reach": {
        "by_air": "Check for local airports",
        "by_rail": "Rail connections from major cities",
        "by_road": "National highways and road network"
    },
    "accommodation": {
        "luxury": "Premium 4-5 star hotels with full amenities",
        "mid_range": "Comfortable 3-4 star hotels",
        "budget": "Budget hotels, hostels, guesthouses"
    },
    "activities": [
        "Sightseeing & landmark visits",
        "Local market exploration",
        "Cultural performances",
        "Outdoor activities",
        "Food tours & dining",
        "Shopping & souvenirs",
        "Photography & scenic walks",
        "Local transportation tours"
    ],
    "culture": "Rich local traditions and heritage with unique customs and festivals."
}


def get_state_attractions(country, state):
    """Get attractions for a specific state - returns generic data as fallback"""
    if country in STATE_ATTRACTIONS and state in STATE_ATTRACTIONS[country]:
        return STATE_ATTRACTIONS[country][state]
    # Return generic fallback data for unknown destinations
    return GENERIC_DESTINATION_DATA


def get_must_visit_spots(country, state):
    """Get must-visit spots for a destination"""
    state_info = get_state_attractions(country, state)
    if state_info:
        return state_info.get("must_visit", GENERIC_DESTINATION_DATA["must_visit"])
    return GENERIC_DESTINATION_DATA["must_visit"]


def get_local_cuisine(country, state):
    """Get local cuisine specialties"""
    state_info = get_state_attractions(country, state)
    if state_info:
        return state_info.get("local_cuisine", GENERIC_DESTINATION_DATA["local_cuisine"])
    return GENERIC_DESTINATION_DATA["local_cuisine"]


def get_accommodation_prices(country, state):
    """Get accommodation price ranges"""
    state_info = get_state_attractions(country, state)
    if state_info:
        return state_info.get("accommodation", GENERIC_DESTINATION_DATA["accommodation"])
    return GENERIC_DESTINATION_DATA["accommodation"]


def get_activities(country, state):
    """Get popular activities"""
    state_info = get_state_attractions(country, state)
    if state_info:
        return state_info.get("activities", GENERIC_DESTINATION_DATA["activities"])
    return GENERIC_DESTINATION_DATA["activities"]


def get_best_time(country, state):
    """Get best time to visit"""
    state_info = get_state_attractions(country, state)
    if state_info:
        return state_info.get("best_time", GENERIC_DESTINATION_DATA["best_time"])
    return GENERIC_DESTINATION_DATA["best_time"]


def get_how_to_reach(country, state):
    """Get transportation information"""
    state_info = get_state_attractions(country, state)
    if state_info:
        return state_info.get("how_to_reach", GENERIC_DESTINATION_DATA["how_to_reach"])
    return GENERIC_DESTINATION_DATA["how_to_reach"]


def get_culture_info(country, state):
    """Get cultural information"""
    state_info = get_state_attractions(country, state)
    if state_info:
        return state_info.get("culture", GENERIC_DESTINATION_DATA["culture"])
    return GENERIC_DESTINATION_DATA["culture"]
