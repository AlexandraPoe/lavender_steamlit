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
        background: linear-gradient(rgba(80, 0, 120, 0.80), rgba(80, 0, 120, 0.80)),
                    url('https://www.creativefabrica.com/wp-content/uploads/2023/08/25/French-Impressionist-Painting-In-Monet-Style-Of-Lavender-Fields-77673167-1.png');
        background-size: cover;
        background-attachment: fixed;
    }
    .product-card {
        background: rgba(255, 255, 255, 0.92);
        color: #2d123d;
        border-radius: 18px;
        padding: 18px;
        min-height: 450px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.18);
        border: 1px solid rgba(255,255,255,0.4);
     }   
        .text-box {
            border: 1px solid rgba(255,255,255,0.7);
            background: rgba(255,255,255,0.15);
            backdrop-filter: blur(5px);
        }

        .price-box {
            border: 2px solid white;
            border-radius: 10px;
            padding: 6px;
            margin-top: 6px;
            font-weight: bold;
            text-align: center;
        }
        .price-box:hover {
        box-shadow: 0 0 10px white;
        }
        
    .product-title {font-size: 1.05rem; font-weight: 800; margin-top: 10px;}
    .price {font-size: 1.2rem; font-weight: 800; color: #6B00B0;}
    .small-muted {color: #5d4a68; font-size: 0.92rem; min-height: 48px;}
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("💜 Lavender Shop")
st.caption("Comenzile se plasează doar prin apel telefonic. Verifică numărul de telefon in postarea de pe Facebook. Vă mulțumim pentru înțelegere.")

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
            st.markdown(f'<div class="product-title">{product["name"]}</div>', unsafe_allow_html=True)
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
