# Import Streamlit library
import streamlit as st

color_codes = [
    "#B71C1C", # Dark red
    "#E65100", # Orange deep
    "#F57F17", # Deep yellow
    "#1B5E20", # Dark green
    "#006064", # Cyan dark
    "#0D47A1", # Dark blue
    "#1A237E", # Indigo
    "#4A148C", # Purple deep
    "#880E4F", # Deep purple
    "#004D40", # Deep teal
    "#3E2723", # Dark brown
    "#3E2723", # Coffee
    "#212121", # Almost black
    "#BF360C", # Deep orange
    "#827717", # Olive
    "#1B5E20", # Green dark (Repeated for balance)
]

task = "Summarize this paper in detail for a scientific audience."

title = "Next Visit Diagnosis Prediction via Medical Code-Centric Multimodal Contrastive EHR Modelling with Hierarchical Regularisation"

title_css = f'<span style="color: {color_codes[0]};">Next Visit Diagnosis Prediction via Medical Code-Centric Multimodal Contrastive EHR Modelling with Hierarchical Regularisation</span>'

abstract = "Predicting next visit diagnosis using Electronic Health Records (EHR) is an essential task in healthcare, critical for devising proactive future plans for both healthcare providers and patients. Nonetheless, many preceding studies have not sufficiently addressed the heterogeneous and hierarchical characteristics inherent in EHR data, inevitably leading to sub-optimal performance. To this end, we propose NECHO, a novel medical code-centric multimodal contrastive EHR learning framework with hierarchical regularisation. First, we integrate multifaceted information encompassing medical codes, demographics, and clinical notes using a tailored network design and a pair of bimodal contrastive losses, all of which pivot around a medical codes representation. We also regularise modality-specific encoders using a parental level information in medical ontology to learn hierarchical structure of EHR data. A series of experiments on MIMIC-III data demonstrates effectiveness of our approach."

abstract_css = f'Predicting next visit diagnosis using Electronic Health Records (EHR) is an essential task in healthcare, critical for devising proactive future plans for both healthcare providers and patients. <span style="color: {color_codes[8]};">Nonetheless, many preceding studies have not sufficiently addressed the heterogeneous and hierarchical characteristics inherent in EHR data, inevitably leading to sub-optimal performance.</span> <span style="color: {color_codes[1]};">To this end, we propose NECHO, a novel medical code-centric multimodal contrastive EHR learning framework with hierarchical regularisation.</span> <span style="color: {color_codes[3]};">First, we integrate multifaceted information encompassing medical codes, demographics, and clinical notes using a tailored network design and a pair of bimodal contrastive losses, all of which pivot around a medical codes representation. We also regularise modality-specific encoders using a parental level information in medical ontology to learn hierarchical structure of EHR data.</span> <span style="color: {color_codes[4]};">A series of experiments on MIMIC-III data demonstrates effectiveness of our approach.</span>'

introduction = "Predicting a patient's future diagnosis has been a longstanding objective in both academic and industrial healthcare sectors. Its significance is highlighted for healthcare providers with refining decision-making processes and resource allocation, and also for patients with effective future plans. By leveraging the extensive accumulation of EHR data, data-driven deep learning methodologies have achieved considerable advancements in the healthcare practices, particularly in next admissions diagnosis prediction (Choi et al., 2016a; Ma et al., 2018; Qiao et al., 2019; Zhang et al., 2020a). However, most of previous studies have shown limited consideration into multifaceted and hierarchical properties inherent in EHR data. First, it is heterogeneous, encompassing a range of modalities including demographics (e.g. age), medical images (e.g., Computed Tomography), text (e.g. clinical notes), time series (e.g. laboratory tests), and medical codes (e.g. ICD-9). Each modality offers diverse and unique perspectives of a single observation and holds substantial potential to improve representative power if it is integrated seamlessly with other modalities. Nevertheless, the majority of previous works have solely focused on medical codes or shown limited exploration into effective multimodal fusion strategies (Choi et al., 2017; Zhang et al., 2020a; Yang and Wu, 2021). Second, EHR data employs International Classification of Diseases (ICD) codes (Slee, 1978), an organised hierarchical medical concept ontology. It is used by domain experts to systematically categorise patient diagnoses into relevant medical concepts. For instance, in its ninth version (ICD-9), circulatory system diseases (ICD-9 code 390-459) are further categorised into 9 subcategories, each denoting specific conditions, such as hypertensive disease (ICD-9 code 401-405). Each is further divided into 10 subcategories (e.g. ICD-9 code 401.0 to 401.9). This shows a highly structured and hierarchical dependency amongst them. Despite the critical importance of these attributes, they have been largely overlooked in earlier studies. To address the aforementioned characteristics of EHR data, we present a novel framework for Next Visit Diagnosis Prediction via Medical Code-Centric Multimodal Contrastive EHR Modelling with Hierarchical Regularisation (NECHO). To the best of our knowledge, this framework is the first work designed in a medical code-centric fashion for diagnosis prediction. It tightly and seamlessly entangles three distinct modalities of medical codes, demographics, and clinical notes through a meticulously designed multimodal fusion network and two bimodal contrastive losses. Its goal is to boost representational power by positioning demographics and clinical notes as supplementary modalities. Furthermore, we harness an auxiliary loss to regularise each modality-specialised encoder based on the ancestral level of medical codes, thereby successfully injecting more general information from the ICD-9 medical ontology. Therefore, the main contributions of our work are threefold as follows: We effectively integrate three distinct modalities by developing a novel fusion network and a pair of bimodal contrastive losses, centralised around medical codes representation. We also propose to use auxiliary losses for each modality-specific model to regularise them using the parental level of medical codes to learn more general information, leveraging hierarchical nature of ICD-9 codes. Our proposed NECHO framework achieves superior performance over previous works on MIMIC-III (Johnson et al., 2016), a publicly available large-scale real-world healthcare data."

introduction_css = f'Predicting a patient\'s future diagnosis has been a longstanding objective in both academic and industrial healthcare sectors. Its significance is highlighted for healthcare providers with refining decision-making processes and resource allocation, and also for patients with effective future plans. By leveraging the extensive accumulation of EHR data, data-driven deep learning methodologies have achieved considerable advancements in the healthcare practices, particularly in next admissions diagnosis prediction (Choi et al., 2016a; Ma et al., 2018; Qiao et al., 2019; Zhang et al., 2020a). <span style="color: {color_codes[2]};">However, most of previous studies have shown limited consideration into multifaceted and hierarchical properties inherent in EHR data.</span> First, it is heterogeneous, encompassing a range of modalities including demographics (e.g. age), medical images (e.g., Computed Tomography), text (e.g. clinical notes), time series (e.g. laboratory tests), and medical codes (e.g. ICD-9). Each modality offers diverse and unique perspectives of a single observation and holds substantial potential to improve representative power if it is integrated seamlessly with other modalities. Nevertheless, the majority of previous works have solely focused on medical codes or shown limited exploration into effective multimodal fusion strategies (Choi et al., 2017; Zhang et al., 2020a; Yang and Wu, 2021). Second, EHR data employs International Classification of Diseases (ICD) codes (Slee, 1978), an organised hierarchical medical concept ontology. It is used by domain experts to systematically categorise patient diagnoses into relevant medical concepts. For instance, in its ninth version (ICD-9), circulatory system diseases (ICD-9 code 390-459) are further categorised into 9 subcategories, each denoting specific conditions, such as hypertensive disease (ICD-9 code 401-405). Each is further divided into 10 subcategories (e.g. ICD-9 code 401.0 to 401.9). This shows a highly structured and hierarchical dependency amongst them. Despite the critical importance of these attributes, they have been largely overlooked in earlier studies. <span style="color: {color_codes[5]};">To address the aforementioned characteristics of EHR data, we present a novel framework for Next Visit Diagnosis Prediction via Medical Code-Centric Multimodal Contrastive EHR Modelling with Hierarchical Regularisation (NECHO).</span> To the best of our knowledge, this framework is the first work designed in a medical code-centric fashion for diagnosis prediction. <span style="color: {color_codes[9]};">It tightly and seamlessly entangles three distinct modalities of medical codes, demographics, and clinical notes through a meticulously designed multimodal fusion network and two bimodal contrastive losses.</span> Its goal is to boost representational power by positioning demographics and clinical notes as supplementary modalities. <span style="color: {color_codes[10]};">Furthermore, we harness an auxiliary loss to regularise each modality-specialised encoder based on the ancestral level of medical codes, thereby successfully injecting more general information from the ICD-9 medical ontology.</span> Therefore, the main contributions of our work are threefold as follows: <span style="color: {color_codes[12]};">We effectively integrate three distinct modalities by developing a novel fusion network and a pair of bimodal contrastive losses, centralised around medical codes representation.</span> <span style="color: {color_codes[6]};">We also propose to use auxiliary losses for each modality-specific model to regularise them using the parental level of medical codes to learn more general information, leveraging hierarchical nature of ICD-9 codes.</span> <span style="color: {color_codes[11]};">Our proposed NECHO framework achieves superior performance over previous works on MIMIC-III (Johnson et al., 2016), a publicly available large-scale real-world healthcare data.</span>'

conclusion = "Next visit diagnosis prediction is beneficial in AI-driven healthcare applications and has shown remarkable progress. However, the multifaceted and hierarchical properties of EHR data are beyond the consideration for the most of existing studies. To address these limitations, we introduce the novel multimodal EHR modelling framework, NECHO. It effectively aggregates representations from three heterogeneous modalities through meticulously designed multimodal fusion network and the pair of two bimodal contrastive losses in a medical code-centric manner. It also uses parental level information of ICD-9 codes to regularise each modality-specialised encoder to learn more general information. Experimental results including the ablation studies and case study on MIMIC-III data highlight the NECHO's efficacy and superiority."

conclusion_css = f'<span style="color: {color_codes[13]};">Next visit diagnosis prediction is beneficial in AI-driven healthcare applications and has shown remarkable progress.</span> However, the multifaceted and hierarchical properties of EHR data are beyond the consideration for the most of existing studies. <span style="color: {color_codes[14]};">To address these limitations, we introduce the novel multimodal EHR modelling framework, NECHO.</span> It effectively aggregates representations from three heterogeneous modalities through meticulously designed multimodal fusion network and the pair of two bimodal contrastive losses in a medical code-centric manner. It also uses parental level information of ICD-9 codes to regularise each modality-specialised encoder to learn more general information. <span style="color: {color_codes[7]};">Experimental results including the ablation studies and case study on MIMIC-III data highlight the NECHO\'s efficacy and superiority.</span>'

text = f"{task}\n\n**Title:** {title}\n\n**Abstract:** {abstract}\n\n**Introduction**\n\n{introduction}\n\n**Conclusion**\n\n{conclusion}" 

text_css = f"{task}\n\n**Title:** {title_css}\n\n**Abstract:** {abstract_css}\n\n**Introduction**\n\n{introduction_css}\n\n**Conclusion**\n\n{conclusion_css}" 

olmo = 'The paper "Next Visit Diagnosis Prediction via Medical Code-Centric Multimodal Contrastive EHR Modelling with Hierarchical Regularisation" proposes a medical code-centric multimodal contrastive EHR modelling framework called NECHO for next visit diagnosis prediction. The paper addresses the challenges of heterogeneous and hierarchical properties inherent in EHR data, which have been largely overlooked in previous studies. The proposed framework integrates medical codes, demographics, and clinical notes through a tailored network design and a pair of bimodal contrastive losses, with a goal of boosting representational power and addressing the hierarchical properties of ICD-9 codes. Experimental results on MIMIC-III show the efficacy and superiority of the proposed framework.\n\nKey points:\n\n* The paper proposes the novel multimodal EHR modelling framework called NECHO, which effectively integrates three distinct modalities by developing a novel fusion network and a pair of bimodal contrastive losses, centralised around medical codes representation.\n\n* The proposed framework uses auxiliary losses for each modality-specific model to regularise them using the parental level of medical codes, leveraging the hierarchical nature of ICD-9 codes.\n\n* Experimental results including ablation studies and a case study on MIMIC-III data highlight the NECHO\'s efficacy and superiority.\n\nDetailed summary:\n\nThe paper introduces a novel multimodal EHR modelling framework called NECHO for next visit diagnosis prediction. The framework addresses the challenges of heterogeneous and hierarchical properties inherent in EHR data. The proposed framework integrates medical codes, demographics, and clinical notes through a tailored network design and a pair of bimodal contrastive losses, in a medical code-centric manner.\n\nThe multimodal fusion network is designed to efficiently aggregate representations from three distinct modalities by exploiting the inherent relationships among them. The paper also explains how auxiliary losses are used to regularise each modality-specific encoder based on the ancestral level of medical codes, thereby effectively injecting more general information from the ICD-9 medical ontology.\n\nThe paper demonstrates superior performance of the proposed framework over previous works on MIMIC-III (a publicly available large-scale real-world healthcare data), with ablation studies and a case study. The experimental results highlight the efficacy and superiority of the proposed framework.\n\nOverall, the paper contributes significantly to the field of EHR data analysis and AI-driven healthcare applications. The proposed framework is a step forward in addressing the challenges of heterogeneous and hierarchical properties in EHR data, and is promising for future research in this direction.'

olmo_css = f'The paper <span style="color: {color_codes[0]};">"Next Visit Diagnosis Prediction via Medical Code-Centric Multimodal Contrastive EHR Modelling with Hierarchical Regularisation"</span> <span style="color: {color_codes[1]};">proposes a medical code-centric multimodal contrastive EHR modelling framework called NECHO for next visit diagnosis prediction.</span> <span style="color: {color_codes[2]};">The paper addresses the challenges of heterogeneous and hierarchical properties inherent in EHR data, which have been largely overlooked in previous studies.</span> <span style="color: {color_codes[3]};">The proposed framework integrates medical codes, demographics, and clinical notes through a tailored network design and a pair of bimodal contrastive losses, with a goal of boosting representational power and addressing the hierarchical properties of ICD-9 codes.</span> <span style="color: {color_codes[4]};">Experimental results on MIMIC-III show the efficacy and superiority of the proposed framework.</span>\n\nKey points:\n\n* <span style="color: {color_codes[5]};">The paper proposes the novel multimodal EHR modelling framework called NECHO,</span> <span style="color: {color_codes[12]};">which effectively integrates three distinct modalities by developing a novel fusion network and a pair of bimodal contrastive losses, centralised around medical codes representation.</span>\n\n* <span style="color: {color_codes[6]};">The proposed framework uses auxiliary losses for each modality-specific model to regularise them using the parental level of medical codes, leveraging the hierarchical nature of ICD-9 codes.</span>\n\n* <span style="color: {color_codes[7]};">Experimental results including ablation studies and a case study on MIMIC-III data highlight the NECHO\'s efficacy and superiority.</span>\n\nDetailed summary:\n\n<span style="color: {color_codes[5]};">The paper introduces a novel multimodal EHR modelling framework called NECHO for next visit diagnosis prediction.</span> <span style="color: {color_codes[8]};">The framework addresses the challenges of heterogeneous and hierarchical properties inherent in EHR data.</span> <span style="color: {color_codes[3]};">The proposed framework integrates medical codes, demographics, and clinical notes through a tailored network design and a pair of bimodal contrastive losses, in a medical code-centric manner.</span>\n\n<span style="color: {color_codes[9]};">The multimodal fusion network is designed to efficiently aggregate representations from three distinct modalities by exploiting the inherent relationships among them.</span> <span style="color: {color_codes[10]};">The paper also explains how auxiliary losses are used to regularise each modality-specific encoder based on the ancestral level of medical codes, thereby effectively injecting more general information from the ICD-9 medical ontology.</span>\n\n<span style="color: {color_codes[11]};">The paper demonstrates superior performance of the proposed framework over previous works on MIMIC-III (a publicly available large-scale real-world healthcare data), with ablation studies and a case study.</span> <span style="color: {color_codes[7]};">The experimental results highlight the efficacy and superiority of the proposed framework.</span>\n\n<span style="color: {color_codes[13]};">Overall, the paper contributes significantly to the field of EHR data analysis and AI-driven healthcare applications. <span style="color: {color_codes[14]};">The proposed framework is a step forward in addressing the challenges of heterogeneous and hierarchical properties in EHR data, and is promising for future research in this direction.</span>'

falcon = "Invalid response: just repeated the input."

xgen = "Invalid: did not return a response within 10 minutes."

def inline_css():
    st.markdown("""
        <style>
            }}
                .appview-container .main .block-container{{
                max-width: {percentage_width_main}%;
                padding-top: {1}rem;
                padding-right: {10}rem;
                padding-left: {10}rem;
                padding-bottom: {1}rem;
            }}
        </style>

        """, unsafe_allow_html=True)


css='''
<style>
    section.main > div {max-width:75rem}
</style>
'''
st.markdown(css, unsafe_allow_html=True) 

# Title of the overall app
st.title('Open Source LLM Comparison on Scholarly Summarization Task')

# Defining four chunks of text and their titles
text_chunks = {
    "Model Input": text,
    "OLMo Response": olmo,
    "Falcon Response": falcon,
    "XGen-7B-8K Response": xgen
}

# Initialize or update the page state
if 'page' not in st.session_state:
    st.session_state['page'] = 'home'

# Define a function to change the page state
def go_to_page(page_name):
    st.session_state['page'] = page_name

# Home page
if st.session_state['page'] == 'home':

    # Loop through the text chunks and their titles to display them
    for title, text in text_chunks.items():
        st.subheader(title)
        st.markdown(text)
        if title == "OLMo Response":
            if st.button('Go to side by side view'):
              go_to_page('side_by_side')
              
# Side by side page
elif st.session_state['page'] == 'side_by_side':
    st.title('Side by Side View')
    
    col1, col2 = st.columns([1.5,1])
    
    with col1:
        st.subheader('Model Input')
        st.markdown(text_css, unsafe_allow_html=True)
    
    with col2:
        st.subheader('OLMo Response')
        st.markdown(olmo_css, unsafe_allow_html=True)

    # Optionally, add a button to go back to the home page
    if st.button('Go back'):
        go_to_page('home')

