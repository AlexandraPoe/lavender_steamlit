from pathlib import Path
import streamlit as st

st.set_page_config(page_title="Lavender Shop", page_icon="💜", layout="wide")

ASSET_DIR = Path(__file__).parent / "assets"

PRODUCTS = [
    #{"id": "lavender-label", "name": "LAVENDER LABEL", "description": "Premium smooth whiskey with rich flavor.", "price": 100, "image": "black-label.png", "category": "Lavender Gifts"},
    #{"id": "aqua-flask", "name": "AQUA FLASK", "description": "Durable, portable water bottle for hydration.", "price": 15, "image": "aqua-flask.png", "category": "Lavender Gifts"},
    #{"id": "black-notebook", "name": "BLACK NOTEBOOK", "description": "Versatile, essential tool for writing and planning.", "price": 25, "image": "black-notebook.png", "category": "Lavender Gifts"},
    #{"id": "essential-oil-mixed", "name": "ESSENTIAL OIL", "description": "Natural, aromatic oil for holistic well-being. Mixed aroma.", "price": 40, "image": "essential-oil.png", "category": "Lavender Gifts"},
    {"id": "essential-oil-lavender", "name": " ULEI ESENTIAL DE LEVĂNȚICĂ", "description": "Ulei de levănțică natural, puternic aromat, bio pentru o stare de bine. Obtinuta din culturi ECO de lavanda prin distilare în Comuna Gogoșu. Miros puternic, terapeutic.", "price": 35, "image": "essential-oil-lavender.png", "category": "Lavender Gifts"},
    #{"id": "gift-bag", "name": "GIFT BAG", "description": "Versatile, stylish bag for thoughtful gifting.", "price": 70, "image": "gift-net.png", "category": "Lavender Gifts"},
    #{"id": "perfume-her", "name": "PERFUME FOR HER", "description": "Elegant fragrance for feminine allure.", "price": 55, "image": "perfume-her.png", "category": "Perfumes"},
    #{"id": "perfume-him", "name": "PERFUME FOR HIM", "description": "Masculine scent for sophisticated charm.", "price": 50, "image": "perfume-him.png", "category": "Perfumes"},
    #{"id": "wallet-her", "name": "WALLET FOR HER", "description": "Stylish accessory for organizing essentials.", "price": 100, "image": "wallet-her.png", "category": "Accessories"},
    #{"id": "wallet-him", "name": "WALLET FOR HIM", "description": "Classic accessory for carrying cards and cash.", "price": 130, "image": "wallet-him.png", "category": "Accessories"},
    #{"id": "watch-her", "name": "WATCH FOR HER", "description": "Timeless accessory for feminine elegance.", "price": 150, "image": "watch-her.png", "category": "Accessories"},
    #{"id": "watch-him", "name": "WATCH FOR HIM", "description": "Sophisticated timepiece for masculine style.", "price": 200, "image": "watch-him.png", "category": "Accessories"},
]

if "cart" not in st.session_state:
    st.session_state.cart = {}
if "checkout_done" not in st.session_state:
    st.session_state.checkout_done = False

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(rgba(72, 0, 110, 0.82), rgba(72, 0, 110, 0.82)),
                    url('https://www.creativefabrica.com/wp-content/uploads/2023/08/25/French-Impressionist-Painting-In-Monet-Style-Of-Lavender-Fields-77673167-1.png');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    
    /* Main title */
    h1 {
        font-size: 46px !important;
        font-weight: 900 !important;
        color: white !important;
        margin-bottom: 8px !important;
    }
    
    /* Product image */
    img {
        border-radius: 18px;
        box-shadow: 0 14px 35px rgba(0,0,0,0.30);
        transition: transform 0.25s ease, box-shadow 0.25s ease;
    }
    
    img:hover {
        transform: scale(1.02);
        box-shadow: 0 18px 42px rgba(0,0,0,0.38);
    }
    
    /* Product title */
    .product-title {
        color: white;
        font-size: 22px;
        font-weight: 900;
        margin-top: 18px;
        letter-spacing: 0.3px;
        text-transform: uppercase;
    }
    
    /* Product description */
    .text-box {
        border: 1px solid rgba(255,255,255,0.85);
        background: rgba(255,255,255,0.94);
        color: #2d123d;
        border-radius: 16px;
        padding: 16px;
        margin-top: 10px;
        line-height: 1.65;
        font-weight: 500;
        box-shadow: 0 8px 24px rgba(0,0,0,0.20);
    }
    
    /* Price */
    .price-box {
        border: 2px solid white;
        background: linear-gradient(135deg, #ffffff, #f0ddff);
        color: #5a007f;
        border-radius: 16px;
        padding: 12px;
        margin-top: 10px;
        margin-bottom: 12px;
        font-size: 20px;
        font-weight: 900;
        text-align: center;
        box-shadow: 0 8px 22px rgba(0,0,0,0.22);
    }
    
    /* Streamlit buttons */
    .stButton > button {
        background: linear-gradient(135deg, #ffffff, #ead5ff);
        color: #4b006e;
        border: none;
        border-radius: 14px;
        padding: 12px 24px;
        font-weight: 900;
        font-size: 16px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.25);
        transition: all 0.25s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        background: white;
        color: #6B00B0;
        box-shadow: 0 12px 26px rgba(0,0,0,0.32);
    }
    
    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: #24172f;
    }
    
    section[data-testid="stSidebar"] * {
        color: white;
    }
    
    /* Mobile */
    @media (max-width: 768px) {
        .stApp {
            background-attachment: scroll;
        }
    
        h1 {
            font-size: 34px !important;
            text-align: center;
        }
    
        .product-title {
            font-size: 22px;
            text-align: left;
            color: white;
        }
    
        .text-box {
            font-size: 17px;
            background: rgba(255,255,255,0.97);
            padding: 18px;
        }
    
        .price-box {
            font-size: 21px;
            padding: 14px;
        }
    
        .stButton > button {
            width: 100%;
            font-size: 18px;
            padding: 14px;
        }
    }

        /* Force readable text on main page */
    [data-testid="stAppViewContainer"] h1,
    [data-testid="stAppViewContainer"] h2,
    [data-testid="stAppViewContainer"] h3,
    [data-testid="stAppViewContainer"] p,
    [data-testid="stAppViewContainer"] div {
        color: white;
    }
    
    /* Product boxes keep dark text */
    .text-box,
    .text-box *,
    .price-box,
    .price-box * {
        color: #2d123d !important;
    }
    
    /* Better mobile spacing */
    @media (max-width: 768px) {
        .block-container {
            padding-top: 2rem;
            padding-left: 1.2rem;
            padding-right: 1.2rem;
        }
    
        h1 {
            font-size: 38px !important;
            line-height: 1.1 !important;
            text-align: left !important;
            color: white !important;
        }
    
        h2, h3 {
            color: white !important;
        }
    
        [data-testid="stMarkdownContainer"] p {
            color: white !important;
            font-size: 16px;
            line-height: 1.5;
        }
    
        img {
            max-height: 420px;
            object-fit: cover;
        }
    }

    .hero-title {
    color: white !important;
    font-size: 48px;
    font-weight: 900;
    }

    @media (max-width: 768px) {
        .hero-title {
            font-size: 40px !important;
            line-height: 1.1;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<h1 class="hero-title">💜 GOGOȘU Lavender Shop</h1>', unsafe_allow_html=True)
st.caption("Comenzile se plasează doar prin apel telefonic. Verificați numărul de telefon în postarea de pe Facebook. Vă mulțumim pentru înțelegere.")

with st.sidebar:
    st.header("Căutare și filtrare")
    query = st.text_input("Caută produse", placeholder="Incearcă: ulei, ceas, parfum...")
    categories = sorted({p["category"] for p in PRODUCTS})
    selected_categories = st.multiselect("Categorii", categories, default=categories)
    sort_by = st.selectbox("Sort by", ["Default", "Preț: crescător", "Preț: descrescător", "Name"])

    st.divider()
    st.header("🛒 Coșul tău")

    if not st.session_state.cart:
        st.info("Coșul tău este gol.")
    else:
        total = 0
        for product_id, qty in list(st.session_state.cart.items()):
            product = next(p for p in PRODUCTS if p["id"] == product_id)
            line_total = product["price"] * qty
            total += line_total
            st.write(f"**{product['name']}**")
            st.write(f"RON {product['price']} × {qty} = **RON {line_total}**")
            new_qty = st.number_input(
                f"Quantity for {product['name']}", min_value=1, max_value=99, value=qty, key=f"qty_{product_id}", label_visibility="collapsed"
            )
            st.session_state.cart[product_id] = new_qty
            if st.button("Șterge ", key=f"remove_{product_id}"):
                del st.session_state.cart[product_id]
                st.rerun()
            st.divider()

        st.subheader(f"Total: RON {total}")
        if st.button("Checkout", type="primary"):
            st.session_state.cart = {}
            st.session_state.checkout_done = True
            st.rerun()

if st.session_state.checkout_done:
    st.success("Comenzile se plasează doar prin apel telefonic. Verifică numărul de telefon in postarea de pe Facebook. Vă mulțumim pentru înțelegere.")
    st.session_state.checkout_done = False

filtered = [
    p for p in PRODUCTS
    if p["category"] in selected_categories
    and (query.lower() in p["name"].lower() or query.lower() in p["description"].lower())
]

if sort_by == "Price: low to high":
    filtered = sorted(filtered, key=lambda p: p["price"])
elif sort_by == "Price: high to low":
    filtered = sorted(filtered, key=lambda p: p["price"], reverse=True)
elif sort_by == "Name":
    filtered = sorted(filtered, key=lambda p: p["name"])

st.write(f"Showing **{len(filtered)}** product(s)")

if not filtered:
    st.warning("Nu s-a găsit produsul. Incercați un alt cuvânt.")

for category in categories:
    category_products = [p for p in filtered if p["category"] == category]
    if not category_products:
        continue
    st.subheader(category)
    cols = st.columns(4)
    for index, product in enumerate(category_products):
        with cols[index % 4]:
            #st.markdown('<div class="product-card">', unsafe_allow_html=True)
            image_path = ASSET_DIR / product["image"]
            if image_path.exists():
                st.image(str(image_path), use_container_width=True)
                
            st.markdown(
                f'<div class="product-title">{product["name"]}</div>',
                unsafe_allow_html=True
            )
            
            st.markdown(
                f'<div class="text-box">{product["description"]}</div>',
                unsafe_allow_html=True
            )

            st.markdown(
                f'<div class="price-box">{product["price"]} RON</div>',
                unsafe_allow_html=True
            )
            
            if st.button("Cumpără", key=f"add_{product['id']}"):
                st.session_state.cart[product["id"]] = st.session_state.cart.get(product["id"], 0) + 1
                st.toast(f"Produsul {product['name']} a fost adăugat în coș")
                st.rerun()
            #st.markdown('</div>', unsafe_allow_html=True)
