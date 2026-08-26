import streamlit as st

st.set_page_config(page_title="About Founder | MountainTecher", page_icon="👨‍💻")
st.title("👨‍💻 About The Founder")
st.markdown("---")

col1, col2 = st.columns([1, 2])

with col1:
    # Later you can replace this with your actual professional photo URL
    st.image("https://api.dicebear.com/7.x/avataaars/svg?seed=TechEngineer", width=250)
    st.markdown("### Bhaskar Chauhan")
    st.caption("Tech Creator & Software Engineer")

with col2:
    st.markdown("""
    ### Background & Expertise
    MountainTecher is founded and run by a passionate **Computer Science Engineer (B.Tech, 2024)**. 
    
    Bridging the gap between core engineering and consumer technology, the vision is to simplify complex tech problems through AI and logic. 
    
    ### 🔬 Research & Academic Focus
    Beyond content creation, there is a strong focus on advanced computing and network structures. Manuscripts and technical research work have been submitted to prestigious journals like:
    *   *Journal of Data Structures and Computing*
    *   *Journal of Computer Networks and Virtualization*
    *   *International Journal of Research and Analytical Reviews*
    
    ### 🎯 Future Roadmap
    Currently preparing for top-tier competitive engineering exams (GATE, ISRO) while building a comprehensive ecosystem of AI tools for the MountainTecher community.
    """)