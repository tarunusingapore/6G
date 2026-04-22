
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from PIL import Image
import requests
from io import BytesIO

st.set_page_config(page_title="The Invisible Fabric", layout="wide", page_icon="🌐")

st.markdown("""
<style>
.stApp { background: #ffffff; color: #101114; }
.block-container { padding-top: 1rem; padding-bottom: 3rem; max-width: 1280px; }
h1, h2, h3, h4, h5 { color: #0f1115 !important; }
p, li, span, div, label { color: #1d2129; }
.hero {
    background: linear-gradient(135deg, #f8fbff 0%, #eef4ff 100%);
    border: 1px solid #dbe6ff;
    border-radius: 28px;
    padding: 2rem;
    box-shadow: 0 18px 60px rgba(18,38,63,0.08);
}
.card {
    background: #ffffff;
    border: 1px solid #e6ebf2;
    border-radius: 22px;
    padding: 1.15rem;
    box-shadow: 0 12px 28px rgba(17,24,39,0.06);
}
.soft { color: #5b6574; }
.section-space { margin-top: 1.2rem; }
.imgbox {
    border-radius: 22px;
    overflow: hidden;
    border: 1px solid #e6ebf2;
    box-shadow: 0 14px 30px rgba(15, 23, 42, 0.07);
}
.smallcap { font-size: 0.92rem; color: #667085; }
</style>
""", unsafe_allow_html=True)

st.markdown("# The Invisible Fabric: How 6G Will Rewire the World")
st.caption("A polished, scroll-first Streamlit website that turns the original PPT story into a premium web narrative.")

# Hero
st.markdown('<div class="hero">', unsafe_allow_html=True)
left, right = st.columns([1.25, 1])
with left:
    st.markdown("## Meet the Protagonist")
    st.write("6G is not just faster internet. It is the invisible fabric that fuses communication, sensing, and AI into one adaptive system.")
    st.write("This page is designed to feel like a product launch: clean white surfaces, strong typography, generous spacing, and a story that flows as you scroll.")
    st.write("The main use case is **smart cities and autonomous mobility**, with the prototype framed as a real digital twin.")
with right:
    c1, c2 = st.columns(2)
    c1.metric("Peak speed", "1 Tbps", "~100x 5G")
    c2.metric("Latency", "<0.1 ms", "Ultra-low")
    c3, c4 = st.columns(2)
    c3.metric("Density", "10M/km²", "Massive scale")
    c4.metric("Rollout", "~2030", "Emerging")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="section-space"></div>', unsafe_allow_html=True)

# Story 1
st.markdown("### 1. The Moment of Choice")
st.write("Why 6G rather than the alternatives?")
alt = pd.DataFrame({
    "Dimension": ["Peak speed", "Latency", "Mobility", "Device density", "AI integration", "Sensing"],
    "5G": ["10 Gbps", "1-10 ms", "Excellent", "1M/km²", "Add-on", "None"],
    "Wi-Fi 7": ["46 Gbps", "~5 ms", "Poor", "Limited", "Minimal", "None"],
    "Starlink": ["250 Mbps", "20-50 ms", "Moderate", "Very limited", "Minimal", "None"],
    "6G": ["1 Tbps", "0.1 ms", "Excellent", "10M/km²", "Native", "Integrated"]
})
st.dataframe(alt, use_container_width=True, hide_index=True)

st.markdown('<div class="section-space"></div>', unsafe_allow_html=True)

# Architecture section
st.markdown("### 2. Under the Hood")
arch_l, arch_r = st.columns([1.05, 1.25])
with arch_l:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("#### Architecture translated from your diagram")
    st.write("**Experience layer** → users, city operators, enterprises")
    st.write("**AI intelligence layer** → AI-native control and optimization")
    st.write("**Trusted layer** → secure processing / clean room")
    st.write("**Orchestration layer** → APIs, workflows, network control")
    st.write("**Business systems layer** → revenue, partners, SAP / enterprise systems")
    st.markdown('</div>', unsafe_allow_html=True)
with arch_r:
    fig_arch = go.Figure()
    fig_arch.add_trace(go.Funnel(y=["Users", "AI layer", "Trusted core", "Orchestration", "Business systems"], x=[100, 84, 68, 54, 42], textinfo="value+percent initial"))
    fig_arch.update_layout(height=430, showlegend=False, paper_bgcolor='white', plot_bgcolor='white', margin=dict(l=10,r=10,t=25,b=10))
    st.plotly_chart(fig_arch, use_container_width=True)

# Image + caption
st.markdown('<div class="imgbox">', unsafe_allow_html=True)
try:
    img = Image.open(BytesIO(requests.get("https://pplx-res.cloudinary.com/image/upload/pplx_search_images/af609ef6bf0618758a491d3806982c1dd9f56a96.jpg", timeout=8).content))
    st.image(img, use_container_width=True)
except Exception:
    st.info("Digital twin image placeholder will render here in deployment if external image access is available.")
st.markdown('</div>', unsafe_allow_html=True)
st.caption("Visual reference for the prototype: smart-city digital twin style with real-time control feel.")

# Prototype section
st.markdown('<div class="section-space"></div>', unsafe_allow_html=True)
st.markdown("### 3. Prototype: Digital Twin for a Smart City")
st.write("This is the centerpiece: a believable, premium-looking operational twin rather than a generic dashboard.")

p1, p2, p3 = st.columns([1.0, 1.6, 1.0])
with p1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("#### Control panel")
    mode = st.radio("Twin mode", ["Traffic", "Mobility corridor", "City sensing"], index=0)
    tier = st.select_slider("Service tier", options=["Basic", "Enhanced", "Premium", "Platform"], value="Premium")
    st.write("- live vehicle movement")
    st.write("- sensor density")
    st.write("- safety score")
    st.write("- revenue tier")
    st.markdown('</div>', unsafe_allow_html=True)

with p2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("#### Live digital twin")
    if mode == "Traffic":
        pts = pd.DataFrame({
            "x": [1.2,2,3,4,5,6,1.5,2.5,3.5,4.5,5.5,6.4,1.1,2.1,4.1,5.9],
            "y": [5.9,5.7,5.8,5.6,5.9,5.7,4.2,4.3,4.2,4.1,4.3,4.2,2.7,2.6,2.7,2.6],
            "type": ["vehicle"]*6 + ["sensor"]*6 + ["zone"]*4
        })
        fig = px.scatter(pts, x="x", y="y", color="type", color_discrete_map={"vehicle":"#0a84ff", "sensor":"#34c759", "zone":"#f59e0b"}, height=520)
        fig.update_traces(marker=dict(size=19, line=dict(width=0.6, color='white')), cliponaxis=False)
        fig.update_layout(showlegend=True, legend_title_text="Entity", paper_bgcolor='white', plot_bgcolor='#f7f9fc', margin=dict(l=10,r=10,t=10,b=10), xaxis=dict(showgrid=False, visible=False), yaxis=dict(showgrid=False, visible=False))
        fig.add_shape(type="rect", x0=0.6, y0=2.0, x1=6.9, y1=6.2, line=dict(color="#d0d7e2", width=2), fillcolor="rgba(0,0,0,0)")
        fig.add_annotation(x=3.7, y=6.35, text="Urban core", showarrow=False, font=dict(size=16, color="#243447"))
    elif mode == "Mobility corridor":
        df = pd.DataFrame({"point": [f"P{i}" for i in range(1,9)], "latency": [0.18,0.16,0.14,0.12,0.11,0.10,0.09,0.08], "coverage": [82,84,86,88,90,92,94,96]})
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df["point"], y=df["latency"], mode='lines+markers', name='Latency (ms)', line=dict(color='#0a84ff', width=4)))
        fig.add_trace(go.Scatter(x=df["point"], y=df["coverage"], mode='lines+markers', name='Coverage %', line=dict(color='#34c759', width=4), yaxis='y2'))
        fig.update_layout(height=520, paper_bgcolor='white', plot_bgcolor='#f7f9fc', margin=dict(l=10,r=10,t=10,b=10), yaxis=dict(title='Latency', gridcolor='#e8edf4'), yaxis2=dict(title='Coverage', overlaying='y', side='right', gridcolor='rgba(0,0,0,0)'))
    else:
        df = pd.DataFrame({"sector": ["traffic","air","noise","mobility","safety"], "value": [88,76,69,92,81]})
        fig = px.bar(df, x="sector", y="value", color="sector", color_discrete_sequence=["#0a84ff", "#34c759", "#f59e0b", "#7c3aed", "#ff6b6b"], height=520)
        fig.update_traces(cliponaxis=False)
        fig.update_layout(showlegend=False, paper_bgcolor='white', plot_bgcolor='#f7f9fc', margin=dict(l=10,r=10,t=10,b=10), yaxis=dict(gridcolor='#e8edf4'))
    st.plotly_chart(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with p3:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("#### Prototype metrics")
    st.metric("Monthly revenue", "₹28.4 cr", "premium tier")
    st.metric("Latency", "0.08 ms", "mission critical")
    st.metric("Sensing confidence", "96%", "live map")
    st.metric("Active nodes", "1.2M", "city scale")
    st.markdown('</div>', unsafe_allow_html=True)

# Strategy section
st.markdown('<div class="section-space"></div>', unsafe_allow_html=True)
st.markdown("### 4. Strategic Impact")
strategy = pd.DataFrame([
    ["First mover advantage", "Shape standards, lock partnerships, control ecosystem", "High capex, uncertain demand, long payback"],
    ["First mover risks", "Can learn early and influence rules", "May overbuild before market matures"],
    ["Fast follower advantage", "Lower risk, clearer standards, better capital discipline", "Less influence over architecture"],
    ["Fast follower risks", "Can enter with proven use cases", "May miss ecosystem power and learning"],
], columns=["Category", "Upside", "Downside"])
st.dataframe(strategy, use_container_width=True, hide_index=True)

# Business model section
st.markdown('<div class="section-space"></div>', unsafe_allow_html=True)
st.markdown("### 5. Business Model Impact")
model_df = pd.DataFrame({
    "Revenue stream": ["Connectivity-as-a-Service", "Sensing-as-a-Service", "Network Slicing-as-a-Service", "Platform models", "Outcome-based pricing", "B2B2X"],
    "What changes": ["Tiered by use case", "Environmental awareness data", "Dedicated private slivers", "APIs + developer ecosystem", "Pay for results", "Telco sells to enterprise who sells to consumer"]
})
st.dataframe(model_df, use_container_width=True, hide_index=True)
cols = st.columns(3)
cols[0].metric("Cost structure", "Capex-heavy", "Opex improves later")
cols[1].metric("Key moat", "AI + data + ecosystem", "not just spectrum")
cols[2].metric("Partnership need", "High", "cloud + chip + city")

# Risks
st.markdown('<div class="section-space"></div>', unsafe_allow_html=True)
st.markdown("### 6. Risks and Challenges")
risks = pd.DataFrame({
    "Risk": ["Technical fragility", "Regulatory/geopolitical fragmentation", "Adoption resistance", "Ethical surveillance concerns", "ROI uncertainty"],
    "Implication": ["Terahertz links are fragile and short-range", "Competing standards can break interoperability", "Enterprises may delay another capex cycle", "ISAC raises privacy and monitoring issues", "No single killer app yet justifies scale"]
})
st.dataframe(risks, use_container_width=True, hide_index=True)

# Future
st.markdown('<div class="section-space"></div>', unsafe_allow_html=True)
st.markdown("### 7. Future Outlook")
future = pd.DataFrame({
    "Phase": ["2025-2028", "2028-2033", "2033+"],
    "Story": ["Research and standardization", "Trials and early deployment", "Mainstream disruption"],
    "What appears": ["Early terahertz prototypes", "Niche industrial and mobility use cases", "Digital twins, XR, ambient intelligence"]
})
st.dataframe(future, use_container_width=True, hide_index=True)

st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("### Closing thesis")
st.write("6G is not a connectivity upgrade. It is the invisible operating system of an AI-native economy, and the firms that understand this are building the fabric — not just using it.")
st.markdown('</div>', unsafe_allow_html=True)
