import os
import json
import openpyxl
from shutil import copyfile

from classes.clinical_study import ClinicalStudy
from classes.environment_variable import EnvironmentVariable
import classes.functions as func


class Processor(object):
    def __init__(self, realms=None, priority=None, languages=None, earliest=None, max=10, prefix=None):
        self.realms = realms
        self.priority = priority
        self.languages = languages
        self.earliest = earliest
        self.max = max
        self.prefix = prefix

        self.realms = func.parse(self.realms, "|")
        self.languages = func.parse(self.languages, "|")

        self.clinical_studies = []
        self.configure()
        self.filename = EnvironmentVariable('source_file', 'string', permit_omission=False).value
        self.copy_to = EnvironmentVariable('copy_to', 'string', permit_omission=True).value
        print("\n\nProcessing " + ", ".join(self.realms))

    def process(self):
        wb_obj = openpyxl.load_workbook(self.filename)
        sheet_obj = wb_obj.active
        row_count = sheet_obj.max_row
        if row_count > 1:
            for row_index in range(2, row_count + 1):
                authors = sheet_obj.cell(row=row_index, column=1).value
                title = sheet_obj.cell(row=row_index, column=2).value
                url = sheet_obj.cell(row=row_index, column=3).value
                publication = sheet_obj.cell(row=row_index, column=4).value
                subject = sheet_obj.cell(row=row_index, column=5).value
                priority = sheet_obj.cell(row=row_index, column=6).value
                language = sheet_obj.cell(row=row_index, column=7).value
                year = func.convert_to_int(sheet_obj.cell(row=row_index, column=8).value)

                process_study = True
                # Check realm
                if self.realms is not None and subject not in (self.realms):
                    process_study = False

                # Check priority
                if self.priority is not None and priority > self.priority:
                    process_study = False

                # Check language
                if self.languages is not None and language not in (self.languages):
                    process_study = False

                # Check earliest year
                if self.earliest is not None and year < self.earliest:
                    process_study = False

                if process_study:
                    clinical_study = ClinicalStudy(
                        authors, title, url, publication,
                        subject, priority, language, year
                    )
                    self.clinical_studies.append(clinical_study)
                    print(" - " + clinical_study.title)

                if len(self.clinical_studies) >= self.max:
                    break

        self.clinical_studies.sort(key=lambda x: x.year, reverse=True)

    def configure(self):
        self.resources_folder = os.path.join(os.getcwd(), "resources")
        self.source_folder = os.path.join(self.resources_folder, "source")
        self.html_folder = os.path.join(self.resources_folder, "html")
        self.json_folder = os.path.join(self.resources_folder, "json")
        self.csv_folder = os.path.join(self.resources_folder, "csv")

    def export(self):
        # Data
        json_data = []
        csv_data = '"Subject","Authors","Title,"URL","Publication"\n'
        html_data = ""

        # Filenames
        self.json_file = "clinical_studies.json"
        self.json_filename = os.path.join(self.json_folder, self.prefix + "_clinical_studies.json")
        self.csv_filename = os.path.join(self.csv_folder, self.prefix + "_clinical_studies.csv")
        self.html_filename = os.path.join(self.html_folder, self.prefix + "_clinical_studies.html")

        # Process
        for clinical_study in self.clinical_studies:
            json_data.append(clinical_study.as_dict())
            csv_data += clinical_study.as_row()
            html_data += clinical_study.as_html()

        html_data = "<div class='clinical_studies'><ol class='clinical_studies'>\n{list_items}</ol></div>".format(
            list_items=html_data
        )

        # Save JSON
        with open(self.json_filename, "w") as file:
            json.dump(json_data, file, indent=4)

        # Save CSV
        with open(self.csv_filename, "w") as file:
            file.write(csv_data)

        # Save HTML
        with open(self.html_filename, "w") as file:
            file.write(html_data)

        self.copy_json()

    def copy_json(self):
        if "Neuropad" in self.realms:
            if self.copy_to is not None:
                copyfile(self.json_filename, os.path.join(self.copy_to, self.json_file))
