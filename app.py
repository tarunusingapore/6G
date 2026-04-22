
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

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
    box-shadow: 0 16px 48px rgba(18,38,63,0.08);
}
.card {
    background: #ffffff;
    border: 1px solid #e6ebf2;
    border-radius: 22px;
    padding: 1.2rem;
    box-shadow: 0 12px 28px rgba(17,24,39,0.06);
}
.soft {
    color: #5b6574;
}
.section-title {
    margin-top: 1rem;
    margin-bottom: 0.35rem;
}
</style>
""", unsafe_allow_html=True)

st.markdown("# The Invisible Fabric: How 6G Will Rewire the World")
st.caption("Streamlit prototype following the original PPT story flow, optimized for scrolling and presentation.")

st.markdown('<div class="hero">', unsafe_allow_html=True)
hero_l, hero_r = st.columns([1.35, 1])
with hero_l:
    st.markdown("## Meet the Protagonist")
    st.write("6G is not just faster internet. It is the invisible fabric that fuses communication, sensing, and AI into one adaptive system.")
    st.write("This version is built for a clean, scroll-friendly presentation with a white background, sharper contrast, and more cinematic visuals.")
    st.write("The main use case is **smart cities and autonomous mobility**, with the prototype logic centered on a digital twin.")
with hero_r:
    m1, m2 = st.columns(2)
    m1.metric("Peak speed", "1 Tbps", "~100x 5G")
    m2.metric("Latency", "<0.1 ms", "Ultra-low")
    m3, m4 = st.columns(2)
    m3.metric("Density", "10M/km²", "Massive scale")
    m4.metric("Rollout", "~2030", "Emerging")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<h3 class='section-title'>1. The Moment of Choice</h3>", unsafe_allow_html=True)
st.write("Why 6G instead of the alternatives?")
alt = pd.DataFrame({
    "Dimension": ["Peak speed", "Latency", "Mobility", "Device density", "AI integration", "Sensing"],
    "5G": ["10 Gbps", "1-10 ms", "Excellent", "1M/km²", "Add-on", "None"],
    "Wi-Fi 7": ["46 Gbps", "~5 ms", "Poor", "Limited", "Minimal", "None"],
    "Starlink": ["250 Mbps", "20-50 ms", "Moderate", "Very limited", "Minimal", "None"],
    "6G": ["1 Tbps", "0.1 ms", "Excellent", "10M/km²", "Native", "Integrated"]
})
st.dataframe(alt, use_container_width=True, hide_index=True)

st.markdown("<h3 class='section-title'>2. Under the Hood</h3>", unsafe_allow_html=True)
arch_cols = st.columns(4)
arch = [
    ("Spectrum layer", "Terahertz band, dense cell infrastructure"),
    ("AI-native RAN", "Embedded learning, prediction, auto-healing"),
    ("ISAC", "Integrated sensing + communication"),
    ("Cloud-edge continuum", "Workload placement at device, edge, or cloud")
]
for col, (title, body) in zip(arch_cols, arch):
    with col:
        st.markdown(f'<div class="card"><h4>{title}</h4><p class="soft">{body}</p></div>', unsafe_allow_html=True)

st.write("The architecture can be read as a stack: user experience → AI intelligence → secure processing → orchestration → business systems.")

st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("### Architecture diagram")
fig = go.Figure()
fig.add_trace(go.Funnel(y=["Users", "AI intelligence", "Clean room", "Orchestration", "Business systems"], x=[100, 84, 68, 54, 42], textinfo="value+percent initial"))
fig.update_layout(height=450, showlegend=False, paper_bgcolor='white', plot_bgcolor='white', margin=dict(l=10,r=10,t=25,b=10))
st.plotly_chart(fig, use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<h3 class='section-title'>3. Prototype: Digital Twin for a Smart City</h3>", unsafe_allow_html=True)
st.write("This section should look like a real operational twin, not a generic dashboard.")

left, center, right = st.columns([1.15, 1.65, 1.15])
with left:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### Control panel")
    mode = st.radio("Prototype mode", ["Traffic", "Mobility corridor", "City sensing"], index=0)
    tier = st.select_slider("Service tier", options=["Basic", "Enhanced", "Premium", "Platform"], value="Premium")
    st.write("- Live vehicle movement")
    st.write("- Sensor density")
    st.write("- Sensing confidence")
    st.write("- Revenue layer")
    st.markdown('</div>', unsafe_allow_html=True)
with center:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### Live city twin")
    n = 16
    if mode == "Traffic":
        xs = [1,2,3,4,5,6,1.5,2.5,3.5,4.5,5.5,6.5,1,2.2,4.2,5.8]
        ys = [5.8,5.6,5.7,5.5,5.8,5.6,4.1,4.2,4.1,4.0,4.2,4.1,2.6,2.5,2.6,2.5]
        color = ["vehicle"]*6 + ["sensor"]*6 + ["zone"]*4
        fig2 = px.scatter(x=xs, y=ys, color=color, color_discrete_map={"vehicle":"#0a84ff","sensor":"#34c759","zone":"#f59e0b"}, height=480)
        fig2.update_traces(marker=dict(size=18, line=dict(width=0.5, color='white')), cliponaxis=False)
        fig2.update_layout(showlegend=True, legend_title_text="Entity", paper_bgcolor='white', plot_bgcolor='#f7f9fc', margin=dict(l=10,r=10,t=10,b=10), xaxis=dict(showgrid=False, visible=False), yaxis=dict(showgrid=False, visible=False))
        fig2.add_shape(type="rect", x0=0.6, y0=2.0, x1=6.9, y1=6.2, line=dict(color="#d0d7e2", width=2), fillcolor="rgba(0,0,0,0)")
        fig2.add_annotation(x=3.7, y=6.35, text="Urban core", showarrow=False, font=dict(size=16, color="#243447"))
    elif mode == "Mobility corridor":
        df = pd.DataFrame({"point": [f"P{i}" for i in range(1,9)], "latency": [0.18,0.16,0.14,0.12,0.11,0.10,0.09,0.08], "coverage": [82,84,86,88,90,92,94,96]})
        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(x=df["point"], y=df["latency"], mode='lines+markers', name='Latency (ms)', line=dict(color='#0a84ff', width=4)))
        fig2.add_trace(go.Scatter(x=df["point"], y=df["coverage"], mode='lines+markers', name='Coverage %', line=dict(color='#34c759', width=4), yaxis='y2'))
        fig2.update_layout(height=480, paper_bgcolor='white', plot_bgcolor='#f7f9fc', margin=dict(l=10,r=10,t=10,b=10), yaxis=dict(title='Latency', gridcolor='#e8edf4'), yaxis2=dict(title='Coverage', overlaying='y', side='right', gridcolor='rgba(0,0,0,0)'))
    else:
        df = pd.DataFrame({"sector": ["traffic","air","noise","mobility","safety"], "value": [88,76,69,92,81]})
        fig2 = px.bar(df, x="sector", y="value", color="sector", color_discrete_sequence=["#0a84ff", "#34c759", "#f59e0b", "#7c3aed", "#ff6b6b"], height=480)
        fig2.update_traces(cliponaxis=False)
        fig2.update_layout(showlegend=False, paper_bgcolor='white', plot_bgcolor='#f7f9fc', margin=dict(l=10,r=10,t=10,b=10), yaxis=dict(gridcolor='#e8edf4'))
    st.plotly_chart(fig2, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
with right:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### Prototype metrics")
    st.metric("Monthly revenue", "₹28.4 cr", "premium tier")
    st.metric("Latency", "0.08 ms", "mission critical")
    st.metric("Sensing confidence", "96%", "live map")
    st.metric("Active nodes", "1.2M", "city scale")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<h3 class='section-title'>4. Strategic Impact</h3>", unsafe_allow_html=True)
strat = pd.DataFrame({
    "Dimension": ["Best for", "Positives", "Risks"],
    "First mover": ["Infrastructure providers, chipset makers, standards leaders", "Shapes rules, gains early ecosystem control, builds partnerships", "High capex, uncertainty, long payback"],
    "Fast follower": ["Enterprises, application builders, vertical solution teams", "Lower risk, clearer standards, better capital discipline", "Less influence, later learning, may miss ecosystem power"]
})
st.table(strat)

st.markdown("<h3 class='section-title'>5. Business Model Impact</h3>", unsafe_allow_html=True)
model_df = pd.DataFrame({
    "Revenue stream": ["Connectivity-as-a-Service", "Sensing-as-a-Service", "Network Slicing-as-a-Service", "Platform models", "Outcome-based pricing", "B2B2X"],
    "What changes": ["Tiered by use case", "Environmental awareness data", "Dedicated private slivers", "APIs + developer ecosystem", "Pay for results", "Telco sells to enterprise who sells to consumer"]
})
st.dataframe(model_df, use_container_width=True, hide_index=True)

cols = st.columns(3)
cols[0].metric("Cost structure", "Capex-heavy", "Opex improves later")
cols[1].metric("Key moat", "AI + data + ecosystem", "not just spectrum")
cols[2].metric("Partnership need", "High", "cloud + chip + city")

st.markdown("<h3 class='section-title'>6. Risks</h3>", unsafe_allow_html=True)
risks = pd.DataFrame({
    "Risk": ["Technical fragility", "Regulatory/geopolitical fragmentation", "Adoption resistance", "Ethical surveillance concerns", "ROI uncertainty"],
    "Implication": ["Terahertz links are fragile and short-range", "Competing standards can break interoperability", "Enterprises may delay another capex cycle", "ISAC raises privacy and monitoring issues", "No single killer app yet justifies scale"]
})
st.table(risks)

st.markdown("<h3 class='section-title'>7. Future Outlook</h3>", unsafe_allow_html=True)
future = pd.DataFrame({
    "Phase": ["2025-2028", "2028-2033", "2033+"],
    "Story": ["Research and standardization", "Trials and early deployment", "Mainstream disruption"],
    "What appears": ["Early terahertz prototypes", "Niche industrial and mobility use cases", "Digital twins, XR, ambient intelligence"]
})
st.table(future)

st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("### Closing thesis")
st.write("6G is not a connectivity upgrade. It is the invisible operating system of an AI-native economy, and the firms that understand this are not just building a network — they are building the fabric.")
st.markdown('</div>', unsafe_allow_html=True)
