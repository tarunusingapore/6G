
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="The Invisible Fabric", layout="wide", page_icon="🌐")

st.markdown("""
<style>
    .stApp { background: linear-gradient(180deg, #07070b 0%, #0b0b12 45%, #111118 100%); color: #f4f4f8; }
    .block-container { padding-top: 1.2rem; padding-bottom: 3rem; }
    h1, h2, h3 { color: #f8f8ff; }
    .hero {
        background: radial-gradient(circle at top left, rgba(0,255,136,0.16), transparent 35%),
                    linear-gradient(135deg, rgba(17,17,24,0.96), rgba(10,10,15,0.96));
        border: 1px solid rgba(0,255,136,0.18);
        border-radius: 24px;
        padding: 2rem;
        box-shadow: 0 0 40px rgba(0,255,136,0.08);
    }
    .card {
        background: rgba(17,17,24,0.92);
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 18px;
        padding: 1rem 1.1rem;
        box-shadow: 0 12px 30px rgba(0,0,0,0.25);
    }
    .metric {
        font-size: 2rem;
        font-weight: 700;
        color: #00ff88;
    }
    .subtle { color: #a6a6b7; }
</style>
""", unsafe_allow_html=True)

st.markdown("# The Invisible Fabric: How 6G Will Rewire the World")
st.caption("A cinematic Streamlit prototype that follows the original PPT story flow: thesis, alternatives, architecture, prototype, strategy, business model, risks, and future outlook.")

with st.container():
    st.markdown('<div class="hero">', unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1.2,1,1])
    with c1:
        st.subheader("Meet the Protagonist")
        st.write("6G is not just faster internet. It is the invisible fabric that fuses communication, sensing, and AI into one adaptive system.")
        st.write("This demo is designed for a smart-city and autonomous-mobility scenario, with the story translated directly from the original presentation flow.")
    with c2:
        st.metric("Peak speed", "1 Tbps", "~100x 5G")
        st.metric("Latency", "< 0.1 ms", "Ultra-low")
    with c3:
        st.metric("Device density", "10M/km²", "Massive scale")
        st.metric("Commercial rollout", "~2030", "Emerging")
    st.markdown('</div>', unsafe_allow_html=True)

st.divider()

st.subheader("1. Why 6G, not the alternatives?")
alt = pd.DataFrame({
    "Dimension": ["Peak speed", "Latency", "Mobility", "Device density", "AI integration", "Sensing"],
    "5G": ["10 Gbps", "1-10 ms", "Excellent", "1M/km²", "Add-on", "None"],
    "Wi-Fi 7": ["46 Gbps", "~5 ms", "Poor", "Limited", "Minimal", "None"],
    "Starlink": ["250 Mbps", "20-50 ms", "Moderate", "Very limited", "Minimal", "None"],
    "6G": ["1 Tbps", "0.1 ms", "Excellent", "10M/km²", "Native", "Integrated"]
})
st.dataframe(alt, use_container_width=True, hide_index=True)

st.caption("Use this as the 'Moment of Choice' section in the story: 6G wins because it uniquely combines ultra-low latency, urban mobility, massive device density, and sensing.")

st.divider()

st.subheader("2. Under the hood: the architecture")
arch_cols = st.columns(4)
arch = [
    ("Spectrum layer", "Terahertz band, dense cell infrastructure"),
    ("AI-native RAN", "Embedded learning, prediction, auto-healing"),
    ("ISAC", "Integrated sensing + communication"),
    ("Cloud-edge continuum", "Workload placement at device, edge, or cloud")
]
for col, (title, body) in zip(arch_cols, arch):
    with col:
        st.markdown(f'<div class="card"><h4>{title}</h4><p class="subtle">{body}</p></div>', unsafe_allow_html=True)

st.markdown("### Architecture view")
st.write("The network acts like a layered system: user experience, AI intelligence, secure processing, orchestration, and business systems.")
fig = go.Figure()
fig.add_trace(go.Funnel(y=["Users", "AI layer", "Clean room", "Orchestration", "Business systems"], x=[100, 84, 68, 54, 42], textinfo="value+percent initial"))
fig.update_layout(height=420, margin=dict(l=10,r=10,t=30,b=10), showlegend=False, paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
st.plotly_chart(fig, use_container_width=True)

st.divider()

st.subheader("3. Prototype: smart city digital twin")
city = st.radio("Choose prototype mode", ["Digital twin", "Mobility corridor", "Sensing dashboard"], horizontal=True)
rev_mode = st.slider("Service tier", 1, 4, 2)
row1, row2, row3 = st.columns(3)
base_revenue = [8.2, 15.6, 22.1, 28.4][rev_mode-1]
with row1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.metric("Monthly revenue", f"₹{base_revenue:.1f} cr")
    st.write("Revenue rises as the network moves from basic connectivity to slicing, sensing, and platform services.")
    st.markdown('</div>', unsafe_allow_html=True)
with row2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.metric("Latency score", ["High", "Medium", "Low", "Ultra-low"][rev_mode-1])
    st.write("Best suited for mission-critical mobility and city control loops.")
    st.markdown('</div>', unsafe_allow_html=True)
with row3:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.metric("Coverage quality", ["Basic", "Enhanced", "Dense", "Ubiquitous"][rev_mode-1])
    st.write("More infrastructure unlocks more sensing and orchestration value.")
    st.markdown('</div>', unsafe_allow_html=True)

if city == "Digital twin":
    pts = pd.DataFrame({"x": [1,2,3,4,5,6], "y": [2,1,3,2,4,3], "type": ["vehicle", "sensor", "building", "vehicle", "pedestrian", "sensor"]})
    fig2 = px.scatter(pts, x="x", y="y", color="type", title="Live city twin activity")
    fig2.update_layout(height=420, paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig2, use_container_width=True)
elif city == "Mobility corridor":
    t = pd.DataFrame({"time": list(range(1,11)), "latency": [0.18,0.17,0.15,0.13,0.12,0.11,0.10,0.10,0.09,0.08]})
    fig2 = px.line(t, x="time", y="latency", title="Latency trend across corridor")
    fig2.update_layout(height=420, paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig2, use_container_width=True)
else:
    s = pd.DataFrame({"service": ["basic", "slicing", "sensing", "platform"], "value": [8,16,24,32]})
    fig2 = px.bar(s, x="service", y="value", title="Service value stack")
    fig2.update_layout(height=420, paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig2, use_container_width=True)

st.divider()

st.subheader("4. Strategic impact")
fm = st.selectbox("Strategic posture", ["First mover", "Fast follower", "Option builder"])
left, right = st.columns(2)
with left:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    if fm == "First mover":
        st.write("Best for infrastructure players, chipset makers, and standard-setters.")
        st.write("They shape rules, partnerships, and ecosystem architecture.")
    elif fm == "Fast follower":
        st.write("Best for enterprises and application builders.")
        st.write("They avoid premature capex and wait for standard clarity.")
    else:
        st.write("Best for firms building capability without locking in big bets.")
        st.write("Invest in pilots, learning, and flexibility.")
    st.markdown('</div>', unsafe_allow_html=True)
with right:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.write("The competitive winner is the firm that controls the layers above raw connectivity: APIs, data, orchestration, and ecosystems.")
    st.write("That is why 6G is a platform shift, not just a telecom upgrade.")
    st.markdown('</div>', unsafe_allow_html=True)

st.divider()

st.subheader("5. Business model impact")
model = st.multiselect(
    "Select monetization layers",
    ["Connectivity-as-a-Service", "Sensing-as-a-Service", "Network Slicing-as-a-Service", "Platform models", "Outcome-based pricing", "B2B2X"],
    default=["Connectivity-as-a-Service", "Sensing-as-a-Service", "Network Slicing-as-a-Service"]
)
impact = len(model)
cols = st.columns(3)
cols[0].metric("Revenue layers active", impact)
cols[1].metric("Moat", "AI + data + ecosystem")
cols[2].metric("Cost structure", "Capex-heavy, Opex-lighter")

fig3 = go.Figure(go.Indicator(mode="gauge+number", value=impact*15, gauge={"axis": {"range": [None, 100]}, "bar": {"color": "#00ff88"}}, title={"text": "Value capture score"}))
fig3.update_layout(height=300, paper_bgcolor='rgba(0,0,0,0)', font_color="#f4f4f8")
st.plotly_chart(fig3, use_container_width=True)

st.divider()

st.subheader("6. Risks and future outlook")
risks = ["Technical fragility", "Regulatory/geopolitical fragmentation", "Adoption resistance", "Ethical surveillance concerns", "ROI uncertainty"]
selected_risks = st.checkbox("Show risks")
if selected_risks:
    st.write(", ".join(risks))

future = st.radio("Timeline", ["2025-2028: Research & standardization", "2028-2033: Trials & early deployment", "2033+: Mainstream disruption"], horizontal=False)
st.info(future)
st.write("The story ends with 6G becoming invisible infrastructure: digital twins, XR, ambient intelligence, and new platform economics.")

st.divider()
st.caption("Built as a deployable Streamlit prototype for GitHub + Streamlit Community Cloud.")
