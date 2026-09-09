from flask import Flask, render_template, request
from pypdf import PdfReader
import os

from utils.text_processing import clean_text
from utils.resume_extractor import extract_resume_info
from utils.job_extractor import extract_job_skills
from utils.matcher import (
    calculate_skill_match,
    get_matched_skills,
    get_missing_skills,
    get_match_category
)


app = Flask(__name__)

UPLOAD_FOLDER = "uploads"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/", methods=["GET", "POST"])
def home():

    extracted_text = ""
    cleaned_text = ""
    resume_info = {}

    job_description = ""
    job_skills = []

    match_score = None
    match_category = ""
    matched_skills = []
    missing_skills = []

    if request.method == "POST":

        # Get uploaded resume
        file = request.files.get("resume")

        # Get job description
        job_description = request.form.get(
            "job_description",
            ""
        )

        # -----------------------------
        # PROCESS RESUME
        # -----------------------------

        if file and file.filename.endswith(".pdf"):

            file_path = os.path.join(
                app.config["UPLOAD_FOLDER"],
                file.filename
            )

            file.save(file_path)

            # Read PDF
            reader = PdfReader(file_path)

            # Extract text from every page
            for page in reader.pages:

                text = page.extract_text()

                if text:
                    extracted_text += text

            # Clean resume text
            cleaned_text = clean_text(extracted_text)

            # Extract resume information
            resume_info = extract_resume_info(
                extracted_text
            )

        # -----------------------------
        # PROCESS JOB DESCRIPTION
        # -----------------------------

        if job_description:

            job_skills = extract_job_skills(
                job_description
            )

        # -----------------------------
        # MATCH RESUME WITH JOB
        # -----------------------------

        if resume_info and job_skills:

            match_score = calculate_skill_match(
                resume_info["skills"],
                job_skills
            )

            match_category = get_match_category(
                match_score
            )

            matched_skills = get_matched_skills(
                resume_info["skills"],
                job_skills
            )

            missing_skills = get_missing_skills(
                resume_info["skills"],
                job_skills
            )

    return render_template(
        "index.html",
        extracted_text=extracted_text,
        cleaned_text=cleaned_text,
        resume_info=resume_info,
        job_description=job_description,
        job_skills=job_skills,
        match_score=match_score,
        match_category=match_category,
        matched_skills=matched_skills,
        missing_skills=missing_skills
    )


if __name__ == "__main__":
    app.run(debug=True)