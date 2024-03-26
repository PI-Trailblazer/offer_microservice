"""empty message

Revision ID: 1dbd1ee383a8
Revises: 
Create Date: 2024-03-26 03:30:23.936796

"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from app.core.config import settings


# revision identifiers, used by Alembic.
revision = "1dbd1ee383a8"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "review",
        sa.Column(
            "id",
            sa.Integer(),
            autoincrement=True,
            nullable=False,
        ),
        sa.Column("userid", sa.Integer(), nullable=False),
        sa.Column("offerid", sa.Integer(), nullable=False),
        sa.Column("comment", sa.String(length=264), nullable=False),
        sa.Column(
            "score",
            sa.Float(),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["offerid"],
            ["offer_microservice.offer.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        schema=settings.SCHEMA_NAME,
    )
    op.create_index(
        "ix_offer_microservice_review_userid",
        "review",
        ["userid"],
        unique=False,
        schema=settings.SCHEMA_NAME,
    )
    op.create_index(
        "ix_offer_microservice_review_offerid",
        "review",
        ["offerid"],
        unique=False,
        schema=settings.SCHEMA_NAME,
    )
    # TODO : Check the rest of the code
    op.create_table(
        "offer",
        sa.Column(
            "id",
            sa.Integer(),
            autoincrement=True,
            nullable=False,
        ),
        sa.Column("userid", sa.String(), autoincrement=False, nullable=False),
        sa.Column("name", sa.String(length=264), nullable=False),
        sa.Column("description", sa.String(length=264), nullable=False),
        sa.Column("street", sa.String(length=264), nullable=True),
        sa.Column("city", sa.String(length=264), nullable=True),
        sa.Column("postal_code", sa.String(length=264), nullable=True),
        sa.Column(
            "price",
            sa.Float(),
            nullable=False,
        ),
        sa.Column(
            "score",
            sa.Float(),
            nullable=False,
        ),
        sa.Column(
            "discount",
            sa.Float(),
            nullable=False,
        ),
        sa.Column("tags", sa.String(length=264), autoincrement=False, nullable=False),
        sa.Column("max_quantity", sa.Integer(), autoincrement=False, nullable=False),
        sa.Column(
            "modules", sa.String(length=264), autoincrement=False, nullable=False
        ),
        sa.PrimaryKeyConstraint("id", name="pk_offer"),
        schema="offer_microservice",
        postgresql_ignore_search_path=False,
    )
    op.create_table(
        "image",
        sa.Column(
            "id",
            sa.Integer(),
            server_default=sa.text(
                "nextval('offer_microservice.image_id_seq'::regclass)"
            ),
            autoincrement=True,
            nullable=False,
        ),
        sa.Column("offerid", sa.Integer(), autoincrement=False, nullable=False),
        sa.Column("image", sa.String(length=2048), autoincrement=False, nullable=False),
        sa.ForeignKeyConstraint(
            ["offerid"],
            ["offer_microservice.offer.id"],
            name="fk_image_offerid_offer",
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id", name="pk_image"),
        schema="offer_microservice",
    )
    op.create_index(
        "ix_offer_microservice_image_offerid",
        "image",
        ["offerid"],
        unique=False,
        schema="offer_microservice",
    )
    op.create_table(
        "reservation",
        sa.Column(
            "id",
            sa.Integer(),
            server_default=sa.text(
                "nextval('offer_microservice.reservation_id_seq'::regclass)"
            ),
            autoincrement=True,
            nullable=False,
        ),
        sa.Column("userid", sa.Integer(), autoincrement=False, nullable=False),
        sa.Column("offerid", sa.Integer(), autoincrement=False, nullable=False),
        sa.Column("init_date", sa.DATE(), autoincrement=False, nullable=False),
        sa.Column("end_date", sa.DATE(), autoincrement=False, nullable=False),
        sa.ForeignKeyConstraint(
            ["offerid"],
            ["offer_microservice.offer.id"],
            name="fk_reservation_offerid_offer",
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id", name="pk_reservation"),
        schema="offer_microservice",
    )
    op.create_index(
        "ix_offer_microservice_reservation_userid",
        "reservation",
        ["userid"],
        unique=False,
        schema="offer_microservice",
    )
    op.create_index(
        "ix_offer_microservice_reservation_offerid",
        "reservation",
        ["offerid"],
        unique=False,
        schema="offer_microservice",
    )
    op.create_table(
        "menu_item",
        sa.Column(
            "id",
            sa.Integer(),
            server_default=sa.text(
                "nextval('offer_microservice.menu_item_id_seq'::regclass)"
            ),
            autoincrement=True,
            nullable=False,
        ),
        sa.Column("offerid", sa.Integer(), autoincrement=False, nullable=False),
        sa.Column("image", sa.String(length=2048), autoincrement=False, nullable=False),
        sa.Column(
            "description", sa.String(length=264), autoincrement=False, nullable=False
        ),
        sa.Column("vegetarian", sa.BOOLEAN(), autoincrement=False, nullable=False),
        sa.ForeignKeyConstraint(
            ["offerid"],
            ["offer_microservice.offer.id"],
            name="fk_menu_item_offerid_offer",
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id", name="pk_menu_item"),
        schema="offer_microservice",
    )
    op.create_index(
        "ix_offer_microservice_menu_item_offerid",
        "menu_item",
        ["offerid"],
        unique=False,
        schema="offer_microservice",
    )
    op.create_table(
        "calendar",
        sa.Column(
            "id",
            sa.Integer(),
            server_default=sa.text(
                "nextval('offer_microservice.calendar_id_seq'::regclass)"
            ),
            autoincrement=True,
            nullable=False,
        ),
        sa.Column("offerid", sa.Integer(), autoincrement=False, nullable=False),
        sa.Column("init_date", sa.DATE(), autoincrement=False, nullable=False),
        sa.Column("end_date", sa.DATE(), autoincrement=False, nullable=False),
        sa.ForeignKeyConstraint(
            ["offerid"],
            ["offer_microservice.offer.id"],
            name="fk_calendar_offerid_offer",
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id", name="pk_calendar"),
        schema="offer_microservice",
    )
    op.create_index(
        "ix_offer_microservice_calendar_offerid",
        "calendar",
        ["offerid"],
        unique=False,
        schema="offer_microservice",
    )
    op.create_table(
        "extra_info",
        sa.Column(
            "id",
            sa.Integer(),
            server_default=sa.text(
                "nextval('offer_microservice.extra_info_id_seq'::regclass)"
            ),
            autoincrement=True,
            nullable=False,
        ),
        sa.Column("offerid", sa.Integer(), autoincrement=False, nullable=False),
        sa.Column("nbeds", sa.Integer(), autoincrement=False, nullable=False),
        sa.Column("ntoilets", sa.Integer(), autoincrement=False, nullable=False),
        sa.ForeignKeyConstraint(
            ["offerid"],
            ["offer_microservice.offer.id"],
            name="fk_extra_info_offerid_offer",
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id", name="pk_extra_info"),
        schema="offer_microservice",
    )
    op.create_index(
        "ix_offer_microservice_extra_info_offerid",
        "extra_info",
        ["offerid"],
        unique=False,
        schema="offer_microservice",
    )


def downgrade() -> None:
    op.drop_index(
        "ix_offer_microservice_extra_info_offerid",
        table_name="extra_info",
        schema="offer_microservice",
    )
    op.drop_table("extra_info", schema="offer_microservice")
    op.drop_index(
        "ix_offer_microservice_calendar_offerid",
        table_name="calendar",
        schema="offer_microservice",
    )
    op.drop_table("calendar", schema="offer_microservice")
    op.drop_index(
        "ix_offer_microservice_menu_item_offerid",
        table_name="menu_item",
        schema="offer_microservice",
    )
    op.drop_table("menu_item", schema="offer_microservice")
    op.drop_index(
        "ix_offer_microservice_reservation_offerid",
        table_name="reservation",
        schema="offer_microservice",
    )
    op.drop_index(
        "ix_offer_microservice_reservation_userid",
        table_name="reservation",
        schema="offer_microservice",
    )
    op.drop_table("reservation", schema="offer_microservice")
    op.drop_index(
        "ix_offer_microservice_image_offerid",
        table_name="image",
        schema="offer_microservice",
    )
    op.drop_table("image", schema="offer_microservice")
    op.drop_table("offer", schema="offer_microservice")
    op.drop_index(
        "ix_offer_microservice_review_offerid",
        table_name="review",
        schema="offer_microservice",
    )
    op.drop_index(
        "ix_offer_microservice_review_userid",
        table_name="review",
        schema="offer_microservice",
    )
    op.drop_table("review", schema="offer_microservice")
