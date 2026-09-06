from flask import Flask, render_template, request
from pypdf import PdfReader
import os

from utils.text_processing import clean_text
from utils.resume_extractor import extract_resume_info


app = Flask(__name__)

UPLOAD_FOLDER = "uploads"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/", methods=["GET", "POST"])
def home():

    extracted_text = ""
    cleaned_text = ""
    resume_info = {}

    if request.method == "POST":

        file = request.files.get("resume")

        if file and file.filename.endswith(".pdf"):

            # Create file path
            file_path = os.path.join(
                app.config["UPLOAD_FOLDER"],
                file.filename
            )

            # Save uploaded PDF
            file.save(file_path)

            # Read PDF
            reader = PdfReader(file_path)

            # Extract text from every page
            for page in reader.pages:

                text = page.extract_text()

                if text:
                    extracted_text += text

            # Clean extracted text
            cleaned_text = clean_text(extracted_text)

            # Extract resume information
            resume_info = extract_resume_info(extracted_text)

    return render_template(
        "index.html",
        extracted_text=extracted_text,
        cleaned_text=cleaned_text,
        resume_info=resume_info
    )


if __name__ == "__main__":
    app.run(debug=True)