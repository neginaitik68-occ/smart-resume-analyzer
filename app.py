from flask import Flask, render_template, request
from pypdf import PdfReader
import os

from utils.text_processing import clean_text


app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/", methods=["GET", "POST"])
def home():

    extracted_text = ""
    cleaned_text = ""

    if request.method == "POST":

        file = request.files["resume"]

        if file and file.filename.endswith(".pdf"):

            file_path = os.path.join(
                app.config["UPLOAD_FOLDER"],
                file.filename
            )

            file.save(file_path)

            # Read the PDF
            reader = PdfReader(file_path)

            # Extract text from every page
            for page in reader.pages:
                text = page.extract_text()

                if text:
                    extracted_text += text

            # Clean the extracted text
            cleaned_text = clean_text(extracted_text)

    return render_template(
        "index.html",
        extracted_text=extracted_text,
        cleaned_text=cleaned_text
    )


if __name__ == "__main__":
    app.run(debug=True)