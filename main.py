import matplotlib.pyplot as mp
import streamlit as st

def calculateEMI(P,R,T): 
    Actual_amount_per_month = (P/T)if T!=0 else 0
    Intrest_amount_per_month = (P*(R/100)) if R!=0 else 0
    Total_emi_amount_with_intrest = P + (Intrest_amount_per_month*T) if R!=0 else P
    EMI = Actual_amount_per_month + Intrest_amount_per_month if R!=0 else Actual_amount_per_month
    return [EMI, Total_emi_amount_with_intrest,Actual_amount_per_month, Intrest_amount_per_month]

def plot(P,R,T):
    mp.style.use('dark_background')
    calculate = calculateEMI(P,R,T)
    sizes = [P, calculate[3]*T, calculate[0]] if T!=0 and P!=0 else [10,10,10]
    labels = [f'Principal - ₹{sizes[0]}', f'Total Interest - ₹{sizes[1]:.1f}',f'Monthly Payment - ₹{sizes[2]:.1f}'] if T!=0 and P!=0 else ['No Data','No Data','No Data']
    colors = ['#FFF1C9', '#EA5F89', '#57167E']
    explode = (0, 0.05, 0.1)
    fig,ax = mp.subplots(figsize=(5,2),dpi=500)
    ax.pie(sizes,labels=labels,colors=colors,autopct='%1.1f%%',shadow=True,explode=explode,textprops={'fontsize': 4, 'color': 'grey', 'weight':'bold','style':'italic', 'family': 'serif',})
    st.pyplot(fig)
    
    
st.set_page_config(page_title="Emilio - Understand Your Interest. Plan Your Payments.", page_icon='https://github.com/haroontrailblazer/haroontrailblazer/blob/main/Project%20Pngs/Emilio.jpg?raw=true', layout="centered")
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        .stActionButton {display: none;}  /* hides the stop/rerun icon */
    </style>
""", unsafe_allow_html=True)


# --- SEO META TAGS ---
st.markdown("""
<head>
  <title>Emilio - EMI Calculator</title>
  <meta name="description" content="Understand Your Interest. Plan Your Payments.">
  <meta name="keywords" content="haroontrailblazer, Servers, security, Server Health checker, Server strength, MomentoMonto, Haroon K M">
  <meta name="robots" content="index, follow">
</head>
""", unsafe_allow_html=True)


if "show_form" not in st.session_state:
    st.session_state.show_form = False
    
    
if not st.session_state.show_form:
    # --- Title ---
    st.markdown("""
        <h2 style='text-align:left; color:#FFF1C9;'>Emilio</h2>
        <p style='text-align:left; color:grey; font-size:14px; margin-top:-10px;'>Understand Your Interest. Plan Your Payments.</p><br><br>""", unsafe_allow_html=True)
    

    with st.form("emi_form"):
        P1=st.number_input(label="Principal Amount",min_value=0,placeholder="Enter Loan Amount",label_visibility="visible")
        R1=st.number_input(label="Annual Interest Rate (%)",min_value=0.0,placeholder="Enter Annual Interest Rate",label_visibility="visible")
        T1=st.number_input(label="Loan Duration (Months)",min_value=1,placeholder="Enter Duration in Months",label_visibility="visible")
        submitted = st.form_submit_button("Calculate EMI",use_container_width=True)
        st.autorefresh=True
                   
                    
    if submitted:
        st.session_state.show_form = True
        st.session_state["P1"] = P1
        st.session_state["R1"] = R1
        st.session_state["N1"] = T1
        st.rerun()
   
            
else:
    plot(st.session_state["P1"], st.session_state["R1"], st.session_state["N1"])
    
    
    st.markdown("""
    <div class="footer" style="background-color:black;color:#333;padding:18px;border-radius:12px;max-width:820px;margin:20px auto;text-align:center;font-family:Segoe UI, Tahoma, sans-serif;">
        <p style="margin:0 0 8px;font-size:11px;">
            <strong>Contact:</strong>
            <a href="mailto:hexra2025@gmail.com" style="color:#FFF1C9;text-decoration:none;margin-left:8px;">hexra2025@gmail.com</a>
        </p>
        <p style="margin:0 0 12px;font-size:11px;">
            <a href="https://www.instagram.com/hendrix__trailblazer?igsh=MTEyOTEycm9mMGxjaA==" target="_blank" style="color:#FFF1C9;text-decoration:none;margin:0 8px;">Instagram</a> |
            <a href="https://github.com/haroontrailblazer" target="_blank" style="color:#FFF1C9;text-decoration:none;margin:0 8px;">GitHub</a>
        </p>
        <hr style="border:none;border-top:1px solid #e6e6e6;margin:12px 0;">
        <p style="margin:8px 0 0;color:#555;font-size:11px;line-height:1.4;text-align:left;">
            <strong>About:</strong>
            Emilio is a smart, intuitive EMI and loan analysis tool designed to help users understand their financial commitments with clarity and confidence. Built with precision and simplicity in mind, Emilio breaks down your loan into its essential components—principal, interest, and monthly EMI—and visualizes them for effortless understanding.
    </div>
    """, unsafe_allow_html=True)
    
    
    if st.button("Calculate Again", use_container_width=True):
        st.session_state.show_form = False

        st.rerun()

