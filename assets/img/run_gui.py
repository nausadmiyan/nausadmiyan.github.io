import streamlit as st
import sys
import os
dir =os.path.dirname(os.path.abspath(__file__))
path1 = os.path.join(dir,"NN")
path2 = os.path.join(dir,"GAN")
path3 = os.path.join(dir,"SHAP")
path4 = os.path.join(dir,"XGBOOST")
path5 = os.path.join(dir,"RANDOMFOREST")
path6 = os.path.join(dir,"PREPROCESS")
path7 = os.path.join(dir,"POSTPROCESS")

# Add both folders to the system path
sys.path.append(path1)
sys.path.append(path2)
sys.path.append(path3)
sys.path.append(path4)
sys.path.append(path5)
sys.path.append(path6)
sys.path.append(path7)

from lr_tuning import main as file1_main
from batch_epoch import main as file2_main
from actFunc import main as file3_main
from weights import main as file4_main
from dropout import main as file5_main
from model_tuning import main as file6_main
from vgan import main as file7_main
from gan_process import main as file8_main
from shap_dict import main as file9_main
from shap_summary import main as file10_main
from shap_violin import main as file11_main
from shap_river import main as file12_main
from para_tuning import main as file13_main
from model_tuning_xgb import main as file14_main
from post_data_xgb import main as file15_main
from rf_para_tuning import main as file16_main
from rf_model_tuning import main as file17_main
from rf_post_data import main as file18_main
from outliers import main as file19_main
from data_imputation import main as file20_main
from correlation import main as file21_main
from metric_post_xgb import main as file22_main
from metric_post_rf import main as file23_main
from metric_post_nn import main as file24_main
from pred_vs_actual import main as file25_main
from nn_post_data import main as file26_main
from cgan import main as file27_main
from tgan import main as file28_main
from wgan import main as file29_main


# Set page configuration
st.set_page_config(
    page_title="StatML",
    page_icon="📊",
    layout="wide",
)


#st.header('Machine Learning Interface')
st.markdown("<h1 style='font-size:32px;'>StatML Framework</h1>", unsafe_allow_html=True)
st.markdown("<p style='font-size:11px;'>Developed by <a href='https://www.linkedin.com/in/arindam-laha/'>Arindam Laha</a> & <a href='https://scholar.google.com/citations?hl=en&user=orlzgpMAAAAJ'>Nausad Miyan</a></p>", unsafe_allow_html=True)

st.markdown("<p style='font-size:12px;'>A unified statistical machine-learning pipeline from augmentation to explainability.</p>", unsafe_allow_html=True)
# Create 4 separate main tabs
main_tabs = st.tabs([
    "Data Prepocessing",
    "Gen AI",
    "Random Forest",
    "XGBOOST",
    "Neural Network",
    "SHAP",
    "Post Processing",
])

# Inject custom CSS to increase tab font size, padding, and overall size
st.markdown(
    """
    <style>
        /* Increase the size of the tab labels */
        .stTabs [data-baseweb="tab-list"] button {
            font-size: 30pt;  /* Set font size to 30pt */
            padding: 10px 50px; /* Increase padding for larger tab size */
        }

        /* Increase the height of the tab container */
        .stTabs [data-baseweb="tab-list"] {
            gap: 30px;        /* Increase gap between tabs */
            height: 50px;     /* Increase tab container height */
        }

        /* Optional: Increase padding for the tab content */
        .stTabs [data-baseweb="tab-panel"] {
            padding-top: 5px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Content for Main Tab 1
with main_tabs[0]:  # Main Tab 1
    pre_tabs = st.tabs([
        "Data Imputation",
        "Outliers Removal",
        "Dataset Correlation",
    ])
    with pre_tabs[0]:
        #st.success("Data Imputation....")
        st.write(file20_main())
    
    with pre_tabs[1]:
        #st.error("This is the data processing")
        st.write(file19_main())
    with pre_tabs[2]:
        #st.error("This is the data processing")
        st.write(file21_main())

# Content for Main Tab 2
with main_tabs[1]:  # Main Tab 2
    ai_tabs = st.tabs([
        "Tabular GAN",
        "Wasserstein GAN",
        "Conditional GAN",
        "Vanilla GAN",
        "Data Processing"
    ])
    with ai_tabs[0]:
        #st.success("This is the gan data")
        st.write(file28_main())
    with ai_tabs[1]:
        st.write(file29_main())
    with ai_tabs[2]:
        st.write(file27_main())
    with ai_tabs[3]:
        st.write(file7_main())
    with ai_tabs[4]:
        #st.error("This is the data processing")
        st.write(file8_main())

# Content for Main Tab 3
with main_tabs[2]:  # Main Tab 3
    rf_tabs = st.tabs([
        "Parameter Tuning",
        "Model Tuning",
        "Post Data"
    ])
    with rf_tabs[0]:
        #st.success("This is the RF")
        st.write(file16_main())
    with rf_tabs[1]:
        #st.error("This is the data processing")
        st.write(file17_main())
    with rf_tabs[2]:
        #st.error("This is the data processing")
        st.write(file18_main())
  
# Content for Main Tab 4
with main_tabs[3]:  # Main Tab 4
    xgb_tabs = st.tabs([
        "Parameter Tuning",
        "Model Tuning",
        "Post Data"
    ])
    with xgb_tabs[0]:
        #st.success("This is the XGB")
        st.write(file13_main())
    with xgb_tabs[1]:
        #st.error("This is the data processing")
        st.write(file14_main())
    with xgb_tabs[2]:
        #st.error("This is the data processing")
        st.write(file15_main())

with main_tabs[4]:  # Main Tab 6
    tabs = st.tabs([
        "Learning Rate",
        "Batch and Epoch",
        "Activation Function",
        "Weights",
        "Dropouts",
        "Model Tuning",
        "Post Data"
    ])
    with tabs[0]:
        #st.header("📊 Tab 1 - File 1")
        #st.success("This is the first tab")
        st.write(file1_main())
        

    with tabs[1]:
        #st.header("📊 Tab 2 - File 2")
        #st.success("This section contains functionality from **File 2**.")
        st.write(file2_main())

    with tabs[2]:
        #st.header("🔍 Tab 3 - File 3")
        #st.warning("This section contains functionality from **File 3**.")
        st.write(file3_main())

    with tabs[3]:
        #st.header("⚙️ Tab 4 - File 4")
        #st.warning("This section contains functionality from **File 4**.")
        st.write(file4_main())

    with tabs[4]:
        #st.header("⚙️ Tab 4 - File 4")
        #st.error("This section contains functionality from **File 5**.")
        st.write(file5_main())

    with tabs[5]:
        #st.header("⚙️ Tab 4 - File 4")
        #st.error("This section contains functionality from **File 6**.")
        st.write(file6_main())
    with tabs[6]:
        #st.header("⚙️ Tab 4 - File 4")
        #st.error("This section contains functionality from **File 6**.")
        st.write(file26_main())

# Content for Main Tab 6
with main_tabs[5]:  # Main Tab 6
    tab1 = st.tabs([
        "Shap Dictionary",
        "Shap Summary",
        "Shap Violin",
        "Shap River"
    ])
    with tab1[0]:
        #st.header("📊 Tab 1 - File 1")
        #st.success("This is the first tab")
        st.write(file9_main())
        

    with tab1[1]:
        #st.header("📊 Tab 2 - File 2")
        #st.success("This section contains functionality from **File 2**.")
        st.write(file10_main())

    with tab1[2]:
        #st.header("🔍 Tab 3 - File 3")
        #st.warning("This section contains functionality from **File 3**.")
        st.write(file11_main())

    with tab1[3]:
        #st.header("⚙️ Tab 4 - File 4")
        #st.warning("This section contains functionality from **File 4**.")
        st.write(file12_main())

with main_tabs[6]:  # Main Tab 7
    tab_sub = st.tabs([
    "Metric",
    "Prediction vs Actual",
    ])
    with tab_sub[0]:
        metric_tab = st.tabs([
            "RF",
            "XGB",
            "NN",
        ])
        with metric_tab[0]:
            #st.success("This is the RF metric data")
            st.write(file23_main())
        
        with metric_tab[1]:
            #st.success("This is the XGB metric data")
            st.write(file22_main())

        with metric_tab[2]:
            #st.success("This is the NN metric data")
            st.write(file24_main())
    with tab_sub[1]:
        #st.success("This is the prediction vs actual data")
        st.write(file25_main())

