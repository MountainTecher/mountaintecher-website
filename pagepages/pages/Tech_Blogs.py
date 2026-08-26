import streamlit as st

st.set_page_config(page_title="Tech Blogs | MountainTecher", page_icon="📰", layout="wide")
st.title("📰 Tech News & Deep Dives")
st.markdown("Read our latest scripts, smartphone comparisons, and telecom updates.")
st.markdown("---")

# Blog Post 1
with st.expander("🚨 Beware: The Call Forwarding Scam Explained", expanded=True):
    st.write("**Topic:** Cyber Safety & Network Security")
    st.write("Scammers are using simple MMI codes to forward your calls and steal OTPs. Always check your call forwarding status by dialing *#21#...")
    st.button("Read Full Article", key="blog1")

# Blog Post 2
with st.expander("📱 iPhone 17 Pro Max vs Samsung S26 Ultra: Ultimate Comparison"):
    st.write("**Topic:** Flagship Smartphone Showdown")
    st.write("A deep dive into the camera sensors, AI capabilities, and battery endurance of this year's biggest flagship devices...")
    st.button("Read Full Article", key="blog2")

# Blog Post 3
with st.expander("📡 Telecom Update: Jio Prime Membership News"):
    st.write("**Topic:** Mobile Networks & Recharge Plans")
    st.write("Everything you need to know about the latest changes in recharge plans and what it means for average consumers...")
    st.button("Read Full Article", key="blog3")
