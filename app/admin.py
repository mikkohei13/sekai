import os
import uuid
from pathlib import Path

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_admin.form import FileUploadField

from app import db
from app.models import Character


def _unique_filename(obj, file_data):
    ext = Path(file_data.filename).suffix.lower()
    return f"{uuid.uuid4().hex}{ext}"


class CharacterAdmin(ModelView):
    """CRUD for characters. No auth — for local use only."""

    column_list = ("name", "sex", "description", "image_path", "created_at")
    column_searchable_list = ("name", "description")
    column_default_sort = ("name", False)
    form_columns = ("name", "description", "sex", "image_path")

    form_overrides = {
        "image_path": FileUploadField,
    }

    def __init__(self, model, session, upload_folder, **kwargs):
        self.upload_folder = upload_folder
        self.form_args = {
            "image_path": {
                "label": "Image",
                "base_path": upload_folder,
                "allowed_extensions": ("jpg", "jpeg", "png", "gif", "webp"),
                "namegen": _unique_filename,
            },
        }
        super().__init__(model, session, **kwargs)

    def on_model_delete(self, model):
        self._delete_image_file(model.image_path)

    def _delete_image_file(self, filename):
        if not filename:
            return
        path = os.path.join(self.upload_folder, filename)
        if os.path.isfile(path):
            os.remove(path)


def init_admin(app):
    admin = Admin(app, name="Sekai", url="/admin", template_mode="bootstrap4")
    admin.add_view(
        CharacterAdmin(
            Character,
            db.session,
            upload_folder=app.config["UPLOAD_FOLDER"],
            name="Characters",
        )
    )
