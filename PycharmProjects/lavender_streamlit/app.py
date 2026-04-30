from pathlib import Path
import streamlit as st

st.set_page_config(page_title="Lavender Shop", page_icon="💜", layout="wide")

ASSET_DIR = Path(__file__).parent / "assets"

PRODUCTS = [
    {
        "id": "essential-oil-lavender",
        "name": "ULEI ESENȚIAL DE LEVĂNȚICĂ",
        "description": (
            "Ulei de levănțică natural, puternic aromat, bio pentru o stare de bine. "
            "Obținut din culturi ECO de lavandă prin distilare în Comuna Gogoșu. "
            "Miros puternic, terapeutic."
        ),
        "price": 35,
        "image": "essential-oil-lavender.png",
        "category": "Lavender Gifts",
    },
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

/* Main readable text */
h1, h2, h3, p {
    color: white !important;
}

.hero-title {
    color: white !important;
    font-size: 48px !important;
    font-weight: 900 !important;
    line-height: 1.1 !important;
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
    color: white !important;
    font-size: 22px;
    font-weight: 900;
    margin-top: 18px;
    letter-spacing: 0.3px;
    text-transform: uppercase;
}

/* Product description */
.text-box {
    border: 1px solid rgba(255,255,255,0.85);
    background: rgba(255,255,255,0.96);
    color: #2d123d !important;
    border-radius: 16px;
    padding: 16px;
    margin-top: 10px;
    line-height: 1.65;
    font-weight: 500;
    box-shadow: 0 8px 24px rgba(0,0,0,0.20);
}

.text-box * {
    color: #2d123d !important;
}

/* Price */
.price-box {
    border: 2px solid white;
    background: #ffffff;
    color: #5a007f !important;
    border-radius: 16px;
    padding: 12px;
    margin-top: 10px;
    margin-bottom: 12px;
    font-size: 20px;
    font-weight: 900;
    text-align: center;
    box-shadow: 0 8px 22px rgba(0,0,0,0.22);
}

.price-box * {
    color: #5a007f !important;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: #24172f;
}

section[data-testid="stSidebar"] * {
    color: white !important;
}

/* Product count */
.product-count {
    color: white !important;
    font-weight: 600;
    margin-top: 16px;
    margin-bottom: 16px;
}

/* FINAL BUTTON STYLE - do not duplicate elsewhere */
div[data-testid="stButton"] button,
div[data-testid="stButton"] button:hover,
div[data-testid="stButton"] button:active,
div[data-testid="stButton"] button:focus,
div[data-testid="stButton"] button:focus-visible,
div[data-testid="stButton"] button:disabled {
    background: #ffffff !important;
    background-color: #ffffff !important;
    background-image: none !important;
    color: #4b006e !important;
    border: 2px solid #ffffff !important;
    border-radius: 14px !important;
    font-weight: 900 !important;
    font-size: 16px !important;
    opacity: 1 !important;
    outline: none !important;
    box-shadow: 0 8px 20px rgba(0,0,0,0.25) !important;
    -webkit-tap-highlight-color: transparent !important;
}

div[data-testid="stButton"] button *,
div[data-testid="stButton"] button p,
div[data-testid="stButton"] button span,
div[data-testid="stButton"] button div {
    color: #4b006e !important;
}

/* Mobile */
@media (max-width: 768px) {
    .stApp {
        background-attachment: scroll;
    }

    .block-container {
        padding-top: 2rem;
        padding-left: 1.2rem;
        padding-right: 1.2rem;
    }

    .hero-title {
        font-size: 38px !important;
        text-align: left !important;
    }

    .product-title {
        font-size: 22px;
    }

    .text-box {
        font-size: 17px;
        padding: 18px;
    }

    .price-box {
        font-size: 21px;
        padding: 14px;
    }

    div[data-testid="stButton"] button {
        width: 100% !important;
        font-size: 18px !important;
        padding: 14px !important;
    }

    img {
        max-height: 420px;
        object-fit: cover;
    }
}
</style>
""",
    unsafe_allow_html=True,
)


st.markdown(
    '<h1 class="hero-title">💜 GOGOȘU Lavender Shop</h1>',
    unsafe_allow_html=True,
)

st.caption(
    "Comenzile se plasează doar prin apel telefonic. "
    "Verificați numărul de telefon în postarea de pe Facebook. "
    "Vă mulțumim pentru înțelegere."
)


with st.sidebar:
    st.header("Căutare și filtrare")

    query = st.text_input(
        "Caută produse",
        placeholder="Încearcă: ulei, lavandă...",
    )

    categories = sorted({p["category"] for p in PRODUCTS})
    selected_categories = st.multiselect(
        "Categorii",
        categories,
        default=categories,
    )

    sort_by = st.selectbox(
        "Sortează după",
        ["Default", "Preț: crescător", "Preț: descrescător", "Nume"],
    )

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

            st.markdown(f"**{product['name']}**")
            st.write(f"RON {product['price']} × {qty} = **RON {line_total}**")

            new_qty = st.number_input(
                f"Quantity for {product['name']}",
                min_value=1,
                max_value=99,
                value=qty,
                key=f"qty_{product_id}",
                label_visibility="collapsed",
            )

            st.session_state.cart[product_id] = new_qty

            if st.button("Șterge", key=f"remove_{product_id}"):
                del st.session_state.cart[product_id]
                st.rerun()

            st.divider()

        st.subheader(f"Total: RON {total}")

        if st.button("Finalizează comanda", type="primary"):
            st.session_state.cart = {}
            st.session_state.checkout_done = True
            st.rerun()


if st.session_state.checkout_done:
    st.success(
        "Comenzile se plasează doar prin apel telefonic. "
        "Verificați numărul de telefon în postarea de pe Facebook. "
        "Vă mulțumim pentru înțelegere."
    )
    st.session_state.checkout_done = False


filtered = [
    p
    for p in PRODUCTS
    if p["category"] in selected_categories
    and (
        query.lower() in p["name"].lower()
        or query.lower() in p["description"].lower()
    )
]

if sort_by == "Preț: crescător":
    filtered = sorted(filtered, key=lambda p: p["price"])
elif sort_by == "Preț: descrescător":
    filtered = sorted(filtered, key=lambda p: p["price"], reverse=True)
elif sort_by == "Nume":
    filtered = sorted(filtered, key=lambda p: p["name"])


st.markdown(
    f'<div class="product-count">Se afișează {len(filtered)} produs(e)</div>',
    unsafe_allow_html=True,
)

if not filtered:
    st.warning("Nu s-a găsit produsul. Încercați un alt cuvânt.")


for category in categories:
    category_products = [p for p in filtered if p["category"] == category]

    if not category_products:
        continue

    st.subheader(category)

    cols = st.columns(4)

    for index, product in enumerate(category_products):
        with cols[index % 4]:
            image_path = ASSET_DIR / product["image"]

            if image_path.exists():
                st.image(str(image_path), use_container_width=True)
            else:
                st.warning(f"Imagine lipsă: {product['image']}")

            st.markdown(
                f'<div class="product-title">{product["name"]}</div>',
                unsafe_allow_html=True,
            )

            st.markdown(
                f'<div class="text-box">{product["description"]}</div>',
                unsafe_allow_html=True,
            )

            st.markdown(
                f'<div class="price-box">{product["price"]} RON</div>',
                unsafe_allow_html=True,
            )

            if st.button("🛒 Adaugă în coș", key=f"add_{product['id']}", type="primary"):
                st.session_state.cart[product["id"]] = (
                    st.session_state.cart.get(product["id"], 0) + 1
                )
                st.toast(f"Produsul {product['name']} a fost adăugat în coș")
                st.rerun()
