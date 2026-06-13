"""seed real product catalog

Revision ID: 7c9a4f2d1b6e
Revises: 3a6d3c93d7f2
Create Date: 2026-06-04 00:00:00.000000
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "7c9a4f2d1b6e"
down_revision: Union[str, Sequence[str], None] = "3a6d3c93d7f2"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


CATEGORY_PRODUCTS = {
    "Mobiles": [
        "Apple iPhone 15", "Apple iPhone 15 Pro", "Samsung Galaxy S24", "Samsung Galaxy S24 Ultra",
        "Google Pixel 8", "Google Pixel 8 Pro", "OnePlus 12", "OnePlus Nord CE 4",
        "Xiaomi Redmi Note 13 Pro", "Xiaomi 14", "Motorola Edge 50 Pro", "Motorola Razr 40",
        "Nothing Phone 2", "Realme 12 Pro", "Vivo V30 Pro", "Vivo X100",
        "Oppo Reno 11 Pro", "Poco X6 Pro", "iQOO Neo 9 Pro", "Honor 90",
    ],
    "Laptops": [
        "Apple MacBook Air 13", "Apple MacBook Pro 14", "Dell XPS 13", "Dell Inspiron 15",
        "HP Pavilion 14", "HP Spectre x360", "Lenovo ThinkPad X1 Carbon", "Lenovo IdeaPad Slim 5",
        "Asus Zenbook 14", "Asus ROG Zephyrus G14", "Acer Aspire 7", "Acer Swift Go",
        "Microsoft Surface Laptop 5", "MSI Modern 14", "MSI Katana 15", "Samsung Galaxy Book4",
        "LG Gram 16", "Alienware m16", "Gigabyte G5", "Framework Laptop 13",
    ],
    "Electronics": [
        "Sony Bravia 55 inch 4K TV", "Samsung Crystal 4K TV", "LG OLED C3 TV", "TCL QLED 4K TV",
        "Amazon Echo Dot", "Google Nest Hub", "Apple iPad Air", "Samsung Galaxy Tab S9",
        "Sony PlayStation 5", "Microsoft Xbox Series X", "Nintendo Switch OLED", "GoPro Hero 12",
        "DJI Osmo Action 4", "Canon EOS R50", "Nikon Z30", "Fujifilm Instax Mini 12",
        "Anker PowerCore Power Bank", "Logitech MX Master 3S", "Kindle Paperwhite", "Wacom One Tablet",
    ],
    "Headphones": [
        "Apple AirPods Pro", "Apple AirPods Max", "Sony WH-1000XM5", "Sony WF-1000XM5",
        "Bose QuietComfort Ultra", "Bose SoundLink Flex", "Sennheiser Momentum 4", "JBL Tune 770NC",
        "JBL Live Pro 2", "Marshall Major IV", "Beats Studio Pro", "Nothing Ear 2",
        "OnePlus Buds Pro 2", "Samsung Galaxy Buds2 Pro", "Boat Rockerz 450", "Boat Airdopes 141",
        "Skullcandy Crusher Evo", "Anker Soundcore Liberty 4", "Audio-Technica ATH-M50x", "Jabra Elite 8 Active",
    ],
    "Fashion": [
        "Levi's 511 Slim Jeans", "Levi's Trucker Jacket", "H&M Cotton Shirt", "Zara Linen Shirt",
        "Uniqlo AIRism T-Shirt", "Allen Solly Formal Shirt", "Peter England Chinos", "Van Heusen Blazer",
        "Nike Sportswear Hoodie", "Adidas Originals Track Jacket", "Puma Essentials Joggers", "Under Armour Training Tee",
        "Tommy Hilfiger Polo", "Calvin Klein Crew T-Shirt", "U.S. Polo Assn. Shirt", "Roadster Denim Jacket",
        "Jack & Jones Slim Shirt", "Marks & Spencer Trousers", "Forever 21 Dress", "Mango Midi Dress",
    ],
    "Shoes": [
        "Nike Air Max 90", "Nike Revolution 7", "Adidas Ultraboost", "Adidas Samba OG",
        "Puma RS-X", "Puma Softride", "Reebok Classic Leather", "Converse Chuck Taylor",
        "Vans Old Skool", "New Balance 574", "Skechers Go Walk", "Asics Gel-Kayano",
        "Under Armour Charged", "Crocs Classic Clog", "Woodland Leather Boot", "Clarks Desert Boot",
        "Red Tape Sneakers", "Bata Formal Shoes", "Hush Puppies Loafers", "Lee Cooper Boots",
    ],
    "Home & Kitchen": [
        "Prestige Pressure Cooker", "Hawkins Contura Cooker", "Pigeon Non Stick Pan", "Wonderchef Granite Set",
        "Borosil Glass Lunch Box", "Milton Thermosteel Flask", "Cello Water Bottle", "Tupperware Storage Container",
        "Ikea Dinner Plate Set", "Philips Air Fryer", "Instant Pot Duo", "Nescafe Coffee Maker",
        "Kent Water Purifier", "Eureka Forbes Vacuum Cleaner", "Dyson V12 Detect", "Atomberg Renesa Fan",
        "Orient Electric Kettle", "Morphy Richards Toaster", "Butterfly Mixer Grinder", "Bajaj Majesty Oven",
    ],
    "Books": [
        "Atomic Habits by James Clear", "The Psychology of Money by Morgan Housel", "Ikigai by Hector Garcia",
        "Deep Work by Cal Newport", "The Lean Startup by Eric Ries", "Rich Dad Poor Dad by Robert Kiyosaki",
        "The Alchemist by Paulo Coelho", "Harry Potter and the Sorcerer's Stone", "The Hobbit by J.R.R. Tolkien",
        "1984 by George Orwell", "The Great Gatsby by F. Scott Fitzgerald", "Pride and Prejudice by Jane Austen",
        "Sapiens by Yuval Noah Harari", "Zero to One by Peter Thiel", "Thinking Fast and Slow by Daniel Kahneman",
        "To Kill a Mockingbird by Harper Lee", "The Silent Patient by Alex Michaelides", "The Kite Runner by Khaled Hosseini",
        "A Brief History of Time by Stephen Hawking", "Clean Code by Robert C. Martin",
    ],
    "Beauty": [
        "Maybelline Fit Me Foundation", "Maybelline Colossal Mascara", "Lakme 9to5 Lipstick", "Lakme Eyeconic Kajal",
        "L'Oreal Paris Serum", "L'Oreal Paris Shampoo", "Nivea Soft Cream", "Nivea Body Lotion",
        "Cetaphil Gentle Cleanser", "Minimalist Niacinamide Serum", "The Ordinary Hyaluronic Acid", "Neutrogena Sunscreen",
        "Biotique Bio Cucumber Toner", "Mamaearth Ubtan Face Wash", "Plum Green Tea Moisturizer", "Dove Body Wash",
        "Garnier Micellar Water", "Himalaya Neem Face Wash", "Forest Essentials Cleanser", "Kama Ayurveda Rose Water",
    ],
    "Sports": [
        "Yonex Astrox Badminton Racquet", "Li-Ning Turbo Badminton Racquet", "Cosco Football", "Nivia Storm Football",
        "SG Cricket Bat", "MRF Genius Cricket Bat", "Kookaburra Cricket Ball", "Wilson Tennis Racquet",
        "Head Graphene Tennis Racquet", "Spalding Basketball", "Nike Dri-FIT Shorts", "Adidas Training Gloves",
        "Fitbit Charge 6", "Garmin Forerunner Watch", "Decathlon Yoga Mat", "Strauss Foam Roller",
        "Boldfit Resistance Band", "Lifeline Dumbbell Set", "Speedo Swimming Goggles", "Quechua Hiking Backpack",
    ],
    "Toys": [
        "LEGO Classic Bricks", "LEGO City Police Car", "Hot Wheels 5 Car Pack", "Barbie Dreamhouse Doll",
        "Nerf Elite Blaster", "Monopoly Classic Board Game", "Scrabble Original", "Jenga Classic",
        "Funskool Memory Game", "Play-Doh Modeling Compound", "Fisher-Price Rock-a-Stack", "VTech Learning Laptop",
        "Rubik's Cube 3x3", "Ravensburger Puzzle", "Melissa & Doug Wooden Blocks", "Remote Control Monster Truck",
        "Pokemon Trading Card Pack", "Marvel Action Figure", "Disney Frozen Elsa Doll", "Transformers Optimus Prime",
    ],
    "Grocery": [
        "Tata Sampann Toor Dal", "Tata Salt", "Aashirvaad Atta", "Daawat Basmati Rice",
        "India Gate Basmati Rice", "Fortune Sunflower Oil", "Saffola Gold Oil", "Amul Butter",
        "Amul Cheese Slices", "Nestle Everyday Milk Powder", "Nescafe Classic Coffee", "Tata Tea Gold",
        "Bru Instant Coffee", "Maggi 2 Minute Noodles", "Kellogg's Corn Flakes", "Quaker Oats",
        "Britannia Good Day Cookies", "Parle-G Biscuits", "Haldiram's Bhujia", "Cadbury Dairy Milk",
    ],
    "Furniture": [
        "Ikea Billy Bookcase", "Ikea Poang Chair", "Wakefit Orthopedic Mattress", "Wakefit Study Table",
        "Nilkamal Plastic Chair", "Nilkamal Storage Cabinet", "Godrej Interio Wardrobe", "Godrej Interio Office Chair",
        "Urban Ladder Sofa", "Pepperfry Coffee Table", "Durian Recliner", "HomeTown Dining Table",
        "Sleepyhead Bed Frame", "The Sleep Company Mattress", "Featherlite Ergonomic Chair", "Spacewood TV Unit",
        "DeckUp Shoe Rack", "Amazon Basics Office Desk", "Solimo Bean Bag", "Bluewud Wall Shelf",
    ],
    "Watches": [
        "Apple Watch Series 9", "Apple Watch SE", "Samsung Galaxy Watch6", "Garmin Venu 3",
        "Fitbit Versa 4", "Amazfit GTR 4", "Noise ColorFit Pro", "Boat Wave Call",
        "Titan Neo Analog Watch", "Titan Edge Watch", "Fastrack Reflex Watch", "Casio G-Shock",
        "Casio Enticer Watch", "Timex Expedition Watch", "Fossil Grant Watch", "Fossil Gen 6",
        "Seiko 5 Sports Watch", "Citizen Eco-Drive Watch", "Tissot PRX Watch", "Daniel Wellington Classic Watch",
    ],
    "Appliances": [
        "LG 260L Refrigerator", "Samsung 253L Refrigerator", "Whirlpool Double Door Refrigerator", "Haier Mini Refrigerator",
        "LG 7kg Washing Machine", "Samsung 8kg Washing Machine", "Bosch Front Load Washing Machine", "IFB Dishwasher",
        "Voltas 1.5 Ton AC", "Daikin Inverter AC", "Blue Star Window AC", "Havells Air Cooler",
        "Philips Steam Iron", "Bajaj Mixer Grinder", "Preethi Zodiac Mixer", "Panasonic Microwave Oven",
        "LG Convection Microwave", "Crompton Room Heater", "Usha Sewing Machine", "Eureka Forbes Air Purifier",
    ],
    "Automotive": [
        "Bosch Car Wiper Blade", "Michelin Tyre Inflator", "3M Car Shampoo", "Shell Helix Engine Oil",
        "Castrol Magnatec Engine Oil", "Wavex Car Wax", "Jopasu Car Duster", "Bergmann Car Vacuum",
        "Amaron Car Battery", "Exide Car Battery", "Autofy Phone Holder", "Qubo Dash Camera",
        "Steelbird Helmet", "Vega Full Face Helmet", "Studds Riding Helmet", "GoMechanic Tool Kit",
        "Turtle Wax Polish", "Motul Chain Lube", "Liqui Moly Additive", "Osram LED Headlight",
    ],
    "Baby": [
        "Pampers Active Pants", "Huggies Wonder Pants", "MamyPoko Pants", "Johnson's Baby Lotion",
        "Johnson's Baby Shampoo", "Himalaya Baby Powder", "Sebamed Baby Wash", "Chicco Feeding Bottle",
        "Philips Avent Bottle", "Mee Mee Baby Stroller", "R for Rabbit Car Seat", "LuvLap Baby Carrier",
        "Fisher-Price Baby Gym", "Mothercare Romper", "Babyhug Cotton Onesie", "Nestle Cerelac",
        "Lactogen Infant Formula", "Pigeon Baby Wipes", "Chicco Baby Soap", "Aveeno Baby Moisturizer",
    ],
    "Health": [
        "Omron Blood Pressure Monitor", "Dr Trust Pulse Oximeter", "Accu-Chek Glucometer", "OneTouch Glucometer",
        "HealthSense Weighing Scale", "Dettol Antiseptic Liquid", "Savlon Handwash", "Dabur Chyawanprash",
        "Himalaya Liv.52", "Baidyanath Honey", "Revital H Capsules", "Supradyn Multivitamin",
        "MuscleBlaze Whey Protein", "Optimum Nutrition Whey", "Ensure Nutrition Drink", "Vicks Vaporub",
        "Volini Pain Relief Gel", "Moov Pain Relief Spray", "Cetaphil Moisturizing Lotion", "N95 Protective Mask",
    ],
    "Pet Supplies": [
        "Pedigree Adult Dog Food", "Royal Canin Puppy Food", "Drools Chicken Dog Food", "Whiskas Cat Food",
        "Me-O Cat Food", "Sheba Cat Food", "Himalaya Erina Coat Cleanser", "Captain Zack Dog Shampoo",
        "Trixie Dog Leash", "Heads Up For Tails Collar", "Petsy Dog Bed", "Petkit Water Fountain",
        "Amazon Basics Pet Crate", "Goofy Tails Chew Toy", "Choostix Dog Treats", "Farmina N&D Pet Food",
        "Purepet Cat Litter", "Foodie Puppies Bowl", "Beaphar Tick Spray", "PetSafe Training Clicker",
    ],
    "Gaming": [
        "Sony DualSense Controller", "Xbox Wireless Controller", "Nintendo Switch Joy-Con", "Logitech G Pro Mouse",
        "Razer DeathAdder V3", "SteelSeries Apex Keyboard", "HyperX Cloud II Headset", "Corsair K70 Keyboard",
        "ASUS TUF Gaming Monitor", "Acer Nitro Gaming Monitor", "BenQ Zowie Monitor", "Elgato Stream Deck",
        "Blue Yeti Microphone", "Secretlab Titan Chair", "Razer Iskur Chair", "PlayStation Spider-Man 2",
        "Xbox Forza Horizon 5", "Nintendo Zelda Tears of the Kingdom", "Steam Deck OLED", "Meta Quest 3",
    ],
}

VARIANTS = [
    ("Standard", 0, 1),
    ("Plus", 500, 2),
    ("Premium", 1200, 3),
    ("Pro", 2400, 4),
    ("Bundle Pack", 3600, 5),
]


def upgrade() -> None:
    connection = op.get_bind()

    for category_name in CATEGORY_PRODUCTS:
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
            {"names": list(CATEGORY_PRODUCTS.keys())},
        ).fetchall()
    }

    products = []
    for category_index, (category_name, product_lines) in enumerate(CATEGORY_PRODUCTS.items(), start=1):
        for product_index, product_name in enumerate(product_lines, start=1):
            for variant_name, variant_price, variant_stock in VARIANTS:
                products.append(
                    {
                        "name": f"{product_name} - {variant_name}",
                        "description": f"{variant_name} variant of {product_name} in {category_name}.",
                        "price": float((category_index * 100) + (product_index * 75) + variant_price),
                        "stock": 25 + variant_stock + (product_index % 10),
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
    for product_lines in CATEGORY_PRODUCTS.values():
        for product_name in product_lines:
            for variant_name, _, _ in VARIANTS:
                names.append(f"{product_name} - {variant_name}")

    connection.execute(
        sa.text("DELETE FROM product WHERE name = ANY(:names)"),
        {"names": names},
    )
