import streamlit as st

st.set_page_config(page_title="MountainTecher | Tech Hub", page_icon="⛰️", layout="wide")

# Hero Section
st.markdown("<h1 style='text-align: center; color: #1E90FF;'>⛰️ MountainTecher</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Decoding Technology, Empowering Users</h3>", unsafe_allow_html=True)
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.header("🚀 Welcome to Our Tech Ecosystem")
    st.write("""
    We don't just review tech—we build solutions. MountainTecher is a next-generation tech platform bringing you the latest in consumer technology, smartphone comparisons, and AI-powered troubleshooting.
    """)
    st.info("👈 **Use the sidebar to explore our AI Tools and Tech Blogs.**")

with col2:
    st.header("📺 Join the Community")
    st.write("Subscribe to our YouTube channel for cutting-edge tech analysis and updates.")
    st.link_button("👉 Subscribe to MountainTecher", "https://www.youtube.com/channel/UC4xdSlpqQta9eUY-2Mauh-Q")
    
st.markdown("---")
st.markdown("<p style='text-align: center;'>© 2026 MountainTecher. Built with AI & Python.</p>", unsafe_allow_html=True)