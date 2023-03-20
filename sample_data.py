import random

# List of available car makes
MAKES = ["Acura", "Alfa Romeo", "Audi", "BMW", "Bentley", "Bugatti", "Cadillac", "Chevrolet", "Chrysler", "Dodge",
         "Ferrari", "Fiat", "Ford", "GMC", "Honda", "Hyundai", "Infiniti", "Jaguar", "Jeep", "Kia", "Lamborghini",
         "Land Rover", "Lexus", "Lincoln", "Lotus", "Maserati", "Mazda", "McLaren", "Mercedes-Benz", "Mini",
         "Mitsubishi", "Nissan", "Pagani", "Porsche", "Ram", "Rolls-Royce", "Subaru", "Tesla", "Toyota",
         "Volkswagen", "Volvo"]

# Dictionary of available car models per make
MODELS = {
    "Acura": ["ILX", "MDX", "NSX", "RDX", "RLX", "TLX"],
    "Alfa Romeo": ["Giulia", "Stelvio"],
    "Audi": ["A3", "A4", "A5", "A6", "A7", "A8", "Q3", "Q5", "Q7", "Q8", "RS5", "S4", "S5", "S6", "S7", "S8"],
    "BMW": ["2 Series", "3 Series", "4 Series", "5 Series", "6 Series", "7 Series", "8 Series", "i3", "i8", "M2", "M3",
            "M4", "M5", "M6", "X1", "X2", "X3", "X4", "X5", "X6", "X7", "Z4"],
    "Bentley": ["Bentayga", "Continental GT", "Flying Spur", "Mulsanne"],
    "Bugatti": ["Chiron", "Divo"],
    "Cadillac": ["ATS", "CT4", "CT5", "CT6", "CTS", "Escalade", "XT4", "XT5", "XT6"],
    "Chevrolet": ["Camaro", "Colorado", "Corvette", "Equinox", "Impala", "Malibu", "Silverado", "Tahoe", "Traverse"],
    "Chrysler": ["300", "Pacifica", "Voyager"],
    "Dodge": ["Challenger", "Charger", "Durango", "Grand Caravan", "Journey", "Ram 1500", "Ram 2500"],
    "Ferrari": ["488 GTB", "488 Pista", "812 Superfast", "GTC4Lusso"],
    "Fiat": ["500"],
    "Ford": ["Bronco", "Edge", "Escape", "Expedition", "Explorer", "F-150", "Fiesta", "Focus", "Fusion", "Mustang",
             "Ranger", "Taurus"],
    "GMC": ["Acadia", "Canyon", "Sierra 1500", "Sierra 2500HD", "Terrain", "Yukon"],
    "Honda": ["Accord", "Civic", "Clarity", "CR-V", "Fit", "HR-V", "Insight", "Odyssey", "Passport", "Pilot",
              "Ridgeline"],
    "Hyundai": ['Accent', 'Elantra', 'Genesis', 'Santa Fe', 'Sonata', 'Tucson', 'Veloster'],
    "Infiniti": ['Q50', 'Q60', 'Q70', 'QX30', 'QX50', 'QX60', 'QX70', 'QX80'],
    "Jaguar": ['E-PACE', 'F-PACE', 'F-TYPE', 'I-PACE', 'XE', 'XF', 'XJ'],
    "Jeep": ['Cherokee', 'Compass', 'Gladiator', 'Grand Cherokee', 'Renegade', 'Wrangler'],
    "Kia": ['Forte', 'Optima', 'Rio', 'Sedona', 'Sorento', 'Soul', 'Sportage', 'Stinger'],
    "Lamborghini": ['Aventador', 'Huracan', 'Urus'],
    "Land Rover": ['Defender', 'Discovery', 'Discovery Sport', 'Range Rover', 'Range Rover Evoque', 'Range Rover Sport',
                   'Range Rover Velar'],
    "Lexus": ['ES', 'GX', 'IS', 'LC', 'LS', 'NX', 'RX', 'UX'],
    "Lincoln": ['Aviator', 'Continental', 'Corsair', 'MKC', 'MKZ', 'Nautilus', 'Navigator'],
    "Lotus": ['Elise', 'Evora', 'Exige'],
    "Maserati": ['Ghibli', 'GranTurismo', 'Levante', 'Quattroporte'],
    "Mazda": ['CX-3', 'CX-30', 'CX-5', 'CX-9', 'Mazda3', 'Mazda6', 'MX-5 Miata'],
    "McLaren": ['540C', '570GT', '570S', '600LT', '720S'],
    "Mercedes-Benz": ['A-Class', 'C-Class', 'CLA-Class', 'CLS-Class', 'E-Class', 'G-Class', 'GLA-Class', 'GLC-Class',
                      'GLE-Class', 'GLS-Class', 'S-Class', 'SL-Class', 'Sprinter', 'AMG GT'],
    "Mini": ['Clubman', 'Convertible', 'Countryman', 'Hardtop', 'John Cooper Works'],
    "Mitsubishi": ['Eclipse Cross', 'Mirage', 'Outlander', 'Outlander PHEV'],
    "Nissan": ['Altima', 'Armada', 'Frontier', 'GT-R', 'Kicks', 'Leaf', 'Maxima', 'Murano', 'Pathfinder', 'Rogue',
               'Sentra', 'Titan', 'Versa'],
    "Pagani": ['Huayra', 'Zonda'],
    "Porsche": ['911', 'Boxster', 'Cayenne', 'Cayman', 'Macan', 'Panamera', 'Taycan'],
    "Ram": ['1500', '2500', '3500', 'Promaster', 'Promaster City'],
    "Rolls-Royce": ['Dawn', 'Ghost', 'Wraith'],
    "Subaru": ['Ascent', 'BRZ', 'Crosstrek', 'Forester', 'Impreza', 'Legacy', 'Outback'],
    "Tesla": ['Model 3', 'Model S', 'Model X', 'Model Y'],
    "Toyota": ['4Runner', 'Camry', 'Corolla', 'Highlander', 'Prius', 'RAV4'],
    "Volkswagen": ["Atlas", "Beetle", "Golf", "Golf GTI", "Golf R", "Jetta", "Passat", "Tiguan", "Touareg"],
    "Volvo": ["S60", "S90", "V60", "V90", "XC40", "XC60", "XC90"]
}


def generate_random_autos(num_autos):
    autos_data = []
    for i in range(num_autos):
        make = random.choice(MAKES)
        model = random.choice(MODELS[make])
        year = random.randint(1900, 2024)
        price = round(random.uniform(0, 200000), 2)
        vin = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', k=17))
        auto = {"vin": vin, "make": make, "model": model, "year": year, "price": price}
        autos_data.append(auto)
    return autos_data
