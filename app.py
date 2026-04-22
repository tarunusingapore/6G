
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
.stApp { background: #fbfcfe; color: #12141a; }
.block-container { padding-top: 0.9rem; padding-bottom: 3rem; max-width: 1340px; }
h1, h2, h3, h4, h5 { color: #10131a !important; letter-spacing: -0.02em; }
p, li, span, div, label { color: #1d2430; }
.hero {
    background: linear-gradient(135deg, rgba(242,246,255,0.95), rgba(250,252,255,0.96));
    border: 1px solid #dbe5f5;
    border-radius: 30px;
    padding: 2rem;
    box-shadow: 0 20px 70px rgba(15, 23, 42, 0.08);
}
.card {
    background: #ffffff;
    border: 1px solid #e7ebf2;
    border-radius: 24px;
    padding: 1.15rem;
    box-shadow: 0 14px 32px rgba(15, 23, 42, 0.06);
}
.section { margin-top: 1.35rem; }
.soft { color: #5f6b7a; }
.badge { display:inline-block; padding: 0.35rem 0.7rem; border-radius: 999px; background:#edf3ff; color:#2050c9; font-size:0.8rem; font-weight:600; }
.imgframe { border-radius: 24px; overflow:hidden; border:1px solid #e7ebf2; box-shadow:0 14px 36px rgba(15,23,42,0.07); background: linear-gradient(180deg, #ffffff, #f8fbff); }
</style>
""", unsafe_allow_html=True)

st.markdown("# The Invisible Fabric: How 6G Will Rewire the World")
st.caption("A presentation-grade website prototype: minimal text, strong visuals, layered architecture, and a digital twin control-room story.")

# HERO
st.markdown('<div class="hero">', unsafe_allow_html=True)
l, r = st.columns([1.2, 1])
with l:
    st.markdown('<span class="badge">6G · Smart Cities · Digital Twin · Strategy</span>', unsafe_allow_html=True)
    st.markdown("## Meet the Protagonist")
    st.write("6G is the invisible fabric that combines communication, sensing, and AI into one adaptive urban system.")
    st.write("The page is intentionally designed to feel like a premium product launch, not a dashboard builder: airy layout, large visuals, and a clear narrative arc.")
    st.write("The main use case is a smart city / autonomous mobility digital twin.")
with r:
    m1, m2 = st.columns(2)
    m1.metric("Peak speed", "1 Tbps", "~100x 5G")
    m2.metric("Latency", "<0.1 ms", "ultra-low")
    m3, m4 = st.columns(2)
    m3.metric("Density", "10M/km²", "massive scale")
    m4.metric("Rollout", "~2030", "emerging")
st.markdown('</div>', unsafe_allow_html=True)

# WHY 6G
st.markdown('<div class="section"></div>', unsafe_allow_html=True)
st.markdown("### 1. The Moment of Choice")
st.write("A single visual comparison is more persuasive than paragraphs.")
comp = pd.DataFrame({
    "Dimension": ["Peak speed", "Latency", "Mobility", "Device density", "AI integration", "Sensing"],
    "5G": ["10 Gbps", "1-10 ms", "Excellent", "1M/km²", "Add-on", "None"],
    "Wi-Fi 7": ["46 Gbps", "~5 ms", "Poor", "Limited", "Minimal", "None"],
    "Starlink": ["250 Mbps", "20-50 ms", "Moderate", "Very limited", "Minimal", "None"],
    "6G": ["1 Tbps", "0.1 ms", "Excellent", "10M/km²", "Native", "Integrated"]
})
st.markdown("""<div class="card"><h4>Why 6G wins</h4><div class="soft">6G uniquely combines ultra-low latency, urban mobility, massive device density, native AI, and integrated sensing.</div></div>""", unsafe_allow_html=True)

# ARCHITECTURE
st.markdown('<div class="section"></div>', unsafe_allow_html=True)
st.markdown("### 2. Architecture")
cols = st.columns([1.02, 1.1, 1.1])
with cols[0]:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("#### The stack, translated")
    st.write("**Experience** → city users, operators, enterprises")
    st.write("**AI intelligence** → adaptive control and optimization")
    st.write("**Trusted core** → secure processing and clean-room logic")
    st.write("**Orchestration** → APIs, workflows, network steering")
    st.write("**Business systems** → revenue, partners, enterprise systems")
    st.markdown('</div>', unsafe_allow_html=True)
with cols[1]:
    try:
        img = Image.open(BytesIO(requests.get('https://pplx-res.cloudinary.com/image/upload/pplx_search_images/a4e5c900332735c1a397aeadcc7868f422cd7732.jpg', timeout=8).content))
        st.image(img, use_container_width=True)
    except Exception:
        st.info('Architecture image placeholder')
with cols[2]:
    try:
        img2 = Image.open(BytesIO(requests.get('https://pplx-res.cloudinary.com/image/upload/pplx_search_images/8be354356929ddb1decd969d0260aa8daa505208.jpg', timeout=8).content))
        st.image(img2, use_container_width=True)
    except Exception:
        st.info('6G architecture placeholder')

st.markdown("#### Layered diagram")
fig_arch = go.Figure()
fig_arch.add_trace(go.Sunburst(
    labels=["6G", "Experience", "AI", "Trusted core", "Orchestration", "Business systems", "Users", "City ops", "Adaptive control", "Secure core", "APIs", "Revenue", "Partners", "Enterprise"],
    parents=["", "6G", "6G", "6G", "6G", "6G", "Experience", "Experience", "AI", "Trusted core", "Orchestration", "Business systems", "Business systems", "Business systems"],
    branchvalues="total"
))
fig_arch.update_layout(height=540, paper_bgcolor='white', margin=dict(l=10,r=10,t=18,b=10))
st.plotly_chart(fig_arch, use_container_width=True)


# PROTOTYPE
st.markdown('<div class="section"></div>', unsafe_allow_html=True)
st.markdown("### 3. Prototype: Animated Digital Twin Control Room")
st.write("This section now behaves more like a live operational twin: glowing layers, moving markers, and motion-rich visualization.")

p_l, p_c, p_r = st.columns([0.92, 1.7, 0.88])
with p_l:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("#### Control deck")
    mode = st.radio("View", ["Traffic", "Mobility corridor", "City sensing"], index=0)
    layer = st.select_slider("Layer", options=["Basic", "Enhanced", "Premium", "Platform"], value="Platform")
    st.markdown("- live vehicles")
    st.markdown("- sensor rings")
    st.markdown("- safety score")
    st.markdown("- service tier")
    st.markdown('</div>', unsafe_allow_html=True)
with p_c:
    st.markdown('<div class="imgframe">', unsafe_allow_html=True)
    try:
        twin = Image.open(BytesIO(requests.get('https://pplx-res.cloudinary.com/image/upload/pplx_search_images/3f5d34595593eb87c8bfd362fa34ccd3866f900e.jpg', timeout=8).content))
        st.image(twin, use_container_width=True)
    except Exception:
        st.info('Digital twin image placeholder')
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<div class="card">', unsafe_allow_html=True)
    if mode == 'Traffic':
        df = pd.DataFrame({'x':[1,2,3,4,5,6,1.3,2.4,3.6,4.6,5.7,6.7,1.0,2.2,4.1,5.9], 'y':[5.8,5.7,5.8,5.6,5.8,5.7,4.2,4.3,4.2,4.1,4.2,4.1,2.6,2.6,2.7,2.6], 'type':['vehicle']*6+['sensor']*6+['zone']*4})
        fig = px.scatter(df, x='x', y='y', color='type', color_discrete_map={'vehicle':'#0a84ff','sensor':'#34c759','zone':'#f59e0b'}, height=320)
        fig.update_traces(marker=dict(size=17, line=dict(width=0.5, color='white')), cliponaxis=False)
        fig.update_layout(showlegend=True, legend_title_text='Entity', paper_bgcolor='white', plot_bgcolor='#f7f9fc', margin=dict(l=6,r=6,t=6,b=6), xaxis=dict(showgrid=False, visible=False), yaxis=dict(showgrid=False, visible=False))
        fig.add_shape(type='circle', xref='x', yref='y', x0=0.8, y0=2.0, x1=6.9, y1=6.2, line=dict(color='#dbe5f5', width=2), fillcolor='rgba(0,0,0,0)')
        fig.add_annotation(x=3.7, y=6.35, text='Live traffic ring', showarrow=False, font=dict(size=14, color='#0a84ff'))
    elif mode == 'Mobility corridor':
        t = list(range(1,13))
        latency = [0.18,0.17,0.16,0.15,0.13,0.12,0.11,0.10,0.09,0.09,0.08,0.08]
        coverage = [82,83,84,85,86,88,89,91,92,93,95,96]
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=t, y=latency, mode='lines+markers', name='Latency (ms)', line=dict(color='#0a84ff', width=4), fill='tozeroy', fillcolor='rgba(10,132,255,0.08)'))
        fig.add_trace(go.Scatter(x=t, y=coverage, mode='lines+markers', name='Coverage %', line=dict(color='#34c759', width=4), yaxis='y2'))
        fig.update_layout(height=320, paper_bgcolor='white', plot_bgcolor='#f7f9fc', margin=dict(l=6,r=6,t=6,b=6), yaxis=dict(title='Latency', gridcolor='#e8edf4'), yaxis2=dict(title='Coverage', overlaying='y', side='right', gridcolor='rgba(0,0,0,0)'))
    else:
        df = pd.DataFrame({'sector':['traffic','air','noise','mobility','safety'], 'value':[88,76,69,92,81]})
        fig = px.bar(df, x='sector', y='value', color='sector', color_discrete_sequence=['#0a84ff','#34c759','#f59e0b','#7c3aed','#ff6b6b'], height=320)
        fig.update_traces(cliponaxis=False)
        fig.update_layout(showlegend=False, paper_bgcolor='white', plot_bgcolor='#f7f9fc', margin=dict(l=6,r=6,t=6,b=6), yaxis=dict(gridcolor='#e8edf4'))
    st.plotly_chart(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
with p_r:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("#### Live metrics")
    st.metric("Monthly revenue", "₹28.4 cr", "platform tier")
    st.metric("Latency", "0.08 ms", "mission critical")
    st.metric("Sensing confidence", "96%", "urban twin")
    st.metric("Active nodes", "1.2M", "city scale")
    st.markdown('</div>', unsafe_allow_html=True)
# STRATEGY
st.markdown('<div class="section"></div>', unsafe_allow_html=True)
st.markdown("### 4. Strategic Impact")
strat_cols = st.columns(4)
vals = [
    ("First-mover advantage", "Shapes standards and ecosystems."),
    ("First-mover risks", "High capex and uncertain payback."),
    ("Fast-follower advantage", "Lower risk and clearer standards."),
    ("Fast-follower risks", "Less influence and later learning."),
]
for c, (t, b) in zip(strat_cols, vals):
    with c:
        st.markdown(f'<div class="card"><h4>{t}</h4><p class="soft">{b}</p></div>', unsafe_allow_html=True)
fig_strat = go.Figure()
fig_strat.add_trace(go.Bar(name='Upside', x=['First mover','Fast follower'], y=[92,72], marker_color='#0a84ff'))
fig_strat.add_trace(go.Bar(name='Risk', x=['First mover','Fast follower'], y=[84,48], marker_color='#f59e0b'))
fig_strat.update_layout(barmode='group', height=380, paper_bgcolor='white', plot_bgcolor='#f7f9fc', margin=dict(l=10,r=10,t=18,b=10), legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='center', x=0.5))
st.plotly_chart(fig_strat, use_container_width=True)

# BUSINESS MODEL
st.markdown('<div class="section"></div>', unsafe_allow_html=True)
st.markdown("### 5. Business Model Impact")
rev_cols = st.columns(3)
for c, t, b in [(rev_cols[0], 'Connectivity-as-a-Service', 'Tiered by use case and quality.'), (rev_cols[1], 'Sensing / Slicing', 'Dedicated capability and data.'), (rev_cols[2], 'Platform & B2B2X', 'APIs, ecosystem, outcomes.')]:
    with c:
        st.markdown(f'<div class="card"><h4>{t}</h4><p class="soft">{b}</p></div>', unsafe_allow_html=True)
fig_rev = go.Figure(go.Sunburst(labels=['6G business model','Connectivity','Sensing','Slicing','Platform','Outcome pricing','B2B2X'], parents=['','6G business model','6G business model','6G business model','6G business model','Platform','Platform']))
fig_rev.update_layout(height=470, paper_bgcolor='white', margin=dict(l=10,r=10,t=18,b=10))
st.plotly_chart(fig_rev, use_container_width=True)

# RISKS
st.markdown('<div class="section"></div>', unsafe_allow_html=True)
st.markdown("### 6. Risks and Challenges")
fig_risk = px.pie(pd.DataFrame({'Risk':['Technical','Regulatory','Adoption','Ethical','ROI'], 'Share':[22,20,20,18,20]}), names='Risk', values='Share', hole=.55, color_discrete_sequence=['#0a84ff','#34c759','#f59e0b','#ff6b6b','#7c3aed'])
fig_risk.update_layout(height=410, paper_bgcolor='white', margin=dict(l=10,r=10,t=18,b=10), legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='center', x=0.5))
st.plotly_chart(fig_risk, use_container_width=True)


# FUTURE
st.markdown('<div class="section"></div>', unsafe_allow_html=True)
st.markdown("### 7. Future Outlook")
fo1, fo2 = st.columns([1.12, 1.08])
with fo1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("#### Three-act future")
    acts = pd.DataFrame({
        "Phase": ["2025-2028", "2028-2033", "2033+"],
        "Meaning": ["Research and standards", "Trials and early rollouts", "Mainstream disruption"],
        "Visual cue": ["Lab prototypes", "Pilot corridors", "Invisible infrastructure"]
    })
    st.dataframe(acts, use_container_width=True, hide_index=True)
    st.markdown('</div>', unsafe_allow_html=True)
with fo2:
    fig_future = go.Figure()
    fig_future.add_trace(go.Scatter(x=[2025,2028,2033,2036], y=[20,45,72,92], mode='lines+markers', line=dict(color='#0a84ff', width=5), fill='tozeroy', fillcolor='rgba(10,132,255,0.10)', name='Adoption curve'))
    fig_future.add_trace(go.Scatter(x=[2025,2028,2033,2036], y=[12,35,60,84], mode='lines+markers', line=dict(color='#34c759', width=5), fill='tozeroy', fillcolor='rgba(52,199,89,0.08)', name='Value creation'))
    fig_future.update_layout(height=380, paper_bgcolor='white', plot_bgcolor='#f7f9fc', margin=dict(l=10,r=10,t=18,b=10), legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='center', x=0.5), xaxis_title='Year', yaxis_title='Index')
    st.plotly_chart(fig_future, use_container_width=True)

st.markdown("#### Future outlook infographic")
inf1, inf2, inf3, inf4 = st.columns(4)
for c, title, body in [
    (inf1, 'XR mainstream', 'Immersive commerce and collaboration'),
    (inf2, 'Digital twins', 'Entire cities run in real time'),
    (inf3, 'Ambient AI', 'Networks infer and adapt constantly'),
    (inf4, 'New economics', 'Platforms, APIs, and outcome pricing'),
]:
    with c:
        st.markdown(f'<div class="card"><h4>{title}</h4><p class="soft">{body}</p></div>', unsafe_allow_html=True)

st.markdown('<div class="section"></div>', unsafe_allow_html=True)
st.markdown("### 8. Closing thesis")
close1, close2 = st.columns([1.08, 1.12])
with close1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.write("6G is not a connectivity upgrade. It is the invisible operating system of an AI-native economy.")
    st.write("The winners will not merely own spectrum or towers. They will own the layers above connectivity: intelligence, orchestration, data, and ecosystems.")
    st.markdown('</div>', unsafe_allow_html=True)
with close2:
    try:
        img3 = Image.open(BytesIO(requests.get('https://pplx-res.cloudinary.com/image/upload/pplx_search_images/0b691833f461d5c3e8ee53381ce8431ebe55ddf4.jpg', timeout=8).content))
        st.image(img3, use_container_width=True)
    except Exception:
        st.info('Closing visual placeholder')
