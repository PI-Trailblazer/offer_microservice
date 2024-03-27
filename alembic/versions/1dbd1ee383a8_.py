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
        "offer",
        sa.Column(
            "id",
            sa.Integer(),
            autoincrement=True,
            nullable=False,
        ),
        sa.Column("userid", sa.String(length=128), nullable=False),
        sa.Column("name", sa.String(length=264), nullable=False),
        sa.Column("description", sa.String(length=1028), nullable=False),
        sa.Column("street", sa.String(length=264), nullable=False),
        sa.Column("city", sa.String(length=264), nullable=False),
        sa.Column("postal_code", sa.String(length=264), nullable=False),
        sa.Column(
            "price",
            sa.Float(),
            nullable=False,
        ),
        sa.Column(
            "max_review_score",
            sa.Float(),
            nullable=False,
        ),
        sa.Column(
            "n_reviews",
            sa.Integer(),
            nullable=False,
        ),
        sa.Column(
            "discount",
            sa.Float(),
            nullable=False,
        ),
        sa.Column("tags", sa.ARRAY(sa.Text()), nullable=False),
        sa.Column("max_quantity", sa.Integer(), nullable=False),
        sa.Column("modules", sa.ARRAY(sa.Integer()), nullable=False),
        sa.PrimaryKeyConstraint("id", name="pk_offer"),
        schema=settings.SCHEMA_NAME,
    )
    op.create_table(
        "review",
        sa.Column(
            "id",
            sa.Integer(),
            autoincrement=True,
            nullable=False,
        ),
        sa.Column("userid", sa.String(length=128), nullable=False),
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

    op.create_table(
        "image",
        sa.Column(
            "id",
            sa.Integer(),
            autoincrement=True,
            nullable=False,
        ),
        sa.Column("offerid", sa.Integer(), nullable=False),
        sa.Column("image", sa.String(length=2048), nullable=False),
        sa.ForeignKeyConstraint(
            ["offerid"],
            ["offer_microservice.offer.id"],
            name="fk_image_offerid_offer",
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id", name="pk_image"),
        schema=settings.SCHEMA_NAME,
    )
    op.create_index(
        "ix_offer_microservice_image_offerid",
        "image",
        ["offerid"],
        unique=False,
        schema=settings.SCHEMA_NAME,
    )
    op.create_table(
        "reservation",
        sa.Column(
            "id",
            sa.Integer(),
            autoincrement=True,
            nullable=False,
        ),
        sa.Column("userid", sa.String(128), nullable=False),
        sa.Column("offerid", sa.Integer(), nullable=False),
        sa.Column("init_date", sa.DATE(), nullable=False),
        sa.Column("end_date", sa.DATE(), nullable=False),
        sa.ForeignKeyConstraint(
            ["offerid"],
            ["offer_microservice.offer.id"],
            name="fk_reservation_offerid_offer",
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id", name="pk_reservation"),
        schema=settings.SCHEMA_NAME,
    )
    op.create_index(
        "ix_offer_microservice_reservation_userid",
        "reservation",
        ["userid"],
        unique=False,
        schema=settings.SCHEMA_NAME,
    )
    op.create_index(
        "ix_offer_microservice_reservation_offerid",
        "reservation",
        ["offerid"],
        unique=False,
        schema=settings.SCHEMA_NAME,
    )
    op.create_table(
        "menu_item",
        sa.Column(
            "id",
            sa.Integer(),
            autoincrement=True,
            nullable=False,
        ),
        sa.Column("offerid", sa.Integer(), nullable=False),
        sa.Column("image", sa.String(length=2048), nullable=False),
        sa.Column("description", sa.String(length=264), nullable=False),
        sa.Column("vegetarian", sa.BOOLEAN(), nullable=False),
        sa.ForeignKeyConstraint(
            ["offerid"],
            ["offer_microservice.offer.id"],
            name="fk_menu_item_offerid_offer",
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id", name="pk_menu_item"),
        schema=settings.SCHEMA_NAME,
    )
    op.create_index(
        "ix_offer_microservice_menu_item_offerid",
        "menu_item",
        ["offerid"],
        unique=False,
        schema=settings.SCHEMA_NAME,
    )
    op.create_table(
        "calendar",
        sa.Column(
            "id",
            sa.Integer(),
            autoincrement=True,
            nullable=False,
        ),
        sa.Column("offerid", sa.Integer(), nullable=False),
        sa.Column("init_date", sa.DATE(), nullable=False),
        sa.Column("end_date", sa.DATE(), nullable=False),
        sa.ForeignKeyConstraint(
            ["offerid"],
            ["offer_microservice.offer.id"],
            name="fk_calendar_offerid_offer",
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id", name="pk_calendar"),
        schema=settings.SCHEMA_NAME,
    )
    op.create_index(
        "ix_offer_microservice_calendar_offerid",
        "calendar",
        ["offerid"],
        unique=False,
        schema=settings.SCHEMA_NAME,
    )
    op.create_table(
        "extra_info",
        sa.Column(
            "id",
            sa.Integer(),
            autoincrement=True,
            nullable=False,
        ),
        sa.Column("offerid", sa.Integer(), nullable=False),
        sa.Column("nbeds", sa.Integer(), nullable=True),
        sa.Column("ntoilets", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["offerid"],
            ["offer_microservice.offer.id"],
            name="fk_extra_info_offerid_offer",
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id", name="pk_extra_info"),
        schema=settings.SCHEMA_NAME,
    )
    op.create_index(
        "ix_offer_microservice_extra_info_offerid",
        "extra_info",
        ["offerid"],
        unique=False,
        schema=settings.SCHEMA_NAME,
    )


def downgrade() -> None:
    op.drop_index(
        "ix_offer_microservice_extra_info_offerid",
        table_name="extra_info",
        schema=settings.SCHEMA_NAME,
    )
    op.drop_table("extra_info", schema=settings.SCHEMA_NAME)
    op.drop_index(
        "ix_offer_microservice_calendar_offerid",
        table_name="calendar",
        schema=settings.SCHEMA_NAME,
    )
    op.drop_table("calendar", schema=settings.SCHEMA_NAME)
    op.drop_index(
        "ix_offer_microservice_menu_item_offerid",
        table_name="menu_item",
        schema=settings.SCHEMA_NAME,
    )
    op.drop_table("menu_item", schema=settings.SCHEMA_NAME)
    op.drop_index(
        "ix_offer_microservice_reservation_offerid",
        table_name="reservation",
        schema=settings.SCHEMA_NAME,
    )
    op.drop_index(
        "ix_offer_microservice_reservation_userid",
        table_name="reservation",
        schema=settings.SCHEMA_NAME,
    )
    op.drop_table("reservation", schema=settings.SCHEMA_NAME)
    op.drop_index(
        "ix_offer_microservice_image_offerid",
        table_name="image",
        schema=settings.SCHEMA_NAME,
    )
    op.drop_table("image", schema=settings.SCHEMA_NAME)
    op.drop_table("offer", schema=settings.SCHEMA_NAME)
    op.drop_index(
        "ix_offer_microservice_review_offerid",
        table_name="review",
        schema=settings.SCHEMA_NAME,
    )
    op.drop_index(
        "ix_offer_microservice_review_userid",
        table_name="review",
        schema=settings.SCHEMA_NAME,
    )
    op.drop_table("review", schema=settings.SCHEMA_NAME)
