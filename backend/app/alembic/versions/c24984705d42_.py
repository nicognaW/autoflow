"""empty message

Revision ID: c24984705d42
Revises: 893aff1b8621
Create Date: 2024-07-03 13:46:48.736303

"""

from alembic import op
import sqlalchemy as sa
import sqlmodel.sql.sqltypes
from tidb_vector.sqlalchemy import VectorType
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = "c24984705d42"
down_revision = "893aff1b8621"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "feedbacks",
        sa.Column(
            "comment", sqlmodel.sql.sqltypes.AutoString(length=500), nullable=False
        ),
    )
    op.add_column(
        "feedbacks", sa.Column("chat_id", sqlmodel.sql.sqltypes.GUID(), nullable=False)
    )
    op.add_column(
        "feedbacks", sa.Column("chat_message_id", sa.Integer(), nullable=False)
    )
    op.add_column(
        "feedbacks", sa.Column("user_id", sqlmodel.sql.sqltypes.GUID(), nullable=True)
    )
    op.create_foreign_key(
        None, "feedbacks", "chat_messages", ["chat_message_id"], ["id"]
    )
    op.create_foreign_key(None, "feedbacks", "chats", ["chat_id"], ["id"])
    op.create_foreign_key(None, "feedbacks", "users", ["user_id"], ["id"])
    op.drop_column("feedbacks", "langfuse_link")
    op.drop_column("feedbacks", "query")
    op.drop_column("feedbacks", "relationships")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("feedbacks", sa.Column("relationships", mysql.JSON(), nullable=True))
    op.add_column(
        "feedbacks", sa.Column("query", mysql.VARCHAR(length=255), nullable=False)
    )
    op.add_column(
        "feedbacks",
        sa.Column("langfuse_link", mysql.VARCHAR(length=255), nullable=False),
    )
    op.drop_constraint(None, "feedbacks", type_="foreignkey")
    op.drop_constraint(None, "feedbacks", type_="foreignkey")
    op.drop_constraint(None, "feedbacks", type_="foreignkey")
    op.drop_column("feedbacks", "user_id")
    op.drop_column("feedbacks", "chat_message_id")
    op.drop_column("feedbacks", "chat_id")
    op.drop_column("feedbacks", "comment")
    # ### end Alembic commands ###