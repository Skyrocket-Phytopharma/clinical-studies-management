from classes.clinical_study_processor import ClinicalStudyProcessor


# Neuropad
clinical_study_processor = ClinicalStudyProcessor(
    themes="Neuropad",
    priority=10,
    languages="English",
    earliest=2000,
    max=999,
    prefix="neuropad",
)
clinical_study_processor.process_excel_source()
clinical_study_processor.export()

# Monofilament
clinical_study_processor = ClinicalStudyProcessor(
    themes="Monofilament",
    priority=10,
    languages="",
    earliest=2000,
    max=999,
    prefix="monofilament",
)
clinical_study_processor.process_excel_source()
clinical_study_processor.export()
