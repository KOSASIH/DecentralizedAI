case_studies = {
    "case_study_1": {
        "name": "Predicting Customer Churn with Machine Learning",
        "application": "Customer Analytics",
        "problem": "A telecommunications company wants to develop a machine learning model to predict which of its customers are at risk of churning, so that it can proactively address their concerns and retain them as customers.",
        "approach": "1. Data Collection: Collected customer data, including account information and call detail records (CDRs), and transformed it into a structured format.",
        "technologies": {
            "data_processing": ["pandas", "numpy"],
            "machine_learning": ["scikit-learn", "xgboost"],
            "data_visualization": ["matplotlib", "seaborn"],
            "customization": [],
            "integration": [],
            "optimization": ["ray"],
            "natural_language_processing": [],
            "computer_vision": []
        },
        "results": {
            "key_performance_indicator_1": 12,
            "key_performance_indicator_2": 15,
            "key_performance_indicator_3": 3
        },
        "impact": {
            "financial_impact": "Retained customers worth $1.2 million in revenue",
            "operational_impact": "Reduced customer churn rate by 50%"
        }
    },
    "case_study_2": {
        "name": "Automated Quality Assurance with Deep Learning",
        "application": "Quality Assurance",
        "problem": "A manufacturing company wants to automate the quality assurance process for its products, which involves inspecting each product for defects.",
        "approach": "1. Data Collection: Collected images of various types of defects, along with images of non-defective products.",
        "technologies": {
            "data_processing": ["pandas", "numpy"],
            "machine_learning": ["tensorflow", "keras"],
            "data_visualization": [],
            "customization": ["OpenCV"],
            "integration": ["Docker"],
            "optimization": ["ray"],
            "natural_language_processing": [],
            "computer_vision": []
        },
        "results": {
            "key_performance_indicator_1": 92,
            "key_performance_indicator_2": 0.5,
            "key_performance_indicator_3": 0.01
        },
        "impact": {
            "financial_impact": "Reduced quality assurance costs by 30%",
            "operational_impact": "Improved inspection speed by a factor of 10"
        }
    }
}

def get_case_studies():
    """
    Returns a dictionary of case studies.

    Returns:
        dict -- A dictionary of case studies.
    """
    return case_studies

if __name__ == '__main__':
    print(get_case_studies())
