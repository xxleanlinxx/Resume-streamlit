# --- Basics ---
WORK_NAME = "Lean Lin"
TC_NAME = "Ming Yan, Lin"
DESCRIPTION_a = """
a **Data Science Professional** with **6+ years** Practical Experience
"""
DESCRIPTION_b = """
- Leverage **Exploratory Data Analysis**, **Data Mining**, and **Machine Learning**
- Create impactful **Visualizations** to uncover **Actionable Trends**
- Extracting **Data-driven Insights** into **Strategic Business Decisions**
- A **Self-Motivated Learner**, with a special focus on data science and managerial soft skills
"""

# --- Contacts ---
EMAIL = "xxleanlinxx@email.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/leanlin/",
    "GitHub": "https://github.com/xxleanlinxx",
    "Line ID": "archer840510"
}

# --- Information of About ---
EDU = {
    'degree': '#### **Master Degree**, *Public Administration & Policy*',
    'school': 'National Taipei University',
    'period': '2017 Sep ~ 2021 Jan',
    'info':'''
        ---
        ##### Thesis
        - **The Research on the Influence of Influencers’ Political Endorsement and Policy Marketing Effect:** *Using Internet Public Opinion Big Data to Analyze its Impact on Social Media* 
        - Thesis URL 🔗 : [Link](https://hdl.handle.net/11296/834k8b)
        ---
        ##### Grade
        - GPA : **3.8**
        ---
        ##### Honor
        - *Phi Tau Phi Honorary Membership*
        - *The C. C. Chang Scholarship of Administrative Science*
        - *The Rotary Foundation Scholarship*
    '''
}

CAREER = {
    'shopee':{
        'title': '#### **Data Analyst, Business Intelligence**',
        'corp_name': '*Shopee*',
        'period': '*2024 Jan ~ Present*',
        'info': '''
            - Leverage RFM framework to `segment users` and `predict their future login inclination` using `LightGBM` with `93% precison rate`.
            - Building a `Prophet` model to `predict upcoming campaign GMV` with `2.7% MAPE` (train) and `1.8% MAPE gap` (valid - train) , further enhancing efficiency on marketing resources allocation
            - Building a `local crm data warehouse` conserved `95%` of computation time, which `integrate user features` from different departments, and `standardize the data structure` for future analysis.
            - Building a `business metrics projection tool`(streamlit app) reduced `40%` of working time, further enhancing the efficiency and optimizing the working fashion.
            - `Develop and maintain Data Dashboards or Trackers` for marketing analysis needs and routine monitoring, including but not limited to `marketing campaign performance`, `consumer traffic`, and `ordering incentives`.
            - `Collaborate with cross-functional teams` to `Identify and Prioritize business needs`, and `Provide Data-Driven Insights` to support decision-making.
            - `Communicate effectively` with stakeholders to ensure alignment on project goals and deliverables.
        '''
    },
    'ailabs':{
        'title': '#### **Lead Data Analyst**',
        'corp_name': '*Taiwan AiLabs*',
        'period': '*2023 Feb ~ 2023 Dec*',
        'info': '''
            - `Lead 3 Data Analysts` and distribute the workload, `organizing the needs` from clients & senior management, also `planning the analytical framework and layout to meet the overall goals` of the business unit's expectations.
            - Set up a `standardized data analysis framework` to `clearly uncover the relationship between abnormal user groups and popular manipulated issues`, which became a part of the focal features on `infodemic.cc`.
            - `Utilizing community detection algorithms` to group atypical accounts, also `detecting atypical behavior patterns` on social media based on feature engineering & other ML methods. (2+ models for `YouTube` & `TikTok`)
            - Experienced in data visualization, `demonstrating evidence of coordinated inauthentic behaviors`, and `concluding with insights about how collaborative groups manipulated` specific information. (40+ reports)
        '''
    },
    'eland':{
        'title': '#### **Sr. Business Analyst**',
        'corp_name': '*eLand Information*',
        'period': '*2019 Mar ~ 2023 Feb*',
        'info': '''
            - `Providing conclusions and insights` among various realms based on data-driven evidence. (realms including `politics & policies`, `public relations`, `business analytics` and `marketing campaign`)
            - Involved in data-related tasks such as `Data Cleaning`, `Data Integration`, `Data Transformation` & `Data Visualization`, routinely delivering analytic reports. (100+ reports)
            - `Offering assistance and advice to clients` to help deal with system-operating or data-processing issues. (clients including business group, ad agency and public sector) 
            - `Occasionally serve as a lecturer` sharing thoughts or insights about Social Big Data and various quantitative methods. (25+ lectures or workshops)
        '''
    }
}

# --- Information of Skills ---
SKILLS = {
    'soft':'''
        #### Communication 🤝
        - *Clear Data Storytelling*
        - *Cross-Functional Collaboration*
        ---
        #### Critical Thinking 🧠
        - *Problem Decomposition*
        - *Logical Reasoning*
        - *Data-Driven Decision-Making*
        ---
        #### Adaptability Mindset 🌵
        - *Learning New Tools and Techniques*
        - *Adapting to Change*
    ''',
    'hard':'''
        #### Code & Data Tool 🐍
        - `Python`, `SQL`, `Streamlit`
        - `Looker Studio`, `Tableau`, `Power BI`
        - `Excel`, `Power Query`, `Power Pivot`
        ---
        #### Analytical Skills 📖
        - `Exploratory Data Analysis` and `Feature Engineering`
        - `Data Visualization` 
            - *Seaborn, Plotly, PyGWalker*
        - `Machine Learning`
            - Tree-Based: *RandomForest, XgBoost, CatBoost, LightGBM*
            - Deep Learning: *LSTM*
        - `Explainable AI Method`
            - *LIME, SHAP*
        - `Statistical Models`
            - Linear: *OLS, LR*
            - Dimensionality Reduction: *PCA, t-SNE, Clustering*
            - Time-Series: *ARIMAX, Prophet*
        - `ETL` & `Data Management`
        ---
    ''',
    'certificate_1':'''
        - *Stanford  **Machine Learning**  Specialization*
    ''',
    'certificate_2':'''
        - *Google  **Business Intelligence**  Specialization*
    '''
}

# --- Information of Projects ---
PROJECTS = {
    'side':{
        'ml':{
            'name':'''
                #### *Showcase Demo of ML Model & XAI (Web app)*
            ''',
            'info':'''
                - This Showcase Demo app helps user to better understand how a `Machine Learning Model` works, also realizing `how features interprete & predict` target variable via `Explainable AI method`(SHAP Value).
                - I expected to `standerdize the process of understanding a ML Model` by building this app with meaningful metrics & visualization.
            ''',
            'access':'''
                https://ml-xai-showcase-toolkit.streamlit.app/
            ''',
            'repo':'''
                https://github.com/xxleanlinxx/MLshowcase-streamlit/tree/main
            '''
        },
        'app':{
            'name':'''
                #### *EDA Toolkit - a No-Code Data Tool (Web app)*
            ''',
            'info':'''
                - The EDA Toolkit is a user-friendly web application built with Streamlit that assists data analysts and data scientists in `performing quick, interactive, and comprehensive EDA`.
                - I aimed to `simplify the process of understanding datasets` by providing tools for statistical insights and visualization.
            ''',
            'access':'''
                https://data-eda-toolkit.streamlit.app/
            ''',
            'repo':'''
                https://github.com/xxleanlinxx/EDA-streamlit/tree/main
            '''
        },
        'wal':{
            'name':'''
                #### *Business Case Study - Walmart Sales Factors Analysis & Forecasting*
            ''',
            'info':'''
                - This case study aimed to realize `how factors affect 'Weekly_Sales' of Walmart` and `what's the intersection effect between factors` by Using `K-means Clustering`, `Random Forest Regressor` and `Partial Dependence Plot`.
                - Using `LSTM` to `Predict the future 'Weekly_Sales' by different shop clusters` to help optimize the stocking strategy.
            ''',
            'access':'''
                https://walmart-casestudy-leanlinmy.my.canva.site/
            ''',
            'repo':'''
                https://github.com/xxleanlinxx/case_study/blob/e5288101aeb8f9292dc6b2e9433e3e53842e7d89/factor_analysis_on_walmart_sales_performance.ipynb
            '''
        }
    },
    'work':{
        'ls':{
            'name':'''
                #### *Guidelines for Early-Life Live Stream Sellers*
            ''',
            'info':'''
                - Using `Random Forest Regressor` & `EDA` to assess the most influential key factors that drive live stream success.
                - Compiling the insights into an executive summary for the Live Streaming Team to `help build up Guidelines for recruiting and persuading new streamers`.
            '''
        },
        'dws':{
            'name':'''
                #### *Build a Local Data Warehouse of Integrated Consumer Segmentations for Taiwan Business*
            ''',
            'info':'''
                - `Standardize consumer segmentation` by aligning different departments' goals and integrating them with existing academic frameworks. 
                - Over `60+` User Features retrievedd from `14` different tables has been built into a local data warehouse (ETL) for `Enhancing Marketing Efficiency` and to `Improve Analysis Quality`.
                - `Reduce computation time by 90%` and potentially `save an average of 6 hours per week` in manual data retrieval efforts. 
            '''
        },
        'rfm':{
            'name':'''
                #### *RFM Clustering for CLV Prediction* ***(on-going)***
            ''',
            'info':'''
                - Using RFM Features to `Classified Consumer into Meaningful Groups` to help seek high CLV Users to:
                    - Improving `Cost-Efficiency` (Target on Right Users)
                    - Prevent Potential Loss on A1 & Buyers (`Churn-Preventing` Strategy)
                - `Predict the future behavior patterns` on whether the User will:
                    - Login
                    - Purchase
                    - Create Incremental Orders
            ''',
            'access': '''
                https://twilight-torta-0ee.notion.site/RFM-Clustering-for-CLV-Prediction-2ae71451866f431ebb3d156783c7ddea?pvs=4
            '''
        },
        'app':{
            'name':'''
                #### *Projection Automation Tool (Web app)*
            ''',
            'info':'''
                - Developed a Streamlit application that analyzes business metrics and creates projections based on historical data.
                - Allowed for easy visualization of various metrics and their change differences.
                - Optimized the process of `creating business metrics projections` by `automating the data analysis and visualization process`.
            ''',
            'access': '''
                https://projection-tool-app.streamlit.app/
            '''
        },
        'topline':{
            'name':'''
                #### *Marketplace Business Topline Prediction* ***(on-going)*** 
            ''',
            'info':'''
                - Using Granger Causality Test to `Identify Important Lag Features` to help predict Topline Metrics, aiming to:
                    - Improving `Resources Allocaiton` before the Campaign
                    - `Optimize the Campaign Strategy` by `Identifying the Key Factors`
                - Leverage `ARIMAX` and `Prophet` Models in testing phase
            ''',
            'access_granger': '''
                https://www.notion.so/Testify-Causality-Correlation-for-Time-Series-Data-1e55d7926f8f80f6a442c6841471014b?pvs=4
            ''',
            'access_prophet': '''
                https://www.notion.so/Facebook-Prophet-Modeling-101-1f35d7926f8f805ca4bcc5ba06f2a91d?pvs=4
            '''
        }
    }
}
