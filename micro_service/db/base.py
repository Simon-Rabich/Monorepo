# Import all the models, so that Base has them before being
# imported by Alembic
from micro_service.db.base_class import Base  # noqa
from micro_service.db.models.item import Item  # noqa
from micro_service.db.models.user import User  # noqa