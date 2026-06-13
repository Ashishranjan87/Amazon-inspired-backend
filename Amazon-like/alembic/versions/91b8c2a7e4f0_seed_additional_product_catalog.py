"""seed additional product catalog

Revision ID: 91b8c2a7e4f0
Revises: 7c9a4f2d1b6e
Create Date: 2026-06-04 00:00:00.000000
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "91b8c2a7e4f0"
down_revision: Union[str, Sequence[str], None] = "7c9a4f2d1b6e"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


CATEGORY_SPECS = {
    "Mobiles": {
        "brands": ["Samsung", "Apple", "Google", "OnePlus"],
        "lines": ["Galaxy A55 5G", "iPhone 16", "Pixel 9", "Nord 4", "Galaxy M35 5G", "iPhone 16 Plus", "Pixel 9a", "Ace 3V", "Galaxy Z Flip6", "iPhone SE 4"],
    },
    "Laptops": {
        "brands": ["Dell", "HP", "Lenovo", "Asus"],
        "lines": ["XPS 14 9440", "Envy x360 14", "Yoga Slim 7", "Vivobook S15", "Latitude 7450", "Omen 16", "Legion Slim 5", "TUF A15", "Precision 3490", "EliteBook 840"],
    },
    "Electronics": {
        "brands": ["Sony", "LG", "Samsung", "Panasonic"],
        "lines": ["Bravia XR A80L", "QNED 80 TV", "The Frame TV", "Lumix G9 II", "Alpha ZV-E10", "UltraGear Monitor", "Freestyle Projector", "SoundSlayer Speaker", "Walkman A306", "SmartThings Station"],
    },
    "Headphones": {
        "brands": ["Sony", "Bose", "Sennheiser", "JBL"],
        "lines": ["ULT Wear", "QuietComfort Earbuds", "Accentum Plus", "Live Beam 3", "LinkBuds S", "SoundLink Max", "HD 450BT", "Tour One M2", "Inzone Buds", "Tune Beam"],
    },
    "Fashion": {
        "brands": ["Levi's", "Zara", "H&M", "Uniqlo"],
        "lines": ["Relaxed Fit Cargo", "Oxford Shirt", "Ribbed Knit Top", "Dry Pique Polo", "501 Original Jeans", "Linen Blend Blazer", "Cotton Twill Overshirt", "Smart Ankle Pants", "Sherpa Trucker", "Poplin Midi Dress"],
    },
    "Shoes": {
        "brands": ["Nike", "Adidas", "Puma", "New Balance"],
        "lines": ["Pegasus 41", "Gazelle Indoor", "Velocity Nitro 3", "Fresh Foam 1080", "Dunk Low", "Forum Low", "Suede Classic XXI", "327 Lifestyle", "Metcon 9", "Terrex Swift R3"],
    },
    "Home & Kitchen": {
        "brands": ["Philips", "Prestige", "Wonderchef", "Borosil"],
        "lines": ["Digital Air Fryer HD9252", "Svachh Nakshatra Cooker", "Nutri-Blend Mixer", "Pronto Glass Set", "Viva Collection Blender", "Omega Deluxe Cooktop", "Crimson Edge Knife Set", "Klara Lunch Box", "Daily Collection Kettle", "Cast Iron Kadhai"],
    },
    "Books": {
        "brands": ["Penguin", "HarperCollins", "O'Reilly", "Bloomsbury"],
        "lines": ["The Almanack of Naval Ravikant", "Dopamine Nation", "Designing Data-Intensive Applications", "Harry Potter Illustrated", "The Midnight Library", "Python Crash Course", "The Pragmatic Programmer", "The Song of Achilles", "Four Thousand Weeks", "System Design Interview"],
    },
    "Beauty": {
        "brands": ["Nykaa", "The Ordinary", "L'Oreal", "Neutrogena"],
        "lines": ["Matte Luxe Lipstick", "Retinol Serum", "Glycolic Bright Cream", "Hydro Boost Gel", "Clay It Cool Mask", "Multi-Peptide Serum", "Revitalift Day Cream", "Ultra Sheer Sunscreen", "SKINgenius Foundation", "Salicylic Acid Cleanser"],
    },
    "Sports": {
        "brands": ["Nike", "Adidas", "Decathlon", "Yonex"],
        "lines": ["Academy Football", "Tiro League Ball", "Domyos Training Bench", "Nanoflare 1000Z", "Pro Dri-FIT Tee", "Powerlift Belt", "Kipsta Agility Ladder", "Astrox 77 Play", "Run Division Jacket", "Predator Gloves"],
    },
    "Toys": {
        "brands": ["LEGO", "Hot Wheels", "Hasbro", "Mattel"],
        "lines": ["Creator Space Shuttle", "City Fire Rescue", "Premium Car Culture", "Transformers Legacy", "UNO Flip", "Technic Race Car", "Monster Trucks Pack", "Play-Doh Kitchen", "Barbie Fashionista", "Nerf Pro Stryfe"],
    },
    "Grocery": {
        "brands": ["Tata", "Amul", "Nestle", "Britannia"],
        "lines": ["Sampann Masoor Dal", "Taaza Milk", "Gold Corn Flakes", "NutriChoice Digestive", "Premium Tea", "Dark Chocolate", "Munch Nuts", "Cheese Cubes", "Himalayan Pink Salt", "Greek Style Yogurt"],
    },
    "Furniture": {
        "brands": ["Ikea", "Urban Ladder", "Pepperfry", "Wakefit"],
        "lines": ["Malm Chest", "Terry Sofa", "Amber Coffee Table", "Elevate Office Chair", "Kallax Shelf", "Apollo Recliner", "Kosmo Bed", "Dreamer Mattress", "Lack Side Table", "Aero Study Desk"],
    },
    "Watches": {
        "brands": ["Casio", "Titan", "Fossil", "Seiko"],
        "lines": ["Edifice Chronograph", "Maritime Automatic", "Machine Gen 6", "Presage Cocktail", "G-Shock GA-B2100", "Raga Viva", "Neutra Chrono", "Prospex Diver", "Vintage A168", "Workwear Multifunction"],
    },
    "Appliances": {
        "brands": ["LG", "Samsung", "Bosch", "Whirlpool"],
        "lines": ["Inverter Refrigerator 308L", "Bespoke Microwave", "Serie 6 Dishwasher", "Magicook Oven", "AI Direct Drive Washer", "Convertible Freezer", "Front Load Washer 8kg", "Intellifresh Fridge", "Dual Inverter AC", "PowerClean Dishwasher"],
    },
    "Automotive": {
        "brands": ["Bosch", "Shell", "3M", "Castrol"],
        "lines": ["AeroTwin Wiper", "Helix Ultra 5W40", "Ceramic Coating Kit", "Edge 5W30 Oil", "Horns Symphony", "Advance Scooter Oil", "Interior Cleaner", "Power1 Racing Oil", "Cabin Filter", "Tyre Shine Spray"],
    },
    "Baby": {
        "brands": ["Chicco", "Pampers", "Himalaya", "Philips Avent"],
        "lines": ["Bravo Stroller", "Premium Care Pants", "Gentle Baby Wipes", "Natural Response Bottle", "KeyFit Car Seat", "Splashers Diapers", "Soothing Baby Lotion", "Ultra Air Pacifier", "Next2Me Crib", "Complete Care Gift Set"],
    },
    "Health": {
        "brands": ["Omron", "Dr Trust", "HealthSense", "MuscleBlaze"],
        "lines": ["HEM 7156 Monitor", "Digital Thermometer", "Ultra-Lite Scale", "Biozyme Whey", "Compressor Nebulizer", "BP Smart Connect", "Kitchen Scale", "Creatine Monohydrate", "Pulse Oximeter 210", "Mass Gainer XXL"],
    },
    "Pet Supplies": {
        "brands": ["Royal Canin", "Pedigree", "Whiskas", "Trixie"],
        "lines": ["Maxi Adult Food", "Dentastix Treats", "Ocean Fish Pouch", "Premium Harness", "Kitten Persian Food", "Gravy Chicken Pouch", "Tuna Dry Food", "Scratching Post", "Mini Puppy Food", "Rubber Ball Toy"],
    },
    "Gaming": {
        "brands": ["Razer", "Logitech", "Corsair", "ASUS"],
        "lines": ["BlackWidow V4", "G502 X Plus", "Void RGB Elite", "ROG Ally X", "Basilisk V3", "Pro X Superlight", "HS80 Max", "ROG Azoth", "Kishi V2", "G Cloud Handheld"],
    },
    "Garden": {
        "brands": ["Karcher", "Ugaoo", "Gardena", "TrustBasket"],
        "lines": ["K2 Pressure Washer", "Jade Plant", "Classic Hose Reel", "Cocopeat Block", "WV 2 Window Vac", "Snake Plant", "Pruning Shears", "Vermicompost Mix", "Patio Cleaner", "Monstera Deliciosa"],
    },
    "Music": {
        "brands": ["Yamaha", "Casio", "Fender", "Roland"],
        "lines": ["F310 Acoustic Guitar", "CT-S300 Keyboard", "Squier Stratocaster", "FP-10 Digital Piano", "P-45 Piano", "SA-81 Mini Keyboard", "Mustang Micro Amp", "TD-02K Drum Kit", "C40 Classical Guitar", "GO:KEYS 5"],
    },
    "Travel": {
        "brands": ["Samsonite", "American Tourister", "Skybags", "Wildcraft"],
        "lines": ["S'Cure Spinner", "Kamiliant Harrier", "Trooper Backpack", "Rucksack 45L", "Evoa Cabin Bag", "Airconic Trolley", "Triton Duffel", "Hydra Trek Bag", "Proxis Spinner", "Rain Cover Pack"],
    },
    "Stationery": {
        "brands": ["Classmate", "Camlin", "Faber-Castell", "Pilot"],
        "lines": ["Pulse Notebook", "Kokuyo Brush Pen", "Connector Pens", "Hi-Tecpoint V5", "Long Book A4", "Scholar Geometry Box", "Polychromos Pencil", "G2 Gel Pen", "Origami Sheets", "V7 Cartridge Pen"],
    },
    "Tools": {
        "brands": ["Bosch", "Stanley", "Black+Decker", "Dewalt"],
        "lines": ["GSB 500W Drill", "FatMax Hammer", "Angle Grinder", "Cordless Impact Driver", "Laser Measure", "Socket Set", "Jigsaw 550W", "ToughSystem Toolbox", "Screwdriver Kit", "Rotary Tool Kit"],
    },
    "Smart Home": {
        "brands": ["Amazon", "Google", "Philips Hue", "TP-Link"],
        "lines": ["Echo Show 8", "Nest Mini", "White Ambiance Bulb", "Tapo Smart Plug", "Echo Pop", "Nest Doorbell", "Gradient Lightstrip", "Kasa Camera", "Fire TV Cube", "Nest Thermostat"],
    },
    "Cameras": {
        "brands": ["Canon", "Nikon", "Sony", "Fujifilm"],
        "lines": ["EOS R10", "Z fc", "Alpha A6700", "X-S20", "RF 50mm Lens", "Z 40mm Lens", "G Master 35mm", "XF 23mm Lens", "PowerShot V10", "Instax SQ40"],
    },
    "Kitchen Appliances": {
        "brands": ["KitchenAid", "Philips", "Bajaj", "Preethi"],
        "lines": ["Artisan Stand Mixer", "Soup Maker", "Rex Mixer Grinder", "Blue Leaf Platinum", "Classic Hand Blender", "Pop-Up Toaster HD2582", "Juicer Mixer JX4", "Chefpro Wet Grinder", "Food Processor 5KFP", "Chopper HR1393"],
    },
    "Personal Care": {
        "brands": ["Philips", "Braun", "Dyson", "Panasonic"],
        "lines": ["OneBlade Pro", "Series 9 Shaver", "Airwrap Multi-Styler", "ER-GN30 Trimmer", "Sonicare 3100", "Silk-epil 9", "Supersonic Dryer", "EH-NA65 Hair Dryer", "Multigroom 7000", "Oral-B iO Brush"],
    },
    "Jewelry": {
        "brands": ["Tanishq", "CaratLane", "Swarovski", "Mia"],
        "lines": ["Gold Hoop Earrings", "Solitaire Pendant", "Crystal Tennis Bracelet", "Diamond Nose Pin", "Pearl Drop Earrings", "Rose Gold Ring", "Angelic Necklace", "Silver Anklet", "Mangalsutra Chain", "Gemstone Studs"],
    },
    "Bags": {
        "brands": ["Fastrack", "Lavie", "Caprese", "Tommy Hilfiger"],
        "lines": ["Transit Backpack", "Satchel Handbag", "Structured Tote", "Core Laptop Bag", "Urban Sling", "Quilted Shoulder Bag", "Flap Crossbody", "Duffle Weekender", "Campus Backpack", "Classic Wallet"],
    },
    "Eyewear": {
        "brands": ["Ray-Ban", "Oakley", "Lenskart", "Fastrack"],
        "lines": ["Wayfarer Classic", "Holbrook Sunglasses", "Air Flex Frame", "Aviator Sunglasses", "Clubmaster Optics", "Frogskins Lite", "Blu Zero Glasses", "Navigator Shades", "Justin Sunglasses", "Rectangle TR90 Frame"],
    },
    "Home Decor": {
        "brands": ["Ikea", "Home Centre", "Chumbak", "Fabindia"],
        "lines": ["Ribba Frame", "Ceramic Vase", "Printed Cushion", "Block Print Runner", "Sinnerlig Lamp", "Wall Clock", "Quirky Mug Set", "Cotton Dhurrie", "Artificial Plant", "Brass Candle Holder"],
    },
    "Cleaning": {
        "brands": ["Surf Excel", "Harpic", "Lizol", "Scotch-Brite"],
        "lines": ["Matic Liquid", "Power Plus Cleaner", "Disinfectant Floor Cleaner", "Scrub Pad Set", "Easy Wash Powder", "Bathroom Cleaner", "Kitchen Cleaner", "Spin Mop Refill", "Detergent Bar", "Glass Cleaner"],
    },
    "Industrial": {
        "brands": ["3M", "Honeywell", "Bosch", "Stanley"],
        "lines": ["N95 8210 Mask", "Safety Goggles", "Cutting Disc", "Measuring Tape Pro", "Ear Plug Set", "Safety Helmet", "Metal Drill Bit", "Utility Knife", "Reflective Vest", "Work Gloves"],
    },
    "Seasonal": {
        "brands": ["Havells", "Usha", "Crompton", "Orient"],
        "lines": ["Mist Air Cooler", "Mist Fan", "Aura Heater", "Aeroquiet Fan", "Instanio Geyser", "Bloom Ceiling Fan", "Solarium Heater", "Cloud 3 Fan", "Quartz Heater", "Tower Fan"],
    },
    "Luxury": {
        "brands": ["Montblanc", "Tumi", "Hugo Boss", "Michael Kors"],
        "lines": ["Meisterstuck Pen", "Alpha Bravo Backpack", "Signature Wallet", "Jet Set Tote", "Explorer Cologne", "Voyageur Briefcase", "Chronograph Watch", "Parker Handbag", "Sartorial Card Holder", "Mercer Crossbody"],
    },
    "Outdoor": {
        "brands": ["Quechua", "Coleman", "Wildcraft", "The North Face"],
        "lines": ["2 Seconds Tent", "Sundome Tent", "Hypagrip Trek Shoes", "Borealis Backpack", "Arpenaz Jacket", "Cooler Box 28QT", "Poncho Raincoat", "Resolve Jacket", "Camping Chair", "Trekking Pole"],
    },
    "Art Supplies": {
        "brands": ["Camlin", "Faber-Castell", "Winsor & Newton", "Brustro"],
        "lines": ["Acrylic Colour Set", "Watercolour Pencils", "Cotman Paint Set", "Sketchbook A4", "Oil Pastel Set", "Graphite Pencil Set", "Canvas Board", "Fineliner Pack", "Brush Set", "Marker Pad"],
    },
    "Computer Accessories": {
        "brands": ["Logitech", "Anker", "Belkin", "SanDisk"],
        "lines": ["MX Keys S", "PowerExpand Hub", "BoostCharge Cable", "Extreme Portable SSD", "Brio 4K Webcam", "GaNPrime Charger", "USB-C Dock", "Ultra Dual Drive", "Lift Vertical Mouse", "SoundForm Speaker"],
    },
}

VARIANTS = [
    ("2026 Standard", 0, 1),
    ("2026 Plus", 650, 2),
    ("2026 Premium", 1450, 3),
    ("2026 Pro", 2800, 4),
    ("2026 Bundle", 4200, 5),
]


def _product_lines(spec):
    lines = []
    for brand in spec["brands"]:
        for line in spec["lines"]:
            lines.append(f"{brand} {line}")
    return lines


def upgrade() -> None:
    connection = op.get_bind()

    for category_name in CATEGORY_SPECS:
        connection.execute(
            sa.text(
                """
                INSERT INTO category (name, created_at, updated_at)
                VALUES (:name, NOW(), NOW())
                ON CONFLICT (name) DO NOTHING
                """
            ),
            {"name": category_name},
        )

    category_ids = {
        row.name: row.id
        for row in connection.execute(
            sa.text("SELECT id, name FROM category WHERE name = ANY(:names)"),
            {"names": list(CATEGORY_SPECS.keys())},
        ).fetchall()
    }

    products = []
    for category_index, (category_name, spec) in enumerate(CATEGORY_SPECS.items(), start=1):
        for product_index, product_name in enumerate(_product_lines(spec), start=1):
            for variant_name, variant_price, variant_stock in VARIANTS:
                products.append(
                    {
                        "name": f"{product_name} - {variant_name}",
                        "description": f"{variant_name} expansion catalog item for {product_name} in {category_name}.",
                        "price": float((category_index * 125) + (product_index * 85) + variant_price),
                        "stock": 30 + variant_stock + (product_index % 15),
                        "category_id": category_ids[category_name],
                    }
                )

    product_table = sa.table(
        "product",
        sa.column("name", sa.String),
        sa.column("description", sa.String),
        sa.column("price", sa.Float),
        sa.column("stock", sa.Integer),
        sa.column("category_id", sa.Integer),
        sa.column("created_at", sa.DateTime),
        sa.column("updated_at", sa.DateTime),
    )

    op.bulk_insert(product_table, products)


def downgrade() -> None:
    connection = op.get_bind()
    names = []
    for spec in CATEGORY_SPECS.values():
        for product_name in _product_lines(spec):
            for variant_name, _, _ in VARIANTS:
                names.append(f"{product_name} - {variant_name}")

    connection.execute(
        sa.text("DELETE FROM product WHERE name = ANY(:names)"),
        {"names": names},
    )
