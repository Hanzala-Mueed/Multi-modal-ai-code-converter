from app.ui.gradio_ui import create_ui


def start_application():

    app = create_ui()

    app.launch()