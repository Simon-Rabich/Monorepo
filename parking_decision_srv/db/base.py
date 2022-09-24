# Import all the models, so that Base has them before being
# imported by Alembic
from parking_decision_srv.db.base_class import Base  # noqa
from parking_decision_srv.db.models.item import Item  # noqa
from parking_decision_srv.db.models.user import User  # noqa