from pathlib import Path
from connexion import FlaskApp
from connexion.options import SwaggerUIOptions


def main():
    file_path = Path(__file__).resolve().parent
    swagger_options = SwaggerUIOptions(swagger_ui_path="/docs")
    app = FlaskApp(__name__, specification_dir=file_path / "specification")
    app.add_api(
        "openapi.yaml",
        swagger_ui_options=swagger_options,
        strict_validation=True,
    )
    app.run(host="127.0.0.1", port=8080)


if __name__ == "__main__":
    main()
